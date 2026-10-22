# Legacy Vault — Archived & Dormant Classics

> Tools that earned their place in Heaven but whose upstream has gone quiet — nothing is deleted.
> Archived classics and dormant tools live here with their last-commit dates, so the main list
> stays a map of tools you can rely on. [← Back to the main list](README.md)
> Status verified **2026-10-23** via the GitHub API — 33 tools: 9 archived upstream, 24 dormant (no commit in 18+ months).

## The Cartographers — Recon & Fingerprinting

- [JA3](https://github.com/salesforce/ja3) - The TLS client fingerprint standard: a 12-byte hash that identifies client software across the wire. Used by defenders detecting C2 and by researchers fingerprinting TLS clients; the free hashing standard adopted by commercial sensors too. (BSD-3-Clause)
- [HASSH](https://github.com/salesforce/hassh) - SSH key-exchange fingerprinting: identify client/server software from the KEX packet alone. Used by threat hunters fingerprinting SSH clients and servers; the open fingerprinting standard for network telemetry. (BSD-3-Clause)

## The Vault — Secrets Scanning

- [noseyparker](https://github.com/praetorian-inc/noseyparker) - Blazing-fast secret scanning built for huge codebases and full-history sweeps. Used by incident responders and bug hunters scanning large corpora for secrets fast; the Rust-powered open alternative for scale.

## The Foundry — DevSecOps & SCA

- [OWASP Dependency-Check](https://github.com/jeremylong/DependencyCheck) - The classic SCA engine: NVD-backed dependency CVE scanning for JVM/.NET/JS ecosystems. Used by CI pipelines flagging vulnerable dependencies; the OWASP alternative to commercial SCA engines.

## The Oracle's Domain — AI/LLM Security

- [llm-guard](https://github.com/protectai/llm-guard) - Input/output security filtering for LLMs: prompt-injection defense as a pipeline stage. Used by AI engineers hardening prompts and outputs in production LLM services; the open-source defense library for injection and leakage risks. (MIT)

## The Academy — Learning Resources

- [hacker-roadmap](https://github.com/sundowndev/hacker-roadmap) - The illustrated cybersecurity study/career roadmap; the "where do I start?" answer. Used by beginners planning their path into security; the free curated curriculum for self-learners.

## The Proving Grounds — Practice Labs

- [DVWS (Web Services)](https://github.com/snoopysecurity/dvws) - Vulnerable web services for SOA/API security practice. Used by students practicing SOAP and REST attacks; the vulnerable web-services lab. (Apache-2.0)
- [Hackademic](https://github.com/Hackademic/hackademic) - WordPress-based vulnerable lab scenarios for classroom use. Used by learners practicing realistic web scenarios; the free vulnerable target used in RTB-era trainings. (GPL-3.0)
- [XVWA](https://github.com/s4n7h0/xvwa) - Xtreme Vulnerable Web Application: dozens of flaws across one PHP app. Used by testers practicing the full OWASP range on one app; the Xtreme Vulnerable Web Application. (GPL-3.0)

# 🧊 Dormant upstream — no commit in 18+ months (24)

Still-working tools whose upstream has not committed in 18 months or more. Last-commit dates
verified via the GitHub API on 2026-10-23. Many remain the reference implementation for their
class — but no upstream fix is coming, so they live outside the main list. *Exempt from this rule: deliberately frozen practice targets (Metasploitable, HEVD, NodeGoat, DVIA) and published datasets (EVTX-ATTACK-SAMPLES, Security Datasets, BOTS, MITRE CAR) — static artifacts are the point. Curated awesome-lists in this vault are judged on coverage completeness, not commit cadence.*

## ⚔️ The Armory

- [ACSTIS](https://github.com/tijme/angularjs-csti-scanner) - The classic AngularJS client-side template injection scanner — legacy framework, still found everywhere. Used by bug hunters verifying this niche on legacy apps. (unmaintained classic). Last upstream commit 2021-10-20 (5.0y idle).
- [JoomScan](https://github.com/OWASP/joomscan) - OWASP's Joomla scanner: vulnerable components and misconfigurations on Joomla sites; quiet upstream, still OWASP's reference. Used by pentesters auditing Joomla deployments; OWASP's free Joomla scanner. (GPL-3.0). Last upstream commit 2024-09-11 (2.1y idle).
- [tplmap](https://github.com/epinna/tplmap) - Server-side template injection detection and exploitation across a dozen template engines; quiet upstream but still the SSTI reference. Used by pentesters for server-side template injection proof across a dozen engines; no commercial equivalent needed. (GPL-3.0). Last upstream commit 2024-04-21 (2.5y idle).

## 🛡️ The Bastion

- [GoPhish](https://github.com/gophish/gophish) - Open-source phishing-simulation platform: launch awareness campaigns and measure exactly who clicks (community edition). Used by security awareness teams running phishing simulations; the open-source alternative to commercial awareness platforms like KnowBe4. Last upstream commit 2024-09-23 (2.1y idle).
- [Awesome WebSocket Security](https://github.com/PalindromeLabs/awesome-websocket-security) - Curated research, tools and CVEs for WebSocket protocol security. Used by web pentesters studying WebSocket attack surface. (Apache-2.0, curated list). Last upstream commit 2022-01-10 (4.8y idle).

## 🗺️ The Cartographers

- [assetfinder](https://github.com/tomnomnom/assetfinder) - Passive subdomain discovery that polls a dozen public sources and prints a clean list — no keys needed; quiet upstream, still the classic. Used by bug bounty hunters for quick passive subdomain finds; the lightweight staple of recon one-liners. Last upstream commit 2024-06-07 (2.4y idle).
- [dnstwist](https://github.com/elceef/dnstwist) - Detect typosquat, homograph and permutation lookalikes of your domain — a must for phishing defense and brand monitoring. Used by brand-protection and anti-phishing teams hunting lookalike domains; the open-source alternative to commercial domain-monitoring services. Last upstream commit 2025-04-15 (1.5y idle).
- [ike-scan](https://github.com/royhills/ike-scan) - IKE/IPsec security auditing: fingerprint VPN gateways and enumerate transform proposals. Used by network pentesters fingerprinting IKE/VPN endpoints; the classic free IPSec scanner. (GPL-2.0). Last upstream commit 2024-09-15 (2.1y idle).

## 🐳 The Foundry

- [kube-hunter](https://github.com/aquasecurity/kube-hunter) - Active Kubernetes security testing: probe clusters for exposed dashboards, weak RBAC and known exploits; quiet upstream. Used by cluster security teams probing Kubernetes for weaknesses; the open-source pentest tool for Kubernetes. Last upstream commit 2024-03-19 (2.6y idle).
- [logdissect](https://github.com/dogoncouch/logdissect) - Parse, merge and analyze logs from many formats into one timeline. Used by analysts parsing and correlating logs from the CLI; the open-source alternative to commercial log-analytics frontends. (MIT). Last upstream commit 2024-08-07 (2.2y idle).
- [sobelow](https://github.com/nccgroup/sobelow) - Security testing for Elixir/Phoenix applications; the Sobelow family's namesake. Used by Elixir/Phoenix teams auditing their apps; the standard security-testing tool for the Phoenix framework. (MPL-2.0). Last upstream commit 2024-08-20 (2.2y idle).
- [Awesome Container Security](https://github.com/kai5263499/container-security-awesome) - Curated container and cloud-native security resources. Used by DevSecOps engineers hardening container stacks. (MIT, curated list). Last upstream commit 2019-03-07 (7.6y idle).
- [Awesome ICS Security](https://github.com/mpesen/awesome-industrial-control-system-security) - Curated industrial-control-system security tools and research. Used by OT security engineers building their toolset. (Apache-2.0, curated list). Last upstream commit 2016-05-27 (10.4y idle).


## 🔵 The Sentinel Ops

- [DeepBlueCLI](https://github.com/sans-blue-team/DeepBlueCLI) - SANS blue-team PowerShell for fast Windows event-log hunting: logons, mutants, suspicious service installs — quiet upstream but still a blue-team staple. Used by defenders triaging Windows event logs quickly; the free PowerShell tool for fast log review. (GPL-3.0). Last upstream commit 2023-10-14 (3.0y idle).
- [HELK](https://github.com/Cyb3rWard0g/HELK) - The Hunting ELK: a pre-built Elasticsearch/Kafka/Spark lab for threat-hunting research — a research project with low churn. Used by threat-hunting learners standing up an ELK hunting lab; the open-source project for detection-engineering practice. (GPL-3.0). Last upstream commit 2024-06-01 (2.4y idle).
- [Revoke-Obfuscation](https://github.com/danielbohannon/Revoke-Obfuscation) - Daniel Bohannon's framework for detecting obfuscated PowerShell at scale; quiet upstream, still the reference. Used by DFIR analysts decoding obfuscated PowerShell; the open-source framework for deobfuscation work. Last upstream commit 2023-12-01 (2.9y idle).
- [sysmon-config](https://github.com/SwiftOnSecurity/sysmon-config) - The battle-tested Sysmon configuration behind thousands of SOC detections; the de-facto starting point for Windows telemetry. Used by blue teams deploying hardened Windows logging; the widely-adopted SwiftOnSecurity baseline. Last upstream commit 2024-07-03 (2.3y idle).

## 🕵️ The Shadow Bureau

- [holehe](https://github.com/megadose/holehe) - Checks which sites an email is registered on via password-reset and account-exist flows; quiet upstream but still the standard. Used by investigators checking which services an email registered with; the free breach-recovery check used in authorized account reviews. (GPL-3.0). Last upstream commit 2024-09-10 (2.1y idle).
- [waybackpack](https://github.com/jsvine/waybackpack) - Bulk-download a site's history from the Wayback Machine; the archivist's archive. Used by researchers downloading archived sites in bulk; the open downloader for Wayback Machine investigations. (MIT). Last upstream commit 2025-04-21 (1.5y idle).
- [waybackpy](https://github.com/akamhy/waybackpy) - Python client and CLI for the Wayback Machine: search, save and diff archived snapshots from your own scripts; quiet upstream, works fine. Used by researchers scripting Wayback Machine lookups from Python and CLI; the open client for archive intelligence. Last upstream commit 2024-02-26 (2.7y idle).

## 🧰 The Workshop

- [Voltron](https://github.com/snare/voltron) - A debugger-agnostic UI: multiple synchronized views across GDB/LLDB. Used by exploit developers unifying GDB, lldb and radare2 views; the free debugger-UI multiplexer. (MIT). Last upstream commit 2025-01-30 (1.7y idle).
- [boxxy](https://github.com/kpcyrd/boxxy-rs) - A rules-based sandbox for misbehaving programs; redirects what they touch. Used by researchers sandboxing file operations at the syscall layer; the free isolation tool for dynamic analysis. (LGPL-2.1). Last upstream commit 2025-01-23 (1.7y idle).
- [Awesome Malware Analysis](https://github.com/rshipp/awesome-malware-analysis) - The curated malware-analysis tool index. Used by malware analysts assembling their toolkit. (CC-BY-4.0, curated list). Last upstream commit 2024-06-07 (2.4y idle).

## 🎯 The Proving Grounds

- [flightsim](https://github.com/alphasoc/flightsim) - Generates malicious network traffic for IDS/NDR validation; defender-side only. Used by defenders safely generating malicious-looking network traffic; the free attack simulator for testing detections. (CC-BY-4.0). Last upstream commit 2024-04-04 (2.6y idle).

