# 🔑 The Vault

> **18 tools** · [← Back to the main list](../README.md) · Data verified **2026-10-22** (re-verified monthly)

## Curator's notes

Credential hygiene: secret scanners, live-secret verifiers, password audit corpora and hash oracles. We deliberately list no credential-attack or cracking-delivery tools — the line between auditing and attacking credentials is a policy, not an accident.

## Maintenance snapshot (2026-10-22)

- **Active in the last 30 days:** 10 of 16 tracked GitHub repos (63%)
- **Quiet classics (no push in 12+ months, still listed):** LaZagne
- **Earliest entries:** John the Ripper (2011), LaZagne (2015), HashiCorp Vault (2015)

## Flagship picks

| Tool | ★ Stars | Created | Last push | What it does |
|---|---|---|---|---|
| [HashiCorp Vault](https://github.com/hashicorp/vault) | 36.4k | 2015 | 2026-10-21 ✅ | A tool for secrets management, encryption as a service, and privileged access management |
| [gitleaks](https://github.com/gitleaks/gitleaks) | 30.2k | 2018 | 2026-09-30 ✅ | Find secrets with Gitleaks 🔑 |
| [KeePassXC](https://github.com/keepassxreboot/keepassxc) | 29.4k | 2016 | 2026-10-21 ✅ | KeePassXC is a cross-platform community-driven port of the Windows application “KeePass Password Safe”. |
| [trufflehog](https://github.com/trufflesecurity/trufflehog) | 28.6k | 2016 | 2026-10-22 ✅ | Find, verify, and analyze leaked credentials |
| [hashcat](https://github.com/hashcat/hashcat) | 27k | 2015 | 2026-10-21 ✅ | World's fastest and most advanced password recovery utility |
| [age](https://github.com/FiloSottile/age) | 24k | 2019 | 2026-08-29 | A simple, modern and secure encryption tool (and Go library) with small explicit keys, no config options, and… |

## Full inventory (18 tools)

| Tool | ★ Stars | Created | Last push | License / tier |
|---|---|---|---|---|
| [HashiCorp Vault](https://github.com/hashicorp/vault) | 36.4k | 2015 | 2026-10-21 ✅ | — the enterprise secrets platform: dynamic credentials, PKI, encryption-as-a-service. Used by platform teams managing secrets at scale; the open-source alternative to cloud secret stores and CyberArk for dynamic secrets. (source-available BSL) |
| [gitleaks](https://github.com/gitleaks/gitleaks) | 30.2k | 2018 | 2026-09-30 ✅ | — fast git-history secret scanning from pre-commit hooks to CI; the default choice for repos. Used by DevSecOps teams scanning repos for secrets in CI; the open-source alternative to GitGuardian's paid platform. |
| [KeePassXC](https://github.com/keepassxreboot/keepassxc) | 29.4k | 2016 | 2026-10-21 ✅ | — cross-platform, offline, no-cloud password manager — the security-community standard. Used by security-conscious professionals storing credentials offline; the community alternative to 1Password and LastPass. (GPL-3.0) |
| [trufflehog](https://github.com/trufflesecurity/trufflehog) | 28.6k | 2016 | 2026-10-22 ✅ | — deep secret scanning across git, S3, Docker images and 800+ detector types with live credential verification. Used by security teams hunting leaked secrets across git history and object stores; the open-source alternative to commercial secret-scanning services. (AGPL-3.0) |
| [hashcat](https://github.com/hashcat/hashcat) | 27k | 2015 | 2026-10-21 ✅ | — the world's fastest password-recovery tool; the standard for authorized password-strength audits. Used by password auditors and DFIR teams worldwide; the cracker commercial rigs also run. |
| [age](https://github.com/FiloSottile/age) | 24k | 2019 | 2026-08-29 | — simple, modern, opinionated file-encryption tool for the post-GPG era. Used by developers wanting simple, modern file encryption; the spiritual successor to GPG for the gitops era. |
| [SOPS](https://github.com/getsops/sops) | 23.5k | 2015 | 2026-10-20 ✅ | — encrypted secrets in git: edit YAML/JSON values, commit ciphertext, rotate keys. Used by DevOps teams encrypting secrets inside config repos; the open standard for gitops-friendly secret management. (MPL-2.0) |
| [Bitwarden](https://github.com/bitwarden/server) | 20.4k | 2015 | 2026-10-22 ✅ | — open-source, sync-everywhere password management for teams and families. Used by teams and individuals wanting open-source password management; the self-hostable alternative to commercial password SaaS. (AGPL + commercial options) |
| [John the Ripper](https://github.com/openwall/john) | 13.8k | 2011 | 2026-10-11 ✅ | — the classic password auditor: hundreds of hash formats and the legendary jumbo community build. Used by password auditors for three decades; the classic open-source cracker no pentest kit ships without. (GPL-2.0) |
| [LaZagne](https://github.com/AlessandroZ/LaZagne) | 11k | 2015 | 2025-09-18 ⏳ | — audits which passwords your workstations remember — browsers, mail clients, OS stores — for authorized inventory and exposure checks only. Used by pentesters in authorized engagements demonstrating credential exposure on compromised hosts; the classic credential-harvesting tool. (LGPL-3.0) |
| [detect-secrets](https://github.com/Yelp/detect-secrets) | 4.7k | 2017 | 2026-04-02 | — enterprise secret scanner designed for baseline diffs and incremental CI audits. Used by CI pipelines baseline-scanning for secrets; Yelp's open scanner that complements commercial enterprise offerings. |
| [hardened_malloc](https://github.com/GrapheneOS/hardened_malloc) | 2k | 2018 | 2026-10-21 ✅ | — the allocator that makes exploitation harder by design; from the GrapheneOS project. Used by hardened deployments and privacy distros for exploit-mitigating memory allocation; the open allocator adopted by GrapheneOS-class systems. (MIT) |
| [Kingfisher](https://github.com/mongodb/kingfisher) | 1.3k | 2025 | 2026-10-20 ✅ | — MongoDB's open-source Rust secret scanner: detect leaked secrets across code/Git/history/containers/cloud, then live-validate credentials, map blast radius and revoke — the full post-detection lifecycle. Used by security teams killing the "leaked-but-rotated key" false-positive class; embeddable as CLI, Rust lib or Python SDK. (Apache-2.0) |
| [keyFinder](https://github.com/momenbasel/keyFinder) | 726 | 2019 | 2026-07-19 | — passively discovers leaked API keys and secrets in web pages during browsing. Used by forensic analysts locating crypto key material in memory images; the niche free utility for DFIR work. (MIT) |
| [Retraced (BoxyHQ)](https://github.com/retracedhq/retraced) | 451 | 2016 | 2026-08-07 | — open-source audit-log API: compliant, tamper-evident activity records for your SaaS. Used by SaaS builders adding compliance-grade audit logging; the open-source alternative to commercial audit-log services. (Apache-2.0) |
| [siloscan](https://github.com/RandomCodeSpace/siloscan) | - | 2026 | 2026-09-12 | — offline air-gapped repository secret and code-quality scanner with 228 rules and SARIF output; zero telemetry. Used by teams scanning sensitive repositories where nothing may leave the network; the air-gap-friendly secret scanner for restricted environments. (MIT) |
|---|---|---|---|---|
| [Databunker](https://databunker.org/) | — | — | — | — encrypted personal-data vault: API-first storage for PII with built-in privacy compliance. Used by backend teams storing customer PII encrypted and auditable; the open-source alternative to commercial customer-data vaults. (GPL-3.0) |
| [MAT2](https://0xacab.org/jvoisin/mat2) | — | — | — | — Metadata Anonymisation Toolkit v2: strips hidden metadata from documents, images and more. Used by journalists and privacy-conscious users stripping metadata from documents; the free alternative to commercial redaction suites. (GPL-3.0) |

---
*This page is auto-audited from the GitHub API on every monthly verification pass. Stars, ages and push dates are re-snapshotted; the main list only changes when a tool dies or a better one takes its place. See the [editorial standards](../README.md#-editorial-standards).*
