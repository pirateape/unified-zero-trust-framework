# Unified Zero Trust Framework — Specification

**Version:** 1.0.0  
**Status:** Draft  
**Last Updated:** 2026-05-31

---

## 1. Overview

The Unified Zero Trust Framework (UZTF) is an 8-pillar maturity model for assessing and improving an organization's Zero Trust security posture. It extends the CISA Zero Trust Maturity Model with quantitative scoring, automated data collection, and actionable gap analysis.

### 1.1 Design Principles

1. **Quantitative over qualitative** — Every pillar receives a numerical score (0–100) derived from real findings, not subjective assessment.
2. **Automation-first** — Designed for machine consumption. Pillar scores should be computable from automated scanner output without manual intervention.
3. **CISA-compatible** — Builds on CISA's maturity tiers and extends them. Any organization using CISA's model can adopt UZTF as an implementation layer.
4. **Action-oriented** — Every gap must produce a recommendation. The goal is a prioritized remediation plan, not just a score.
5. **Tool-agnostic** — The framework defines the model and scoring. Any tool or set of tools can implement it.

### 1.2 Terminology

| Term | Definition |
|------|------------|
| **Pillar** | A domain of Zero Trust capability (8 total) |
| **Finding** | A security issue detected by a scanner |
| **Gap** | The delta between current and target maturity for a pillar |
| **Maturity Tier** | Baseline, Advanced, or Adaptive |
| **Score** | Numerical value 0–100 for a single pillar |
| **Scorecard** | All 8 pillar scores + overall score + gap analysis |

---

## 2. Pillar Definitions

### 2.1 Identity

**Focus:** Authentication, authorization, credential management, identity governance.

**Sample findings types:**
- Hardcoded API keys / secrets / tokens
- Passwords in source code or config
- Missing or weak MFA
- Over-privileged service accounts
- Stale or orphaned credentials

**ZT principle:** Never trust, always verify. Every access request must be authenticated and authorized.

**Example CISA alignment:** DCITE 1.1–1.5 (Identity)

### 2.2 Devices

**Focus:** Endpoint health, software composition, static code quality, supply chain security.

**Sample finding types:**
- Vulnerable dependencies (CVEs)
- Code injection flaws (SQLi, XSS, RCE)
- Outdated libraries or runtimes
- Compiler warnings that indicate unsound code
- Missing security headers

**ZT principle:** Every device accessing resources must be healthy and compliant.

**Example CISA alignment:** DCITE 2.1–2.5 (Devices)

### 2.3 Networks

**Focus:** Network segmentation, traffic security, infrastructure-as-code, network policy.

**Sample finding types:**
- Open ports / exposed services
- SSRF vulnerabilities
- IaC misconfigurations (Docker, Kubernetes, Terraform)
- Missing TLS/SSL
- Permissive firewall rules

**ZT principle:** All network traffic should be encrypted and explicitly authorized.

**Example CISA alignment:** DCITE 3.1–3.5 (Networks)

### 2.4 Applications

**Focus:** Application security, input validation, web security, API security.

**Sample finding types:**
- Web application vulnerabilities (SQLi, XSS, CSRF, SSTI)
- API security issues
- Business logic flaws
- Dependency vulnerabilities in production apps
- Missing security controls

**ZT principle:** Applications enforce access decisions and maintain their own security posture.

**Example CISA alignment:** DCITE 4.1–4.5 (Applications)

### 2.5 Data

**Focus:** Data encryption, classification, DLP, secrets management.

**Sample finding types:**
- Secrets and credentials exposed
- Unencrypted sensitive data
- Missing data classification
- Inadequate access controls on data stores
- Data exfiltration paths

**ZT principle:** Data is protected at rest and in transit, with access based on explicit policy.

**Example CISA alignment:** DCITE 5.1–5.5 (Data)

### 2.6 Visibility

**Focus:** Monitoring, logging, observability, analytics, audit trails.

**Sample finding types:**
- Missing audit logging
- Inadequate monitoring coverage
- Log retention gaps
- Lack of centralized logging
- Missing security analytics

**ZT principle:** All activity must be observable, logged, and analyzable in real time.

**Note:** UZTF extension. CISA addresses visibility as a cross-cutting concern rather than a standalone pillar.

### 2.7 Automation

**Focus:** Automated policy enforcement, CI/CD security, orchestrated response, shift-left.

**Sample finding types:**
- Missing SAST/SCA in CI/CD pipeline
- Manual deployment processes
- No automated rollback capability
- Inconsistent policy enforcement
- Lack of infrastructure-as-code

**ZT principle:** Security controls must be automated and enforced programmatically.

**Note:** UZTF extension. CISA addresses automation under cross-cutting "Automation and Orchestration."

### 2.8 Infrastructure

**Focus:** Cloud configuration, container security, host hardening, IAM configuration.

**Sample finding types:**
- Container running as root
- Missing HEALTHCHECK
- Overly permissive IAM roles
- Unpatched base images
- Misconfigured cloud resources

**ZT principle:** Infrastructure must be explicitly configured, hardened, and immutable.

**Note:** UZTF extension. CISA addresses infrastructure within the Applications and Devices pillars.

---

## 3. Scoring Methodology

### 3.1 Per-Pillar Score

```
pillar_score = max(0, 100 - (gap_count × 20))
```

Where `gap_count` = number of distinct finding groups mapped to that pillar (capped at 5).

**Finding grouping:** Findings are grouped by (rule_id, severity) to prevent duplicate rules from inflating gap count.

### 3.2 Overall Score

```
overall_score = sum(pillar_score for each of 8 pillars)
```

Range: 0–800.

### 3.3 Maturity Classification

| Overall Score | Classification |
|:-------------:|----------------|
| 641–800 | **Mostly Adaptive** — strong posture, real-time capabilities |
| 401–640 | **Mostly Advanced** — proactive posture, partial automation |
| 161–400 | **Mostly Baseline** — foundational controls, manual processes |
| 0–160 | **Initial** — significant gaps across all pillars |

### 3.4 Pillars at Advanced+

Count of pillars with score ≥ 51 (Advanced tier or above).

---

## 4. Gap Analysis

### 4.1 Gap Calculation

```
current_maturity = derive_maturity(pillar_score)
gap = current_maturity → target_maturity
```

### 4.2 Gap Levels

| Gap | Threshold | Implication |
|-----|-----------|-------------|
| None | Current ≥ Target | On track |
| Small | 1 tier difference | Incremental improvements |
| Medium | 2 tier difference | Significant effort |
| Large | 3 tier difference | Foundational changes needed |

### 4.3 Gap Output

Each gap analysis includes:
- **Pillar name**
- **Current maturity tier**
- **Target maturity tier** (configurable, default: Advanced)
- **Gap level** (None / Small / Medium / Large)
- **Blocking findings count** (findings preventing progression)
- **Recommendations** (actionable remediation steps)

---

## 5. Finding-to-Pillar Mapping

### 5.1 Keyword-Based Mapping

Findings are mapped to pillars using keyword matching on their title and description:

| Keywords | Pillar | Default Maturity |
|----------|--------|:----------------:|
| secret, credential, password | identity | Baseline |
| injection, xss, rce | devices | Baseline |
| sqli, csrf, ssti, idor, open redirect | applications | Baseline |
| misconfig, ssrf, iac, docker | networks | Baseline |
| dependency, vulnerability, cve | applications | Baseline |
| cwe | applications | Baseline |

### 5.2 Scanner-Specific Overrides

Scanners can explicitly specify pillar mappings in their output. These overrides take precedence over keyword-based mapping.

### 5.3 Default Pillar

Any finding that doesn't match a keyword or override maps to `applications` by default.

---

## 6. Implementation Requirements

A conforming UZTF implementation must:

1. **Accept findings** from at least 2 different security scanner types
2. **Map findings to pillars** using the keyword mapping or explicit overrides
3. **Compute pillar scores** using the formula in §3.1
4. **Generate a scorecard** with all 8 pillars, scores, and maturity tiers
5. **Perform gap analysis** against a configurable target maturity
6. **Output results** in machine-readable format (JSON) and human-readable format (report)
