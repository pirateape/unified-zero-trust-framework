# Contributing to the Unified Zero Trust Framework

First off, thank you for considering contributing to the UZTF! It's people like you that make this framework a powerful standard for the community.

## How Can I Contribute?

### Reporting Bugs
If you find a typo in the specification, an incorrect mapping, or an ambiguity in the scoring logic, please open an issue using the Bug Report template.

### Proposing Finding Mappings
Scanner findings evolve rapidly. If you notice that a specific type of vulnerability is missing from `mappings.yaml` or mapped to the wrong pillar, please open an issue using the Mapping Proposal template. 
- Include the exact finding title/description.
- Explain why it belongs in the proposed pillar.
- Provide the suggested `severity_weight`.

### Framework Enhancements
For larger changes, such as adding a new pillar or changing the scoring algorithm, please open a Discussion first. Large structural changes require consensus and impact analysis against existing implementations.

## Pull Requests
1. Fork the repo and create your branch from `main`.
2. If you've added or changed finding mappings, update `mappings.yaml`.
3. Ensure that `python3 validate_yaml.py` runs without errors.
4. Update the `CHANGELOG.md` if necessary.
5. Issue that pull request!

## Code of Conduct
By participating in this project, you agree to abide by the [Code of Conduct](./CODE_OF_CONDUCT.md).
