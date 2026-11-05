# 🔭 The Watchtower

> **47 tools** · [← Back to the main list](../README.md) · Data verified **2026-11-06** (re-verified monthly)

## Curator's notes

Feeds, frameworks and enrichment for the SOC's morning routine. Threat-intel platforms, IOC pipelines and detection-as-data. Most entries here are pipelines rather than point tools — chaining them is the whole game.

## Maintenance snapshot (2026-11-06)

- **Active in the last 30 days:** 12 of 18 tracked GitHub repos (67%)
- **Quiet classics (no push in 12+ months, still listed):** none
- **Earliest entries:** SpiderFoot (2012), cve-search (2012), MISP (2013)

## Flagship picks

| Tool | ★ Stars | Created | Last push | What it does |
|---|---|---|---|---|
| [SpiderFoot](https://github.com/smicallef/spiderfoot) | 24.2k | 2012 | 2026-04-13 | SpiderFoot automates OSINT for threat intelligence and mapping your attack surface. |
| [OpenCTI](https://github.com/OpenCTI-Platform/OpenCTI) | 10.2k | 2018 | 2026-11-01 ✅ | Open Cyber Threat Intelligence Platform |
| [MISP](https://github.com/MISP/MISP) | 6.6k | 2013 | 2026-11-01 ✅ | MISP (core software) - Open Source Threat Intelligence and Sharing Platform |
| [IntelOwl](https://github.com/intelowlproject/IntelOwl) | 4.8k | 2019 | 2026-10-31 ✅ | IntelOwl: manage your Threat Intelligence at scale |
| [firehol/blocklist-ipsets](https://github.com/firehol/blocklist-ipsets) | 4k | 2015 | 2026-10-31 ✅ | ipsets dynamically updated with firehol's update-ipsets.sh script |
| [Uncover](https://github.com/projectdiscovery/uncover) | 3.1k | 2022 | 2026-10-27 ✅ | Quickly discover exposed hosts on the internet using multiple search engines. |

## Full inventory (47 tools)

| Tool | ★ Stars | Created | Last push | License / tier |
|---|---|---|---|---|
| [SpiderFoot](https://github.com/smicallef/spiderfoot) | 24.2k | 2012 | 2026-04-13 | — open-source OSINT automation with 200+ data sources; attack-surface and exposure monitoring out of the box. Used by OSINT investigators automating recon; the free self-hosted version of the SpiderFoot HX service. |
| [OpenCTI](https://github.com/OpenCTI-Platform/OpenCTI) | 10.2k | 2018 | 2026-11-01 ✅ | — threat-intel knowledge graph built on STIX2; analyst-first investigation dashboards instead of raw feeds. Used by CTI teams building knowledge graphs of threat data; the open-source alternative to commercial intel platforms with graph UIs. |
| [MISP](https://github.com/MISP/MISP) | 6.6k | 2013 | 2026-11-01 ✅ | — the de-facto open threat-sharing platform: events, attributes, galaxies and thousands of community feeds. Used by CERTs and threat-intel teams worldwide; the leading open-source alternative to commercial threat-intelligence platforms like Recorded Future and ThreatQ. (AGPL-3.0) |
| [IntelOwl](https://github.com/intelowlproject/IntelOwl) | 4.8k | 2019 | 2026-10-31 ✅ | — bulk-analyze observables across 100+ online services from one API and web UI. Used by SOC analysts enriching observables in bulk; the open-source alternative to commercial one-click threat-inquiry APIs. (AGPL-3.0) |
| [EQGRP](https://github.com/x0rz/EQGRP) | 4.2k | 2017 | 2017-05-24 ⏳ | — Decrypted content of the EQGRP auction file attributed to offensive tooling. Used by researchers and defenders; a historical artifact for threat analysis. |
| [firehol/blocklist-ipsets](https://github.com/firehol/blocklist-ipsets) | 4k | 2015 | 2026-10-31 ✅ | — aggregated, daily-updated IP blocklists (attacks, spam, abuse) ready for iptables/fail2ban; check each list's own license before redistribution. Used by firewall admins feeding blocklists; the community-maintained alternative to commercial IP-reputation feeds. |
| [Uncover](https://github.com/projectdiscovery/uncover) | 3.1k | 2022 | 2026-10-27 ✅ | — query exposed services across Shodan, Censys and friends in one sweep — the instant exposure check. Used by recon teams querying exposure across search engines at once; the free aggregator for Shodan-style lookups. |
| [OpenCVE](https://github.com/opencve/opencve) | 2.9k | 2020 | 2026-10-26 ✅ | — self-hosted vulnerability intelligence platform: indexes CVEs and notifies on the products and keywords you follow. Used by security teams tracking new CVEs for their asset inventory; the self-hosted alternative to commercial CVE feeds. (Apache-2.0) |
| [cve-search](https://github.com/cve-search/cve-search) | 2.7k | 2012 | 2026-10-13 ✅ | — self-hosted CVE/CPE database in MongoDB with web UI, API and CLI. Used by orgs (incl. CIRCL's former public CVE service) to run local, rate-limit-free vulnerability lookups; strict/lax CPE matching, 14 yrs of maintenance. (AGPL-3.0) |
| [Yeti](https://github.com/yeti-platform/yeti) | 2k | 2015 | 2026-10-28 ✅ | — organize your threat intel: observables, indicators and TTPs in one searchable, API-first platform. Used by CTI analysts organizing indicators and TTPs; the open-source threat-intel tracker for teams without commercial TIP budgets. |
| [IntelMQ](https://github.com/certtools/intelmq) | 1.1k | 2014 | 2026-04-28 | — the feed plumber's dream: collect, normalize and route threat-intel feeds from hundreds of sources into your stack. Used by national CERTs automating feed ingestion; the open-source alternative to commercial intel-pipeline tooling. (AGPL-3.0) |
| [ThreatHunting-Keywords](https://github.com/mthcht/ThreatHunting-Keywords) | 683 | 2023 | 2025-08-04 ⏳ | — Massive database of keywords, artifacts, and patterns organized by offensive tool, ATT&CK technique, and log type with ready queries. Used by threat hunters; a practical detection keyword reference. |
| [RansomLook](https://github.com/RansomLook/RansomLook) | 682 | 2022 | 2026-10-30 ✅ | — open ransomware-group leak-site tracker with historical victim data (see also the live stats at ransomware.live). Used by CTI analysts tracking ransomware leak sites; the free watchtower the commercial feeds also scrape. (GPL-3.0) |
| [CVE2CAPEC](https://github.com/Galeax/CVE2CAPEC) | 322 | 2024 | 2026-11-01 ✅ | — Maps CVEs through CWE to CAPEC, MITRE ATT&CK, D3FEND and ATLAS techniques with a daily-updated database; showcased at BlackHat Europe 2025 Arsenal. Used by threat-intel analysts turning CVE lists into technique-level attack context; the free CVE-to-technique enrichment engine.. (GPL-3.0) |
| [Trust Scan](https://github.com/undeadlist/trust-scan) | 5 | 2025 | 2026-03-25 ⏳ | — URL security scanner combining threat intelligence feeds like URLhaus, PhishTank and Spamhaus with 40+ scam and phishing pattern checks. Used by defenders and analysts; a practical phishing triage helper. (MIT) |
| [CrawlerScope](https://github.com/ipanalytics/CrawlerScope) | 1 | 2026 | 2026-11-01 ✅ | — operator-published crawler and AI-bot CIDR dataset for bot attribution. Used by defenders verifying whether traffic is a legitimate crawler; the public dataset for bot-network attribution. (CC0) |
| [http-detection-agent](https://github.com/ai-blueteam/http-detection-agent) | 1 | 2026 | 2026-10-28 ✅ | — traffic anomaly detection for the blue team: labels HTTP datasets without shipping them off-box. Used by recon pipelines fingerprinting web servers at scale; a focused open utility for asset inventories. (MIT) |
| [threat-intel (GitHub)](https://github.com/phutran1210dev/threat-intel) | 0 | 2025 | 2025-11-25 ⏳ | — Real-time threat intelligence aggregation and visualization platform with IOC tracking, actor profiling and Elasticsearch/Kibana dashboards. Used by SOC analysts and CTI teams; an open-source aggregation stack. (MIT) |
|---|---|---|---|---|
| [Emerging Threats Open](http://doc.emergingthreats.net/bin/view/Main/EmergingFAQ) | — | — | — | — the open Suricata/Snort rule feed from Proofpoint; thousands of community-maintained detection rules. Used by Suricata and Snort defenders everywhere; the free ruleset that the commercial ET Pro subscription extends. (free feed) |
| [ICHI — Internet Cyber Health Index](https://ichi.global) | — | — | — | — free, source-transparent daily barometer of internet cyber health, aggregating threat intelligence, security news, and telemetry from 20+ named public sources. Used by SOC analysts and security researchers for daily situational awareness of global cyber conditions; the free daily-refresh alternative to scattered vendor intelligence portals. (free service) |
| [Malpedia](https://malpedia.caad.fkie.fraunhofer.de) | — | — | — | — curated malware encyclopedia: families, actors, papers and sample references for researchers. Used by malware researchers as the reference index of families and papers; the free, vendor-neutral encyclopedia. |
| [MITRE ATT&CK](https://attack.mitre.org) | — | — | — | — the adversary tactics & techniques knowledge base that the entire industry maps detections and emulations against. Used by red teams, defenders and vendors as the shared language of adversary behavior; the free framework the whole industry maps to. |
| [NetworkMiner](https://www.netresec.com/?page=NetworkMiner) | — | — | — | — passive network-forensics analyzer: extracts files, credentials and sessions from recorded traffic without touching the live network. Used by DFIR analysts for passive network forensics and artifact extraction; the free alternative to commercial network-forensics suites. (free, proprietary) |
| [vx-underground](https://vx-underground.org) | — | — | — | — the malware corpus and INT report archive; free, massive and respected across the research community. Used by malware researchers studying live collections; the free sample and paper archive with no commercial gate. (free service) |
| [ZDI advisories](https://www.zerodayinitiative.com/advisories/published/) | — | — | — | — published zero-day advisories from the Zero Day Initiative; the disclosure record for enterprise-software flaws. Used by patch-priority teams tracking pre-disclosure zero-days; the free advisory stream competing with vendor feeds. (free service) |
| [WhiteIntel](https://whiteintel.io/) | — | — | — | — Dark web monitoring service tracking exposed data and credentials across underground sources. Used by defenders and organizations; a free-tier early warning for leaked credentials. (free tier) |
| [ThreatFox](https://threatfox.abuse.ch/) | — | — | — | — Free community IOC platform by abuse.ch for searching domains, IPs and file hashes against known malware infrastructure. Used by threat analysts and SOC teams; a constantly updated IOC lookup. (free, proprietary) |
| [IBM X-Force Exchange](https://exchange.xforce.ibmcloud.com/) | — | — | — | — Free community threat intelligence research platform offering IOC search and malware analysis data. Used by CTI analysts and researchers; a long-standing free exchange for threat data. (free tier) |
| [VulnWatch](https://vulnwatch.tech/) | — | — | — | — Cybersecurity platform dedicated to tracking vulnerabilities, monitoring emerging security threats, and providing insights. Used by security analysts and defenders; a free vulnerability and threat tracking service. (free, proprietary) |
| [MITRE ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/) | — | — | — | — Coverage mapping tool visualizing detection and hunting coverage against the ATT&CK matrix, with an MCP server for AI assistance. Used by defenders; the standard ATT&CK coverage mapper. |
| [CrowdStrike Blog](https://www.crowdstrike.com/blog/) | — | — | — | — CrowdStrike's vendor blog with investigative research on threats, vulnerabilities, and APT groups; used by defenders for threat intelligence. (free, proprietary) |
| [Google Project Zero](https://googleprojectzero.blogspot.com/) | — | — | — | — Google Project Zero's blog publishing deep technical analyses of zero-day vulnerabilities and exploitation techniques; read by elite researchers. (free, proprietary) |
| [Mandiant Blog](https://www.mandiant.com/resources/blog) | — | — | — | — Mandiant's research blog providing frontline threat intelligence and incident response insights; used by defenders tracking major breaches. (free, proprietary) |
| [Check Point Research](https://research.checkpoint.com/) | — | — | — | — Check Point Research blog covering APT campaigns, vulnerability discoveries, and attack trends; read by threat intelligence analysts. (free, proprietary) |
| [Cisco Talos Intelligence](https://blog.talosintelligence.com/) | — | — | — | — Cisco Talos threat research blog covering vulnerabilities, malware campaigns, and threat actor activity; used by defenders for intelligence. (free, proprietary) |
| [Fortinet Threat Research](https://www.fortinet.com/blog/threat-research) | — | — | — | — FortiGuard Labs research blog covering emerging threats, malware analysis, and vulnerability intelligence; read by security operations teams. (free, proprietary) |
| [Securelist (Kaspersky)](https://securelist.com/) | — | — | — | — Kaspersky's research blog with deep malware analysis, APT tracking, and threat intelligence; used by researchers and defenders. (free, proprietary) |
| [Malwarebytes Labs](https://www.malwarebytes.com/blog) | — | — | — | — Malwarebytes Labs blog covering malware research, threat analysis, and security news; read by practitioners tracking emerging threats. (free, proprietary) |
| [SentinelLabs](https://www.sentinelone.com/labs/) | — | — | — | — SentinelOne's research division publishing threat intelligence, malware analysis, and offensive security research; used by defenders and researchers. (free, proprietary) |
| [CISA Advisories](https://www.cisa.gov/cybersecurity-advisories) | — | — | — | — CISA's official alerts, advisories, and Known Exploited Vulnerabilities catalog; used by defenders worldwide to prioritize patching. (free, proprietary) |
| [CERT-FR (ANSSI)](https://www.cert.ssi.gouv.fr/) | — | — | — | — French national cybersecurity agency's advisories and alerts on vulnerabilities and threats; used by defenders tracking European intelligence. (free, proprietary) |
| [Zero Day Initiative (ZDI)](https://www.zerodayinitiative.com/) | — | — | — | — Trend Micro's bug bounty program publishing vulnerability advisories and zero-day disclosures; used by defenders tracking unpatched flaws. (free, proprietary) |
| [Google Online Security Blog](https://security.googleblog.com/) | — | — | — | — Google's security team blog covering vulnerabilities, security features, and threat research; read by practitioners and researchers. (free, proprietary) |
| [SANS Internet Storm Center](https://isc.sans.edu/) | — | — | — | — Daily diary of security incidents and handler insights from SANS. Used by defenders and threat analysts; a trusted community resource for real-time threat awareness. |
| [The Record by Recorded Future](https://therecord.media/) | — | — | — | — Intelligence-driven reporting on attackers, vulnerabilities, and global security incidents backed by Recorded Future. Used by defenders and analysts; a reliable news source for threat awareness. |
| [NSFOCUS](https://nti.nsfocus.com/) | — | — | — | — NSFOCUS threat intelligence portal providing IOC and threat data. Used by SOC analysts and defenders; a vendor threat intel resource. (free tier) |
| [ssltest](https://www.ssllabs.com/ssltest/) | — | — | — | — Online service performing deep analysis of SSL web server configuration. Used by sysadmins and security testers; the standard TLS configuration grader. (free, proprietary) |



---
*This page is auto-audited from the GitHub API on every monthly verification pass. Stars, ages and push dates are re-snapshotted; the main list only changes when a tool dies or a better one takes its place. See the [editorial standards](../README.md#-editorial-standards).*
