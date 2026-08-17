# Unified Zero Trust Framework — Specification

**Version:** 2.0.0  
**Status:** Draft  
**Last Updated:** 2026-08-17

---

## 1. Overview

The Unified Zero Trust Framework (UZTF) is a 12-pillar maturity model for assessing and improving an organization's Zero Trust security posture. It extends the CISA Zero Trust Maturity Model with quantitative scoring, automated data collection, and actionable gap analysis.

### 1.1 Design Principles

1. **Quantitative over qualitative** — Every pillar receives a numerical score (0–100) derived from real findings, not subjective assessment.
2. **Automation-first** — Designed for machine consumption. Pillar scores should be computable from automated scanner output without manual intervention.
3. **CISA-compatible** — Builds on CISA's maturity tiers and extends them. Any organization using CISA's model can adopt UZTF as an implementation layer.
4. **Action-oriented** — Every gap must produce a recommendation. The goal is a prioritized remediation plan, not just a score.
5. **Tool-agnostic** — The framework defines the model and scoring. Any tool or set of tools can implement it.
6. **Comprehensive coverage** — 12 pillars address all modern attack surfaces including AI, Supply Chain, and IoT/OT.

### 1.2 Terminology

| Term | Definition |
|------|------------|
| **Pillar** | A domain of Zero Trust capability (12 total) |
| **Finding** | A security issue detected by a scanner |
| **Gap** | The delta between current and target maturity for a pillar |
| **Maturity Tier** | Baseline, Advanced, or Adaptive |
| **Score** | Numerical value 0–100 for a single pillar |
| **Scorecard** | All 12 pillar scores + overall score + gap analysis |
| **Severity** | Critical, High, Medium, Low, Info — finding impact classification |

---

## 2. Pillar Definitions

### 2.1 Identity

**Focus:** Authentication, authorization, credential management, identity governance.

**Sample finding types:**
- Hardcoded API keys / secrets / tokens
- Passwords in source code or config
- Missing or weak MFA
- Over-privileged service accounts
- Stale or orphaned credentials
- Weak password policies
- Missing SSO integration

**ZT principle:** Never trust, always verify. Every access request must be authenticated and authorized.

**Example alignment (DoD ZTRA):** DCITE 1.1–1.5 (Identity)

### 2.2 Endpoints

**Focus:** Endpoint health, software composition, static code quality, supply chain security.

**Sample finding types:**
- Vulnerable dependencies (CVEs)
- Code injection flaws (SQLi, XSS, RCE)
- Outdated libraries or runtimes
- Compiler warnings that indicate unsound code
- Missing security headers
- Unvalidated/unsanitized input
- Path traversal, LFI, directory traversal
- Buffer overflow, use-after-free, memory safety issues

**ZT principle:** Every device accessing resources must be healthy and compliant.

**Example alignment (DoD ZTRA):** DCITE 2.1–2.5 (Devices)

### 2.3 IoT & OT Systems

**Focus:** Unmanaged device visibility, network isolation, behavioral monitoring.

**Sample finding types:**
- Undiscovered IoT/OT assets
- Missing VLAN isolation for unmanaged devices
- No traffic baselining for "dumb" endpoints
- Anomalous behavior in OT protocols
- Missing port lockdown on behavioral deviation
- Default credentials on IoT devices
- Unencrypted OT communications

**ZT principle:** Unmanaged devices must be discovered, isolated, and continuously monitored.

**Note:** UZTF extension. CISA addresses IoT/OT within Devices pillar.

### 2.4 Networks

**Focus:** Network segmentation, traffic security, infrastructure-as-code, network policy.

**Sample finding types:**
- Open ports / exposed services
- SSRF vulnerabilities
- IaC misconfigurations (Terraform, CloudFormation)
- Missing TLS/SSL
- Permissive firewall rules
- Missing network segmentation
- Insecure DNS configuration
- Exposed management interfaces

**ZT principle:** All network traffic should be encrypted and explicitly authorized.

**Example alignment (DoD ZTRA):** DCITE 3.1–3.5 (Networks)

### 2.5 Infrastructure

**Focus:** Cloud configuration, container security, host hardening, IAM configuration.

**Sample finding types:**
- Container running as root
- Missing HEALTHCHECK
- Overly permissive IAM roles
- Unpatched base images
- Misconfigured cloud resources
- Missing OS hardening (STIGs)
- Exposed Docker socket
- Kubernetes RBAC misconfigurations
- Public cloud storage buckets
- Missing vulnerability scanning

**ZT principle:** Infrastructure must be explicitly configured, hardened, and immutable.

**Example alignment (DoD ZTRA):** Cross-cutting (Infrastructure)

### 2.6 Applications

**Focus:** Application security, input validation, web security, API security.

**Sample finding types:**
- Web application vulnerabilities (SQLi, XSS, CSRF, SSTI)
- API security issues
- Business logic flaws
- Dependency vulnerabilities in production apps
- Missing security controls
- Insecure deserialization
- XXE (XML External Entity)
- Open redirect
- IDOR (Insecure Direct Object Reference)
- Missing authentication/authorization on endpoints

**ZT principle:** Applications enforce access decisions and maintain their own security posture.

**Example alignment (DoD ZTRA):** DCITE 4.1–4.5 (Applications)

### 2.7 Supply Chain

**Focus:** Vendor risk, SBOM management, third-party access, dependency integrity.

**Sample finding types:**
- Missing SBOM for dependencies
- Vendor risk assessments not performed
- Unrestricted VPN access for contractors
- Missing ZTNA for vendor access
- Typosquatting risk in package names
- Transitive dependency vulnerabilities
- Compromised build pipeline
- Unsigned artifacts
- Missing provenance verification

**ZT principle:** Supply chain integrity must be verified continuously from source to deployment.

**Note:** UZTF extension. CISA addresses supply chain as cross-cutting.

### 2.8 Data

**Focus:** Data encryption, classification, DLP, secrets management.

**Sample finding types:**
- Secrets and credentials exposed
- Unencrypted sensitive data
- Missing data classification
- Inadequate access controls on data stores
- Data exfiltration paths
- Missing backup encryption
- PII/PHI in logs or error messages
- Inadequate data retention policies

**ZT principle:** Data is protected at rest and in transit, with access based on explicit policy.

**Example alignment (DoD ZTRA):** DCITE 5.1–5.5 (Data)

### 2.9 AI Systems

**Focus:** AI/ML model security, prompt injection, data privacy, output handling.

**Sample finding types:**
- Prompt injection vulnerabilities
- Model inversion attacks
- Training data leakage
- Unauthorized model access
- Insecure model deployment
- Missing AI usage visibility
- Data privacy violations in AI processing
- Unvalidated AI-generated output
- Model supply chain attacks

**ZT principle:** AI systems must be governed with the same rigor as traditional applications, with additional controls for probabilistic behavior.

**Note:** UZTF extension. Emerging domain not in CISA ZTMM.

### 2.10 Operations

**Focus:** Monitoring, logging, observability, analytics, audit trails, threat intelligence.

**Sample finding types:**
- Missing audit logging
- Inadequate monitoring coverage
- Log retention gaps
- Lack of centralized logging
- Missing security analytics
- No threat intelligence integration
- Insufficient alerting
- Missing distributed tracing

**ZT principle:** All activity must be observable, logged, and analyzable in real time.

**Note:** UZTF extension. CISA addresses visibility as a cross-cutting concern.

### 2.11 Resilience

**Focus:** Backup, recovery, incident response, business continuity.

**Sample finding types:**
- Missing backup validation
- No immutable backups
- Inadequate incident response plan
- No tabletop exercises
- Missing automated isolation on breach
- No zero-downtime recovery capability
- Insufficient disaster recovery testing
- Single points of failure

**ZT principle:** Systems must be architected assuming breaches will occur, prioritizing rapid isolation and recovery.

**Note:** UZTF extension. CISA addresses resilience within Operations.

### 2.12 Governance

**Focus:** Security culture, training, risk scoring, policy alignment, insider threat.

**Sample finding types:**
- Missing security awareness training
- No role-specific training
- No insider threat monitoring
- Policies misaligned with business workflows
- Missing continuous risk scoring
- No security culture metrics
- Inadequate policy review cadence
- Missing compliance mapping

**ZT principle:** Security governance must be continuous, measurable, and aligned with business objectives.

**Note:** UZTF extension. CISA addresses governance as cross-cutting.

---

## 3. Cross-Cutting Layers

These layers intersect and support every pillar:

### 3.1 Virtualization & Cloud Layer
Secures hypervisors, container orchestration (Kubernetes), and cloud control planes. Applies vertical controls: cloud IAM (Identity), VPC/VNET segmentation (Networks), CSPM (Infrastructure).

### 3.2 Automation & Integration Layer
Orchestration and response connective tissue. Uses APIs and SOAR to ensure detection in one pillar triggers prevention in another.

### 3.3 Governance & Resilience Layer
Overarching human element and business continuity. Aligns security policies with business workflows, champions awareness, ensures rapid isolation and recovery.

---

## 4. Scoring Methodology

### 4.1 Per-Pillar Score

```
pillar_score = max(0, 100 - Σ(severity_weight × finding_count))
```

Where `finding_count` = number of distinct finding groups mapped to that pillar, grouped by (rule_id, severity) to prevent duplicate rules from inflating gap count.

**Severity Weights:**
| Severity | Weight |
|----------|--------|
| Critical | 55 |
| High | 25 |
| Medium | 10 |
| Low | 5 |
| Info | 1 |

**Example:** 1 Critical + 1 High + 3 Medium findings in Identity pillar:
- Score = 100 - (1×55 + 1×25 + 3×10) = 100 - (55 + 25 + 30) = 0 → Baseline

### 4.2 Overall Score

```
overall_score = sum(pillar_score for each of 12 pillars)
```

Range: 0–1200.

### 4.3 Maturity Classification

| Overall Score | Classification |
|:-------------:|----------------|
| 961–1200 | **Mostly Adaptive** — strong posture, real-time capabilities |
| 601–960 | **Mostly Advanced** — proactive posture, partial automation |
| 241–600 | **Mostly Baseline** — foundational controls, manual processes |
| 0–240 | **Initial** — significant gaps across all pillars |

### 4.4 Pillars at Advanced+

Count of pillars with score ≥ 51 (Advanced tier or above).

---

## 5. Gap Analysis

### 5.1 Gap Calculation

```
current_maturity = derive_maturity(pillar_score)
gap = current_maturity → target_maturity
```

### 5.2 Gap Levels

With 3 maturity tiers (Baseline → Advanced → Adaptive), the possible gap sizes are:

| Gap | Threshold | Implication |
|-----|-----------|-------------|
| None | Current ≥ Target | On track |
| Small | 1 tier difference (e.g., Baseline→Advanced) | Incremental improvements needed |
| Large | 2 tier difference (e.g., Baseline→Adaptive) | Foundational changes needed |

### 5.3 Gap Output

Each gap analysis includes:
- **Pillar name**
- **Current maturity tier**
- **Target maturity tier** (configurable, default: Advanced)
- **Gap level** (None / Small / Large)
- **Blocking findings count** (findings preventing progression)
- **Recommendations** (actionable remediation steps)

---

## 6. Finding-to-Pillar Mapping

### 6.1 Keyword-Based Mapping

Findings are mapped to pillars using keyword matching on their title and description. See `mappings.yaml` for the complete rule set.

### 6.2 Scanner-Specific Overrides

Scanners can explicitly specify pillar mappings in their output. These overrides take precedence over keyword-based mapping.

### 6.3 Default Pillar

Any finding that doesn't match a keyword or override maps to `applications` by default.

---

## 7. OS-Specific Infrastructure Guidance

Because different operating systems require distinct technical controls, the Infrastructure pillar includes tailored execution modules. Organizations should map these requirements to open, industry-recognized standards such as DISA STIGs or official Vendor Security Baselines.

### 7.1 Windows Environments
- **Baseline:** Strict Active Directory lockdowns, robust Group Policy Objects (GPOs), mandatory MFA for all network logins. Application of robust configuration standards (e.g., DISA STIGs, Microsoft Security Compliance Toolkit).
- **Advanced:** Automated, zero-downtime patching schedules and continuous threat monitoring via EDR integration.
- **Adaptive:** Real-time, context-aware policy enforcement tied directly to telemetry and domain health.

### 7.2 Linux Environments
- **Baseline:** Enforced key-based SSH authentication, strict `sudo` privilege controls, and comprehensive system hardening using established frameworks (e.g., DISA STIGs, vendor security guides).
- **Advanced:** Centralized patch management and implementation of Linux Security Modules (LSM) such as SELinux or AppArmor.
- **Adaptive:** Dynamic access controls, automated kernel compliance checks, and real-time container security evaluation.

### 7.3 macOS Environments
- **Baseline:** Centralized identity management via Mobile Device Management (MDM) and deployment of baseline configuration profiles (aligned with Apple Platform Security guidelines).
- **Advanced:** Continuous threat monitoring tailored for Apple ecosystems and automated patch compliance tracking.
- **Adaptive:** Real-time device posture checks (e.g., FileVault status, OS version, XProtect definitions) prior to network authentication.

---

## 8. Implementation Requirements

A conforming UZTF implementation must:

1. **Accept findings** from at least 2 different security scanner types
2. **Map findings to pillars** using the keyword mapping or explicit overrides
3. **Compute pillar scores** using the formula in §4.1
4. **Generate a scorecard** with all 12 pillars, scores, and maturity tiers
5. **Perform gap analysis** against a configurable target maturity
6. **Output results** in machine-readable format (JSON) and human-readable format (report)

---

## 9. CISA Zero Trust Maturity Model Mapping

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

---

## 10. Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-05-31 | Initial 8-pillar specification |
| 2.0.0 | 2026-08-17 | Expanded to 12 pillars; severity-weighted scoring; added IoT/OT, Supply Chain, AI Systems, Resilience, Governance; OS-specific guidance; cross-cutting layers |
