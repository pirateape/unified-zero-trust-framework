# CISA Bridge — Mapping UZTF to CISA Zero Trust Maturity Model

This document maps the Unified Zero Trust Framework (UZTF) to the [CISA Zero Trust Maturity Model](https://www.cisa.gov/zero-trust-maturity-model) (ZTMM), version 2.0.

## Why This Matters

CISA's ZTMM is the **foundational reference** for Zero Trust architecture in the US Federal government and beyond. UZTF does not replace it. Instead, UZTF provides:

1. **Quantitative scoring** on top of CISA's qualitative maturity tiers
2. **3 additional pillars** that CISA treats as cross-cutting concerns
3. **Automated data collection** via security scanners
4. **Actionable gap analysis** with specific recommendations

Organizations already using CISA's model can adopt UZTF as an **implementation layer** without changing their strategic framework.

---

## Pillar Mapping

### Direct 1:1 Mapping (5 pillars)

| CISA Pillar | UZTF Pillar | DCITE Ref | Notes |
|-------------|-------------|----------------|-------|
| Identity | Identity | 1.1–1.5 | Direct mapping |
| Devices | Devices | 2.1–2.5 | Direct mapping |
| Networks | Networks | 3.1–3.5 | Direct mapping |
| Applications | Applications | 4.1–4.5 | Direct mapping |
| Data | Data | 5.1–5.5 | Direct mapping |

### Extended Pillars (3 new)

| CISA Cross-Cutting | UZTF Pillar | Rationale |
|--------------------|-------------|-----------|
| Visibility & Analytics | Visibility | CISA treats this as a cross-cutting function. UZTF elevates it to a standalone pillar because you cannot implement Zero Trust without visibility into all other pillars. |
| Automation & Orchestration | Automation | CISA recommends automation across all pillars. UZTF makes it explicit because manual processes are the #1 blocker to Zero Trust at scale. |
| *(implicit in Devices/Applications)* | Infrastructure | UZTF elevates infrastructure posture to a standalone pillar because cloud/container misconfigurations are the #1 root cause of breaches. This replaces CISA's cross-cutting Governance pillar as an explicit operational concern, while Governance is treated as an overarching input to all pillars. |

---

## Maturity Alignment

UZTF adapts CISA's 4-tier maturity model into 3 actionable tiers: Baseline (0–50, mapping CISA's Traditional+Initial), Advanced (51–80), and Adaptive (81–100, mapping CISA's Optimal).

| Tier | CISA Definition | UZTF Equivalent |
|------|----------------|-----------------|
| **Traditional/Baseline** | Manual processes, ad-hoc security | Baseline (0–50) |
| **Advanced** | Automated processes, proactive security | Advanced (51–80) |
| **Target/Adaptive** | Real-time, automated, self-healing | Adaptive (81–100) |

### Key Difference

CISA defines maturity qualitatively per pillar with descriptive text. UZTF adds a **numerical score** that maps to these tiers:

```
CISA "Traditional/Baseline"     ↔ UZTF 0–50  ↔  "Baseline"
CISA "Advanced"                 ↔ UZTF 51–80 ↔  "Advanced"
CISA "Target/Adaptive"          ↔ UZTF 81–100 ↔  "Adaptive"
```

---

## Example: Identity Pillar Across Both Frameworks

### CISA ZTMM Descriptors (DCITE 1.x)

- **Traditional:** Manual identity management, no MFA, static credentials
- **Advanced:** Automated identity lifecycle, MFA for most access, some PAM
- **Target:** Continuous authentication, risk-based access, zero standing privileges

### UZTF Score Derivation

1. Scanner finds 3 hardcoded secrets → mapped to `identity` pillar
2. Gap count = 3
3. Score = 100 − (3 × 20) = **40** → **Baseline**
4. Gap analysis: *"Medium gap from Baseline to Advanced. Rotate all hardcoded secrets, enforce MFA."*

The CISA assessment says "we need to improve identity." The UZTF scorecard says *"your identity score is 40, here are the 3 blocking findings, and here's the remediation plan."*

---

## Adoption Path

For organizations using CISA's model:

```
1. Already using CISA ZTMM
   │
   ├─ 2a. Keep CISA for strategic planning ──┐
   │                                          │
   └─ 2b. Adopt UZTF for implementation ──────┤
                                                │
   3. Use ApeGuard (or any UZTF-compatible      │
      tool) to automate scorecard generation    │
                                                │
   4. UZTF scorecard feeds back into ───────────┘
      CISA strategic review with quantified gaps
```

---

## References

- [CISA Zero Trust Maturity Model](https://www.cisa.gov/zero-trust-maturity-model) — v2.0, April 2023
- [CISA Zero Trust Cross-Agency Initiative (ZCII)](https://www.cisa.gov/zero-trust)
- [NIST SP 800-207: Zero Trust Architecture](https://csrc.nist.gov/publications/detail/sp/800-207/final)
- [DCITE 1.0: Zero Trust Reference Architecture](https://dodcio.defense.gov/Portals/0/Documents/Library/(U)ZT_RA_v2.0(U)_Sep22.pdf)
