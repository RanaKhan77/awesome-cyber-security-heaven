# 🐳 The Foundry

> **33 tools** · [← Back to the main list](../README.md) · Data verified **2026-10-23** (re-verified monthly)

## Curator's notes

The pipeline guardians — SAST, dependency scanning, IaC misconfig audits, container hardening. This realm moves fastest of all: CI/CD attack research regularly rewrites the ground rules here.

## Maintenance snapshot (2026-10-23)

- **Active in the last 30 days:** 27 of 31 tracked GitHub repos (87%)
- **Quiet classics (no push in 12+ months, still listed):** ScoutSuite, ProgPilot
- **Earliest entries:** cppcheck (2009), Brakeman (2010), Dependency-Track (2013)

## Flagship picks

| Tool | ★ Stars | Created | Last push | What it does |
|---|---|---|---|---|
| [Trivy](https://github.com/aquasecurity/trivy) | 38.6k | 2019 | 2026-10-21 ✅ | Find vulnerabilities, misconfigurations, secrets, SBOM in containers, Kubernetes, code repositories, clouds an… |
| [Semgrep](https://github.com/semgrep/semgrep) | 17.2k | 2019 | 2026-10-22 ✅ | Lightweight static analysis for many languages. Find bug variants with patterns that look like source code. |
| [Prowler](https://github.com/prowler-cloud/prowler) | 15.1k | 2016 | 2026-10-21 ✅ | This repo hosts Prowler OSS (CLI and Local Server). Prowler is the world’s most widely used open-source cloud… |
| [Grype](https://github.com/anchore/grype) | 13.1k | 2020 | 2026-10-21 ✅ | A vulnerability scanner for container images and filesystems |
| [Kubescape](https://github.com/kubescape/kubescape) | 11.8k | 2021 | 2026-10-22 ✅ | Kubescape is an open-source Kubernetes security platform for your IDE, CI/CD pipelines, and clusters. It inclu… |
| [OSV-Scanner](https://github.com/google/osv-scanner) | 11.2k | 2022 | 2026-10-21 ✅ | Vulnerability scanner written in Go which uses the data provided by https://osv.dev |

## Full inventory (33 tools)

| Tool | ★ Stars | Created | Last push | License / tier |
|---|---|---|---|---|
| [Trivy](https://github.com/aquasecurity/trivy) | 38.6k | 2019 | 2026-10-21 ✅ | — the all-in-one scanner: containers, IaC, repos, SBOMs, licenses and secrets, with one binary. Used by DevSecOps teams scanning containers, IaC and repos in CI; the open-source alternative to Snyk and Aqua's commercial scanners. |
| [Semgrep](https://github.com/semgrep/semgrep) | 17.2k | 2019 | 2026-10-22 ✅ | — fast, expressive static analysis with community rule packs for 30+ languages; write rules like you write code. Used by AppSec teams writing custom code-scanning rules fast; the open-source alternative to commercial SAST like Checkmarx and Veracode. (LGPL-2.1) |
| [Prowler](https://github.com/prowler-cloud/prowler) | 15.1k | 2016 | 2026-10-21 ✅ | — AWS/Azure/GCP security posture: hundreds of checks mapped to CIS benchmarks and compliance frameworks. Used by cloud security teams auditing AWS, GCP and Azure; the open-source alternative to commercial CSPM platforms. |
| [Grype](https://github.com/anchore/grype) | 13.1k | 2020 | 2026-10-21 ✅ | — vulnerability scanner for container images and SBOMs with KEV/EPSS enrichment for prioritization. Used in CI pipelines scanning SBOMs and images for vulnerabilities; the open-source vulnerability scanner from Anchore. |
| [Kubescape](https://github.com/kubescape/kubescape) | 11.8k | 2021 | 2026-10-22 ✅ | — CNCF-incubating Kubernetes security platform: scan manifests, Helm charts, Kustomize dirs, live clusters and images against NSA-CISA, MITRE ATT&CK and CIS frameworks from one CLI. Used by platform teams hardening k8s before and after deploy; CNCF-backed with an in-cluster operator option. (Apache-2.0) |
| [OSV-Scanner](https://github.com/google/osv-scanner) | 11.2k | 2022 | 2026-10-21 ✅ | — dependency vulnerability scanner backed by Google's OSV database; fast, transparent, no vendor lock. Used by developers scanning dependencies against the OSV database; Google's free alternative to commercial SCA tools. |
| [Clair](https://github.com/quay/clair) | 11.1k | 2015 | 2026-10-14 ✅ | — static vulnerability analysis for container images and registries, from the Quay project. Used by platform teams scanning images in CI/CD pipelines; the veteran open-source container scanner alongside Grype and Trivy. (Apache-2.0) || [Syft](https://github.com/anchore/syft) | 9.7k | 2020 | 2026-10-21 ✅ | — generate clean SBOMs (SPDX/CycloneDX) from images and filesystems; feeds Grype and everything else. Used by supply-chain teams producing SBOMs in CI; the open-source SBOM generator that Grype and commercial tooling build on. |
| [Docker Bench for Security](https://github.com/docker/docker-bench-security) | 9.7k | 2015 | 2026-06-04 | — audits your Docker host and daemon configuration against the CIS Benchmark in a single script run. Used by admins auditing Docker hosts against the CIS benchmark; the reference open-source check script. |
| [Falco](https://github.com/falcosecurity/falco) | 9.5k | 2016 | 2026-10-20 ✅ | — CNCF runtime threat detection for containers, Kubernetes and cloud workloads. Used by cloud SOC teams detecting runtime threats in Kubernetes; the open-source alternative to commercial CNAPP runtime agents. |
| [Checkov](https://github.com/bridgecrewio/checkov) | 9.1k | 2019 | 2026-10-20 ✅ | — IaC scanning for Terraform, CloudFormation, Kubernetes and more, with auto-fix guidance. Used by DevSecOps scanning Terraform, CloudFormation and Kubernetes for misconfigurations; the open-source IaC scanner alternative to commercial policy platforms. |
| [Bandit](https://github.com/PyCQA/bandit) | 8.3k | 2018 | 2026-10-19 ✅ | — the standard Python security linter; wire it into CI and never merge an `eval()` again. Used by Python teams catching security issues in CI; the standard open-source Python SAST tool. |
| [Kyverno](https://github.com/kyverno/kyverno) | 8.3k | 2019 | 2026-10-22 ✅ | — CNCF policy engine for Kubernetes: validate, mutate and generate configurations as code. Used by Kubernetes platform teams enforcing policies natively in-cluster; the CNCF alternative to commercial admission-control products. |
| [kube-bench](https://github.com/aquasecurity/kube-bench) | 8.2k | 2017 | 2026-10-19 ✅ | — run the CIS Kubernetes Benchmark checks against your nodes in minutes. Used by cluster admins running CIS Kubernetes benchmarks; the open-source compliance check for cluster hardening. |
| [ScoutSuite](https://github.com/nccgroup/ScoutSuite) | 7.9k | 2018 | 2025-09-23 ⏳ | — the classic multi-cloud security auditor with a friendly HTML report — quiet upstream, still the reference. Used by cloud auditors assessing multi-cloud security posture; the open-source alternative to commercial cloud-security audits. (GPL-3.0) |
| [Brakeman](https://github.com/presidentbeef/brakeman) | 7.3k | 2010 | 2026-10-22 ✅ | — static analysis purpose-built for Ruby on Rails; no config, no instrumentation, just findings. Used by Rails teams scanning source for security flaws; the standard open-source Rails SAST tool. |
| [cppcheck](https://github.com/danmar/cppcheck) | 6.8k | 2009 | 2026-10-21 ✅ | — static analysis for C/C++: detects bugs and undefined behavior, not just style. Used by C/C++ developers catching defects and undefined behavior; the free static analyzer alongside commercial suites. (GPL-3.0) |
| [cosign](https://github.com/sigstore/cosign) | 6.4k | 2021 | 2026-10-21 ✅ | — Sigstore's keyless container signing and verification; make provenance part of your pipeline. Used by supply-chain automation signing and verifying containers; the Sigstore tool making signed images the default, free. |

| [Dependency-Track](https://github.com/DependencyTrack/dependency-track) | 4.3k | 2013 | 2026-10-21 ✅ | — SBOM-based continuous component analysis platform with portfolio risk dashboards. Used by supply-chain teams managing SBOMs and vulnerability exposure continuously; the OWASP alternative to commercial SBOM platforms. |
| [retire.js](https://github.com/RetireJS/retire.js) | 4.2k | 2013 | 2026-10-23 ✅ | — scanner detecting JavaScript libraries with known vulnerabilities, in web pages and Node dependencies. Used by developers and pentesters flagging risky client-side libraries; the long-standing reference scanner for this niche. (Apache-2.0) || [KICS](https://github.com/Checkmarx/kics) | 2.7k | 2020 | 2026-10-21 ✅ | — 1,000+ security queries across Terraform, Ansible, K8s, Dockerfile and other IaC. Used by platform teams scanning infrastructure-as-code across platforms; the open-source alternative to commercial IaC security products. |
| [cloudsplaining](https://github.com/salesforce/cloudsplaining) | 2.3k | 2020 | 2026-10-22 ✅ | — maps AWS IAM policies and flags the privilege-escalation paths you never meant to grant. Used by AWS security teams finding over-privileged IAM policies; the open-source alternative to commercial IAM analyzers. |

| [Copacetic](https://github.com/project-copacetic/copacetic) | 1.7k | 2023 | 2026-10-21 ✅ | — CLI that patches container images directly from vulnerability scan reports, without rebuilding the Dockerfile. Used by platform teams cutting fix latency on deployed images; a focused open-source image-patching tool. (Apache-2.0) || [ChipWhisperer](https://github.com/newaetech/chipwhisperer) | 1.6k | 2014 | 2026-10-21 ✅ | — side-channel analysis and glitching for hardware security research. Used by hardware-security researchers performing side-channel and glitching attacks; the open-source hardware lab that commercial gear costs six figures to replicate. (GPL-3.0) |
| [cwe_checker](https://github.com/fkie-cad/cwe_checker) | 1.4k | 2018 | 2026-09-28 ✅ | — finds common CWE patterns in binaries, direct from firmware images. Used by firmware auditors mapping binary patterns to CWEs; the open-source binary-analysis aid for embedded reviews. (LGPL-2.1+) |
| [Horusec](https://github.com/ZupIT/horusec) | 1.3k | 2020 | 2026-10-22 ✅ | — open-source SAST orchestration aggregating multiple language analyzers into one report. Used by dev teams running multi-language static analysis in CI; the self-hosted alternative to commercial SAST suites. (Apache-2.0) || [secureCodeBox](https://github.com/secureCodeBox/secureCodeBox) | 990 | 2017 | 2026-10-22 ✅ | — Kubernetes-native scanning orchestration: chains nmap, ZAP, Semgrep, SSLyze and more into automated pipelines. Used by DevSecOps teams running declarative scan flows; the open-source continuous-security-testing framework. (Apache-2.0) || [Substation](https://github.com/brexhq/substation) | 408 | 2022 | 2026-10-16 ✅ | — an event and data pipeline toolkit for detection engineering at scale. Used by OT/ICS security researchers testing industrial protocols; the open-source toolkit for power-grid-class engagements. (MIT) |
| [ProgPilot](https://github.com/designsecurity/progpilot) | 370 | 2017 | 2025-08-17 ⏳ | — static taint analysis for PHP sources: finds input-to-sink flows at build time. Used by PHP AppSec teams doing taint analysis of sources and sinks; the open-source PHP static-analysis tool. (GPL-3.0) |

| [command-center](https://github.com/openjs-foundation/command-center) | 3 | 2025 | 2026-04-17 | — OpenJS security and compliance monitor tracking SECURITY.md hygiene and OSSF Scorecard posture across projects. Used by open-source maintainers monitoring project security posture; the OpenJS supply-chain health monitor. (MIT) |
| [StackRadar](https://github.com/lockdep/stackradar) | 3 | 2026 | 2026-10-20 ✅ | — Kubernetes vulnerability scanner that builds an SBOM of every running image and ranks findings by CVSS, EPSS and CISA KEV. Used by DevSecOps teams prioritizing which container CVE actually matters in-cluster; the self-hosted alternative to commercial runtime CSPM. (AGPL-3.0) |
|---|---|---|---|---|
| [GDB](https://www.sourceware.org/gdb/) | — | — | — | — the GNU debugger: breakpoints, watchpoints and reverse debugging across dozens of architectures. Used by reverse engineers and exploit developers on every platform; the GNU debugger standard for binary analysis. (GPL-3.0) |
| [WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) | — | — | — | — the Windows debugger for user, kernel and crash-dump analysis; now with a modern UI. Used by malware analysts and driver developers debugging Windows; Microsoft's debugger at the core of Windows-forensics work. (free, proprietary) |

---
*This page is auto-audited from the GitHub API on every monthly verification pass. Stars, ages and push dates are re-snapshotted; the main list only changes when a tool dies or a better one takes its place. See the [editorial standards](../README.md#-editorial-standards).*
