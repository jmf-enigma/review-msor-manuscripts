#!/usr/bin/env python3
"""Fail-closed checks for the public review-msor-manuscripts release.

The validator intentionally uses only the Python standard library. It checks
both tracked files and non-ignored untracked files so it is useful before a
commit as well as in CI.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / ".public-release-files"
OPENAI_YAML_PATH = ROOT / "agents/openai.yaml"
MAX_PUBLIC_FILE_BYTES = 1_048_576

OPENAI_YAML_INTERFACE_FIELDS = {
    "display_name",
    "short_description",
    "default_prompt",
}
OPENAI_YAML_POLICY_FIELDS = {"allow_implicit_invocation"}
OPENAI_YAML_SKILL_TOKEN = "$review-msor-manuscripts"

REQUIRED_RELEASE_FILES = {
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/feature_request.yml",
    ".github/workflows/validate.yml",
    ".gitignore",
    ".public-release-files",
    "LICENSE",
    "README.md",
    "SKILL.md",
    "agents/openai.yaml",
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
)

FORBIDDEN_CONTENT_PATTERNS = (
    (
        "email address",
        re.compile(r"(?<![\w.+-])[\w.+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+"),
    ),
    ("macOS home path", re.compile(r"(?<![\w.-])/Users/[A-Za-z0-9._-]+/")),
    ("Unix home path", re.compile(r"(?<![\w.-])/home/[A-Za-z0-9._-]+/")),
    (
        "Windows home path",
        re.compile(r"\b[A-Za-z]:[\\/]+Users[\\/]+[^\\/:*?\"<>|\r\n]+[\\/]", re.I),
    ),
    ("local file URL", re.compile(r"\bfile://(?:localhost)?/", re.I)),
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
    r"(?im)^\s*(?:[-*]\s*)?"
    r"(?P<label>(?:submission|manuscript|case|review(?:er)?)\s*"
    r"(?:id|number|no\.?|#)|(?:author|reviewer|editor)\s+name)\s*[:=]\s*"
    r"(?P<value>\S.*)$"
)
PLACEHOLDER_VALUE_RE = re.compile(
    r"^(?:\[[^\]]+\]|<[^>]+>|\{[^}]+\}|none|unknown|redacted|n/?a)(?:\s*[,;].*)?$",
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
        "LICENSE",
        "README.md",
        "SKILL.md",
        "agents/openai.yaml",
        "scripts/validate_public_skill.py",
        ".github/workflows/validate.yml",
        ".github/ISSUE_TEMPLATE/config.yml",
    }:
        return True
    if len(path.parts) == 2 and path.parts[0] in {"assets", "references"}:
        return path.suffix == ".md"
    if path.parts and path.parts[0] == "evals":
        return path.suffix in {".json", ".md"}
    if (
        len(path.parts) == 3
        and path.parts[:2] == (".github", "ISSUE_TEMPLATE")
        and path.suffix == ".yml"
    ):
        return True
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
        if data.startswith(signature):
            errors.append(f"{relative_path}: disguised {description} content is forbidden")
    if b"\0" in data:
        errors.append(f"{relative_path}: NUL byte/binary content is forbidden")
        return None
    try:
        return data.decode("utf-8")
    except UnicodeError as exc:
        errors.append(f"{relative_path}: file is not valid UTF-8 text: {exc}")
        return None


def validate_private_content(relative_path: str, text: str, errors: list[str]) -> None:
    for description, pattern in FORBIDDEN_CONTENT_PATTERNS:
        match = pattern.search(text)
        if match:
            errors.append(
                f"{relative_path}:{line_number(text, match.start())}: "
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
        config_text = config.read_text(encoding="utf-8").casefold()
    except (OSError, UnicodeError):
        return
    if "blank_issues_enabled: false" not in config_text:
        errors.append("issue-template config must disable blank issues")

    for filename in ("bug_report.yml", "feature_request.yml"):
        path = ROOT / ".github/ISSUE_TEMPLATE" / filename
        try:
            text = path.read_text(encoding="utf-8").casefold()
        except (OSError, UnicodeError):
            continue
        required_phrases = ("do not upload", "manuscript", "referee report", "personal")
        for phrase in required_phrases:
            if phrase not in text:
                errors.append(f"{path.relative_to(ROOT)}: privacy warning omits {phrase!r}")
        if "required: true" not in text or "i confirm" not in text:
            errors.append(f"{path.relative_to(ROOT)}: missing required privacy acknowledgement")


def main() -> int:
    errors: list[str] = []
    validate_repository_root(errors)
    manifest = parse_manifest(errors)
    candidates = validate_release_surface(manifest, errors)
    validate_frontmatter(errors)
    validate_openai_yaml(errors)

    for relative_path in sorted(manifest & candidates):
        text = validate_file_bytes(relative_path, errors)
        if text is None:
            continue
        suffix = PurePosixPath(relative_path).suffix.lower()
        if suffix in {".json", ".md", ".txt", ".yaml", ".yml"}:
            validate_private_content(relative_path, text, errors)
        if suffix == ".md":
            validate_markdown_references(relative_path, text, manifest, errors)
        elif suffix == ".json":
            validate_json_references(relative_path, text, manifest, errors)

    validate_issue_templates(errors)

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
