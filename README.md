<p align="center">
  <img src="assets/banner.png" alt="Awesome Cyber Security Heaven" width="100%">
</p>

# 🛡️ Awesome Cyber Security Heaven ☁️🔐

> **The Ultimate Curated Arsenal — 100% Free & Open Source.** A hand-curated, license-aware map of the
> best free cybersecurity tools — from pentesting and bug bounty to OSINT, threat intel, DFIR,
> DevSecOps and AI/LLM security. Every entry earns its place. 🌟

🧭 **160+ curated tools** · 🏰 **12 themed realms** · 🆓 **100% free / free-tier** · 🔬 **license-verified** · 🔄 **actively maintained** · 💯 **no paywalls, no AI-gated entries**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC0](https://img.shields.io/badge/list%20content-CC0-1e8b44.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![API Verified](https://img.shields.io/badge/entries%20verified-2026--10--14-blue.svg)](#-editorial-standards)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat-square)](CONTRIBUTING.md)

**Legend** — ⚖️ `(GPL-…)` / `(AGPL-…)` = copyleft license · 🎁 `(free tier)` / `(freemium)` = free tier of a
commercial service · 🔒 `(free, proprietary)` = freeware, not open source · 🏠 `(maintainer's project)` =
the curator's own tool, included transparently.

## 📖 Contents

- [⚔️ The Armory — Offensive Security, Pentesting & Bug Bounty Tools (19)](#️-the-armory--offensive-security-pentesting--bug-bounty-tools)
- [🛡️ The Bastion — Hardening & Defensive Infrastructure Tools (12)](#️-the-bastion--hardening--defensive-infrastructure-tools)
- [🔭 The Watchtower — Threat Intelligence Tools & Feeds (10)](#-the-watchtower--threat-intelligence-tools--feeds)
- [🗺️ The Cartographers — Recon, OSINT & Attack-Surface Mapping Tools (18)](#️-the-cartographers--recon-osint--attack-surface-mapping-tools)
- [🔑 The Vault — Secrets, Credentials & Password Security Tools (11)](#-the-vault--secrets-credentials--password-security-tools)
- [🐳 The Foundry — DevSecOps, Cloud & Container Security Tools (17)](#-the-foundry--devsecops-cloud--container-security-tools)
- [🔵 The Sentinel Ops — Blue Team, SOC & DFIR Tools (15)](#-the-sentinel-ops--blue-team-soc--dfir-tools)
- [🤖 The Oracle's Domain — AI Security & LLM Security Tools (6)](#-the-oracles-domain--ai-security--llm-security-tools)
- [🆓 The Free Bazaar — Free Cybersecurity APIs, Feeds & Data (16)](#-the-free-bazaar--free-cybersecurity-apis-feeds--data)
- [🎓 The Academy — Cybersecurity Learning Resources & Career Paths (12)](#-the-academy--cybersecurity-learning-resources--career-paths)
- [🎯 The Proving Grounds — CTF Practice, Labs & Hacking Training (14)](#-the-proving-grounds--ctf-practice-labs--hacking-training)
- [🧰 The Workshop — Utilities & Swiss-Army Tools (10)](#️-the-workshop--utilities--swiss-army-tools)

---

## ⚔️ The Armory — Offensive Security, Pentesting & Bug Bounty Tools
Intro: The professional offensive toolkit for authorized engagements, red-team exercises and training labs — the weapons every pentester reaches for first.

- [Metasploit Framework](https://github.com/rapid7/metasploit-framework) — the world's most-used pentest framework; thousands of validated modules for exploitation, post-engagement evidence gathering and reporting in authorized tests.
- [Nmap](https://nmap.org) — the original network mapper: port, service and OS discovery plus the NSE scripting engine for everything from TLS audits to SMB checks.
- [Burp Suite Community Edition](https://portswigger.net/burp/communitydownload) — the industry-standard intercepting proxy for manual web testing; the free tier is where nearly every bug hunter starts. (free, proprietary)
- [Nuclei](https://github.com/projectdiscovery/nuclei) — template-driven vulnerability scanner; the huge community template corpus gives it detection breadth no single scanner matches.
- [OWASP ZAP](https://github.com/zaproxy/zaproxy) — the open-source intercepting proxy and scanner — a full free Burp alternative with CI/CD integration and a big add-on ecosystem.
- [sqlmap](https://github.com/sqlmapproject/sqlmap) — the definitive SQL injection detection and exploitation tool for authorized web application testing. (GPL-2.0)
- [Impacket](https://github.com/fortra/impacket) — the standard Python library for low-level Windows protocol work (SMB, LDAP, Kerberos); powers wmiexec/secretsdump-class tooling and AD assessments.
- [MITRE Caldera](https://github.com/apache/caldera) — scalable adversary-emulation platform built on ATT&CK; run purple-team exercises that prove your detections actually fire.
- [BloodHound](https://github.com/SpecterOps/BloodHound) — maps the shortest attack paths through Active Directory; defenders run it to find and fix their way to Domain Admin.
- [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) — all-in-one mobile app security: static + dynamic analysis for Android/iOS in a single pipeline. (GPL-3.0)
- [WPScan](https://github.com/wpscanteam/wpscan) — black-box WordPress scanner: plugin/theme enumeration and version-based vuln lookups. (free for non-commercial use)
- [Bettercap](https://github.com/bettercap/bettercap) — the Swiss-army knife for authorized network assessments: ARP/DNS spoofing, MITM proxies, WiFi and BLE modules. (GPL-3.0)
- [Nikto](https://github.com/sullo/nikto) — venerable web-server scanner; noisy but thorough on server misconfigurations and default files. (GPL-3.0; DB files have custom terms)
- [Dalfox](https://github.com/hahwul/dalfox) — fast XSS scanner with DOM-aware analysis and a strong payload set; the modern XSS go-to.
- [NetExec](https://github.com/Pennyw0rth/NetExec) — CrackMapExec's actively maintained successor; audit credential hygiene and service misconfigurations across whole subnets.
- [Responder](https://github.com/lgandx/Responder) — LLMNR/NBT-NS/MDNS poisoner; the fastest way to demonstrate credential-leak exposure on an authorized internal network. (GPL-3.0)
- [commix](https://github.com/commixproject/commix) — automated OS command injection detection and exploitation for web tests. (GPL-3.0)
- [Ghauri](https://github.com/r0oth3x49/ghauri) — a strong sqlmap alternative for error/union/blind SQLi with clever parameter tampering; slower release cadence but unique value.
- [2mny Website Vulnerability Scanner](https://github.com/RanaKhan77/Website-Vulnerability-Scanner) — open-source web vulnerability scanner with 200 deterministic modules: OWASP Top 10, XSS/SQLi/SSRF, subdomain takeover, WordPress and AI/LLM surface checks, CVSS-scored evidence and HTML/PDF reports. Self-hosted via Docker. (maintainer's project)

## 🛡️ The Bastion — Hardening & Defensive Infrastructure Tools
Intro: Lock it down before they get in — auditing, hardening and host/network defense tooling.

- [CrowdSec](https://github.com/crowdsecurity/crowdsec) — collaborative behavior-detection engine with a global IP-reputation network; the modern Fail2ban, 60x faster and IPv6-ready.
- [Fail2ban](https://github.com/fail2ban/fail2ban) — the classic log-watching IPS that bans brute-forcing IPs; still the default answer on every Linux server. (GPL-2.0)
- [Lynis](https://github.com/CISOfy/lynis) — agentless system auditing and hardening with CIS/PCI-DSS-aligned findings; runs anywhere in minutes. (GPL-3.0)
- [OpenSnitch](https://github.com/evilsocket/opensnitch) — interactive application firewall (Little Snitch for Linux): allow/deny every outbound connection per process. (GPL-3.0)
- [testssl.sh](https://github.com/drwetter/testssl.sh) — command-line TLS/SSL configuration auditor: protocols, ciphers, chains, vulnerabilities, grading — no agent required. (GPL-2.0)
- [ComplianceAsCode content](https://github.com/ComplianceAsCode/content) — the open SCAP/Baseline rule corpus for RHEL, Ubuntu and friends; the content that powers OpenSCAP-style audits.
- [ssh-audit](https://github.com/jtesta/ssh-audit) — SSH server configuration auditor: algorithms, keys and best-practice flags in one run. (GPL-3.0)
- [OSSEC](https://github.com/ossec/ossec-hids) — the original open-source HIDS: log analysis, file integrity and rootkit detection (Wazuh's ancestor). (GPL-2.0)
- [Coraza](https://github.com/corazawaf/coraza) — ModSecurity-compatible WAF engine in Go; the actively developed successor for OWASP CRS deployments.
- [OWASP Core Rule Set](https://github.com/coreruleset/coreruleset) — the world's most-deployed WAF ruleset; battle-tested protection for web servers, tuned for ModSecurity and Coraza.
- [dev-sec hardening collection](https://github.com/dev-sec/ansible-collection-hardening) — battle-tested Ansible roles for OS, SSH, nginx and MySQL baselines; hardening as code.
- [OPNsense](https://github.com/opnsense/core) — open-source firewall/router distro with IDS, VPN and reporting — a pfSense successor built on HardenedBSD. (BSD-2)

## 🔭 The Watchtower — Threat Intelligence Tools & Feeds
Intro: See what's coming — intel platforms, knowledge bases, ransomware trackers and exposure watchtowers.

- [MISP](https://github.com/MISP/MISP) — the de-facto open threat-sharing platform: events, attributes, galaxies and thousands of community feeds. (AGPL-3.0)
- [OpenCTI](https://github.com/OpenCTI-Platform/OpenCTI) — threat-intel knowledge graph built on STIX2; analyst-first investigation dashboards instead of raw feeds.
- [MITRE ATT&CK](https://attack.mitre.org) — the adversary tactics & techniques knowledge base that the entire industry maps detections and emulations against.
- [IntelOwl](https://github.com/intelowlproject/IntelOwl) — bulk-analyze observables across 100+ online services from one API and web UI. (AGPL-3.0)
- [SpiderFoot](https://github.com/smicallef/spiderfoot) — open-source OSINT automation with 200+ data sources; attack-surface and exposure monitoring out of the box.
- [Uncover](https://github.com/projectdiscovery/uncover) — query exposed services across Shodan, Censys and friends in one sweep — the instant exposure check.
- [Yeti](https://github.com/yeti-platform/yeti) — organize your threat intel: observables, indicators and TTPs in one searchable, API-first platform.
- [RansomLook](https://github.com/RansomLook/RansomLook) — open ransomware-group leak-site tracker with historical victim data (see also the live stats at ransomware.live). (GPL-3.0)
- [Malpedia](https://malpedia.caad.fkie.fraunhofer.de) — curated malware encyclopedia: families, actors, papers and sample references for researchers.
- [firehol/blocklist-ipsets](https://github.com/firehol/blocklist-ipsets) — aggregated, daily-updated IP blocklists (attacks, spam, abuse) ready for iptables/fail2ban; check each list's own license before redistribution.

## 🗺️ The Cartographers — Recon, OSINT & Attack-Surface Mapping Tools
Intro: Map the terrain before you move — subdomain, content and OSINT discovery for bug bounty and asset management.

- [Amass](https://github.com/owasp-amass/amass) — deep attack-surface mapping: DNS enumeration, scraping, archives, APIs and permutations in one OWASP project.
- [subfinder](https://github.com/projectdiscovery/subfinder) — fast, passive subdomain discovery from dozens of sources; the standard first command of any engagement.
- [katana](https://github.com/projectdiscovery/katana) — next-generation crawler with headless-browser support for JavaScript-heavy applications.
- [theHarvester](https://github.com/laramies/theHarvester) — emails, subdomains, hosts and names from public sources — the OSINT starter kit. (GPL-2.0)
- [httpx](https://github.com/projectdiscovery/httpx) — the HTTP prober: filter thousands of hosts by status, title, tech, CDN and TLS in a single pass.
- [bbot](https://github.com/blacklanternsecurity/bbot) — recursive, modular OSINT/scanning framework — spider the whole attack surface with one command. (AGPL-3.0)
- [feroxbuster](https://github.com/epi052/feroxbuster) — fast recursive content discovery in Rust with great heuristics and recursion handling.
- [ffuf](https://github.com/ffuf/ffuf) — the fast web fuzzer everyone uses for content, parameter and vhost discovery.
- [GHunt](https://github.com/mxrch/GHunt) — investigate a Google account's public footprint (photos, reviews, services) from an email — for authorized OSINT; respect ToS. (AGPL-3.0)
- [sherlock](https://github.com/sherlock-project/sherlock) — hunt one username across 400+ social networks; people-OSINT in seconds.
- [naabu](https://github.com/projectdiscovery/naabu) — fast, SYN-based port scanner built to be pipelined, not watched.
- [dnsx](https://github.com/projectdiscovery/dnsx) — multi-purpose DNS toolkit: reverse lookups, wildcard detection, response filtering.
- [massdns](https://github.com/blechschmidt/massdns) — high-performance DNS stub resolver for bulk subdomain brute-forcing at scale. (GPL-3.0)
- [gobuster](https://github.com/OJ/gobuster) — the classic directory/DNS/vhost buster in Go; the tool feroxbuster and ffuf grew from.
- [gau](https://github.com/lc/gau) — fetch URLs indexed by AlienVault OTX, the Wayback Machine and Common Crawl.
- [waymore](https://github.com/xnl-h4ck3r/waymore) — pull way more from the Wayback Machine: full responses, not just URLs.
- [Maltego CE](https://www.maltego.com) — the standard OSINT graphing tool for entity-relationship investigation; free community edition. (free tier)
- [dnstwist](https://github.com/elceef/dnstwist) — detect typosquat, homograph and permutation lookalikes of your domain — a must for phishing defense and brand monitoring.

## 🔑 The Vault — Secrets, Credentials & Password Security Tools
Intro: Where secrets live and leak — find them before attackers do, and keep the new ones safe.

- [gitleaks](https://github.com/gitleaks/gitleaks) — fast git-history secret scanning from pre-commit hooks to CI; the default choice for repos.
- [trufflehog](https://github.com/trufflesecurity/trufflehog) — deep secret scanning across git, S3, Docker images and 800+ detector types with live credential verification. (AGPL-3.0)
- [hashcat](https://github.com/hashcat/hashcat) — the world's fastest password-recovery tool; the standard for authorized password-strength audits.
- [John the Ripper](https://github.com/openwall/john) — the classic password auditor: hundreds of hash formats and the legendary jumbo community build. (GPL-2.0)
- [KeePassXC](https://github.com/keepassxreboot/keepassxc) — cross-platform, offline, no-cloud password manager — the security-community standard. (GPL-3.0)
- [Bitwarden](https://github.com/bitwarden/server) — open-source, sync-everywhere password management for teams and families. (AGPL + commercial options)
- [HashiCorp Vault](https://github.com/hashicorp/vault) — the enterprise secrets platform: dynamic credentials, PKI, encryption-as-a-service. (source-available BSL)
- [SOPS](https://github.com/getsops/sops) — encrypted secrets in git: edit YAML/JSON values, commit ciphertext, rotate keys. (MPL-2.0)
- [age](https://github.com/FiloSottile/age) — simple, modern, opinionated file-encryption tool for the post-GPG era.
- [detect-secrets](https://github.com/Yelp/detect-secrets) — enterprise secret scanner designed for baseline diffs and incremental CI audits.
- [noseyparker](https://github.com/praetorian-inc/noseyparker) — blazing-fast secret scanning built for huge codebases and full-history sweeps.

## 🐳 The Foundry — DevSecOps, Cloud & Container Security Tools
Intro: Shift security left — SAST, SCA, IaC, SBOM and container scanning that fit the pipeline.

- [Trivy](https://github.com/aquasecurity/trivy) — the all-in-one scanner: containers, IaC, repos, SBOMs, licenses and secrets, with one binary.
- [Semgrep](https://github.com/semgrep/semgrep) — fast, expressive static analysis with community rule packs for 30+ languages; write rules like you write code. (LGPL-2.1)
- [Falco](https://github.com/falcosecurity/falco) — CNCF runtime threat detection for containers, Kubernetes and cloud workloads.
- [Prowler](https://github.com/prowler-cloud/prowler) — AWS/Azure/GCP security posture: hundreds of checks mapped to CIS benchmarks and compliance frameworks.
- [Grype](https://github.com/anchore/grype) — vulnerability scanner for container images and SBOMs with KEV/EPSS enrichment for prioritization.
- [Syft](https://github.com/anchore/syft) — generate clean SBOMs (SPDX/CycloneDX) from images and filesystems; feeds Grype and everything else.
- [OSV-Scanner](https://github.com/google/osv-scanner) — dependency vulnerability scanner backed by Google's OSV database; fast, transparent, no vendor lock.
- [Checkov](https://github.com/bridgecrewio/checkov) — IaC scanning for Terraform, CloudFormation, Kubernetes and more, with auto-fix guidance.
- [KICS](https://github.com/Checkmarx/kics) — 1,000+ security queries across Terraform, Ansible, K8s, Dockerfile and other IaC.
- [Kyverno](https://github.com/kyverno/kyverno) — CNCF policy engine for Kubernetes: validate, mutate and generate configurations as code.
- [kube-bench](https://github.com/aquasecurity/kube-bench) — run the CIS Kubernetes Benchmark checks against your nodes in minutes.
- [OWASP Dependency-Check](https://github.com/jeremylong/DependencyCheck) — the classic SCA engine: NVD-backed dependency CVE scanning for JVM/.NET/JS ecosystems.
- [Dependency-Track](https://github.com/DependencyTrack/dependency-track) — SBOM-based continuous component analysis platform with portfolio risk dashboards.
- [ScoutSuite](https://github.com/nccgroup/ScoutSuite) — the classic multi-cloud security auditor with a friendly HTML report — quiet upstream, still the reference. (GPL-3.0)
- [cosign](https://github.com/sigstore/cosign) — Sigstore's keyless container signing and verification; make provenance part of your pipeline.
- [Bandit](https://github.com/PyCQA/bandit) — the standard Python security linter; wire it into CI and never merge an `eval()` again.
- [Brakeman](https://github.com/presidentbeef/brakeman) — static analysis purpose-built for Ruby on Rails; no config, no instrumentation, just findings.

## 🔵 The Sentinel Ops — Blue Team, SOC & DFIR Tools
Intro: Detect, hunt, forensicate — the defensive operations toolkit.

- [Wazuh](https://github.com/wazuh/wazuh) — open-source XDR/SIEM: FIM, log analysis, vulnerability detection and compliance reporting in one free platform. (GPL-2.0)
- [Velociraptor](https://github.com/Velocidex/velociraptor) — endpoint visibility and DFIR at scale: hunt across thousands of machines with one query language. (AGPL-3.0)
- [Suricata](https://github.com/OISF/suricata) — high-performance IDS/IPS/NSM engine with full protocol logging and Eve JSON output. (GPL-2.0)
- [Zeek](https://github.com/zeek/zeek) — the network analysis framework that turns raw traffic into structured, queryable intelligence. (BSD-3)
- [YARA](https://github.com/VirusTotal/yara) — the pattern-matching language for malware identification — if you write detections, you write YARA. (BSD-3)
- [Sigma](https://github.com/SigmaHQ/sigma) — vendor-neutral SIEM detection rules — "Snort for logs", convertible to Splunk/Sentinel/Elastic. (DRL 1.1 rules)
- [osquery](https://github.com/osquery/osquery) — operate endpoints as a SQL database: ask security questions, get rows back.
- [Security Onion](https://github.com/Security-Onion-Solutions/securityonion) — the free SOC-in-a-box distro: Suricata, Zeek, Elastic, dashboards and detection pipelines. (Elastic License 2.0)
- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) — library of executable detection tests mapped to MITRE ATT&CK; prove your defenses fire.
- [Timesketch](https://github.com/google/timesketch) — Google's collaborative forensic timeline analysis for multi-investigator cases.
- [Volatility 3](https://github.com/volatilityfoundation/volatility3) — memory forensics framework — RAM malware has nowhere to hide.
- [CAPEv2](https://github.com/CAPEv2/CAPEv2) — the maintained Cuckoo sandbox: automated malware detonation, config extraction and reporting. (GPL-3.0)
- [Arkime](https://github.com/arkime/arkime) — full-packet capture plus indexed search at scale (formerly Moloch); PCAP you can actually query.
- [RITA](https://github.com/activecm/rita) — detects C2 beaconing in Zeek logs — traffic analysis that finds the quiet intruders. (GPL-3.0)
- [sysmon-config](https://github.com/SwiftOnSecurity/sysmon-config) — the battle-tested Sysmon configuration behind thousands of SOC detections; the de-facto starting point for Windows telemetry.

## 🤖 The Oracle's Domain — AI Security & LLM Security Tools
Intro: Secure the new surface — LLM red teaming, guardrails and model-file safety for AI-powered applications.

- [promptfoo](https://github.com/promptfoo/promptfoo) — LLM evaluation and red-teaming framework: prompt-injection and jailbreak test suites that run in CI.
- [garak](https://github.com/NVIDIA/garak) — NVIDIA's LLM vulnerability scanner: hundreds of probes for injection, data leakage, hallucination and misuse.
- [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) — programmable guardrail layer for LLM apps: input/output rails, dialog safety, topic control.
- [deepteam](https://github.com/confident-ai/deepteam) — red-teaming library for LLMs: simulated attacks with vulnerability scoring and reporting.
- [modelscan](https://github.com/protectai/modelscan) — scan model files (pickle, safetensors) for malicious code before you load them — supply-chain defense for ML.
- [OWASP Top 10 for LLM Applications](https://genai.owasp.org) — the standard risk taxonomy for LLM apps; the shared language for AI threat modeling.

## 🆓 The Free Bazaar — Free Cybersecurity APIs, Feeds & Data
Intro: Free (or free-tier) data sources every security program should be using — no budget required.

- [Shodan](https://www.shodan.io) — the search engine for internet-exposed devices; free tier plus Monitor alerts for your own assets (free tier)
- [VirusTotal](https://www.virustotal.com) — the multi-engine file/URL reputation service with a free public API.
- [HaveIBeenPwned](https://haveibeenpwned.com) — breach database lookups for emails and whole domains, with a free API.
- [Censys](https://search.censys.io) — internet asset search with certificate-aware pivots; free academic/community tier. (free tier)
- [GreyNoise](https://www.greynoise.io) — classifies internet-wide scanner noise so your team can ignore it; free community API.
- [AbuseIPDB](https://www.abuseipdb.com) — community-driven IP-abuse reports with a free API (1,000 checks/day).
- [urlscan.io](https://urlscan.io) — URL scanning with sandbox screenshots and full resource capture; free tier. (free tier)
- [AlienVault OTX](https://otx.alienvault.com) — open threat exchange: community-contributed threat pulses with a free API.
- [PhishTank](https://phishtank.org) — the community phishing-URL database with a free API.
- [abuse.ch](https://abuse.ch) — the free malware-intel feed suite: URLhaus, ThreatFox, MalwareBazaar and Feodo Tracker.
- [CISA KEV Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — the Known Exploited Vulnerabilities list; patch-first prioritization, straight from the source.
- [NVD](https://nvd.nist.gov) — the National Vulnerability Database feeds and API (free API key) — the backbone of CVE enrichment.
- [OSV.dev](https://osv.dev) — Google's open-source vulnerability database with a clean free API and per-package queries.
- [FIRST EPSS](https://www.first.org/epss) — exploit-prediction scores for every CVE — probability-based patch prioritization, free data.
- [Exploit-DB](https://www.exploit-db.com) — the classic public exploit archive and Google Hacking Database; still where PoCs surface first.
- [SecLists](https://github.com/danielmiessler/SecLists) — the security tester's wordlist collection: usernames, passwords, URLs, fuzz payloads — the one corpus everyone uses.

## 🎓 The Academy — Cybersecurity Learning Resources & Career Paths
Intro: Learn the craft — free academies, knowledge bases, walkthroughs and career roadmaps.

- [PortSwigger Web Security Academy](https://portswigger.net/web-security) — free, best-in-class web-hacking labs from the Burp Suite team; the standard web-security curriculum.
- [HackTricks](https://github.com/HackTricks-wiki/hacktricks) — the pentester's playbook: technique-by-technique attack references from recon to post-exploitation. (free; custom content license)
- [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) — the curated payload and methodology repo — copy, paste, understand, learn.
- [GTFOBins](https://github.com/GTFOBins/GTFOBins.github.io) — the living Linux binary-abuse matrix; the privilege-escalation bible. (GPL-3.0)
- [LOLBAS](https://github.com/LOLBAS-Project/LOLBAS) — the Windows counterpart to GTFOBins: living-off-the-land binaries and scripts. (GPL-3.0)
- [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) — the Web Security Testing Guide — the methodology standard for thorough assessments.
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) — concise, developer-friendly defensive guidance per topic; the fix side of every finding.
- [hacker-roadmap](https://github.com/sundowndev/hacker-roadmap) — the illustrated cybersecurity study/career roadmap; the "where do I start?" answer.
- [Professor Messer](https://www.professormesser.com) — free complete video courses for Security+, Network+ and CySA+; the default free cert-prep resource.
- [pwn.college](https://pwn.college) — ASU's free hands-on curriculum from Linux basics to kernel exploitation, with dojo challenges.
- [IppSec](https://ippsec.rocks) — the legendary HTB walkthrough archive; watch a master work through every box, searchable by technique.
- [LiveOverflow](https://www.youtube.com/@LiveOverflow) — deep-dive security videos that explain *why* things break — the channel every hacker watched.

## 🎯 The Proving Grounds — CTF Practice, Labs & Hacking Training
Intro: Hack legally — wargames, CTF platforms and deliberately-vulnerable apps to sharpen your skills.

- [Hack The Box](https://www.hackthebox.com) — the platform for ranked machines, pro labs and active-dir ranges; the industry's proving ground. (free tier)
- [TryHackMe](https://tryhackme.com) — guided rooms from your first command to advanced red/blue paths — the friendliest on-ramp. (free tier)
- [picoCTF](https://picoctf.org) — CMU's beginner-friendly CTF — the best first flag anyone can capture.
- [OverTheWire](https://overthewire.org) — Bandit and friends: learn Linux, networking and protocols through SSH wargames.
- [VulnHub](https://www.vulnhub.com) — downloadable vulnerable VMs; build and break your own home lab offline.
- [CTFtime](https://ctftime.org) — the global CTF calendar, team rankings and writeup index — the hub of the sport.
- [OWASP Juice Shop](https://github.com/juice-shop/juice-shop) — the modern deliberately-vulnerable app with gamified challenges covering the whole OWASP spectrum.
- [DVWA](https://github.com/digininja/DVWA) — the classic Damn Vulnerable Web Application for safely learning injection basics. (GPL-3.0)
- [WebGoat](https://github.com/WebGoat/WebGoat) — OWASP's teaching app: guided lessons with a solution walkthrough for each vulnerability class. (GPL-2.0)
- [Metasploitable 3](https://github.com/rapid7/metasploitable3) — Rapid7's purpose-built vulnerable target VM; the canonical Metasploit practice range.
- [CTFd](https://github.com/CTFd/CTFd) — the CTF platform that powers thousands of events; self-host your own competition.
- [pwntools](https://github.com/Gallopsled/pwntools) — the CTF exploit-development library: from sockets to ROP chains, pwn everything.
- [Cryptopals](https://cryptopals.com) — the legendary crypto challenges; finish them and AES is no longer magic.
- [Gandalf](https://gandalf.lakera.ai) — Lakera's free prompt-injection game; learn AI-security attacks hands-on, level by level.

## 🧰 The Workshop — Utilities & Swiss-Army Tools
Intro: The everyday carry — decoding, proxying, dissecting and transforming anything the job throws at you.

- [CyberChef](https://github.com/gchq/CyberChef) — GCHQ's web Swiss-army knife: 400+ operations for decoding, transforming and analyzing data, all client-side.
- [Wireshark](https://www.wireshark.org) — the packet analyzer everyone knows; deep protocol visibility for troubleshooting and forensics. (GPL-2.0)
- [Ghidra](https://github.com/NationalSecurityAgency/ghidra) — the NSA's open-source reverse-engineering suite; disassembly, decompilation and scripting for free.
- [tcpdump](https://www.tcpdump.org) — the command-line packet capture classic; quick looks and long captures where Wireshark won't fit.
- [mitmproxy](https://github.com/mitmproxy/mitmproxy) — interactive HTTPS interception for debugging and testing your own apps; scriptable as a library.
- [Frida](https://github.com/frida/frida) — inject JavaScript into running processes; dynamic instrumentation for mobile, desktop and IoT. (GPL-2.0 / wxWindows dual)
- [Interactsh](https://github.com/projectdiscovery/interactsh) — out-of-band interaction server for detecting blind vulnerabilities (SSRF, blind RCE, blind XXE).
- [Ciphey](https://github.com/Ciphey/Ciphey) — automated decoder: paste ciphertext, get plaintext plus the method used — evidence triage in seconds.
- [pyWhat](https://github.com/bee-san/pyWhat) — identify anything: hashes, keys, URLs, PII — the "what is this string?" answer.
- [ExifTool](https://github.com/exiftool/exiftool) — the metadata reader/writer for files and images; the last word in metadata triage. (Perl Artistic/GPL)


---

## 🧭 Editorial Standards

Entries must be **free (or free-tier)**, **actively maintained**, and **useful to professionals**.
Copyleft, freemium and proprietary licenses are marked inline. Archived, stale or
non-redistributable projects are excluded by policy. One entry is the curator's own project,
marked `(maintainer's project)`.

✔ Flagship entries' license & activity verified via GitHub API on 2026-10-14 — re-verified quarterly.

## 🤝 Contributing

Found a tool that belongs in Heaven? PRs are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md) for
the entry criteria (free/free-tier + maintained within the last 12 months + a one-line
"when to use it" case + license disclosed if non-permissive).

⭐ **Found Heaven useful?** Starring is the fastest way to help other defenders and bug hunters find it —
and it tells us the quarterly re-verification grind is worth it.

## 💙 Keep Heaven Free

This curation — license checks, API-verified activity, dead-link sweeps and quarterly re-verification —
is supporter-funded. If this map saved you hours of tool-hunting:

- 💵 **USDT (TRC-20):** `TVsfHEzwb9zRz9nMpGVkdL7ABTTvmUcPii`
- 💳 **PayPal / card:** [2mny.com/support](https://2mny.com/support)
- ⭐ **Free alternative:** press the Star button top-right — it genuinely helps others find this list.

Every entry stays free. No ads, no sponsored placements, no data selling — ever.

## 📄 License

The list content is released under [CC0 1.0](LICENSE) (public domain dedication).
Each linked tool retains its own license — check before commercial use.
