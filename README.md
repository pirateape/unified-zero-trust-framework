# Unified Zero Trust Framework (UZTF)

**A practical, implementation-focused maturity model for Zero Trust security posture assessment.**

The Unified Zero Trust Framework extends the [CISA Zero Trust Maturity Model](https://www.cisa.gov/zero-trust-maturity-model) into an actionable 8-pillar scoring system. While CISA provides the foundational *what* and *why* of Zero Trust, UZTF adds the *how* — mapping real-world security findings directly to pillar scores with gap analysis.

> CISA laid the foundation. UZTF builds the house.

---

## Why UZTF?

CISA's Zero Trust Maturity Model defines 5 pillars with high-level maturity descriptors. It's an excellent strategic framework, but it leaves a gap between *"we should be at Advanced maturity"* and *"what do we actually fix today?"*

UZTF bridges that gap:

| | CISA ZT Maturity Model | UZTF (this framework) |
|---|---|---|
| **Pillars** | 5 | 8 |
| **Scoring** | Qualitative per-pillar | 0–100 per pillar, 0–800 total |
| **Input** | Manual assessment | Automated scan findings |
| **Output** | Strategic guidance | Prioritized remediation plan |
| **Audience** | Leadership | Engineers + EMs + Leadership |
| **Feedback loop** | Annual review | Every scan |

---

## The 8 Pillars

| # | Pillar | Domain | CISA Equivalent |
|---|---|---|---|
| 1 | **Identity** | AuthN/AuthZ, credentials, secrets | Identity |
| 2 | **Devices** | Endpoint health, patch status, SAST | Devices |
| 3 | **Networks** | Segmentation, traffic security, IaC | Networks |
| 4 | **Applications** | App sec, input validation, dependencies | Applications |
| 5 | **Data** | Encryption, classification, DLP | Data |
| 6 | **Visibility** | Monitoring, audit logs, analytics | — *(new)* |
| 7 | **Automation** | Automated response, orchestration, CI/CD | — *(new)* |
| 8 | **Infrastructure** | Cloud/host config, IAM, containers | — *(new)* |

### Why 8 pillars instead of 5?

CISA's 5 pillars (Identity, Devices, Networks, Applications, Data) cover the **what**. UZTF adds 3 pillars that address the **operational enablers** of Zero Trust:

- **Visibility** — You can't secure what you can't see. Monitoring, logging, and analytics are prerequisites for all other pillars.
- **Automation** — Zero Trust at scale requires automated policy enforcement and response. Manual processes don't scale.
- **Infrastructure** — Cloud and container configurations are too often the root cause of breaches. Explicit infrastructure posture drives all other pillars.

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
pillar_score = max(0, 100 - (gap_count × 20))
```

Where `gap_count` is the number of distinct finding groups in that pillar (capped at 5).

**Overall score:** Sum of all 8 pillar scores (0–800).

### Scoring Rules

- **0 gaps** → 100 (Adaptive)
- **1 gap** → 80 (Advanced)
- **2 gaps** → 60 (Advanced)
- **3 gaps** → 40 (Baseline)
- **4 gaps** → 20 (Baseline)
- **5+ gaps** → 0 (Baseline)

### Maturity Classification

| Total Score | Classification |
|:-----------:|---------------|
| 641–800 | Mostly Adaptive |
| 401–640 | Mostly Advanced |
| 161–400 | Mostly Baseline |
| 0–160 | Initial |

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
- CISA **Identity** → UZTF **Identity**
- CISA **Devices** → UZTF **Devices**
- CISA **Networks** → UZTF **Networks**
- CISA **Applications** → UZTF **Applications**
- CISA **Data** → UZTF **Data**
- CISA *(cross-cutting)* → UZTF **Visibility** (monitoring & analytics)
- CISA *(cross-cutting)* → UZTF **Automation** (orchestration)
- CISA *(cross-cutting)* → UZTF **Infrastructure** (cloud/host)

> For full details, see [CISA_BRIDGE.md](./CISA_BRIDGE.md).

---

## Automation with ApeGuard

[ApeGuard](https://github.com/pirateape/ape-guard) is the reference CLI implementation of UZTF:

```bash
# Install
brew tap pirateape/tap && brew install apeguard

# Run a scan mapped to all 8 UZTF pillars
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
