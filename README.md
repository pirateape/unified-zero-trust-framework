# Unified Zero Trust Framework (UZTF)

[![CI](https://github.com/pirateape/unified-zero-trust-framework/actions/workflows/ci.yml/badge.svg)](https://github.com/pirateape/unified-zero-trust-framework/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/License-Elastic_2.0-blue.svg)](LICENSE)

**A practical, implementation-focused maturity model for Zero Trust security posture assessment.**

The Unified Zero Trust Framework extends the [CISA Zero Trust Maturity Model](https://www.cisa.gov/zero-trust-maturity-model) into an actionable 12-pillar scoring system. While CISA provides the foundational *what* and *why* of Zero Trust, UZTF adds the *how* — mapping real-world security findings directly to pillar scores with gap analysis.

> CISA laid the foundation. UZTF builds the house.

---

## Why UZTF?

CISA's Zero Trust Maturity Model defines 5 pillars with high-level maturity descriptors. It's an excellent strategic framework, but it leaves a gap between *"we should be at Advanced maturity"* and *"what do we actually fix today?"*

UZTF bridges that gap:

| | CISA ZT Maturity Model | UZTF (this framework) |
|---|---|---|
| **Pillars** | 5 | 12 |
| **Scoring** | Qualitative per-pillar | 0–100 per pillar, 0–1200 total |
| **Input** | Manual assessment | Automated scan findings |
| **Output** | Strategic guidance | Prioritized remediation plan |
| **Audience** | Leadership | Engineers + EMs + Leadership |
| **Feedback loop** | Annual review | Every scan |

---

## The 12 Pillars

| # | Pillar | Domain | CISA Equivalent |
|---|---|---|---|
| 1 | **Identity** | AuthN/AuthZ, credentials, secrets | Identity |
| 2 | **Endpoints** | Endpoint health, patch status, SAST | Devices |
| 3 | **IoT & OT Systems** | Unmanaged devices, network isolation, behavioral monitoring | — *(new)* |
| 4 | **Networks** | Segmentation, traffic security, IaC | Networks |
| 5 | **Infrastructure** | Cloud/host config, IAM, containers | — *(new)* |
| 6 | **Applications** | App sec, input validation, dependencies | Applications |
| 7 | **Supply Chain** | Vendor risk, SBOM, third-party access | — *(new)* |
| 8 | **Data** | Encryption, classification, DLP | Data |
| 9 | **AI Systems** | AI/ML security, prompt injection, data privacy | — *(new)* |
| 10 | **Operations** | Monitoring, audit logs, analytics, threat intel | — *(new)* |
| 11 | **Resilience** | Backup, recovery, incident response | — *(new)* |
| 12 | **Governance** | Security culture, training, risk scoring | — *(new)* |

### Why 12 pillars instead of 5?

CISA's 5 pillars (Identity, Devices, Networks, Applications, Data) cover the **what**. UZTF adds 7 pillars that address the **operational enablers** and **modern attack surfaces** of Zero Trust:

- **IoT & OT Systems** — Unmanaged "dumb" devices are a growing attack surface. Discovery, isolation, and behavioral monitoring are prerequisites.
- **Infrastructure** — Cloud and container configurations are too often the root cause of breaches. Explicit infrastructure posture drives all other pillars.
- **Supply Chain** — Vendor risk, SBOMs, and third-party access are critical in modern software delivery.
- **AI Systems** — GenAI/LLM adoption introduces new attack vectors (prompt injection, model inversion, data leakage) requiring specialized controls.
- **Operations** — You can't secure what you can't see. Monitoring, logging, and analytics are prerequisites for all other pillars.
- **Resilience** — Zero Trust assumes breach. Backup validation, automated isolation, and rapid recovery are essential.
- **Governance** — Security culture, continuous risk scoring, and policy alignment with business workflows sustain the program.

---

## Maturity Tiers

UZTF adapts CISA's maturity model into 3 actionable tiers — **Baseline** (maps to CISA Traditional+Initial, 0–50), **Advanced** (maps to CISA Advanced, 51–80), **Adaptive** (maps to CISA Optimal, 81–100).

| Tier | Score | Description |
|------|:-----:|-------------|
| **Baseline** | 0–50 | Foundational controls present, significant gaps remain |
| **Advanced** | 51–80 | Proactive security measures implemented, partial automation |
| **Adaptive** | 81–100 | Real-time, automated, self-healing posture |

### Tier Characteristics

#### Baseline (0–50)
- Manual processes dominate
- Reactive security posture
- Significant blind spots
- Basic perimeter defenses
- No automated response
- **Example:** Secrets in source code, no SAST in CI/CD, manual dependency review

#### Advanced (51–80)
- Automated scanning in CI/CD pipelines
- Proactive vulnerability management
- Monitoring and alerting operational
- Partial automation of response
- Cross-team visibility
- **Example:** SAST/SCA in CI/CD, automated secret scanning, regular container scanning

#### Adaptive (81–100)
- Real-time threat detection and response
- Automated policy enforcement
- Self-healing infrastructure
- Continuous compliance monitoring
- Integrated security across all pillars
- **Example:** Automated rollback on policy violation, real-time dependency monitoring, immutable infrastructure

---

## Scoring

Each pillar is scored 0–100 based on the count and severity of findings mapped to that pillar:

```
pillar_score = max(0, 100 - Σ(severity_weight × finding_count))
```

Where `finding_count` is the number of distinct finding groups in that pillar (grouped by rule_id + severity).

**Severity Weights:**
| Severity | Weight |
|----------|--------|
| Critical | 20 |
| High | 15 |
| Medium | 10 |
| Low | 5 |
| Info | 1 |

### Scoring Examples

| Findings in Pillar | Calculation | Score | Tier |
|---|---|---|---|
| 0 findings | 100 - 0 | 100 | Adaptive |
| 1 Critical | 100 - 20 | 80 | Advanced |
| 1 High + 2 Medium | 100 - (15 + 20) | 65 | Advanced |
| 2 Critical + 1 High | 100 - (40 + 15) | 45 | Baseline |
| 5 Critical | 100 - 100 | 0 | Baseline |

### Overall Score

```
overall_score = sum(pillar_score for each of 12 pillars)
```

Range: 0–1200.

### Maturity Classification

| Total Score | Classification |
|:-----------:|---------------|
| 961–1200 | **Mostly Adaptive** — strong posture, real-time capabilities |
| 601–960 | **Mostly Advanced** — proactive posture, partial automation |
| 241–600 | **Mostly Baseline** — foundational controls, manual processes |
| 0–240 | **Initial** — significant gaps across all pillars |

### Pillars at Advanced+

Count of pillars with score ≥ 51 (Advanced tier or above).

---

## Gap Analysis

Each pillar includes gap analysis metadata:

```json
{
  "pillar": "identity",
  "current_maturity": "Baseline",
  "target_maturity": "Advanced",
  "gap_level": "Small",
  "blocking_findings": 4,
  "recommendations": [
    "Rotate all hardcoded secrets",
    "Enforce MFA for all service accounts",
    "Implement short-lived credential rotation"
  ]
}
```

### Gap Levels

Gaps are measured as the difference between current and target maturity tiers:

| Gap | Threshold | Description |
|-----|-----------|-------------|
| **None** | Current ≥ Target | On track, no action needed |
| **Small** | 1 tier difference (e.g., Baseline→Advanced) | Incremental improvements needed |
| **Large** | 2 tier difference (e.g., Baseline→Adaptive) | Foundational changes needed |

> **Note:** With 3 maturity tiers, Medium is not a distinct gap level. For implementation, the number of blocking findings can be mapped to these tiers: 0 → None, 1–3 → Small, 4+ → Large.

---

## Relationship to CISA

The Unified Zero Trust Framework is **not a replacement** for CISA's Zero Trust Maturity Model. It is a **complementary implementation layer**:

1. **CISA** defines the strategic pillars and maturity goals for the US Federal government
2. **UZTF** provides a quantitative scoring methodology that any organization can apply
3. **ASTs** (Automated Security Tools like ApeGuard) automate the data collection and scoring

### Mapping

The CISA→UZTF pillar mapping is:

| CISA Pillar | UZTF Pillar(s) | Notes |
|-------------|----------------|-------|
| Identity | Identity | Direct mapping |
| Devices | Endpoints, IoT & OT | Devices split into managed + unmanaged |
| Networks | Networks | Direct mapping |
| Applications | Applications | Direct mapping |
| Data | Data | Direct mapping |
| Visibility & Analytics (cross-cutting) | Operations | Elevated to standalone pillar |
| Automation & Orchestration (cross-cutting) | Automation & Integration Layer | Cross-cutting layer |
| Governance (cross-cutting) | Governance, Governance & Resilience Layer | Elevated + cross-cutting |
| *(implicit)* | Infrastructure | Cloud/host config elevated to pillar |
| *(implicit)* | Supply Chain | Vendor/SBOM elevated to pillar |
| *(implicit)* | AI Systems | Emerging domain |
| *(implicit)* | Resilience | Recovery/IR elevated to pillar |

> For full details, see [CISA_BRIDGE.md](./CISA_BRIDGE.md).

---

## Automation with ApeGuard

[ApeGuard](https://github.com/pirateape/ape-guard) is the reference CLI implementation of UZTF:

```bash
# Install
brew tap pirateape/tap && brew install apeguard

# Run a scan mapped to all 12 UZTF pillars
apeguard scan

# View your UZTF scorecard
apeguard scan --format html
```

ApeGuard automatically maps every finding to UZTF pillars, computes the scorecard, and generates prioritized remediation plans.

---

## See Also

- [ApeGuard](https://github.com/pirateape/ape-guard) — Reference CLI implementation of UZTF
- [ApeGuard GitHub Action](https://github.com/pirateape/apeguard-action) — Run UZTF-scored scans in CI/CD
- [Azure Security Audit Framework](https://github.com/pirateape/Azure-Security) — 148+ Azure defense-in-depth resources (KQL, PowerShell, Policies, Workbooks)

## License

Elastic License 2.0 — see [LICENSE](./LICENSE). Same as ApeGuard.
