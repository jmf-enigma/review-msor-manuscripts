#!/usr/bin/env python3
"""Fail-closed checks for the public review-msor-manuscripts release.

The validator intentionally uses only the Python standard library. It checks
both tracked files and non-ignored untracked files so it is useful before a
commit as well as in CI.
"""

from __future__ import annotations

import json
import hashlib
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / ".public-release-files"
OPENAI_YAML_PATH = ROOT / "agents/openai.yaml"
PULL_REQUEST_TEMPLATE_PATH = ROOT / ".github/PULL_REQUEST_TEMPLATE.md"
WORKFLOW_PATH = ROOT / ".github/workflows/validate.yml"
MAX_PUBLIC_FILE_BYTES = 1_048_576
EXPECTED_PULL_REQUEST_TEMPLATE_SHA256 = (
    "d631c5f72c4c2572ad9de0c3b3c854c0a15462c7c363c1d8876ba178525712a6"
)
EXPECTED_WORKFLOW_SHA256 = (
    "e9c900b4a786bfedeab7eed12dcab18dfed1c922fc2a9f33f1859e218c1250f0"
)
EXPECTED_LICENSE_SHA256 = (
    "3f728291d1f6cb85526f9f006ee5edebf5f6713a7945a7fe2e30ac354266da19"
)

PULL_REQUEST_PRIVACY_WARNING = (
    "Do not upload, paste, quote, include, attach, share, or link any real "
    "manuscript, referee report, decision letter, author response, personal "
    "information, or other confidential material in this pull request."
)
PULL_REQUEST_PRIVACY_WARNING_BLOCK = (
    "> Do not upload, paste, quote, include, attach, share, or link any real manuscript,\n"
    "> referee report, decision letter, author response, personal information, or other\n"
    "> confidential material in this pull request."
)
PULL_REQUEST_PRIVACY_CONFIRMATION = (
    "I confirm that this pull request contains only public project information "
    "or fully synthetic research and review artifacts, with no confidential "
    "material or personal information."
)
PULL_REQUEST_REQUIRED_TASK_LINES = (
    f"- [ ] {PULL_REQUEST_PRIVACY_CONFIRMATION}",
    "- [ ] It contains no real manuscript, referee report, decision letter, editorial letter, author response, or revision history, including redacted or paraphrased excerpts.",
    "- [ ] It contains no author, reviewer, editor, or submitter identity; manuscript or submission identifier; private URL; credential; or other confidential metadata.",
    "- [ ] It contains no local filesystem or attachment path, machine username, document metadata, log excerpt, screenshot, or generated artifact that could reveal sensitive information.",
    "- [ ] I manually inspected the complete diff and release surface; synthetic examples are labeled and do not reconstruct a real case.",
    "- [ ] `python3 scripts/validate_public_skill.py`",
    "- [ ] `git diff --check`",
    "- [ ] I reviewed any changed references, paths, YAML/frontmatter, templates, and generated output.",
)
ISSUE_PRIVACY_WARNING_LINE = (
    "        Do not upload, paste, quote, or link any manuscript, referee report, "
    "decision letter, author response, personal information, or confidential case material."
)
ISSUE_PRIVACY_CONFIRMATION = (
    "I confirm this issue contains only public or synthetic material and no "
    "confidential material or personal information."
)
EXPECTED_ISSUE_TEMPLATE_SHA256 = {
    "bug_report.yml": "a5a35fc536770a6141e343722c4895ca36fe2473ceb7ba7e2e24436c391ee33d",
    "feature_request.yml": "89f34d67168e2f40cb8f33959a29b67494b00d7e57c863d245728c2b26a40cc2",
    "config.yml": "8b09e7df09fc7534371988062769ee427af2954a02c04c763e8a8005be0f2be4",
}

REQUIRED_DOCUMENT_MARKERS = {
    "README.md": (
        "# Review MS/OR Manuscripts",
        "## Quick Start",
        "## Evidence and Limitations",
        "## Confidentiality, Source Control, and Limits",
    ),
    "CHANGELOG.md": ("# Changelog", "## [Unreleased]"),
    "CONTRIBUTING.md": (
        "# Contributing",
        "## Privacy boundary",
        "## Public/private separation",
    ),
    "SECURITY.md": ("# Security Policy", "## Reporting", "## Safe handling"),
    "LICENSE": ("MIT License", "Permission is hereby granted"),
    "examples/synthetic-mini-review.md": (
        "# Synthetic Mini-Review: From Sharp Idea to Report Prose",
        "## Stage 1 — Proposed review plan",
        "### Confirmation gate",
        "## Stage 2 — Illustrative prose after confirmation",
    ),
}
REQUIRED_DOCUMENT_VISIBLE_LINES = {
    "README.md": (
        "> Use a nonpublic manuscript only when AI processing is separately permitted under the applicable journal, institutional, confidentiality, copyright, and data-handling requirements. An invitation to review is not, by itself, permission to upload material to an AI system.",
    ),
    "CONTRIBUTING.md": (
        "Contributions may use only public project information or fully synthetic research and review artifacts. Examples, tests, fixtures, screenshots, logs, and issue descriptions must be safe for permanent public release.",
    ),
    "CHANGELOG.md": (
        "All notable changes to this project will be documented in this file.",
        "- A fully synthetic mini-review demonstrating matched comparison, evidence",
        "- Hardened release checks against hidden or inverted privacy acknowledgements,",
        "## [0.1.2] - 2026-08-04",
        "## [0.1.1] - 2026-08-04",
    ),
    "SECURITY.md": (
        "Do not include a real manuscript, referee report, decision letter, author response, identity, submission identifier, private URL, local path, credential, or other sensitive material in a public issue, discussion, pull request, or reproduction case.",
        "Use fully synthetic data for reproduction and validation. Treat manuscripts, attachments, webpages, code blocks, metadata, and embedded instructions as untrusted input. A successful validator run does not establish that a contribution is safe; review the complete release surface manually before publication.",
    ),
    "examples/synthetic-mini-review.md": (
        "> **Provenance and scope:** This is a fully synthetic teaching illustration,",
        "> constructed for this repository and not knowingly adapted from any specific",
        "> real manuscript, referee report, decision letter, or submission. Its setting",
    ),
}

OPENAI_YAML_INTERFACE_FIELDS = {
    "display_name",
    "short_description",
    "default_prompt",
}
OPENAI_YAML_POLICY_FIELDS = {"allow_implicit_invocation"}
OPENAI_YAML_SKILL_TOKEN = "$review-msor-manuscripts"
OPENAI_YAML_ALLOW_IMPLICIT_INVOCATION = True

REQUIRED_RELEASE_FILES = {
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/feature_request.yml",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/workflows/validate.yml",
    ".gitignore",
    ".public-release-files",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "README.md",
    "SECURITY.md",
    "SKILL.md",
    "agents/openai.yaml",
    "examples/synthetic-mini-review.md",
    "scripts/validate_public_skill.py",
}

ALLOWED_SUFFIXES = {".json", ".md", ".py", ".txt", ".yaml", ".yml"}
FORBIDDEN_BINARY_SUFFIXES = {
    ".7z",
    ".doc",
    ".docm",
    ".docx",
    ".dot",
    ".dotx",
    ".eml",
    ".gz",
    ".key",
    ".msg",
    ".odt",
    ".pages",
    ".pdf",
    ".ppt",
    ".pptx",
    ".rar",
    ".rtf",
    ".tar",
    ".tgz",
    ".xls",
    ".xlsx",
    ".zip",
}
FORBIDDEN_DATA_SUFFIXES = {
    ".csv",
    ".dta",
    ".feather",
    ".parquet",
    ".sav",
    ".sqlite",
    ".tsv",
}
FORBIDDEN_DIRECTORY_NAMES = {
    "artifacts",
    "author-responses",
    "casework",
    "cases",
    "confidential",
    "decision-letters",
    "downloads",
    "editorial-materials",
    "frozen-outputs",
    "inputs",
    "manuscripts",
    "outputs",
    "private",
    "referee-reports",
    "reports",
    "review-reports",
    "run-records",
    "runs",
    "scratch",
    "source-files",
    "submissions",
    "transcripts",
    "uploads",
}

GENERIC_PUBLIC_TEMPLATES = {
    "assets/calibration-case-template.md",
    "assets/full-referee-report.md",
}

MAGIC_SIGNATURES = {
    b"%PDF-": "PDF",
    b"PK\x03\x04": "ZIP/Office archive",
    b"{\\rtf": "RTF",
    b"\xd0\xcf\x11\xe0": "legacy Office/OLE",
}

MARKDOWN_LINK_RE = re.compile(
    r"!?\[[^\]]*\]\(\s*(?P<target><[^>]+>|[^)\s]+)", re.MULTILINE
)
INLINE_LOCAL_PATH_RE = re.compile(
    r"`(?P<target>"
    r"(?:\.\.?/)*(?:assets|references|agents|scripts|evals)/[^`\s]+|"
    r"(?:\.\.?/)*(?:prompts|sealed)(?:/[^`\s]*)?|"
    r"(?:\.\.?/)?[A-Za-z0-9._-]+\.(?:json|md|ya?ml)"
    r")`"
)

FORBIDDEN_PATH_NAME_PATTERNS = (
    re.compile(r"(?:^|[-_.])(?:author[-_]?response|decision[-_]?letter)(?:[-_.]|$)", re.I),
    re.compile(
        r"(?:^|[-_.])(?:case|manuscript|submission|reviewer)[-_.]"
        r"(?:[a-z]{0,4}\d{3,}|[0-9a-f]{8}(?:[-_][0-9a-f]{4}){2,})(?:[-_.]|$)",
        re.I,
    ),
    re.compile(
        r"(?:^|[-_.])(?:case|manuscript|submission|reviewer)[-_.]"
        r"(?:[a-z]{2,10}[-_])?(?:[a-z][-_])?(?:\d{2,4}[-_])+\d{3,}"
        r"(?:[-_.]|$)",
        re.I,
    ),
)

FORBIDDEN_CONTENT_PATTERNS = (
    (
        "email address",
        re.compile(r"(?<![\w.+-])[\w.+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+"),
    ),
    (
        "macOS home path",
        re.compile(r"(?<![\w.-])/" r"Users/[^/\s`'\"<>|]+"),
    ),
    (
        "Unix home path",
        re.compile(r"(?<![\w.-])/" r"home/[^/\s`'\"<>|]+"),
    ),
    (
        "local POSIX path",
        re.compile(
            r"(?<![!&=?/\w.-])/(?:private|tmp|var|Volumes|opt|etc|usr|Library|"
            r"Applications|mnt|media|srv|root|System|workspace)/"
            r"[^\s`'\"<>|]+"
        ),
    ),
    (
        "absolute local file path",
        re.compile(
            r"(?<![=&?}\w./-])/(?:[A-Za-z0-9._~+ -]+/)+"
            r"[A-Za-z0-9._~+ -]+\.(?:pdf|docx?|xlsx?|pptx?|rtf|txt|md|py|json|ya?ml|"
            r"csv|tsv|zip|gz|tar|tex|bib|log)",
            re.I,
        ),
    ),
    ("tilde home path", re.compile(r"(?<![\w.~-])~[/\\][^\s`'\"<>|]+")),
    (
        "Windows absolute path",
        re.compile(
            r"\b[A-Za-z]:[\\/]+(?:[^\\/:*?\"<>|\r\n]+[\\/]+)*"
            r"[^\\/:*?\"<>|\r\n]+",
            re.I,
        ),
    ),
    (
        "UNC path",
        re.compile(r"(?<!\\)\\\\[A-Za-z0-9._-]+\\[^\\\s:*?\"<>|]+", re.I),
    ),
    ("local file URL", re.compile(r"\bfile:" r"/+", re.I)),
    (
        "case-specific identifier",
        re.compile(
            r"\b(?:submission|manuscript|case|review(?:er)?)\s*"
            r"(?:id|identifier|number|no\.?|reference|ref\.?|code|#)(?![A-Za-z])"
            r"[\s*_`|:：=\-–—]{1,24}(?:is[\s*_`|:：=\-–—]+)?"
            r"(?:[A-Z]{2,12}\d{4,}|[A-Z]{2,12}-\d{4,}|"
            r"[A-Z]{1,12}(?:-[A-Z0-9]{1,12}){2,}|"
            r"\d{3,}(?:-\d{2,})+|\d{4,}|"
            r"[0-9a-f]{8}(?:-[0-9a-f]{4}){2,})\b",
            re.I,
        ),
    ),
    (
        "journal-style submission identifier",
        re.compile(
            r"\b(?:[A-Z]{2,10}(?:[-_][A-Z]{2,10})?[-_]\d{4}"
            r"(?:[-_]\d{1,6}){1,3}|[A-Z]{2,10}-[A-Z]-\d{2}-\d{4,6}|"
            r"(?:MSOM|MNSC|OPRE|MKSC)[-_]\d{4,})\b"
        ),
    ),
    ("US Social Security number", re.compile(r"(?<!\d)\d{3}-\d{2}-\d{4}(?!\d)")),
    ("ORCID identifier", re.compile(r"\bORCID\s*(?:iD)?\s*[:=]?\s*\d{4}-\d{4}-\d{4}-[\dX]{4}\b", re.I)),
    (
        "labelled phone number",
        re.compile(r"\b(?:phone|mobile|telephone|tel)\s*[:=]\s*\+?[\d ()-]{7,}\d", re.I),
    ),
    ("private key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("GitHub token", re.compile(r"\b(?:gh[opsu]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b")),
    ("OpenAI-style secret", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
)

LABELLED_PRIVATE_VALUE_RE = re.compile(
    r"(?im)^\s*(?:[-*]\s*)?(?:\|\s*)?[*_`]*"
    r"(?P<label>(?:submission|manuscript|case|review(?:er)?)\s*"
    r"(?:id|identifier|number|no\.?|reference|ref\.?|code|#)|"
    r"(?:author|reviewer|editor)(?:\s+name)?)"
    r"[*_`]*\s*(?::|=|：|\|)\s*[*_`]*"
    r"(?P<value>\S.*)$"
)
PLACEHOLDER_TOKEN = (
    r"(?:redacted|placeholder|id|name|value|unknown|none|n/?a|"
    r"synthetic(?:[-_ ](?:id|name|value))?)"
)
PLACEHOLDER_VALUE_RE = re.compile(
    rf"^(?:\[{PLACEHOLDER_TOKEN}\]|<{PLACEHOLDER_TOKEN}>|"
    rf"\{{{PLACEHOLDER_TOKEN}\}}|{PLACEHOLDER_TOKEN})"
    r"(?:\s*\((?:fully\s+synthetic|placeholder)\))?$",
    re.I,
)


def run_git(*arguments: str) -> bytes:
    command = ["git", "-C", str(ROOT), *arguments]
    try:
        completed = subprocess.run(
            command,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except OSError as exc:
        raise RuntimeError(f"could not execute git: {exc}") from exc
    if completed.returncode != 0:
        detail = completed.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"{' '.join(command[:3])} failed: {detail}")
    return completed.stdout


def git_file_set(*arguments: str) -> set[str]:
    output = run_git("ls-files", "-z", *arguments)
    return {item.decode("utf-8") for item in output.split(b"\0") if item}


def validate_repository_root(errors: list[str]) -> None:
    try:
        top_level = Path(run_git("rev-parse", "--show-toplevel").decode().strip()).resolve()
    except (RuntimeError, OSError) as exc:
        errors.append(str(exc))
        return
    if top_level != ROOT:
        errors.append(f"validator root {ROOT} is not the Git top level {top_level}")


def parse_manifest(errors: list[str]) -> set[str]:
    try:
        lines = MANIFEST_PATH.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        errors.append(f"cannot read .public-release-files: {exc}")
        return set()

    entries: list[str] = []
    for line_number, raw_line in enumerate(lines, start=1):
        value = raw_line.strip()
        if not value or value.startswith("#"):
            continue
        if value != raw_line:
            errors.append(f".public-release-files:{line_number}: surrounding whitespace")
        if "\\" in value:
            errors.append(f".public-release-files:{line_number}: use POSIX separators")
        path = PurePosixPath(value)
        if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
            errors.append(f".public-release-files:{line_number}: unsafe path {value!r}")
        if path.as_posix() != value:
            errors.append(f".public-release-files:{line_number}: non-normalized path {value!r}")
        entries.append(value)

    if len(entries) != len(set(entries)):
        errors.append(".public-release-files contains duplicate entries")
    if entries != sorted(entries):
        errors.append(".public-release-files entries must be sorted")

    manifest = set(entries)
    for missing in sorted(REQUIRED_RELEASE_FILES - manifest):
        errors.append(f"release manifest omits required file: {missing}")
    return manifest


def allowed_location(relative_path: str) -> bool:
    path = PurePosixPath(relative_path)
    if relative_path in {
        ".gitignore",
        ".public-release-files",
        "CHANGELOG.md",
        "CONTRIBUTING.md",
        "LICENSE",
        "README.md",
        "SECURITY.md",
        "SKILL.md",
        "agents/openai.yaml",
        "scripts/validate_public_skill.py",
        ".github/workflows/validate.yml",
        ".github/ISSUE_TEMPLATE/config.yml",
        ".github/PULL_REQUEST_TEMPLATE.md",
    }:
        return True
    if len(path.parts) == 2 and path.parts[0] in {"assets", "references"}:
        return path.suffix == ".md"
    if len(path.parts) == 2 and path.parts[0] == "examples":
        return path.suffix == ".md"
    if path.parts and path.parts[0] == "evals":
        return path.suffix in {".json", ".md"}
    if (
        len(path.parts) == 3
        and path.parts[:2] == (".github", "ISSUE_TEMPLATE")
        and path.suffix == ".yml"
    ):
        return path.name in {"bug_report.yml", "feature_request.yml"}
    return False


def validate_release_surface(manifest: set[str], errors: list[str]) -> set[str]:
    try:
        tracked = git_file_set("--cached")
        candidates = git_file_set("--cached", "--others", "--exclude-standard")
    except (RuntimeError, UnicodeError) as exc:
        errors.append(str(exc))
        return set()

    for path in sorted(tracked - manifest):
        errors.append(f"tracked file is not on the public release manifest: {path}")
    for path in sorted(candidates - manifest):
        errors.append(f"non-ignored file is not on the public release manifest: {path}")
    for path in sorted(manifest - candidates):
        errors.append(f"release manifest entry is missing from the working tree: {path}")

    casefolded: dict[str, str] = {}
    for relative_path in sorted(manifest):
        folded = relative_path.casefold()
        if folded in casefolded and casefolded[folded] != relative_path:
            errors.append(
                "case-insensitive path collision: "
                f"{casefolded[folded]!r} and {relative_path!r}"
            )
        casefolded[folded] = relative_path

        if not allowed_location(relative_path):
            errors.append(f"path is outside the structural allowlist: {relative_path}")

        path = PurePosixPath(relative_path)
        suffix = path.suffix.lower()
        inner_suffixes = {item.lower() for item in path.suffixes[:-1]}
        disguised_suffixes = inner_suffixes & (
            FORBIDDEN_BINARY_SUFFIXES | FORBIDDEN_DATA_SUFFIXES
        )
        spaced_disguise = re.search(
            r"\.(?:7z|csv|docx?|gz|pdf|pptx?|rar|rtf|tar|tgz|tsv|xlsx?|zip)"
            r"\s+\.(?:json|md|py|txt|ya?ml)$",
            path.name,
            flags=re.I,
        )
        if disguised_suffixes:
            errors.append(
                f"forbidden disguised inner extension in {relative_path}: "
                f"{', '.join(sorted(disguised_suffixes))}"
            )
        if spaced_disguise:
            errors.append(f"forbidden spaced double extension in {relative_path}")
        if suffix in FORBIDDEN_BINARY_SUFFIXES:
            errors.append(f"manuscript/report binary format is forbidden: {relative_path}")
        elif suffix in FORBIDDEN_DATA_SUFFIXES:
            errors.append(f"case/data artifact format is forbidden: {relative_path}")
        elif suffix and suffix not in ALLOWED_SUFFIXES:
            errors.append(f"file extension is not allowed: {relative_path}")

        for component in path.parts[:-1]:
            normalized = component.casefold().replace("_", "-")
            if normalized in FORBIDDEN_DIRECTORY_NAMES:
                errors.append(f"private/case directory is forbidden: {relative_path}")

        if relative_path not in GENERIC_PUBLIC_TEMPLATES:
            for pattern in FORBIDDEN_PATH_NAME_PATTERNS:
                if pattern.search(path.name):
                    errors.append(f"case-specific filename is forbidden: {relative_path}")
                    break

    return candidates


def validate_staged_worktree_consistency(
    manifest: set[str], errors: list[str]
) -> None:
    """Prevent clean working-tree bytes from masking different staged bytes."""
    try:
        staged = {
            item.decode("utf-8")
            for item in run_git(
                "diff", "--cached", "--name-only", "-z", "--diff-filter=ACDMRT"
            ).split(b"\0")
            if item
        }
        deleted = {
            item.decode("utf-8")
            for item in run_git(
                "diff", "--cached", "--name-only", "-z", "--diff-filter=D"
            ).split(b"\0")
            if item
        }
    except (RuntimeError, UnicodeError) as exc:
        errors.append(f"cannot inspect staged release bytes: {exc}")
        return

    for relative_path in sorted(staged & manifest):
        if relative_path in deleted:
            errors.append(f"staged deletion removes public release file: {relative_path}")
            continue
        path = ROOT / relative_path
        try:
            worktree_data = path.read_bytes()
            staged_data = run_git("show", f":{relative_path}")
        except (OSError, RuntimeError) as exc:
            errors.append(f"cannot compare staged release file {relative_path}: {exc}")
            continue
        if staged_data != worktree_data:
            errors.append(
                f"staged and working-tree bytes differ for {relative_path}; "
                "stage the reviewed bytes or unstage the file before release validation"
            )


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def validate_frontmatter(errors: list[str]) -> None:
    skill_path = ROOT / "SKILL.md"
    try:
        text = skill_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        errors.append(f"SKILL.md: cannot read UTF-8 text: {exc}")
        return

    lines = text.splitlines()
    if not lines or lines[0] != "---":
        errors.append("SKILL.md: frontmatter must start on the first line with ---")
        return
    try:
        closing = lines.index("---", 1)
    except ValueError:
        errors.append("SKILL.md: frontmatter has no closing --- delimiter")
        return
    if closing > 50:
        errors.append("SKILL.md: frontmatter is unexpectedly long")

    values: dict[str, str] = {}
    key_re = re.compile(r"^[A-Za-z][A-Za-z0-9_-]*$")
    for number, line in enumerate(lines[1:closing], start=2):
        if not line or line.lstrip().startswith("#"):
            continue
        if line[:1].isspace() or ":" not in line:
            errors.append(f"SKILL.md:{number}: frontmatter must use simple key: value fields")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not key_re.fullmatch(key):
            errors.append(f"SKILL.md:{number}: invalid frontmatter key {key!r}")
        if key in values:
            errors.append(f"SKILL.md:{number}: duplicate frontmatter key {key!r}")
        if not value or value in {"|", ">", "|-", ">-"}:
            errors.append(f"SKILL.md:{number}: frontmatter value must be a non-empty scalar")
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
            value = value[1:-1]
        values[key] = value

    name = values.get("name", "")
    description = values.get("description", "")
    if not name:
        errors.append("SKILL.md: frontmatter requires name")
    elif not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        errors.append("SKILL.md: name must be lowercase kebab-case")
    elif name != ROOT.name:
        errors.append(f"SKILL.md: name {name!r} must match directory name {ROOT.name!r}")
    if not description:
        errors.append("SKILL.md: frontmatter requires description")
    elif len(description) > 1_024:
        errors.append("SKILL.md: frontmatter description exceeds 1,024 characters")
    if closing + 1 >= len(lines) or not any(line.strip() for line in lines[closing + 1 :]):
        errors.append("SKILL.md: document body is empty")


def parse_openai_yaml_quoted_string(
    raw_value: str,
    number: int,
    field: str,
    errors: list[str],
) -> str | None:
    """Parse the deliberately small quoted-string subset supported here."""
    location = f"agents/openai.yaml:{number}: {field}"
    if len(raw_value) < 2 or raw_value[0] not in {'"', "'"}:
        errors.append(f"{location} must be a quoted one-line string")
        return None

    if raw_value[0] == '"':
        try:
            value = json.loads(raw_value)
        except json.JSONDecodeError:
            errors.append(
                f"{location} uses unsupported quoted-scalar syntax; "
                "use a JSON-compatible double-quoted string"
            )
            return None
        if not isinstance(value, str):
            errors.append(f"{location} must be a quoted one-line string")
            return None
    else:
        if raw_value[-1] != "'":
            errors.append(f"{location} has an unterminated single-quoted string")
            return None
        inner = raw_value[1:-1]
        characters: list[str] = []
        index = 0
        while index < len(inner):
            if inner[index] != "'":
                characters.append(inner[index])
                index += 1
                continue
            if index + 1 >= len(inner) or inner[index + 1] != "'":
                errors.append(
                    f"{location} uses unsupported single-quoted syntax; "
                    "escape an apostrophe as two single quotes"
                )
                return None
            characters.append("'")
            index += 2
        value = "".join(characters)

    if any(ord(character) < 32 for character in value):
        errors.append(f"{location} must not contain control characters")
        return None
    if not value:
        errors.append(f"{location} must not be empty")
        return None
    return value


def validate_openai_yaml(errors: list[str]) -> None:
    """Validate the fixed, two-level agents/openai.yaml subset used by this Skill."""
    try:
        text = OPENAI_YAML_PATH.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        errors.append(f"agents/openai.yaml: cannot read UTF-8 text: {exc}")
        return

    if not text.strip():
        errors.append("agents/openai.yaml: file is empty")
        return

    expected_fields = {
        "interface": OPENAI_YAML_INTERFACE_FIELDS,
        "policy": OPENAI_YAML_POLICY_FIELDS,
    }
    values: dict[str, dict[str, object]] = {
        "interface": {},
        "policy": {},
    }
    section_lines: dict[str, int] = {}
    field_lines: dict[str, dict[str, int]] = {
        "interface": {},
        "policy": {},
    }
    current_section: str | None = None
    top_level_re = re.compile(r"^(?P<key>[A-Za-z_][A-Za-z0-9_-]*):$")
    field_re = re.compile(
        r"^  (?P<key>[A-Za-z_][A-Za-z0-9_-]*): (?P<value>.+)$"
    )

    for number, raw_line in enumerate(text.splitlines(), start=1):
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if "\t" in raw_line:
            errors.append(
                f"agents/openai.yaml:{number}: tabs are not supported; use two-space indentation"
            )
            current_section = None
            continue
        if raw_line != raw_line.rstrip():
            errors.append(f"agents/openai.yaml:{number}: trailing whitespace is not allowed")
            raw_line = raw_line.rstrip()

        top_level_match = top_level_re.fullmatch(raw_line)
        if top_level_match:
            section = top_level_match.group("key")
            if section not in expected_fields:
                errors.append(
                    f"agents/openai.yaml:{number}: unsupported top-level key {section!r}; "
                    "only 'interface' and 'policy' are allowed"
                )
                current_section = None
                continue
            if section in section_lines:
                errors.append(
                    f"agents/openai.yaml:{number}: duplicate top-level key {section!r} "
                    f"(first declared on line {section_lines[section]})"
                )
            else:
                section_lines[section] = number
            current_section = section
            continue

        field_match = field_re.fullmatch(raw_line)
        if not field_match:
            errors.append(
                f"agents/openai.yaml:{number}: unsupported syntax; expected a top-level "
                "'interface:' or 'policy:' mapping, or a two-space-indented 'key: value' field"
            )
            current_section = None
            continue
        if current_section is None:
            errors.append(
                f"agents/openai.yaml:{number}: field appears outside a supported mapping"
            )
            continue

        key = field_match.group("key")
        raw_value = field_match.group("value")
        if key not in expected_fields[current_section]:
            errors.append(
                f"agents/openai.yaml:{number}: unsupported field "
                f"{current_section}.{key}"
            )
            continue
        if key in field_lines[current_section]:
            errors.append(
                f"agents/openai.yaml:{number}: duplicate field {current_section}.{key} "
                f"(first declared on line {field_lines[current_section][key]})"
            )
            continue
        field_lines[current_section][key] = number

        if current_section == "interface":
            parsed = parse_openai_yaml_quoted_string(raw_value, number, key, errors)
            if parsed is not None:
                values[current_section][key] = parsed
        elif raw_value in {"true", "false"}:
            values[current_section][key] = raw_value == "true"
        else:
            errors.append(
                f"agents/openai.yaml:{number}: policy.{key} must be the explicit "
                "boolean true or false"
            )

    for section in ("interface", "policy"):
        if section not in section_lines:
            errors.append(f"agents/openai.yaml: missing required top-level mapping {section!r}")
        for field in sorted(expected_fields[section] - values[section].keys()):
            errors.append(f"agents/openai.yaml: missing required field {section}.{field}")

    short_description = values["interface"].get("short_description")
    if isinstance(short_description, str) and not 25 <= len(short_description) <= 64:
        errors.append(
            "agents/openai.yaml: interface.short_description must be 25-64 characters "
            f"(found {len(short_description)})"
        )

    default_prompt = values["interface"].get("default_prompt")
    if isinstance(default_prompt, str) and OPENAI_YAML_SKILL_TOKEN not in default_prompt:
        errors.append(
            "agents/openai.yaml: interface.default_prompt must contain "
            f"{OPENAI_YAML_SKILL_TOKEN!r}"
        )

    allow_implicit_invocation = values["policy"].get("allow_implicit_invocation")
    if (
        isinstance(allow_implicit_invocation, bool)
        and allow_implicit_invocation is not OPENAI_YAML_ALLOW_IMPLICIT_INVOCATION
    ):
        errors.append(
            "agents/openai.yaml: policy.allow_implicit_invocation must be true "
            "to match the public invocation contract"
        )


def validate_file_bytes(relative_path: str, errors: list[str]) -> str | None:
    path = ROOT / relative_path
    if path.is_symlink():
        errors.append(f"symbolic links are not allowed in the public release: {relative_path}")
        return None
    try:
        data = path.read_bytes()
    except OSError as exc:
        errors.append(f"cannot read {relative_path}: {exc}")
        return None
    if len(data) > MAX_PUBLIC_FILE_BYTES:
        errors.append(f"public file exceeds 1 MiB: {relative_path}")
    for signature, description in MAGIC_SIGNATURES.items():
        position = data.find(signature, 0, 1024 + len(signature) - 1)
        if 0 <= position < 1024:
            errors.append(f"{relative_path}: disguised {description} content is forbidden")
    if b"\0" in data:
        errors.append(f"{relative_path}: NUL byte/binary content is forbidden")
        return None
    try:
        text = data.decode("utf-8")
    except UnicodeError as exc:
        errors.append(f"{relative_path}: file is not valid UTF-8 text: {exc}")
        return None
    if not text.strip():
        errors.append(f"{relative_path}: public file must not be empty")
    return text


def markdown_visible_lines(text: str) -> list[str]:
    """Return Markdown lines outside comments and code-like non-prose blocks."""
    text = re.sub(r"<!--.*?(?:-->|$)", "", text, flags=re.DOTALL)
    text = re.sub(r"<\?.*?(?:\?>|$)", "", text, flags=re.DOTALL)
    text = re.sub(r"<!\[CDATA\[.*?(?:\]\]>|$)", "", text, flags=re.I | re.DOTALL)
    text = re.sub(r"<![A-Za-z].*?(?:>|$)", "", text, flags=re.DOTALL)
    text = re.sub(
        r"<(?P<html_tag>[A-Za-z][A-Za-z0-9-]*)\b[^>]*>.*?"
        r"</(?P=html_tag)\s*>",
        "",
        text,
        flags=re.I | re.DOTALL,
    )
    hidden_html = (
        r"pre|code|script|style|textarea|template|xmp|details|div|span|section|aside|p"
    )
    text = re.sub(
        rf"<(?P<tag>{hidden_html})\b[^>]*>.*?</(?P=tag)\s*>",
        "",
        text,
        flags=re.I | re.DOTALL,
    )
    text = re.sub(
        r"<[A-Za-z][A-Za-z0-9-]*\b"
        r"(?=[^>]*(?:\bhidden\b|aria-hidden\s*=|display\s*:\s*none|"
        r"visibility\s*:\s*hidden))[^>]*>.*$",
        "",
        text,
        flags=re.I | re.DOTALL,
    )
    text = re.sub(
        rf"<(?:{hidden_html})\b[^>]*>.*$",
        "",
        text,
        flags=re.I | re.DOTALL,
    )

    visible: list[str] = []
    open_fence: tuple[str, int] | None = None
    for line in text.splitlines():
        structural = re.sub(r"^(?: {0,3}>[ \t]?)*", "", line)
        structural = re.sub(r"^(?: {0,3}(?:[-*+]|\d+[.)])[ \t]+)?", "", structural)
        fence = re.match(r"^(?P<fence>`{3,}|~{3,})", structural)
        if open_fence is not None:
            character, minimum_length = open_fence
            if fence and fence.group("fence")[0] == character and len(
                fence.group("fence")
            ) >= minimum_length:
                open_fence = None
            continue
        if fence:
            token = fence.group("fence")
            open_fence = (token[0], len(token))
            continue
        if line.startswith(("    ", "\t")):
            continue
        visible.append(line)
    return visible


def validate_required_document_markers(errors: list[str]) -> None:
    """Keep release-critical documents from degrading into hidden placeholders."""
    for relative_path, markers in REQUIRED_DOCUMENT_MARKERS.items():
        path = ROOT / relative_path
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            continue
        if relative_path == "LICENSE":
            canonical_license = text.replace("\r\n", "\n").replace("\r", "\n")
            if hashlib.sha256(canonical_license.encode("utf-8")).hexdigest() != (
                EXPECTED_LICENSE_SHA256
            ):
                errors.append(
                    "LICENSE differs from the reviewed MIT license text; review it "
                    "and update the expected digest deliberately"
                )
        visible_lines = (
            markdown_visible_lines(text)
            if PurePosixPath(relative_path).suffix.lower() == ".md"
            else text.splitlines()
        )
        visible_text = "\n".join(visible_lines)
        for marker in markers:
            if marker.startswith("#"):
                present = visible_lines.count(marker) == 1
            else:
                present = marker in visible_text
            if not present:
                errors.append(f"{relative_path}: missing required release marker {marker!r}")
        for required_line in REQUIRED_DOCUMENT_VISIBLE_LINES.get(relative_path, ()):
            if visible_lines.count(required_line) != 1:
                errors.append(
                    f"{relative_path}: missing required visible release line "
                    f"{required_line!r}"
                )


def validate_private_content(relative_path: str, text: str, errors: list[str]) -> None:
    scan_variants = [text]
    if relative_path != "scripts/validate_public_skill.py":
        for candidate in (text.replace(r"\/", "/"), text.replace(r"\\", "\\")):
            if candidate not in scan_variants:
                scan_variants.append(candidate)

    for description, pattern in FORBIDDEN_CONTENT_PATTERNS:
        matched_text: str | None = None
        match: re.Match[str] | None = None
        for candidate in scan_variants:
            match = pattern.search(candidate)
            if match:
                matched_text = candidate
                break
        if match:
            errors.append(
                f"{relative_path}:{line_number(matched_text or text, match.start())}: "
                f"possible private data ({description})"
            )

    for match in LABELLED_PRIVATE_VALUE_RE.finditer(text):
        value = match.group("value").strip().strip("*_`")
        if not PLACEHOLDER_VALUE_RE.fullmatch(value):
            errors.append(
                f"{relative_path}:{line_number(text, match.start())}: "
                f"possible case-specific value after {match.group('label')!r}"
            )


def normalized_local_target(source: Path, raw_target: str) -> tuple[Path | None, str | None]:
    target = raw_target.strip().strip("<>")
    if not target or target.startswith("#"):
        return None, None
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc or target.startswith("//"):
        return None, None
    path_text = unquote(parsed.path)
    if not path_text:
        return None, None
    if path_text.startswith(("/", "~")) or re.match(r"^[A-Za-z]:[\\/]", path_text):
        return None, "absolute local path"

    candidate = (source.parent / path_text).resolve()
    try:
        candidate.relative_to(ROOT)
    except ValueError:
        return None, "path escapes repository"
    return candidate, None


def validate_reference(
    source_relative: str,
    raw_target: str,
    manifest: set[str],
    errors: list[str],
) -> None:
    source = ROOT / source_relative
    target, problem = normalized_local_target(source, raw_target)
    if problem:
        errors.append(f"{source_relative}: unsafe local reference {raw_target!r}: {problem}")
        return
    if target is None:
        return

    # Backticked paths in root documents conventionally use repository-root
    # notation. Try that interpretation if normal Markdown-relative resolution
    # did not find the target.
    if not target.exists() and not raw_target.startswith((".", "/", "~")):
        root_candidate = (ROOT / unquote(urlsplit(raw_target).path)).resolve()
        try:
            root_candidate.relative_to(ROOT)
        except ValueError:
            pass
        else:
            if root_candidate.exists():
                target = root_candidate

    if not target.exists():
        errors.append(f"{source_relative}: referenced local target does not exist: {raw_target}")
        return
    if target.is_file():
        target_relative = target.relative_to(ROOT).as_posix()
        if target_relative not in manifest:
            errors.append(
                f"{source_relative}: referenced file is not on release manifest: {target_relative}"
            )


def validate_markdown_references(
    relative_path: str, text: str, manifest: set[str], errors: list[str]
) -> None:
    targets: set[str] = set()
    targets.update(match.group("target") for match in MARKDOWN_LINK_RE.finditer(text))
    targets.update(match.group("target") for match in INLINE_LOCAL_PATH_RE.finditer(text))
    for target in sorted(targets):
        validate_reference(relative_path, target.rstrip(".,;:"), manifest, errors)


def validate_json_references(
    relative_path: str, text: str, manifest: set[str], errors: list[str]
) -> None:
    try:
        document = json.loads(text)
    except json.JSONDecodeError as exc:
        errors.append(f"{relative_path}:{exc.lineno}: invalid JSON: {exc.msg}")
        return

    def strings(value: object):
        if isinstance(value, str):
            yield value
        elif isinstance(value, list):
            for item in value:
                yield from strings(item)
        elif isinstance(value, dict):
            for item in value.values():
                yield from strings(item)

    for value in strings(document):
        if not re.fullmatch(r"[A-Za-z0-9._/-]+\.(?:json|md|py|ya?ml)", value):
            continue
        source = ROOT / relative_path
        candidates = [
            (source.parent / value).resolve(),
            (ROOT / "evals" / value).resolve(),
            (ROOT / value).resolve(),
        ]
        target = next((candidate for candidate in candidates if candidate.exists()), None)
        if target is None:
            errors.append(f"{relative_path}: referenced local target does not exist: {value}")
            continue
        try:
            target_relative = target.relative_to(ROOT).as_posix()
        except ValueError:
            errors.append(f"{relative_path}: referenced path escapes repository: {value}")
            continue
        if target.is_file() and target_relative not in manifest:
            errors.append(
                f"{relative_path}: referenced file is not on release manifest: {target_relative}"
            )


def validate_issue_templates(errors: list[str]) -> None:
    config = ROOT / ".github/ISSUE_TEMPLATE/config.yml"
    try:
        config_bytes = config.read_bytes()
        config_text = config_bytes.decode("utf-8")
    except (OSError, UnicodeError):
        return
    config_text = config_text.replace("\r\n", "\n").replace("\r", "\n")
    if hashlib.sha256(config_text.encode("utf-8")).hexdigest() != EXPECTED_ISSUE_TEMPLATE_SHA256[
        "config.yml"
    ]:
        errors.append(
            "issue-template config differs from the reviewed fail-closed form; "
            "review it and update the expected digest deliberately"
        )
    if "#" in config_text:
        errors.append("issue-template config must not use YAML comments")
    blank_issue_declarations = [
        line
        for line in config_text.splitlines()
        if re.match(r"^blank_issues_enabled\s*:", line)
    ]
    if blank_issue_declarations != ["blank_issues_enabled: false"]:
        errors.append("issue-template config must disable blank issues")

    for filename in ("bug_report.yml", "feature_request.yml"):
        path = ROOT / ".github/ISSUE_TEMPLATE" / filename
        try:
            form_bytes = path.read_bytes()
            text = form_bytes.decode("utf-8")
        except (OSError, UnicodeError):
            continue
        text = text.replace("\r\n", "\n").replace("\r", "\n")
        relative_path = path.relative_to(ROOT).as_posix()
        if hashlib.sha256(text.encode("utf-8")).hexdigest() != EXPECTED_ISSUE_TEMPLATE_SHA256[
            filename
        ]:
            errors.append(
                f"{relative_path}: form differs from the reviewed fail-closed version; "
                "review it and update the expected digest deliberately"
            )

        # Comments are unnecessary in these fixed forms and can otherwise make
        # raw substring checks look satisfied while rendering no safeguard.
        in_literal_block = False
        literal_indent = -1
        for number, line in enumerate(text.splitlines(), start=1):
            indent = len(line) - len(line.lstrip(" "))
            if in_literal_block and line.strip() and indent <= literal_indent:
                in_literal_block = False
            if not in_literal_block and "#" in line:
                errors.append(
                    f"{relative_path}:{number}: YAML comments are not allowed in issue forms"
                )
            if not in_literal_block and re.search(r":\s*[>|][+-]?\s*$", line):
                in_literal_block = True
                literal_indent = indent

        warning_sequence = (
            "  - type: markdown\n"
            "    attributes:\n"
            "      value: |\n"
            "        ## Privacy notice\n"
            f"{ISSUE_PRIVACY_WARNING_LINE}"
        )
        confirmation_sequence = (
            "  - type: checkboxes\n"
            "    id: privacy\n"
            "    attributes:\n"
            "      label: Privacy confirmation\n"
            "      options:\n"
            f"        - label: {ISSUE_PRIVACY_CONFIRMATION}\n"
            "          required: true"
        )
        if text.count(warning_sequence) != 1:
            errors.append(f"{relative_path}: missing the visible privacy-warning block")
        if text.count(confirmation_sequence) != 1:
            errors.append(f"{relative_path}: missing the required privacy checkbox structure")


def validate_pull_request_template(errors: list[str]) -> None:
    """Require a visible warning and an explicit privacy confirmation checkbox."""
    relative_path = PULL_REQUEST_TEMPLATE_PATH.relative_to(ROOT).as_posix()
    try:
        text = PULL_REQUEST_TEMPLATE_PATH.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        errors.append(f"{relative_path}: cannot read UTF-8 text: {exc}")
        return
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    if hashlib.sha256(text.encode("utf-8")).hexdigest() != (
        EXPECTED_PULL_REQUEST_TEMPLATE_SHA256
    ):
        errors.append(
            f"{relative_path}: template differs from the reviewed fail-closed version; "
            "review it and update the expected digest deliberately"
        )

    # HTML comments and code blocks are not actionable safeguards. Strip comments
    # and reject raw HTML or fenced code so hidden/non-actionable examples cannot
    # satisfy or contradict the privacy contract by accident.
    without_comments = re.sub(r"<!--.*?(?:-->|$)", "", text, flags=re.DOTALL)
    if re.search(r"<(?:/?[A-Za-z]|\?|!)", without_comments):
        errors.append(
            f"{relative_path}: raw HTML is not allowed in the pull request template"
        )
    if re.search(
        r"(?m)^[ \t]*(?:>[ \t]*)*(?:[-*+][ \t]+)?(?:`{3,}|~{3,})",
        without_comments,
    ):
        errors.append(
            f"{relative_path}: fenced code is not allowed in the pull request template"
        )
    visible_lines: list[str] = []
    open_fence: tuple[str, int] | None = None
    for line in without_comments.splitlines():
        if open_fence is not None:
            character, minimum_length = open_fence
            closing = re.fullmatch(
                rf" {{0,3}}{re.escape(character)}{{{minimum_length},}}[ \t]*",
                line,
            )
            if closing:
                open_fence = None
            continue

        opening = re.match(r"^ {0,3}(?P<fence>`{3,}|~{3,})(?:[^\n]*)$", line)
        if opening:
            fence = opening.group("fence")
            open_fence = (fence[0], len(fence))
            continue
        if line.startswith(("    ", "\t")):
            continue
        visible_lines.append(line)

    visible_text = "\n".join(visible_lines)
    normalized = visible_text.casefold()

    privacy_concepts = {
        "manuscript": re.compile(r"\bmanuscripts?\b", re.I),
        "referee report": re.compile(r"\breferee\s+reports?\b", re.I),
        "decision letter": re.compile(r"\bdecision\s+letters?\b", re.I),
        "author response": re.compile(r"\bauthor\s+responses?\b", re.I),
        "personal information": re.compile(r"\bpersonal\s+information\b", re.I),
    }
    for concept, pattern in privacy_concepts.items():
        if not pattern.search(visible_text):
            errors.append(
                f"{relative_path}: privacy warning omits {concept!r}"
            )

    if (
        "privacy" not in normalized
        or visible_text.count(PULL_REQUEST_PRIVACY_WARNING_BLOCK) != 1
    ):
        errors.append(f"{relative_path}: missing a visible privacy warning")

    task_lines = [
        line
        for line in without_comments.splitlines()
        if re.match(
            r"^(?: {0,3}>[ \t]?)*[ \t]*[-*+]\s+\[[ xX]\]\s+\S",
            line,
        )
    ]
    if task_lines != list(PULL_REQUEST_REQUIRED_TASK_LINES):
        errors.append(
            f"{relative_path}: task-list structure must exactly match the required "
            "privacy and validation checklist"
        )


def validate_workflow(errors: list[str]) -> None:
    """Pin the CI release gate so it cannot silently become a no-op."""
    relative_path = WORKFLOW_PATH.relative_to(ROOT).as_posix()
    try:
        text = WORKFLOW_PATH.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        errors.append(f"{relative_path}: cannot read UTF-8 text: {exc}")
        return
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    if hashlib.sha256(text.encode("utf-8")).hexdigest() != EXPECTED_WORKFLOW_SHA256:
        errors.append(
            f"{relative_path}: workflow differs from the reviewed release gate; "
            "review it and update the expected digest deliberately"
        )


def main() -> int:
    errors: list[str] = []
    validate_repository_root(errors)
    manifest = parse_manifest(errors)
    candidates = validate_release_surface(manifest, errors)
    validate_staged_worktree_consistency(manifest, errors)
    validate_frontmatter(errors)
    validate_openai_yaml(errors)
    validate_required_document_markers(errors)

    for relative_path in sorted(manifest & candidates):
        text = validate_file_bytes(relative_path, errors)
        if text is None:
            continue
        suffix = PurePosixPath(relative_path).suffix.lower()
        validate_private_content(relative_path, text, errors)
        if suffix == ".md":
            validate_markdown_references(relative_path, text, manifest, errors)
        elif suffix == ".json":
            validate_json_references(relative_path, text, manifest, errors)

    validate_issue_templates(errors)
    validate_pull_request_template(errors)
    validate_workflow(errors)

    if errors:
        print("Public-skill validation failed:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    tracked_count = len(git_file_set("--cached"))
    print(
        f"Public-skill validation passed: {len(manifest)} allowlisted files "
        f"({tracked_count} currently tracked)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
