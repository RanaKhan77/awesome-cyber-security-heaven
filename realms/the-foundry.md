# The Foundry

> **32 tools** · [← Back to the main list](../README.md) · Data verified **2026-10-15** (re-verified monthly)

## Curator's notes

The pipeline guardians — SAST, dependency scanning, IaC misconfig audits, container hardening. This realm moves fastest of all: CI/CD attack research regularly rewrites the ground rules here.

## Maintenance snapshot (2026-10-15)

- **Active in the last 30 days:** 18 of 30 tracked GitHub repos (60%)
- **Archived upstream (kept — still reference-quality):** [OWASP Dependency-Check](https://github.com/jeremylong/DependencyCheck)
- **Quiet classics (no push in 2+ years, still the standard):** kube-hunter, sobelow, logdissect, Awesome ICS Security, Awesome Container Security
- **Youngest entries:** cppcheck (2009), Brakeman (2010), Dependency-Track (2013)

## Flagship picks

| Tool | ★ Stars | Created | Last push | What it does |
|---|---|---|---|---|
| [Trivy](https://github.com/aquasecurity/trivy) | 38.4k | 2019 | 2026-10-15 ✅ | Find vulnerabilities, misconfigurations, secrets, SBOM in containers, Kubernetes, code repositories, clouds an |
| [Semgrep](https://github.com/semgrep/semgrep) | 17.1k | 2019 | 2026-10-15 ✅ | Lightweight static analysis for many languages. Find bug variants with patterns that look like source code. |
| [Prowler](https://github.com/prowler-cloud/prowler) | 15.0k | 2016 | 2026-10-15 ✅ | Prowler is the world’s most widely used open-source cloud security platform that automates security and compli |
| [Grype](https://github.com/anchore/grype) | 13.0k | 2020 | 2026-10-15 ✅ | A vulnerability scanner for container images and filesystems |
| [OSV-Scanner](https://github.com/google/osv-scanner) | 11.2k | 2022 | 2026-10-14 ✅ | Vulnerability scanner written in Go which uses the data provided by https://osv.dev |
| [Docker Bench for Security](https://github.com/docker/docker-bench-security) | 9.7k | 2015 | 2026-06-04 | The Docker Bench for Security is a script that checks for dozens of common best-practices around deploying Doc |

## Full inventory (32 tools)

| Tool | ★ Stars | Created | Last push | License / tier |
|---|---|---|---|---|
| [Trivy](https://github.com/aquasecurity/trivy) | 38.4k | 2019 | 2026-10-15 ✅ | — the all-in-one scanner: containers, IaC, repos, SBOMs, licenses and secrets, with one binary. |
| [Semgrep](https://github.com/semgrep/semgrep) | 17.1k | 2019 | 2026-10-15 ✅ | — fast, expressive static analysis with community rule packs for 30+ languages; write rules like you write code. (LGPL-2.1) |
| [Prowler](https://github.com/prowler-cloud/prowler) | 15.0k | 2016 | 2026-10-15 ✅ | — AWS/Azure/GCP security posture: hundreds of checks mapped to CIS benchmarks and compliance frameworks. |
| [Grype](https://github.com/anchore/grype) | 13.0k | 2020 | 2026-10-15 ✅ | — vulnerability scanner for container images and SBOMs with KEV/EPSS enrichment for prioritization. |
| [OSV-Scanner](https://github.com/google/osv-scanner) | 11.2k | 2022 | 2026-10-14 ✅ | — dependency vulnerability scanner backed by Google's OSV database; fast, transparent, no vendor lock. |
| [Docker Bench for Security](https://github.com/docker/docker-bench-security) | 9.7k | 2015 | 2026-06-04 | — audits your Docker host and daemon configuration against the CIS Benchmark in a single script run. |
| [Syft](https://github.com/anchore/syft) | 9.7k | 2020 | 2026-10-15 ✅ | — generate clean SBOMs (SPDX/CycloneDX) from images and filesystems; feeds Grype and everything else. |
| [Falco](https://github.com/falcosecurity/falco) | 9.5k | 2016 | 2026-10-15 ✅ | — CNCF runtime threat detection for containers, Kubernetes and cloud workloads. |
| [Checkov](https://github.com/bridgecrewio/checkov) | 9.1k | 2019 | 2026-10-15 ✅ | — IaC scanning for Terraform, CloudFormation, Kubernetes and more, with auto-fix guidance. |
| [Bandit](https://github.com/PyCQA/bandit) | 8.3k | 2018 | 2026-10-12 ✅ | — the standard Python security linter; wire it into CI and never merge an `eval()` again. |
| [Kyverno](https://github.com/kyverno/kyverno) | 8.3k | 2019 | 2026-10-15 ✅ | — CNCF policy engine for Kubernetes: validate, mutate and generate configurations as code. |
| [kube-bench](https://github.com/aquasecurity/kube-bench) | 8.2k | 2017 | 2026-10-05 ✅ | — run the CIS Kubernetes Benchmark checks against your nodes in minutes. |
| [ScoutSuite](https://github.com/nccgroup/ScoutSuite) | 7.8k | 2018 | 2025-09-23 ⏳ | — the classic multi-cloud security auditor with a friendly HTML report — quiet upstream, still the reference. (GPL-3.0) |
| [Brakeman](https://github.com/presidentbeef/brakeman) | 7.3k | 2010 | 2026-10-05 ✅ | — static analysis purpose-built for Ruby on Rails; no config, no instrumentation, just findings. |
| [cppcheck](https://github.com/danmar/cppcheck) | 6.8k | 2009 | 2026-10-13 ✅ | — static analysis for C/C++: detects bugs and undefined behavior, not just style. (GPL-3.0) |
| [cosign](https://github.com/sigstore/cosign) | 6.4k | 2021 | 2026-10-14 ✅ | — Sigstore's keyless container signing and verification; make provenance part of your pipeline. |
| [kube-hunter](https://github.com/aquasecurity/kube-hunter) | 5.1k | 2018 | 2024-03-19 ⏳ | — active Kubernetes security testing: probe clusters for exposed dashboards, weak RBAC and known exploits; quiet upstream. |
| [Dependency-Track](https://github.com/DependencyTrack/dependency-track) | 4.3k | 2013 | 2026-10-15 ✅ | — SBOM-based continuous component analysis platform with portfolio risk dashboards. |
| [KICS](https://github.com/Checkmarx/kics) | 2.7k | 2020 | 2026-10-15 ✅ | — 1,000+ security queries across Terraform, Ansible, K8s, Dockerfile and other IaC. |
| [cloudsplaining](https://github.com/salesforce/cloudsplaining) | 2.3k | 2020 | 2026-10-13 ✅ | — maps AWS IAM policies and flags the privilege-escalation paths you never meant to grant. |
| [sobelow](https://github.com/nccgroup/sobelow) | 1.8k | 2017 | 2024-08-20 ⏳ | — security testing for Elixir/Phoenix applications; the Sobelow family's namesake. (MPL-2.0) |
| [ChipWhisperer](https://github.com/newaetech/chipwhisperer) | 1.6k | 2014 | 2026-10-09 ✅ | — side-channel analysis and glitching for hardware security research. (GPL-3.0) |
| [cwe_checker](https://github.com/fkie-cad/cwe_checker) | 1.4k | 2018 | 2026-09-28 ✅ | — finds common CWE patterns in binaries, direct from firmware images. (LGPL-2.1+) |
| [Substation](https://github.com/brexhq/substation) | 408 | 2022 | 2026-01-20 | — an event and data pipeline toolkit for detection engineering at scale. (MIT) |
| [ProgPilot](https://github.com/designsecurity/progpilot) | 369 | 2017 | 2025-08-17 ⏳ | — static taint analysis for PHP sources: finds input-to-sink flows at build time. (GPL-3.0) |
| [logdissect](https://github.com/dogoncouch/logdissect) | 161 | 2017 | 2024-08-07 ⏳ | — parse, merge and analyze logs from many formats into one timeline. (MIT) |
| [OWASP Dependency-Check](https://github.com/jeremylong/DependencyCheck) | 56 | 2025 | 2025-09-27 ⏳ | — the classic SCA engine: NVD-backed dependency CVE scanning for JVM/.NET/JS ecosystems. |
| [Awesome ICS Security](https://github.com/mpesen/awesome-industrial-control-system-security) | 32 | 2016 | 2016-05-27 ⏳ | — curated industrial-control-system security tools and research. (Apache-2.0, curated list) |
| [Awesome Container Security](https://github.com/kai5263499/container-security-awesome) | 19 | 2018 | 2019-03-07 ⏳ |
| [StackRadar](https://github.com/lockdep/stackradar) | 1 | 2026 | 2026-10-19 ✅ | — Kubernetes vulnerability scanner that builds an SBOM of every running image and ranks findings by CVSS, EPSS and CISA KEV. (AGPL-3.0) | — curated container and cloud-native security resources. (MIT, curated list) |
| [GDB](https://www.sourceware.org/gdb/) | — | — | — | — the GNU debugger: breakpoints, watchpoints and reverse debugging across dozens of architectures. (GPL-3.0) |
| [WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) | — | — | — | — the Windows debugger for user, kernel and crash-dump analysis; now with a modern UI. (free, proprietary) |

---
*This page is auto-audited from the GitHub API on every monthly verification pass. Stars, ages and push dates are re-snapshotted; the main list only changes when a tool dies or a better one takes its place. See the [editorial standards](../README.md#-editorial-standards).*
