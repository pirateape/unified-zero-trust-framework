# Security Policy for the Unified Zero Trust Framework (UZTF)

## Supported Versions

| Version | Supported | Notes |
|---------|-----------|-------|
| 1.x     | ✅        | Current major release |

## Reporting a Vulnerability

This repository contains the **specification** for the UZTF framework — not production software. However, if you discover:

- A flaw in the framework logic that could lead to insecure posture assessments
- Incorrect or misleading security guidance
- A security issue in any reference implementation or example code

Please report it privately by emailing the repository owner or opening a [GitHub Security Advisory](https://github.com/pirateape/unified-zero-trust-framework/security/advisories).

We aim to respond within 5 business days.

## Framework Integrity

The UZTF specification is designed to be unambiguous and auditable. Proposed changes to pillar definitions, scoring rules, or CISA mappings should include:

1. A clear rationale for the change
2. Impact analysis on existing implementations
3. Cross-reference to the relevant section(s) of the CISA ZTMM

## Related

For security issues in **ApeGuard** (the reference CLI implementation of this framework), see:
https://github.com/pirateape/ape-guard/blob/main/SECURITY.md
