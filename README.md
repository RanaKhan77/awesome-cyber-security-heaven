<p align="center">
  <img src="assets/banner.png" alt="Awesome Cyber Security Heaven" width="100%">
</p>

# 🛡️ Awesome Cyber Security Heaven ☁️🔐

> **The Ultimate Curated Arsenal — 100% Free & Open Source.** A hand-curated, license-aware map of the
> best free cybersecurity tools — from pentesting and bug bounty to OSINT, threat intel, DFIR,
> DevSecOps and AI/LLM security. Every entry earns its place. 🌟

🧭 **432+ curated tools** · 🏰 **13 themed realms** · 🆓 **100% free / free-tier** · 🔬 **license-verified** · 🔄 **actively maintained** · 💯 **no paywalls, no AI-gated entries**


[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC0](https://img.shields.io/badge/list%20content-CC0-1e8b44.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![API Verified](https://img.shields.io/badge/entries%20verified-2026--10--15-blue.svg)](#-editorial-standards)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat-square)](CONTRIBUTING.md)
[![Links](https://github.com/RanaKhan77/awesome-cyber-security-heaven/actions/workflows/links.yml/badge.svg)](https://github.com/RanaKhan77/awesome-cyber-security-heaven/actions/workflows/links.yml)

**Legend** — ⚖️ `(GPL-…)` / `(AGPL-…)` = copyleft license · 🎁 `(free tier)` / `(freemium)` = free tier of a
commercial service · 🔒 `(free, proprietary)` = freeware, not open source · 🏠 `(maintainer's project)` =
the curator's own tool, included transparently.

## 📖 Contents

- [⚔️ The Armory — Offensive Security, Pentesting & Bug Bounty Tools (40)](#️-the-armory--offensive-security-pentesting--bug-bounty-tools)
- [🛡️ The Bastion — Hardening & Defensive Infrastructure Tools (33)](#️-the-bastion--hardening--defensive-infrastructure-tools)
- [🔭 The Watchtower — Threat Intelligence Tools & Feeds (16)](#-the-watchtower--threat-intelligence-tools--feeds)
- [🗺️ The Cartographers — Recon, OSINT & Attack-Surface Mapping Tools (38)](#️-the-cartographers--recon-osint--attack-surface-mapping-tools)
- [🕵️ The Shadow Bureau — OSINT & Public-Intelligence Tools (29)](#️-the-shadow-bureau--osint--public-intelligence-tools)
- [🔑 The Vault — Secrets, Credentials & Password Security Tools (17)](#-the-vault--secrets-credentials--password-security-tools)
- [🐳 The Foundry — DevSecOps, Cloud & Container Security Tools (31)](#-the-foundry--devsecops-cloud--container-security-tools)
- [🔵 The Sentinel Ops — Blue Team, SOC & DFIR Tools (47)](#-the-sentinel-ops--blue-team-soc--dfir-tools)
- [🤖 The Oracle's Domain — AI Security & LLM Security Tools (9)](#-the-oracles-domain--ai-security--llm-security-tools)
- [🆓 The Free Bazaar — Free Cybersecurity APIs, Feeds & Data (30)](#-the-free-bazaar--free-cybersecurity-apis-feeds--data)
- [🎓 The Academy — Cybersecurity Learning Resources & Career Paths (24)](#-the-academy--cybersecurity-learning-resources--career-paths)
- [🎯 The Proving Grounds — CTF Practice, Labs & Hacking Training (74)](#-the-proving-grounds--ctf-practice-labs--hacking-training)
- [🧰 The Workshop — Utilities & Swiss-Army Tools (44)](#️-the-workshop--utilities--swiss-army-tools)

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
- [masscan](https://github.com/robertdavidgraham/masscan) — the fastest TCP port scanner on earth; scan the whole internet in minutes — on networks you're authorized to test. (AGPL-3.0)
- [RustScan](https://github.com/bee-san/RustScan) — modern Rust port scanner that finds open ports in seconds and pipes them straight into Nmap. (GPL-3.0)
- [Tsunami](https://github.com/google/tsunami-security-scanner) — Google's security scanner for large fleets, focused on reliably exploitable high-severity flaws with few false positives.
- [wafw00f](https://github.com/EnableSecurity/wafw00f) — fingerprints the web application firewall sitting in front of a site so you know exactly what you're testing against.
- [wapiti](https://github.com/wapiti-scanner/wapiti) — open-source black-box web vulnerability scanner that crawls and audits without needing a browser. (GPL-2.0)
- [WhatWeb](https://github.com/urbanadventurer/WhatWeb) — identifies what a website is built with — frameworks, CMSs, servers and versions — in one command. (GPL-2.0)
- [GitTools](https://github.com/internetwache/GitTools) — recovers an exposed `.git` directory into full source and commit history — audit your servers before attackers do.
- [tplmap](https://github.com/epinna/tplmap) — server-side template injection detection and exploitation across a dozen template engines; quiet upstream but still the SSTI reference. (GPL-3.0)
- [JoomScan](https://github.com/OWASP/joomscan) — OWASP's Joomla scanner: vulnerable components and misconfigurations on Joomla sites; quiet upstream, still OWASP's reference. (GPL-3.0)
- [ACSTIS](https://github.com/tijme/angularjs-csti-scanner) — the classic AngularJS client-side template injection scanner — legacy framework, still found everywhere. (unmaintained classic)
- [kiterunner](https://github.com/assetnote/kiterunner) — API route brute-forcer with method-aware wordlists derived from Swagger specs; dormant upstream, still the reference. (AGPL-3.0)
- [osmedeus](https://github.com/j3ssie/osmedeus) — workflow engine that chains recon and scanning into scheduled, repeatable attack-surface pipelines.
- [ettercap](https://github.com/Ettercap/ettercap) — the veteran MITM analysis suite for ARP poisoning, sniffing and protocol dissection — bettercap's classic sibling. (GPL-2.0)
- [OpenVAS Scanner](https://github.com/greenbone/openvas-scanner) — Greenbone's open-source vulnerability scanning engine for network and service flaws. (GPL-2.0)
- [aircrack-ng](https://github.com/aircrack-ng/aircrack-ng) — the complete WiFi security audit suite: capture, inject and audit — the wireless standard for two decades. (GPL-2.0)
- [THC-Hydra](https://github.com/vanhauser-thc/thc-hydra) — the classic parallelized login cracker for 50+ protocols; password audits only on systems you own or are paid to test. (AGPL-3.0)
- [objection](https://github.com/sensepost/objection) — Frida-powered runtime exploration toolkit for mobile apps — inspect and manipulate iOS/Android at runtime. (GPL-3.0)
- [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool) — RSA security-testing tool: attacks weak keys and unprotected disclosures purely offline, for auditors and CTF practice. (GPL-3.0)
- [Pywerview](https://github.com/the-useless-one/pywerview) — a Python port of PowerView's AD recon verbs; same questions, no Windows host required. (GPL-3.0)
- [Red-Teaming-Toolkit](https://github.com/infosecn1nja/Red-Teaming-Toolkit) — curated index of adversary-emulation and red-team tradecraft resources. (curated list)
- [jiraffe](https://github.com/0x48piraj/jiraffe) — Jira recon and security auditing: version fingerprinting, gadget/permission checks and CVE mapping for authorized instances. (MIT)
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
- [BunkerWeb](https://github.com/bunkerity/bunkerweb) — next-gen open WAF built on nginx: HTTPS, bot mitigation and network protections on by default. (AGPL-3.0)
- [open-appsec](https://github.com/openappsec/openappsec) — ML-driven prevention engine that stops OWASP Top 10 and zero-day web attacks without signatures.
- [OpenRASP](https://github.com/baidu/openrasp) — runtime application self-protection: instrument the app itself so attacks get blocked from the inside.
- [GoPhish](https://github.com/gophish/gophish) — open-source phishing-simulation platform: launch awareness campaigns and measure exactly who clicks (community edition).
- [OpenVPN](https://github.com/OpenVPN/openvpn) — the industry-standard open-source VPN daemon for site-to-site and remote-access tunnels. (GPL-2.0 core, component exceptions)
- [stunnel](https://github.com/mtrojnar/stunnel) — universal TLS wrapper that adds encryption to any TCP service in minutes. (GPL-2.0)
- [OpenSSH](https://github.com/openssh/openssh-portable) — the world's default secure remote-access suite: encrypted shells, tunnels and key management. (BSD-style)
- [ClamAV](https://github.com/Cisco-Talos/clamav) — the open-source antivirus engine that powers mail gateways and file-screening pipelines everywhere. (GPL-2.0)
- [AIDE](https://github.com/aide/aide) — Advanced Intrusion Detection Environment: file-integrity monitoring that alerts the moment system files change. (GPL-2.0)
- [Tor](https://www.torproject.org/) — the anonymity network: routed egress through thousands of volunteer relays; the standard for privacy-preserving research access. (BSD-3-Clause)
- [Netfilter/iptables](https://netfilter.org/) — the Linux kernel's native packet-filtering framework; the foundation every host firewall build starts from. (GPL-2.0)
- [SELinux](https://github.com/SELinuxProject/selinux) — mandatory access control for Linux: policy-based confinement that survives a compromised application. (GPL-2.0)
- [OpenBSD PF](https://www.openbsd.org/faq/pf/) — the packet filter famous for correctness and readable rules; the syntax OpenBSD, pfSense and OPNsense share. (ISC)
- [checksec.sh](https://github.com/slimm609/checksec.sh) — one-shot binary hardening audit: NX, canaries, PIE, RELRO and fortify flags in a single run. (BSD-3-Clause)
- [Vuls](https://github.com/future-architect/vuls) — agentless vulnerability scanner for servers and containers, with CVE reporting across Linux and FreeBSD fleets. (GPL-3.0)
- [SpamAssassin](https://spamassassin.apache.org/) — the veteran open-source spam filter; bayesian scoring and rule engine at the mail gateway. (Apache-2.0)
- [Fleet](https://github.com/fleetdm/fleet) — osquery fleet management: device visibility and policy enforcement at scale, open core with a free tier. (MIT, open core)
- [shellfirm](https://github.com/kaplanelad/shellfirm) — a pre-execution guard for your shell: challenges dangerous commands (rm -rf, kubectl delete) before they run. (Apache-2.0)
- [Qubes OS](https://www.qubes-os.org/) — the security-by-compartmentalization desktop OS; " reasonably secure" by architecture, not by antivirus. (GPL-2.0)
- [Awesome WebSocket Security](https://github.com/PalindromeLabs/awesome-websocket-security) — curated research, tools and CVEs for WebSocket protocol security. (Apache-2.0, curated list)
- [Neo23x0 auditd config](https://github.com/Neo23x0/auditd) — Florian Roth's hardened auditd rule set: the Linux logging baseline used across incident-response teams. (Apache-2.0)
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
- [IntelMQ](https://github.com/certtools/intelmq) — the feed plumber's dream: collect, normalize and route threat-intel feeds from hundreds of sources into your stack. (AGPL-3.0)
- [NetworkMiner](https://www.netresec.com/?page=NetworkMiner) — passive network-forensics analyzer: extracts files, credentials and sessions from recorded traffic without touching the live network. (free, proprietary)
- [ZDI advisories](https://www.zerodayinitiative.com/advisories/published/) — published zero-day advisories from the Zero Day Initiative; the disclosure record for enterprise-software flaws. (free service)
- [Emerging Threats Open](http://doc.emergingthreats.net/bin/view/Main/EmergingFAQ) — the open Suricata/Snort rule feed from Proofpoint; thousands of community-maintained detection rules. (free feed)
- [http-detection-agent](https://github.com/ai-blueteam/http-detection-agent) — traffic anomaly detection for the blue team: labels HTTP datasets without shipping them off-box. (MIT)
- [vx-underground](https://vx-underground.org) — the malware corpus and INT report archive; free, massive and respected across the research community. (free service)
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
- [assetfinder](https://github.com/tomnomnom/assetfinder) — passive subdomain discovery that polls a dozen public sources and prints a clean list — no keys needed; quiet upstream, still the classic.
- [ParamSpider](https://github.com/devanshbatham/ParamSpider) — mines archived URLs and parameters from the Wayback Machine to seed injection testing.
- [recon-ng](https://github.com/lanmaster53/recon-ng) — the other recon framework: fully modular, database-backed web recon with a Metasploit-style console. (GPL-3.0)
- [dnsrecon](https://github.com/darkoperator/dnsrecon) — DNS enumeration workhorse: records, zone transfers, reverse lookups and subdomain brute-forcing. (GPL-2.0)
- [VHostScan](https://github.com/codingo/VHostScan) — enumerates virtual hosts on a shared IP — discover the neighbors your target lives with. (GPL-3.0)
- [wfuzz](https://github.com/xmendez/wfuzz) — the web fuzzer that replaces any part of a request with a payload — parameters, headers, paths, verbs. (GPL-2.0)
- [AtDork](https://github.com/amnottdevv/atdork) — multi-engine Google-dork scraper with categorized GHDB output for authorized reconnaissance. (MIT)
- [DorkCraft](https://github.com/juandresrodca/DorkCraft) — rule-based dork generator: translates intent into search queries deterministically, zero AI, zero outbound calls. (MIT)
- [DorkEye](https://github.com/xPloits3c/DorkEye) — OSINT dork pipeline: email, subdomain and people discovery through structured query automation. (MIT)
- [ike-scan](https://github.com/royhills/ike-scan) — IKE/IPsec security auditing: fingerprint VPN gateways and enumerate transform proposals. (GPL-2.0)
- [EyeWitness](https://github.com/RedSiege/EyeWitness) — screenshots, headers and key info from web servers during authorized recon passes. (GPL-3.0)
- [WiGLE](https://wigle.net) — the wireless network mapping archive; queries by BSSID/SSID across millions of observed networks. (free service)
- [DNSdumpster](https://dnsdumpster.com) — visual DNS reconnaissance: subdomains, MX, and infrastructure maps from public records. (free service)
- [CeWL](https://digi.ninja/projects/cewl.php) — custom wordlist generation by spidering target sites — the content-aware dictionary for authorized assessments. (GPL-3.0)
- [Awesome Censys Queries](https://github.com/thehappydinoa/awesome-censys-queries) — a curated corpus of Censys search queries for internet-wide recon. (CC-BY-4.0, curated list)
- [JA3](https://github.com/salesforce/ja3) — the TLS client fingerprint standard: a 12-byte hash that identifies client software across the wire. (BSD-3-Clause)
- [HASSH](https://github.com/salesforce/hassh) — SSH key-exchange fingerprinting: identify client/server software from the KEX packet alone. (BSD-3-Clause)
- [Recog](https://github.com/rapid7/recog) — the fingerprint database behind Metasploit and Nexpose: service banners mapped to OS and product families. (BSD-3-Clause)
- [JARM](https://github.com/salesforce/jarm) — active TLS server fingerprint: identifies servers behind CDNs from their handshake behavior. (BSD-3-Clause)
- [Merklemap](https://merklemap.com) — subdomain discovery through certificate-transparency logs; billions of entries, searchable. (free service)
## 🕵️ The Shadow Bureau — OSINT & Public-Intelligence Tools
Intro: Public data, lawful purpose — OSINT frameworks, people-search, breach lookups, site monitoring and archive history for investigators, defenders and researchers. These tools only surface what is already public; use them for authorized investigations, defense and education only — never to stalk, harass or dox anyone.

### 🧭 Frameworks & Crawlers

- [sn0int](https://github.com/kpcyrd/sn0int) — semi-automatic OSINT framework with scriptable modules, its own package ecosystem and a database that remembers everything you've collected. (GPL-3.0)
- [Photon](https://github.com/s0md3v/Photon) — fast OSINT crawler that rips a target apart for emails, social profiles, intel files and metadata, with exportable reports. (GPL-3.0)
- [chiasmodon](https://github.com/chiasmod0n/chiasmodon) — domain-centric OSINT: pivot from one domain to emails, subdomains, ASN and related-asset intelligence across multiple sources.

### 👤 People & Account Discovery

- [maigret](https://github.com/soxoj/maigret) — builds a full dossier from a single username across thousands of sites; powerful people-OSINT — authorized investigations only.
- [WhatsMyName](https://whatsmyname.app) — web app plus open database for checking one username across hundreds of platforms at once; keep lookups lawful and authorized.
- [Osintgram](https://github.com/Datalux/Osintgram) — interactive Instagram OSINT (followers, public emails/phones, geotags, posting patterns); requires an Instagram account — authorized research only. (GPL-3.0)

### 📧 Email & Phone Intel

- [holehe](https://github.com/megadose/holehe) — checks which sites an email is registered on via password-reset and account-exist flows; quiet upstream but still the standard. (GPL-3.0)
- [MailAccess](https://github.com/KatrielMoses/MailAccess) — email-exposure toolkit that flags breach appearances and stealer-log presence for an address — authorized investigations only.

### 🩸 Breach & Leak Lookup

- [leaker](https://github.com/vflame6/leaker) — one terminal command, ten public breach databases — passive checks for whether an email or domain appears in known leaks.

### 🌐 Website Monitoring & Analysis

- [web-check](https://github.com/lissy93/web-check) — all-in-one website OSINT dashboard — DNS, headers, tech, ports, TLS, whois and more — self-hostable in one Docker pull.
- [changedetection.io](https://github.com/dgtlmoon/changedetection.io) — self-hosted website change monitoring with selectors, visual diffs and dozens of notification targets.

### 🕰️ Archive & History

- [waybackpy](https://github.com/akamhy/waybackpy) — Python client and CLI for the Wayback Machine: search, save and diff archived snapshots from your own scripts; quiet upstream, works fine.

### 🎯 Threat & Attack-Surface Intel

- [opensquat](https://github.com/atenreiro/opensquat) — watches newly-registered domains for typosquats and brand lookalikes, with free daily feeds. (GPL-3.0)
- [cyberbro](https://github.com/stanfrbd/cyberbro) — self-hosted IOC reputation station: paste URLs, IPs or hashes and get verdicts from dozens of engines on one page.
- [HoneyLabs](https://honeylabs.net) — free per-IP honeypot-telemetry reports: see whether an address has been tripping sensors worldwide.
- [ip.thc.org](https://ip.thc.org) — free, keyless JSON API for reverse DNS, subdomain and CNAME lookups on any IP — the quick IP pivot.
- [OSINT-Framework](https://osintframework.com/) — the classic OSINT tool index: categorized sources from public records to social analysis. (free service)
- [aware-online](https://www.aware-online.com/en/) — OSINT training and tooling from the Dutch awareness school; free investigative resources. (free service)
- [Nipe](https://github.com/GouveaHeitor/nipe) — a tool to make your traffic pass through the Tor network; redirect the machine's egress for privacy. (MIT)
- [Whonix](https://www.whonix.org) — the anonymity-focused OS: a Workstation VM routed entirely through a Tor Gateway VM. (GPL-3.0)
- [PhoneInfoga](https://github.com/sundowndev/PhoneInfoga) — phone-number OSINT: carriers, reputation and footprint from public sources, no scraping of private data. (GPL-3.0)
- [waybackpack](https://github.com/jsvine/waybackpack) — bulk-download a site's history from the Wayback Machine; the archivist's archive. (MIT)
- [TOsint](https://github.com/drego85/tosint) — Telegram OSINT: user, channel and bot intelligence from public messaging data. (GPL-3.0)
- [tg-chat-dump](https://github.com/renkagod/tg-chat-dump) — archive public Telegram chats to SQLite for structured analysis. (MIT)
- [VoidAccess](https://github.com/KatrielMoses/voidaccess) — self-hosted dark-web monitoring platform for threat-intelligence teams. (MIT)
- [IntelHub](https://github.com/tomsec8/IntelHub) — browser extension that runs OSINT analysis locally; no data leaves the analyst's machine. (MIT)
- [Taranis AI](https://github.com/taranis-ai/taranis-ai) — OSINT gathering and enrichment platform for analysts; self-hostable with an AI-assist layer. (EUPL-1.2)
- [Mitaka](https://github.com/ninoseki/mitaka) — IOC-pivot browser extension: search an IP/domain/hash across 30+ engines from the context menu. (MIT)
- [ScamSearch](https://scamsearch.io) — scammer profile lookup by phone, email or username; crowdsourced anti-fraud intel. (free service)
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
- [LaZagne](https://github.com/AlessandroZ/LaZagne) — audits which passwords your workstations remember — browsers, mail clients, OS stores — for authorized inventory and exposure checks only. (LGPL-3.0)
- [MAT2](https://0xacab.org/jvoisin/mat2) — Metadata Anonymisation Toolkit v2: strips hidden metadata from documents, images and more. (GPL-3.0)
- [Retraced (BoxyHQ)](https://github.com/retracedhq/retraced) — open-source audit-log API: compliant, tamper-evident activity records for your SaaS. (Apache-2.0)
- [hardened_malloc](https://github.com/GrapheneOS/hardened_malloc) — the allocator that makes exploitation harder by design; from the GrapheneOS project. (MIT)
- [Databunker](https://databunker.org/) — encrypted personal-data vault: API-first storage for PII with built-in privacy compliance. (GPL-3.0)
- [keyFinder](https://github.com/momenbasel/keyFinder) — passively discovers leaked API keys and secrets in web pages during browsing. (MIT)
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
- [kube-hunter](https://github.com/aquasecurity/kube-hunter) — active Kubernetes security testing: probe clusters for exposed dashboards, weak RBAC and known exploits; quiet upstream.
- [cloudsplaining](https://github.com/salesforce/cloudsplaining) — maps AWS IAM policies and flags the privilege-escalation paths you never meant to grant.
- [Docker Bench for Security](https://github.com/docker/docker-bench-security) — audits your Docker host and daemon configuration against the CIS Benchmark in a single script run.
- [GDB](https://www.sourceware.org/gdb/) — the GNU debugger: breakpoints, watchpoints and reverse debugging across dozens of architectures. (GPL-3.0)
- [WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) — the Windows debugger for user, kernel and crash-dump analysis; now with a modern UI. (free, proprietary)
- [ChipWhisperer](https://github.com/newaetech/chipwhisperer) — side-channel analysis and glitching for hardware security research. (GPL-3.0)
- [ProgPilot](https://github.com/designsecurity/progpilot) — static taint analysis for PHP sources: finds input-to-sink flows at build time. (GPL-3.0)
- [sobelow](https://github.com/nccgroup/sobelow) — security testing for Elixir/Phoenix applications; the Sobelow family's namesake. (MPL-2.0)
- [cppcheck](https://github.com/danmar/cppcheck) — static analysis for C/C++: detects bugs and undefined behavior, not just style. (GPL-3.0)
- [cwe_checker](https://github.com/fkie-cad/cwe_checker) — finds common CWE patterns in binaries, direct from firmware images. (LGPL-2.1+)
- [Substation](https://github.com/brexhq/substation) — an event and data pipeline toolkit for detection engineering at scale. (MIT)
- [logdissect](https://github.com/dogoncouch/logdissect) — parse, merge and analyze logs from many formats into one timeline. (MIT)
- [Awesome ICS Security](https://github.com/mpesen/awesome-industrial-control-system-security) — curated industrial-control-system security tools and research. (Apache-2.0, curated list)
- [Awesome Container Security](https://github.com/kai5263499/container-security-awesome) — curated container and cloud-native security resources. (MIT, curated list)
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
- [capa](https://github.com/mandiant/capa) — identifies what malware actually does: maps capabilities and ATT&CK techniques straight from binaries.
- [Revoke-Obfuscation](https://github.com/danielbohannon/Revoke-Obfuscation) — Daniel Bohannon's framework for detecting obfuscated PowerShell at scale; quiet upstream, still the reference.
- [DeepBlueCLI](https://github.com/sans-blue-team/DeepBlueCLI) — SANS blue-team PowerShell for fast Windows event-log hunting: logons, mutants, suspicious service installs — quiet upstream but still a blue-team staple. (GPL-3.0)
- [HELK](https://github.com/Cyb3rWard0g/HELK) — the Hunting ELK: a pre-built Elasticsearch/Kafka/Spark lab for threat-hunting research — a research project with low churn. (GPL-3.0)
- [sysmon-modular](https://github.com/olafhartong/sysmon-modular) — Swiss-army Sysmon configuration: per-ATT&CK-technique logging modules you compose yourself.
- [ElastAlert2](https://github.com/jertel/elastalert2) — the maintained successor to ElastAlert: flexible alerting on Elasticsearch data with dozens of rule types.
- [pspy](https://github.com/DominicBreuker/pspy) — watch process and file events on any Linux box without root — catch cron-based persistence in the act. (GPL-3.0)
- [ThreatMapper](https://github.com/deepfence/ThreatMapper) — Deepfence's open runtime threat scanner: finds and ranks exploitable vulnerabilities in cloud and container workloads.
- [Snort 3](https://github.com/snort3/snort3) — the next generation of the classic open-source IDS/IPS, rewritten in C++ with multi-threading. (GPL-2.0)
- [Kismet](https://github.com/kismetwireless/kismet) — passive wireless detection layer: discovers Wi-Fi and BLE devices, rogue access points and wardrives. (GPL-2.0)
- [ntopng](https://github.com/ntop/ntopng) — high-speed web-based traffic monitoring: flows, top talkers and protocols with long historical views. (GPL-3.0)
- [Nagios Core](https://github.com/NagiosEnterprises/nagioscore) — the classic infrastructure monitor: availability checks that surface outages and anomalies early. (GPL-2.0)
- [The Sleuth Kit](https://github.com/sleuthkit/sleuthkit) — the forensic library behind half the DFIR tools you know: disks, filesystems and timelines. (CPL-1.0)
- [HijackThis](https://github.com/dragokas/hijackthis) — the veteran Windows hijack analyzer: scans browser and OS settings for malicious tampering. (GPL-2.0)
- [NoScript](https://github.com/hackademix/noscript) — the browser extension that blocks JavaScript and plugin content by default — client-side hardening's origin story. (GPL-3.0)
- [Sysinternals Suite](https://learn.microsoft.com/en-us/sysinternals/) — Microsoft's free Windows admin and DFIR toolkit: Process Explorer, Autoruns, Procmon and dozens more. (free, proprietary)
- [Fibratus](https://github.com/rabbitstack/fibratus) — Windows kernel-event tracing with YARA filtering; a Swiss army knife for endpoint visibility. (Apache-2.0)
- [Threat Hunter Playbook](https://github.com/OTRF/ThreatHunter-Playbook) — open hunting playbooks as code: hypotheses mapped to data sources and detections. (MIT)
- [awesome-honeypots](https://github.com/paralax/awesome-honeypots) — the curated honeypot directory: deception tech from low to high interaction. (curated list)
- [Conpot](https://github.com/mushorg/conpot) — ICS/SCADA honeypot: emulates the protocols that run factories, safely. (GPL-2.0)
- [FIR](https://github.com/certsocietegenerale/FIR) — Fast Incident Response from Société Générale: ticketing built for IR workflows. (GPL-3.0)
- [Awesome Incident Response](https://github.com/meirwah/awesome-incident-response) — the curated IR toolkit index used across the industry. (Apache-2.0, curated list)
- [Awesome YARA](https://github.com/InQuest/awesome-yara) — curated YARA rules, tooling and research for malware hunting. (CC-BY-4.0, curated list)
- [Krawl](https://github.com/BlessedRebuS/Krawl) — deception-driven defense: a honeypot server framework for research. (MIT)
- [Shuffle](https://github.com/Shuffle/Shuffle) — self-hosted SOAR automation: connect your TIP, SIEM and responders in drag-and-drop workflows. (AGPL-3.0)
- [Sublime Platform](https://github.com/sublime-security/sublime-platform) — open email threat detection: rules-as-code against phishing and BEC. (MIT)
- [Sublime Rules](https://github.com/sublime-security/sublime-rules) — the community rule corpus for the Sublime platform. (MIT)
- [go-audit](https://github.com/slackhq/go-audit) — auditd in JSON for Linux: structured events that pipelines can actually parse. (MIT)
- [Netcap](https://github.com/dreadl0ck/netcap) — security audit framework over network traffic: sensors, audit and collection from live or captured streams. (GPL-3.0)
- [Sysmon for Linux](https://github.com/Sysinternals/SysmonForLinux) — the Windows-trusted system monitor ported to Linux. (MIT)
- [msticpy](https://github.com/microsoft/msticpy) — SecOps analysis library from Microsoft: pivots, timelines and hunting helpers for Jupyter. (MIT)
- [Elastic detection-rules](https://github.com/elastic/detection-rules) — the detection corpus for Elastic Security: hundreds of maintained rules mapped to MITRE. (Elastic-2.0)
## 🤖 The Oracle's Domain — AI Security & LLM Security Tools
Intro: Secure the new surface — LLM red teaming, guardrails and model-file safety for AI-powered applications.

- [promptfoo](https://github.com/promptfoo/promptfoo) — LLM evaluation and red-teaming framework: prompt-injection and jailbreak test suites that run in CI.
- [garak](https://github.com/NVIDIA/garak) — NVIDIA's LLM vulnerability scanner: hundreds of probes for injection, data leakage, hallucination and misuse.
- [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) — programmable guardrail layer for LLM apps: input/output rails, dialog safety, topic control.
- [deepteam](https://github.com/confident-ai/deepteam) — red-teaming library for LLMs: simulated attacks with vulnerability scoring and reporting.
- [modelscan](https://github.com/protectai/modelscan) — scan model files (pickle, safetensors) for malicious code before you load them — supply-chain defense for ML.
- [OWASP Top 10 for LLM Applications](https://genai.owasp.org) — the standard risk taxonomy for LLM apps; the shared language for AI threat modeling.
- [Awesome Threat Intelligence](https://github.com/hslatman/awesome-threat-intelligence) — the curated threat-intelligence tools and platform index. (Apache-2.0, curated list)
- [llm-guard](https://github.com/protectai/llm-guard) — input/output security filtering for LLMs: prompt-injection defense as a pipeline stage. (MIT)
- [model-transparency](https://github.com/sigstore/model-transparency) — signing for ML models: verify exactly which model you are deploying. (Apache-2.0)
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
- [Splunk security_content](https://github.com/splunk/security_content) — the maintained detection-content corpus: thousands of searches and analytic stories mapped to ATT&CK.
- [MDN HTTP Observatory](https://developer.mozilla.org/en-US/observatory/) — Mozilla's free no-key scanner that grades your site's security headers and best practices.
- [Security Datasets](https://github.com/OTRF/Security-Datasets) — OTRF's library of pre-recorded adversary-emulation event logs (Mordor's successor home) for detection testing; frozen library by design.
- [EVTX-ATTACK-SAMPLES](https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES) — a large collection of real Windows event logs capturing ATT&CK techniques — test detections without a lab; frozen dataset by design. (GPL-3.0)
- [MITRE Cyber Analytics Repository](https://github.com/mitre-attack/car) — CAR: curated, versioned detection analytics with full logic and ATT&CK mappings.
- [Boss of the SOC (BOTS)](https://github.com/splunk/botsv3) — Splunk's public blue-team CTF dataset: full realistic telemetry for investigations, CC0 data; frozen CTF dataset by design.
- [Packet Storm](https://packetstormsecurity.com/) — the advisory and exploit-db archive; a quarter-century of security disclosures. (free service)
- [Awesome Pentest](https://github.com/enaqx/awesome-pentest) — the most-starred pentest resource collection; the community canon. (CC-BY-4.0, curated list)
- [Awesome Web Hacking](https://github.com/infoslack/awesome-web-hacking) — curated web-security research: talks, papers and tooling. (MIT, curated list)
- [Splunk attack_data](https://github.com/splunk/attack_data) — curated attack datasets for detection validation, mapped to MITRE techniques. (Apache-2.0)
- [onion-lookup](https://github.com/ail-project/onion-lookup) — a free API for .onion existence checks; part of the AIL stack. (AGPL-3.0)
- [Chaos](https://chaos.projectdiscovery.io) — the internet-wide subdomain dataset from ProjectDiscovery; free for community use. (free API)
- [SearchWebCode](https://searchwebcode.com) — search engine over the HTML/JS/CSS of 127M websites; source-level search without crawling. (free service)
- [OpenSanctions](https://opensanctions.org) — open data on sanctioned entities and PEPs; the compliance watchlist as a dataset. (open data)
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
- [Hacker101](https://www.hacker101.com/) — HackerOne's free web-security course: video lessons plus an always-on CTF for bug-bounty practice.
- [Hacksplaining](https://www.hacksplaining.com/) — interactive security lessons for developers: exploit each vulnerability class, then patch it yourself.
- [Roppers Academy](https://www.hoppersroppers.org/) — free structured courses from computing fundamentals to security — the patient beginner's path.
- [SEED Labs](https://seedsecuritylabs.org/) — the university-grade lab curriculum: hundreds of hands-on exercises for every security course topic.
- [Infosec Reference](https://github.com/rmusser01/Infosec_Reference) — the giant information-security reference: tools, papers and guides in one place. (curated list)
- [CTF Field Guide](https://trailofbits.github.io/ctf/) — Trail of Bits' field guide to capture-the-flag: from fundamentals to finals. (CC-BY-4.0)
- [Network Segmentation Cheat Sheet](https://github.com/sergiomarotco/Network-segmentation-cheat-sheet) — practical segmentation architecture: VLANs, zones and rules that survive audits. (Apache-2.0)
- [OWASP MSTG](https://github.com/OWASP/owasp-mstg) — the Mobile Security Testing Guide: the canonical methodology for mobile app assessments. (CC-BY-SA-4.0)
- [Android Security Awesome](https://github.com/ashishb/android-security-awesome) — curated Android security research: tools, papers and training. (Apache-2.0, curated list)
- [Bug Bounty Hunter](https://www.bugbountyhunter.com/) — free bug-bounty training platform: real methodology and lab targets. (free service)
- [SecuriBench Micro](https://github.com/too4words/securibench-micro/) — the Stanford benchmark suite for security-analysis tools. (Apache-2.0)
- [Cyber Security Base](https://cybersecuritybase.github.io/) — free course series by Aalto University and F-Secure; from beginner to blue team. (free course)
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
- [bWAPP](http://www.itsecgames.com/) — the "buggy web application" with 100+ vulnerability flavors — an old-school playground that still teaches.
- [OWASP Mutillidae II](https://github.com/webpwnized/mutillidae) — deliberately vulnerable app that re-creates every OWASP Top 10 issue, resettable per install. (GPL-3.0)
- [Root Me](https://www.root-me.org/) — hundreds of real-world hacking challenges across dozens of categories, from web to stego. (free tier)
- [Google Gruyere](http://google-gruyere.appspot.com/) — Google's cheese-themed vulnerable web app: exploit XSS, XSRF and information disclosure in the cloud.
- [GOAD](https://github.com/Orange-Cyberdefense/GOAD) — Game of Active Directory: a three-forest lab purpose-built for safely practicing AD attack techniques. (GPL-3.0)
- [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat) — Rhino Security's "vulnerable by design" AWS scenarios — deploy, attack, tear down.
- [CryptoHack](https://cryptohack.org/) — learn modern cryptography by breaking it: challenges from classical ciphers to ECC.
- [Hackxor](https://hackxor.net/) — a realistic web-app hacking game with a story arc — WebGoat with sharper teeth.
- [WackoPicko](https://github.com/adamdoupe/WackoPicko) — the vulnerable app built for testing vulnerability scanners — a frozen-by-design calibration target for your tooling.
- [CyberDefenders](https://cyberdefenders.org/) — blue-team CTF platform: investigate realistic incidents with the tools a SOC actually uses. (free tier)
- [LetsDefend](https://letsdefend.io/) — browser-based SOC simulator: alert queues, playbooks and IR challenges mapped to MITRE ATT&CK. (free tier)
- [pwnable.kr](https://pwnable.kr/) — the classic system-hacking wargame: exploit your way from userland to kernel.
- [Hack This Site](https://www.hackthissite.org/) — the community wargames veteran: missions, articles and forums since the early 2000s.
- [OWASP NodeGoat](https://github.com/OWASP/NodeGoat) — the Node.js vulnerable-by-design app: the Top 10 in a controllable lab. (Apache-2.0)
- [Vulhub](https://github.com/vulhub/vulhub) — dockerized vulnerable environments: spin up a CVE, test, tear down. (MIT)
- [Pentest-Ground](https://pentest-ground.com/) — hosted practice playground of intentionally vulnerable apps for security testing. (free service)
- [testasp.vulnweb.com](http://testasp.vulnweb.com/) — the ASP demo target for scanner testing. (free service)
- [testaspnet.vulnweb.com](http://testaspnet.vulnweb.com/) — the ASP.NET demo target for scanner testing. (free service)
- [Zero Bank](http://zero.webappsecurity.com/) — demo banking site for web security exercises. (free service)
- [Altoro Mutual](http://demo.testfire.net/) — the classic demo bank: legal target for appsec training and tool demos. (free service)
- [Firing Range](https://public-firing-range.appspot.com/) — Google's XSS testbed: the original scanner benchmarking target. (Apache-2.0)
- [XSS Game](https://xss-game.appspot.com/) — Google's XSS tutorial game: six levels from context basics to DOM tricks. (free service)
- [lfi-labs](https://github.com/paralax/lfi-labs) — LFI/RFI/commix practice pages: one flaw family, many variants. (MIT)
- [Arizona Cyber Warfare Range](http://azcwr.org/az-cyber-warfare-ranges) — free live-fire ranges for defenders and researchers. (free service)
- [0l4bs](https://github.com/tegal1337/0l4bs) — XSS practice labs with progressive difficulty. (GPL-3.0)
- [DSVW](https://github.com/stamparm/DSVW) — Damn Small Vulnerable Web: the Top 10 in ~100 lines of Python. (public domain)
- [DVHMA](https://github.com/logicalhacking/DVHMA) — the Damn Vulnerable Hybrid Mobile App: Android+iOS appsec in one codebase. (Apache-2.0)
- [DVIA-v2](https://github.com/prateek147/DVIA-v2) — Damn Vulnerable iOS App v2: the mobile testing curriculum as an app. (MIT)
- [DVWS (Web Services)](https://github.com/snoopysecurity/dvws) — vulnerable web services for SOA/API security practice. (Apache-2.0)
- [DVWS (Web Sockets)](https://github.com/interference-security/DVWS) — the vulnerable WebSocket app from Interference Security. (MIT)
- [damnvulnerable.me](https://github.com/skepticfx/damnvulnerable.me) — a modern vulnerable webapp for the OWASP Top 10 era. (MIT)
- [Hackademic](https://github.com/Hackademic/hackademic) — WordPress-based vulnerable lab scenarios for classroom use. (GPL-3.0)
- [Java Vulnerable Lab](https://github.com/CSPF-Founder/JavaVulnerableLab) — the Java vulnerable web application from the CSPF crew. (GPL-2.0)
- [SentinelTestbed](https://github.com/dobin/SentinelTestbed) — a testbed app for evaluating security instrumentation. (GPL-3.0)
- [SocketToMe](https://digi.ninja/projects/sockettome.php) — Robin Wood's WebSocket testing challenge app. (free service)
- [techlogia Lab](https://techlogia.de/en/lab) — free browser-based hacking lab for security training. (CC-BY-4.0)
- [Vulnerable Node](https://github.com/cr0hn/vulnerable-node) — the Node.js vulnerable application for testing analysis tools. (MIT-style)
- [XVWA](https://github.com/s4n7h0/xvwa) — Xtreme Vulnerable Web Application: dozens of flaws across one PHP app. (GPL-3.0)
- [CryptOMG](https://github.com/SpiderLabs/CryptOMG) — cryptographic flaw testbed from SpiderLabs. (GPL-3.0)
- [AzureGoat](https://github.com/ine-labs/AzureGoat) — the vulnerable-by-design Azure cloud lab. (MIT)
- [Crackmes.one](https://crackmes.one/) — the reverse-engineering challenge community: thousands of crackmes, all legal. (free service)
- [HEVD](https://github.com/hacksysteam/HackSysExtremeVulnerableDriver) — the Windows kernel-driver training target for exploit development. (GPL-3.0)
- [Microcorruption](https://microcorruption.com/) — embedded-security CTF: reverse the lock firmware, level by level. (free service)
- [MASTG Crackmes](https://github.com/OWASP/mastg/tree/master/Crackmes) — the mobile RE challenges companion to the OWASP MASTG. (CC-BY-SA-4.0)
- [Reversing.kr](http://reversing.kr) — the classic Korean reverse-engineering challenge site. (free service)
- [Vulnserver](http://www.thegreycorner.com/2010/12/introducing-vulnserver.html) — the TCP vulnerable server for exploit-dev practice. (free service)
- [CTFlearn](https://ctflearn.com/) — the beginner-friendly CTF platform with a permanent challenge set. (free service)
- [Hackertest.net](http://www.hackertest.net/) — the 20-level hacking simulation for web basics. (free service)
- [HackThis!!](https://www.hackthis.co.uk/) — 50+ levels of web security challenges, from basics to advanced. (free service)
- [MysteryTwister C3](https://www.mysterytwisterc3.org/en/) — the international cryptography challenge: from Caesar to quantum. (free service)
- [RingZer0 CTF](https://ringzer0ctf.com/) — hundreds of challenges across web, crypto, forensics and reversing. (free service)
- [SmashTheStack](http://smashthestack.org/) — the wargames network: shellcoding, exploitation and logic puzzles. (free service)
- [W3Challs](https://w3challs.com) — pentest training challenges with a ranking system. (free service)
- [WeChall](http://www.wechall.net/) — the challenge-site aggregator: one profile across all major wargames. (free service)
- [DIVA Android](https://github.com/payatu/diva-android) — Damn Insecure and Vulnerable App: the Android training classic. (GPL-3.0)
- [ExploitMe Mobile](http://securitycompass.github.io/AndroidLabs/index.html) — the SecurityCompass mobile labs. (free service)
- [OWASP iGoat](https://wiki.owasp.org/index.php/OWASP_iGoat_Tool_Project) — the iOS learning app from the OWASP mobile family. (wiki project)
- [APTSimulator](https://github.com/NextronSystems/APTSimulator) — makes a Windows host look compromised so you can test detections safely. (MIT)
- [flightsim](https://github.com/alphasoc/flightsim) — generates malicious network traffic for IDS/NDR validation; defender-side only. (CC-BY-4.0)
- [Splunk Attack Range](https://github.com/splunk/attack_range) — builds instrumented detection labs: attack, collect and test in one workflow. (Apache-2.0)
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
- [Scapy](https://github.com/secdev/scapy) — packet crafting without limits: forge, sniff, dissect and send anything — the Python network Swiss-army knife. (GPL-2.0)
- [boofuzz](https://github.com/jtpereyda/boofuzz) — network protocol fuzzing framework descended from Sulley — script your protocol and hardware bug hunts. (GPL-2.0)
- [Dangerzone](https://github.com/freedomofpress/dangerzone) — takes hostile documents and re-renders them as safe PDFs inside an isolated sandbox. (AGPL-3.0)
- [Faraday](https://github.com/infobyte/faraday) — the pentest collaboration platform: import tool output, deduplicate findings and manage the whole engagement. (GPL-3.0)
- [Dradis CE](https://github.com/dradis/dradis-ce) — collaborative pentest reporting: team notes, evidence and findings assembled into one professional report. (GPL-2.0)
- [ATT&CK Navigator](https://github.com/mitre-attack/attack-navigator) — MITRE's matrix explorer: layer, annotate and score ATT&CK techniques for detection-coverage planning.
- [GnuPG](https://github.com/gpg/gnupg) — the free implementation of OpenPGP: encrypt, sign and verify files and mail, everywhere. (GPL-3.0)
- [OpenSSL](https://github.com/openssl/openssl) — the TLS library the internet runs on — and the CLI for keys, certs, CSRs and everything crypto.

---
- [socat](http://www.dest-unreach.org/socat/) — the relay for bidirectional data transfer between addresses: TCP, UDP, sockets, pipes. (GPL-2.0)
- [radare2](https://github.com/radareorg/radare2) — the scriptable reverse-engineering framework: disassemble, debug, patch, anywhere. (LGPL-3.0)
- [x64dbg](https://github.com/x64dbg/x64dbg) — the open Windows debugger for x32/x64, with a plugin ecosystem built for RE. (GPL-3.0)
- [netcat](http://nc110.sourceforge.io/) — the original TCP/IP Swiss army knife: reads and writes across networks with one command. (freeware)
- [Kaitai Struct](https://github.com/kaitai-io/kaitai_struct) — declare a binary format once, generate parsers for nine languages. (MIT)
- [Hachoir](https://github.com/vstinner/hachoir) — binary field inspection: split any file into its fields, even damaged ones. (GPL-2.0)
- [binwalk](https://github.com/ReFirmLabs/binwalk) — firmware analysis: scan, extract and identify embedded files and filesystems. (MIT)
- [Capstone](https://github.com/capstone-engine/capstone) — the disassembly framework behind countless security tools. (BSD-3-Clause)
- [dnSpyEx](https://github.com/dnSpyEx/dnSpy) — the .NET debugger and decompiler, continued; edit assemblies live. (GPL-3.0)
- [UEFITool](https://github.com/LongSoft/UEFITool) — parse, extract and replace UEFI firmware images. (BSD-2-Clause)
- [tcpreplay](https://github.com/appneta/tcpreplay) — replay captured traffic at arbitrary speed for testing and validation. (GPL-3.0)
- [I2P](https://geti2p.net/) — the Invisible Internet Project: anonymous, self-organizing overlay network. (multiple open licenses)
- [Tails](https://tails.boum.org/) — the amnesic incognito live system: no trace left on the machine. (GPL-3.0)
- [Hex Fiend](http://ridiculousfish.com/hexfiend/) — the fast, open-source hex editor for macOS. (BSD-2-Clause)
- [friTap](https://github.com/fkie-cad/friTap) — intercept TLS keys in real time for analysis; a Frida script for the lab. (GPL-3.0)
- [angr](https://angr.io/) — the binary-analysis platform from UCSB's Shellphish: symbolic execution at scale. (BSD-2-Clause)
- [Detect It Easy](https://github.com/horsicq/Detect-It-Easy) — packer/compiler/protection detection with a rule engine. (MIT)
- [Evan's Debugger](http://www.codef00.com/projects#debugger) — the C/C++ debugger with a RE focus: memory views built for analysis. (GPL-2.0+)
- [Voltron](https://github.com/snare/voltron) — a debugger-agnostic UI: multiple synchronized views across GDB/LLDB. (MIT)
- [boxxy](https://github.com/kpcyrd/boxxy-rs) — a rules-based sandbox for misbehaving programs; redirects what they touch. (LGPL-2.1)
- [pwndbg](https://github.com/pwndbg/pwndbg) — GDB with a exploit-dev UX: heap awareness, shortcuts and sane defaults. (MIT)
- [ImHex](https://github.com/WerWolv/ImHex) — the hex editor with pattern language: parse formats while you view them. (GPL-2.0)
- [Brida](https://github.com/federicodotta/Brida) — the bridge between Burp and Frida: custom instrumentation in your proxy workflow. (MIT)
- [Awesome Malware Analysis](https://github.com/rshipp/awesome-malware-analysis) — the curated malware-analysis tool index. (CC-BY-4.0, curated list)
- [OCSF](https://github.com/ocsf/ocsf-schema) — the Open Cybersecurity Schema Framework: one schema for security events. (Apache-2.0)
- [Netron](https://github.com/lutzroeder/netron) — visualize ML models: the layers, weights and graph of what you deploy. (MIT)
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
