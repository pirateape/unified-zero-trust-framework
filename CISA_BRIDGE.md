# CISA Bridge — Mapping UZTF to CISA Zero Trust Maturity Model

This document maps the Unified Zero Trust Framework (UZTF) to the
[CISA Zero Trust Maturity Model](https://www.cisa.gov/zero-trust-maturity-model)
(ZTMM), version 2.0.

## Why This Matters

CISA's ZTMM is the **foundational reference** for Zero Trust architecture
in the US Federal government and beyond. UZTF does not replace it.
Instead, UZTF provides:

1. **Quantitative scoring** on top of CISA's qualitative maturity tiers
2. **7 additional pillars** that CISA treats as cross-cutting concerns
   or leaves implicit
3. **Automated data collection** via security scanners
4. **Actionable gap analysis** with specific recommendations

Organizations already using CISA's model can adopt UZTF as an
**implementation layer** without changing their strategic framework.

---

## Pillar Mapping

### Direct 1:1 Mapping (5 pillars)

| CISA Pillar | UZTF Pillar | DCITE Ref | Notes |
|-------------|-------------|-----------|-------|
| Identity | Identity | 1.1–1.5 | Direct mapping |
| Devices | Endpoints | 2.1–2.5 | Managed endpoints only |
| Networks | Networks | 3.1–3.5 | Direct mapping |
| Applications | Applications | 4.1–4.5 | Direct mapping |
| Data | Data | 5.1–5.5 | Direct mapping |

### Elevated from Cross-Cutting to Standalone Pillars (4 pillars)

| CISA Cross-Cutting | UZTF Pillar | Rationale |
|--------------------|-------------|-----------|
| Visibility & Analytics | Operations | CISA treats this as a cross-cutting function. UZTF elevates it to a standalone pillar because you cannot implement Zero Trust without visibility into all other pillars. |
| Automation & Orchestration | Automation & Integration Layer | CISA recommends automation across all pillars. UZTF makes it explicit as a cross-cutting layer because manual processes are the #1 blocker to Zero Trust at scale. |
| Governance | Governance | CISA addresses governance as cross-cutting. UZTF elevates it to a standalone pillar because security culture, continuous risk scoring, and policy alignment with business workflows are measurable and actionable. |
| *(implicit in Devices/Applications)* | Resilience | CISA addresses resilience within Operations. UZTF elevates it because assuming breach and planning for rapid isolation/recovery is a distinct operational capability. |

### New Pillars Addressing Modern Attack Surfaces (3 pillars)

| UZTF Pillar | Rationale |
|-------------|-----------|
| IoT & OT Systems | Unmanaged "dumb" devices (sensors, printers, OT controllers) are a growing attack surface not addressed by CISA's Devices pillar which assumes managed endpoints. |
| Supply Chain | Vendor risk, SBOMs, and third-party access are critical in modern software delivery. CISA mentions supply chain but doesn't elevate it. |
| AI Systems | GenAI/LLM adoption introduces new attack vectors (prompt injection, model inversion, data leakage) requiring specialized controls. Emerging domain not in CISA ZTMM v2.0. |

### Elevated from Implicit to Explicit (1 pillar)

| UZTF Pillar | Rationale |
|-------------|-----------|
| Infrastructure | Cloud/container configurations are the #1 root cause of breaches. CISA addresses infrastructure within Applications and Devices. UZTF elevates it because explicit infrastructure posture (IAM, container security, cloud config) drives all other pillars. |

---

## Complete 12-Pillar Mapping Summary

| # | UZTF Pillar | CISA Origin | Mapping Type |
|---|-------------|-------------|--------------|
| 1 | Identity | Identity | Direct 1:1 |
| 2 | Endpoints | Devices | Direct 1:1 (managed only) |
| 3 | IoT & OT Systems | — | New (modern attack surface) |
| 4 | Networks | Networks | Direct 1:1 |
| 5 | Infrastructure | Implicit in Devices/Applications | Elevated from implicit |
| 6 | Applications | Applications | Direct 1:1 |
| 7 | Supply Chain | Cross-cutting mention | Elevated from cross-cutting |
| 8 | Data | Data | Direct 1:1 |
| 9 | AI Systems | — | New (emerging domain) |
| 10 | Operations | Visibility & Analytics (cross-cutting) | Elevated from cross-cutting |
| 11 | Resilience | Implicit in Operations | Elevated from implicit |
| 12 | Governance | Governance (cross-cutting) | Elevated from cross-cutting |

---

## Maturity Alignment

UZTF adapts CISA's maturity model into 4 actionable tiers:
Initial (0–20), Baseline (21–50, mapping CISA's Traditional), Advanced (51–80),
and Adaptive (81–100, mapping CISA's Optimal).

| Tier | CISA Definition | UZTF Equivalent |
|------|-----------------|-----------------|
| **Initial** | Not defined in CISA; implies completely unmanaged | Initial (0–20) |
| **Traditional/Baseline** | Manual processes, ad-hoc security | Baseline (21–50) |
| **Advanced** | Automated processes, proactive security | Advanced (51–80) |
| **Target/Adaptive** | Real-time, automated, self-healing | Adaptive (81–100) |

### Key Difference

CISA defines maturity qualitatively per pillar with descriptive text.
UZTF adds a **numerical score** that maps to these tiers:

```text
CISA "Traditional/Baseline"     ↔ UZTF 0–50  ↔  "Baseline"
CISA "Advanced"                 ↔ UZTF 51–80 ↔  "Advanced"
CISA "Target/Adaptive"          ↔ UZTF 81–100 ↔ "Adaptive"
```

---

## Example: Identity Pillar Across Both Frameworks

### CISA ZTMM Descriptors (DCITE 1.x)

- **Traditional:** Manual identity management, no MFA, static credentials
- **Advanced:** Automated identity lifecycle, MFA for most access, some PAM
- **Target:** Continuous authentication, risk-based access, zero standing privileges

### UZTF Score Derivation

1. Scanner finds 3 hardcoded secrets → mapped to `identity` pillar
   (Critical severity)
2. Scanner finds 1 missing MFA on admin → mapped to `identity` pillar
   (High severity)
3. Gap calculation: 3×55 + 1×25 = 190 points deducted
4. Score = max(0, 100 − 190) = **0** → **Initial**
5. Gap analysis: *"Large gap from Initial to Advanced. Rotate all
   hardcoded secrets, enforce MFA on admin accounts."*

The CISA assessment says "we need to improve identity." The UZTF
scorecard says *"your identity score is 0, here are the 4 blocking
findings with severity weights, and here's the remediation plan."*

---

## Adoption Path

For organizations using CISA's model:

```text
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

## Hub & Spoke Deployment Model

UZTF also supports a **Hub & Spoke** deployment architecture, which aligns the 12-pillar framework with CISA's 5 core pillars as the foundational "Hub," while treating emerging attack surfaces as "Spokes."

- **Hub (The Core Foundation):** Identity, Endpoints, Networks, Applications, Data, and Operations/Governance.
- **Spokes (Emerging Domains):** Infrastructure, Supply Chain, IoT & OT Systems, AI Systems, Resilience.

Organizations establish the Hub first—securing the core pathways to data—before plugging in specialized Spokes as business operations require them. This maps to the 12-pillar model as:

| Hub & Spoke | 12-Pillar Model |
|-------------|-----------------|
| Core: Identity | Identity |
| Core: Endpoints | Endpoints |
| Core: Networks | Networks |
| Core: Applications | Applications |
| Core: Data | Data |
| Core: Ops & Gov | Operations + Governance |
| Spoke: Infrastructure | Infrastructure |
| Spoke: Supply Chain | Supply Chain |
| Spoke: IoT/OT | IoT & OT Systems |
| Spoke: AI Systems | AI Systems |
| Spoke: Resilience | Resilience |

---

## References

- [CISA Zero Trust Maturity Model](https://www.cisa.gov/zero-trust-maturity-model)
  — v2.0, April 2023
- [CISA Zero Trust Cross-Agency Initiative (ZCII)](https://www.cisa.gov/zero-trust)
- [NIST SP 800-207: Zero Trust Architecture](https://csrc.nist.gov/publications/detail/sp/800-207/final)
- [DCITE 1.0: Zero Trust Reference Architecture](https://dodcio.defense.gov/Portals/0/Documents/Library/(U)ZT_RA_v2.0(U)_Sep22.pdf)
- [Unified Zero Trust Framework (Open Framework Edition) V2](../APE-Brain/00-Raw/Unified%20Zero%20Trust%20Framework%20(Open%20Framework%20Edition)%20V2.md)
- [Unified Zero Trust Framework (Hub & Spoke Edition)](../APE-Brain/00-Raw/Unified%20Zero%20Trust%20Framework%20(Hub%20&%20Spoke%20Edition).md)
