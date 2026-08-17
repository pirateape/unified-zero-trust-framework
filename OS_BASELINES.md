# UZTF Implementation Guide: OS-Specific Infrastructure Baselines

This document supplements the core Unified Zero Trust Framework (UZTF) specification. While the framework itself is tool- and OS-agnostic, implementing the **Infrastructure** pillar requires specific technical controls tailored to the host operating system.

Organizations should map these requirements to open, industry-recognized standards such as DISA STIGs, CIS Benchmarks, or official Vendor Security Baselines.

## Windows Environments
- **Baseline:** Strict Active Directory lockdowns, robust Group Policy Objects (GPOs), mandatory MFA for all network logins. Application of robust configuration standards (e.g., DISA STIGs, Microsoft Security Compliance Toolkit).
- **Advanced:** Automated, zero-downtime patching schedules and continuous threat monitoring via EDR integration.
- **Adaptive:** Real-time, context-aware policy enforcement tied directly to telemetry and domain health.

## Linux Environments
- **Baseline:** Enforced key-based SSH authentication, strict `sudo` privilege controls, and comprehensive system hardening using established frameworks (e.g., DISA STIGs, vendor security guides).
- **Advanced:** Centralized patch management and implementation of Linux Security Modules (LSM) such as SELinux or AppArmor.
- **Adaptive:** Dynamic access controls, automated kernel compliance checks, and real-time container security evaluation.

## macOS Environments
- **Baseline:** Centralized identity management via Mobile Device Management (MDM) and deployment of baseline configuration profiles (aligned with Apple Platform Security guidelines).
- **Advanced:** Continuous threat monitoring tailored for Apple ecosystems and automated patch compliance tracking.
- **Adaptive:** Real-time device posture checks (e.g., FileVault status, OS version, XProtect definitions) prior to network authentication.

## Mobile Environments (iOS & Android)
- **Baseline:** Mandatory MDM enrollment, enforced device encryption, biometric/passcode requirements, and prevention of sideloading/jailbreaking.
- **Advanced:** App-level VPNs (per-app tunneling), remote wipe capabilities, and mobile threat defense (MTD) integrations.
- **Adaptive:** Contextual access blocking based on device risk score, out-of-date OS versions, or detected root/jailbreak status.

## Container & Kubernetes Environments
- **Baseline:** Distroless or minimalist base images, unprivileged execution (no root containers), read-only root filesystems, and strict Kubernetes RBAC.
- **Advanced:** Automated image scanning in the CI/CD pipeline, image signing (e.g., Sigstore), and strict NetworkPolicies for pod isolation.
- **Adaptive:** Runtime threat defense (e.g., Falco, eBPF monitoring) to kill non-compliant or anomalous container processes instantly.

## Network OS Environments (Cisco IOS, JunOS, PAN-OS)
- **Baseline:** Disabling insecure management protocols (Telnet, HTTP), enforcing strong SNMPv3/SSH, restricting control plane access via ACLs, and centralized AAA (TACACS+/RADIUS).
- **Advanced:** Automated configuration drift detection, continuous vulnerability scanning of firmware, and standardized IaC deployments.
- **Adaptive:** Dynamic routing validation (RPKI) and automated boundary isolation upon detecting BGP hijacking or anomalous traffic patterns.

## IoT & OT Environments (Embedded Linux, RTOS, ICS)
- **Baseline:** Changing all default credentials, disabling unnecessary physical/logical ports, and strict network isolation (VLAN/air-gapping) from corporate networks.
- **Advanced:** Passive network monitoring to baseline expected communication patterns and implementation of zero-trust network access (ZTNA) for remote vendor maintenance.
- **Adaptive:** Automated port-level quarantine via NAC (Network Access Control) if an OT device deviates from its hardcoded protocol baseline (e.g., Modbus/DNP3 anomalies).
