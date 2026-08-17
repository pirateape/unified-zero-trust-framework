# ApeGuard Migration Guide — UZTF v1.0 (8-pillar) → v2.0 (12-pillar)

**Target:** ApeGuard maintainers and contributors  
**Source:** Unified Zero Trust Framework specification repository  
**Version:** 2.0.0  
**Date:** 2026-08-17

---

## Overview

This guide documents the breaking changes required to migrate ApeGuard from the legacy 8-pillar UZTF v1.0 model to the canonical 12-pillar UZTF v2.0 model.

### Model Comparison

| Aspect | UZTF v1.0 (Legacy) | UZTF v2.0 (Canonical) |
|--------|-------------------|----------------------|
| **Pillars** | 8 | 12 |
| **Scoring** | Unweighted gap count (capped at 5) | Severity-weighted (Critical=55, High=25, Medium=10, Low=5, Info=1) |
| **Max Score** | 800 | 1200 |
| **Maturity Thresholds** | 0-50/51-80/81-100 per pillar | 4 Tiers: Initial (0-20), Baseline (21-50), Advanced (51-80), Adaptive (81-100) |

---

## Breaking Changes

### 1. Pillar Enum Changes

**Old (8 pillars):**
```rust
enum Pillar {
    Identity,
    Devices,
    Networks,
    Applications,
    Data,
    Visibility,
    Automation,
    Infrastructure,
}
```

**New (12 pillars):**
```rust
enum Pillar {
    Identity,
    Endpoints,        // renamed from Devices
    IoTOt,            // NEW
    Networks,
    Infrastructure,
    Applications,
    SupplyChain,      // NEW
    Data,
    AiSystems,        // NEW
    Operations,       // renamed from Visibility
    Resilience,       // NEW
    Governance,       // NEW
}
```

**Migration:**
- Rename `Devices` → `Endpoints`
- Rename `Visibility` → `Operations`
- Remove `Automation` (becomes cross-cutting layer)
- Add `IoTOt`, `SupplyChain`, `AiSystems`, `Resilience`, `Governance`

### 2. Scoring Algorithm Changes

**Old (v1.0):**
```rust
fn calculate_pillar_score(gap_count: u32) -> u32 {
    100.saturating_sub(gap_count.min(5) * 20)
}
```

**New (v2.0):**
```rust
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum Severity { Critical, High, Medium, Low, Info }

impl Severity {
    fn weight(&self) -> u32 {
        match self {
            Severity::Critical => 55,
            Severity::High => 25,
            Severity::Medium => 10,
            Severity::Low => 5,
            Severity::Info => 1,
        }
    }
}

fn calculate_pillar_score(findings: &[Finding]) -> u32 {
    let total_deduction: u32 = findings
        .iter()
        .map(|f| f.severity.weight())
        .sum();
    100.saturating_sub(total_deduction)
}
```

**Migration:**
- Replace gap-counting with severity-weighted summation
- Remove the 5-gap cap
- Add `severity` field to `Finding` struct
- Update all scanner adapters to populate severity

### 3. Overall Score Thresholds

**Old:**
```rust
const MAX_SCORE: u32 = 800;
const MOSTLY_ADAPTIVE_MIN: u32 = 641;
const MOSTLY_ADVANCED_MIN: u32 = 401;
const MOSTLY_BASELINE_MIN: u32 = 161;
```

**New:**
```rust
const MAX_SCORE: u32 = 1200;
const MOSTLY_ADAPTIVE_MIN: u32 = 961;
const MOSTLY_ADVANCED_MIN: u32 = 601;
const MOSTLY_BASELINE_MIN: u32 = 241;
```

### 4. Keyword Mapping File

**Old:** `mappings.yaml` with 8 pillars, duplicate keywords, no severity weights

**New:** `mappings.yaml` with 12 pillars, deduplicated keywords, severity_weight field

**Migration:**
- Replace entire `mappings.yaml` with new version from spec repo
- Update mapping loader to parse `severity_weight` field
- Add default severity weight fallback (Medium = 10)

### 5. Scanner Adapter Updates

Each scanner adapter must now emit findings with severity:

```rust
// Old
struct Finding {
    rule_id: String,
    title: String,
    description: String,
    file: String,
    line: u32,
    pillar: Pillar,  // inferred from keywords
}

// New
struct Finding {
    rule_id: String,
    title: String,
    description: String,
    file: String,
    line: u32,
    severity: Severity,  // REQUIRED
    pillar: Option<Pillar>,  // optional override
}
```

**Scanner-specific changes:**

| Scanner | Changes Required |
|---------|-----------------|
| **Gitleaks** | Map rule severity (Critical/High/Medium/Low) to UZTF severity |
| **Semgrep** | Use rule metadata `severity` field; default to Medium |
| **Trivy** | Map vulnerability severity (CRITICAL/HIGH/MEDIUM/LOW) |
| **Nuclei** | Use template severity field |

### 6. Gap Analysis Output

**Old:**
```json
{
  "pillar": "identity",
  "current_maturity": "Baseline",
  "target_maturity": "Advanced",
  "gap_level": "Small",
  "blocking_findings": 3,
  "recommendations": [...]
}
```

**New:**
```json
{
  "pillar": "identity",
  "current_maturity": "Baseline",
  "target_maturity": "Advanced",
  "gap_level": "Large",
  "blocking_findings": 4,
  "total_deduction": 75,
  "findings_by_severity": {
    "critical": 3,
    "high": 1,
    "medium": 0,
    "low": 0,
    "info": 0
  },
  "recommendations": [...]
}
```

### 7. Report Templates

Update all report generators (HTML, JSON, Markdown, SARIF) to:
- Show 12 pillars instead of 8
- Display severity-weighted scores
- Include findings_by_severity breakdown
- Update maturity classification thresholds

---

## Non-Breaking Changes (Enhancements)

### 1. OS-Specific Infrastructure Guidance

Add Windows/Linux/macOS baseline/advanced/adaptive criteria to Infrastructure pillar reporting.

### 2. Cross-Cutting Layers

Add reporting for:
- Virtualization & Cloud Layer
- Automation & Integration Layer
- Governance & Resilience Layer

### 3. Hub & Spoke Deployment Mode

Add optional `--deployment-mode hub-spoke` flag that groups pillars:
- Core: Identity, Endpoints, Networks, Infrastructure, Operations, Resilience, Governance
- Spokes: IoTOt, SupplyChain, AiSystems, Applications, Data (enhanced)

---

## Migration Checklist

### Phase 1: Core Types (Week 1)
- [ ] Update `Pillar` enum to 12 variants
- [ ] Add `Severity` enum with weights
- [ ] Update `Finding` struct with required `severity` field
- [ ] Update `PillarScore` and `Scorecard` structs
- [ ] Update overall score constants

### Phase 2: Scoring Engine (Week 1)
- [ ] Rewrite `calculate_pillar_score` with severity weighting
- [ ] Remove gap-counting logic
- [ ] Update `derive_maturity` thresholds (unchanged per-pillar)
- [ ] Update overall maturity classification thresholds

### Phase 3: Scanner Adapters (Week 2)
- [ ] Gitleaks adapter: map severity
- [ ] Semgrep adapter: use rule metadata severity
- [ ] Trivy adapter: map vulnerability severity
- [ ] Nuclei adapter: use template severity
- [ ] Add integration tests for each adapter

### Phase 4: Mapping System (Week 2)
- [ ] Replace `mappings.yaml` with v2.0 version
- [ ] Update mapping loader for `severity_weight` field
- [ ] Add keyword deduplication validation
- [ ] Add tests for all 12 pillars

### Phase 5: Reporting (Week 3)
- [ ] Update HTML report template (12 pillars, severity breakdown)
- [ ] Update JSON output schema
- [ ] Update Markdown report template
- [ ] Update SARIF output (if applicable)
- [ ] Update gap analysis output format

### Phase 6: CLI & UX (Week 3)
- [ ] Update `--help` text and pillar references
- [ ] Add `--deployment-mode` flag (optional)
- [ ] Update bash completion
- [ ] Update man pages

### Phase 7: Testing & Validation (Week 4)
- [ ] Run full test suite
- [ ] Compare scores on known test repos (v1.0 vs v2.0)
- [ ] Validate against spec repo test cases
- [ ] Update CI/CD pipelines
- [ ] Tag release v2.0.0

---

## Validation Test Cases

### Test Case 1: Identity Pillar
**Input:** 1 Critical secret + 1 High missing MFA
**Expected v1.0:** gap_count=2 → score=60 (Advanced)
**Expected v2.0:** 1×55 + 1×25 = 80 deduction → score=20 (Baseline)

### Test Case 2: Clean Repository
**Input:** 0 findings across all pillars
**Expected v1.0:** 8×100 = 800 (Mostly Adaptive)
**Expected v2.0:** 12×100 = 1200 (Mostly Adaptive)

### Test Case 3: Mixed Severity
**Input:** 1 High, 3 Medium, 5 Low, 10 Info in Networks
**Expected v1.0:** gap_count=4 → score=20 (Baseline)
**Expected v2.0:** 25 + 30 + 25 + 10 = 90 deduction → score=10 (Baseline)

### Test Case 4: New Pillars
**Input:** Findings with keywords: `prompt.injection`, `sbom`, `iot`, `backup.validation`, `insider.threat`
**Expected v1.0:** All map to `applications` (default)
**Expected v2.0:** Map to `ai_systems`, `supply_chain`, `iot_ot`, `resilience`, `governance` respectively

---

## Rollback Plan

If critical issues discovered post-release:
1. Tag `v1.0.1` with critical fixes only
2. Maintain `v1.0` branch for emergency patches
3. Communicate migration timeline to users
4. Provide automated migration script for user configurations

---

## References

- [UZTF v2.0 Specification](../SPEC.md)
- [Updated mappings.yaml](../mappings.yaml)
- [Updated README](../README.md)
- [CISA Bridge](../CISA_BRIDGE.md)
- [Security-Pentest Skill Matrix](../.agents/skills/security-pentest/references/zero-trust-matrix.md)
