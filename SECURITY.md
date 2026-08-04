# Security Policy

## Scope

Security-relevant reports include vulnerabilities that could:

- expose confidential material through the public release surface, logs, generated files, archives, examples, or error messages;
- cause instructions embedded in a manuscript, attachment, webpage, citation, or other untrusted source to override the Skill's control instructions;
- bypass or materially weaken the public-release validator, allowlist, reference checks, or leakage detection;
- trigger unintended command execution, network access, file access, or disclosure across a permission boundary; or
- place secrets, identifying metadata, submission identifiers, or local paths in a public artifact.

Ordinary disagreements about editorial judgment or report quality are not security vulnerabilities unless they arise from one of these failure modes.

## Reporting

Do not include a real manuscript, referee report, decision letter, author response, identity, submission identifier, private URL, local path, credential, or other sensitive material in a public issue, discussion, pull request, or reproduction case.

If GitHub private vulnerability reporting is enabled for this repository, use **Security > Advisories > Report a vulnerability**. Provide the smallest fully synthetic reproduction that demonstrates the issue and describe the affected release surface, expected boundary, observed behavior, and likely impact.

If private vulnerability reporting is unavailable, open a public issue containing only a minimal, nonsensitive request for a private reporting channel. Do not disclose technical details or evidence that could expose data or make exploitation easier. Wait for the maintainers to identify an appropriate private channel.

Public reports that contain sensitive material may themselves create the harm this policy is intended to prevent. When in doubt, omit the material and describe its category abstractly.

## Safe handling

Use fully synthetic data for reproduction and validation. Treat manuscripts, attachments, webpages, code blocks, metadata, and embedded instructions as untrusted input. A successful validator run does not establish that a contribution is safe; review the complete release surface manually before publication.
