# The Vault

> **17 tools** · [← Back to the main list](../README.md) · Data verified **2026-10-15** (re-verified monthly)

## Curator's notes

Credential hygiene: secret scanners, live-secret verifiers, password audit corpora and hash oracles. We deliberately list no credential-attack or cracking-delivery tools — the line between auditing and attacking credentials is a policy, not an accident.

## Maintenance snapshot (2026-10-15)

- **Active in the last 30 days:** 7 of 15 tracked GitHub repos (47%)
- **Archived upstream (kept — still reference-quality):** [noseyparker](https://github.com/praetorian-inc/noseyparker)
- **Youngest entries:** John the Ripper (2011), LaZagne (2015), HashiCorp Vault (2015)

## Flagship picks

| Tool | ★ Stars | Created | Last push | What it does |
|---|---|---|---|---|
| [HashiCorp Vault](https://github.com/hashicorp/vault) | 36.4k | 2015 | 2026-10-14 ✅ | A tool for secrets management, encryption as a service, and privileged access management |
| [gitleaks](https://github.com/gitleaks/gitleaks) | 30.0k | 2018 | 2026-09-30 ✅ | Find secrets with Gitleaks 🔑 |
| [KeePassXC](https://github.com/keepassxreboot/keepassxc) | 29.2k | 2016 | 2026-10-14 ✅ | KeePassXC is a cross-platform community-driven port of the Windows application “KeePass Password Safe”. |
| [trufflehog](https://github.com/trufflesecurity/trufflehog) | 28.5k | 2016 | 2026-10-15 ✅ | Find, verify, and analyze leaked credentials |
| [hashcat](https://github.com/hashcat/hashcat) | 27.0k | 2015 | 2026-10-15 ✅ | World's fastest and most advanced password recovery utility |
| [age](https://github.com/FiloSottile/age) | 23.9k | 2019 | 2026-08-29 | A simple, modern and secure encryption tool (and Go library) with small explicit keys, no config options, and |

## Full inventory (17 tools)

| Tool | ★ Stars | Created | Last push | License / tier |
|---|---|---|---|---|
| [HashiCorp Vault](https://github.com/hashicorp/vault) | 36.4k | 2015 | 2026-10-14 ✅ | — the enterprise secrets platform: dynamic credentials, PKI, encryption-as-a-service. (source-available BSL) |
| [gitleaks](https://github.com/gitleaks/gitleaks) | 30.0k | 2018 | 2026-09-30 ✅ | — fast git-history secret scanning from pre-commit hooks to CI; the default choice for repos. |
| [KeePassXC](https://github.com/keepassxreboot/keepassxc) | 29.2k | 2016 | 2026-10-14 ✅ | — cross-platform, offline, no-cloud password manager — the security-community standard. (GPL-3.0) |
| [trufflehog](https://github.com/trufflesecurity/trufflehog) | 28.5k | 2016 | 2026-10-15 ✅ | — deep secret scanning across git, S3, Docker images and 800+ detector types with live credential verification. (AGPL-3.0) |
| [hashcat](https://github.com/hashcat/hashcat) | 27.0k | 2015 | 2026-10-15 ✅ | — the world's fastest password-recovery tool; the standard for authorized password-strength audits. |
| [age](https://github.com/FiloSottile/age) | 23.9k | 2019 | 2026-08-29 | — simple, modern, opinionated file-encryption tool for the post-GPG era. |
| [SOPS](https://github.com/getsops/sops) | 23.4k | 2015 | 2026-10-13 ✅ | — encrypted secrets in git: edit YAML/JSON values, commit ciphertext, rotate keys. (MPL-2.0) |
| [Bitwarden](https://github.com/bitwarden/server) | 20.3k | 2015 | 2026-10-15 ✅ | — open-source, sync-everywhere password management for teams and families. (AGPL + commercial options) |
| [John the Ripper](https://github.com/openwall/john) | 13.8k | 2011 | 2026-10-11 ✅ | — the classic password auditor: hundreds of hash formats and the legendary jumbo community build. (GPL-2.0) |
| [LaZagne](https://github.com/AlessandroZ/LaZagne) | 11.0k | 2015 | 2025-09-18 ⏳ | — audits which passwords your workstations remember — browsers, mail clients, OS stores — for authorized inventory and exposure checks only. (LGPL-3.0) |
| [detect-secrets](https://github.com/Yelp/detect-secrets) | 4.7k | 2017 | 2026-04-02 | — enterprise secret scanner designed for baseline diffs and incremental CI audits. |
| [noseyparker](https://github.com/praetorian-inc/noseyparker) | 2.3k | 2022 | 2026-02-21 | — blazing-fast secret scanning built for huge codebases and full-history sweeps. |
| [hardened_malloc](https://github.com/GrapheneOS/hardened_malloc) | 2.0k | 2018 | 2026-10-07 ✅ | — the allocator that makes exploitation harder by design; from the GrapheneOS project. (MIT) |
| [keyFinder](https://github.com/momenbasel/keyFinder) | 724 | 2019 | 2026-07-19 | — passively discovers leaked API keys and secrets in web pages during browsing. (MIT) |
| [Retraced (BoxyHQ)](https://github.com/retracedhq/retraced) | 451 | 2016 | 2026-08-07 | — open-source audit-log API: compliant, tamper-evident activity records for your SaaS. (Apache-2.0) |
| [MAT2](https://0xacab.org/jvoisin/mat2) | — | — | — | — Metadata Anonymisation Toolkit v2: strips hidden metadata from documents, images and more. (GPL-3.0) |
| [Databunker](https://databunker.org/) | — | — | — | — encrypted personal-data vault: API-first storage for PII with built-in privacy compliance. (GPL-3.0) |

---
*This page is auto-audited from the GitHub API on every monthly verification pass. Stars, ages and push dates are re-snapshotted; the main list only changes when a tool dies or a better one takes its place. See the [editorial standards](../README.md#-editorial-standards).*
