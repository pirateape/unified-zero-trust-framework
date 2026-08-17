# Changelog

All notable changes to the Unified Zero Trust Framework (UZTF) will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-08-17

### Added
- Expanded from 8 to 12 pillars. New pillars: IoT & OT Systems, Supply Chain, AI Systems, Resilience, Governance.
- Added quantitative severity-weighted scoring system (Critical=20, High=15, Medium=10, Low=5, Info=1).
- Added cross-cutting layers (Virtualization & Cloud, Automation & Integration, Governance & Resilience).
- Added OS-Specific Infrastructure Guidance for Windows, Linux, and macOS.
- Added `mappings.yaml` to standardize finding-to-pillar categorization.
- Added `MIGRATION_GUIDE.md` for tool builders adopting the v2.0 specification.

### Changed
- Increased maximum score from 800 to 1200.
- Renamed `Devices` pillar to `Endpoints`.
- Renamed `Visibility` pillar to `Operations`.
- Updated CISA ZTMM mapping bridge to reflect new 12-pillar structure.

## [1.0.0] - 2026-05-31

### Added
- Initial release of the Unified Zero Trust Framework.
- Defined the core 8 pillars.
- Baseline mapping to CISA Zero Trust Maturity Model.
