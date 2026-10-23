# 🔭 The Watchtower

> **20 tools** · [← Back to the main list](../README.md) · Data verified **2026-10-23** (re-verified monthly)

## Curator's notes

Feeds, frameworks and enrichment for the SOC's morning routine. Threat-intel platforms, IOC pipelines and detection-as-data. Most entries here are pipelines rather than point tools — chaining them is the whole game.

## Maintenance snapshot (2026-10-23)

- **Active in the last 30 days:** 11 of 13 tracked GitHub repos (85%)
- **Earliest entries:** SpiderFoot (2012), cve-search (2012), MISP (2013)

## Flagship picks

| Tool | ★ Stars | Created | Last push | What it does |
|---|---|---|---|---|
| [SpiderFoot](https://github.com/smicallef/spiderfoot) | 23.7k | 2012 | 2026-04-13 | SpiderFoot automates OSINT for threat intelligence and mapping your attack surface. |
| [OpenCTI](https://github.com/OpenCTI-Platform/OpenCTI) | 10.2k | 2018 | 2026-10-22 ✅ | Open Cyber Threat Intelligence Platform |
| [MISP](https://github.com/MISP/MISP) | 6.6k | 2013 | 2026-10-21 ✅ | MISP (core software) - Open Source Threat Intelligence and Sharing Platform |
| [IntelOwl](https://github.com/intelowlproject/IntelOwl) | 4.8k | 2019 | 2026-10-20 ✅ | IntelOwl: manage your Threat Intelligence at scale |
| [firehol/blocklist-ipsets](https://github.com/firehol/blocklist-ipsets) | 3.9k | 2015 | 2026-10-21 ✅ | ipsets dynamically updated with firehol's update-ipsets.sh script |
| [Uncover](https://github.com/projectdiscovery/uncover) | 3.1k | 2022 | 2026-10-22 ✅ | Quickly discover exposed hosts on the internet using multiple search engines. |

## Full inventory (20 tools)

| Tool | ★ Stars | Created | Last push | License / tier |
|---|---|---|---|---|
| [SpiderFoot](https://github.com/smicallef/spiderfoot) | 23.7k | 2012 | 2026-04-13 | — open-source OSINT automation with 200+ data sources; attack-surface and exposure monitoring out of the box. Used by OSINT investigators automating recon; the free self-hosted version of the SpiderFoot HX service. |
| [OpenCTI](https://github.com/OpenCTI-Platform/OpenCTI) | 10.2k | 2018 | 2026-10-22 ✅ | — threat-intel knowledge graph built on STIX2; analyst-first investigation dashboards instead of raw feeds. Used by CTI teams building knowledge graphs of threat data; the open-source alternative to commercial intel platforms with graph UIs. |
| [MISP](https://github.com/MISP/MISP) | 6.6k | 2013 | 2026-10-21 ✅ | — the de-facto open threat-sharing platform: events, attributes, galaxies and thousands of community feeds. Used by CERTs and threat-intel teams worldwide; the leading open-source alternative to commercial threat-intelligence platforms like Recorded Future and ThreatQ. (AGPL-3.0) |
| [IntelOwl](https://github.com/intelowlproject/IntelOwl) | 4.8k | 2019 | 2026-10-20 ✅ | — bulk-analyze observables across 100+ online services from one API and web UI. Used by SOC analysts enriching observables in bulk; the open-source alternative to commercial one-click threat-inquiry APIs. (AGPL-3.0) |
| [firehol/blocklist-ipsets](https://github.com/firehol/blocklist-ipsets) | 3.9k | 2015 | 2026-10-21 ✅ | — aggregated, daily-updated IP blocklists (attacks, spam, abuse) ready for iptables/fail2ban; check each list's own license before redistribution. Used by firewall admins feeding blocklists; the community-maintained alternative to commercial IP-reputation feeds. |
| [Uncover](https://github.com/projectdiscovery/uncover) | 3.1k | 2022 | 2026-10-22 ✅ | — query exposed services across Shodan, Censys and friends in one sweep — the instant exposure check. Used by recon teams querying exposure across search engines at once; the free aggregator for Shodan-style lookups. |
| [OpenCVE](https://github.com/opencve/opencve) | 2.9k | 2020 | 2026-10-14 ✅ | — self-hosted vulnerability intelligence platform: indexes CVEs and notifies on the products and keywords you follow. Used by security teams tracking new CVEs for their asset inventory; the self-hosted alternative to commercial CVE feeds. (Apache-2.0) || [cve-search](https://github.com/cve-search/cve-search) | 2.7k | 2012 | 2026-10-13 ✅ | — self-hosted CVE/CPE database in MongoDB with web UI, API and CLI. Used by orgs (incl. CIRCL's former public CVE service) to run local, rate-limit-free vulnerability lookups; strict/lax CPE matching, 14 yrs of maintenance. (AGPL-3.0) |
| [Yeti](https://github.com/yeti-platform/yeti) | 2k | 2015 | 2026-10-09 ✅ | — organize your threat intel: observables, indicators and TTPs in one searchable, API-first platform. Used by CTI analysts organizing indicators and TTPs; the open-source threat-intel tracker for teams without commercial TIP budgets. |
| [IntelMQ](https://github.com/certtools/intelmq) | 1.1k | 2014 | 2026-04-28 | — the feed plumber's dream: collect, normalize and route threat-intel feeds from hundreds of sources into your stack. Used by national CERTs automating feed ingestion; the open-source alternative to commercial intel-pipeline tooling. (AGPL-3.0) |
| [RansomLook](https://github.com/RansomLook/RansomLook) | 677 | 2022 | 2026-10-21 ✅ | — open ransomware-group leak-site tracker with historical victim data (see also the live stats at ransomware.live). Used by CTI analysts tracking ransomware leak sites; the free watchtower the commercial feeds also scrape. (GPL-3.0) |
| [CrawlerScope](https://github.com/ipanalytics/CrawlerScope) | 1 | 2026 | 2026-10-22 ✅ | — operator-published crawler and AI-bot CIDR dataset for bot attribution. Used by defenders verifying whether traffic is a legitimate crawler; the public dataset for bot-network attribution. (CC0) |
| [http-detection-agent](https://github.com/ai-blueteam/http-detection-agent) | - | 2026 | 2026-10-02 ✅ | — traffic anomaly detection for the blue team: labels HTTP datasets without shipping them off-box. Used by recon pipelines fingerprinting web servers at scale; a focused open utility for asset inventories. (MIT) |
|---|---|---|---|---|
| [Emerging Threats Open](http://doc.emergingthreats.net/bin/view/Main/EmergingFAQ) | — | — | — | — the open Suricata/Snort rule feed from Proofpoint; thousands of community-maintained detection rules. Used by Suricata and Snort defenders everywhere; the free ruleset that the commercial ET Pro subscription extends. (free feed) |
| [ICHI — Internet Cyber Health Index](https://ichi.global) | — | — | — | — free, source-transparent daily barometer of internet cyber health, aggregating threat intelligence, security news, and telemetry from 20+ named public sources. Used by SOC analysts and security researchers for daily situational awareness of global cyber conditions; the free daily-refresh alternative to scattered vendor intelligence portals. (free service) |
| [Malpedia](https://malpedia.caad.fkie.fraunhofer.de) | — | — | — | — curated malware encyclopedia: families, actors, papers and sample references for researchers. Used by malware researchers as the reference index of families and papers; the free, vendor-neutral encyclopedia. |
| [MITRE ATT&CK](https://attack.mitre.org) | — | — | — | — the adversary tactics & techniques knowledge base that the entire industry maps detections and emulations against. Used by red teams, defenders and vendors as the shared language of adversary behavior; the free framework the whole industry maps to. |
| [NetworkMiner](https://www.netresec.com/?page=NetworkMiner) | — | — | — | — passive network-forensics analyzer: extracts files, credentials and sessions from recorded traffic without touching the live network. Used by DFIR analysts for passive network forensics and artifact extraction; the free alternative to commercial network-forensics suites. (free, proprietary) |
| [vx-underground](https://vx-underground.org) | — | — | — | — the malware corpus and INT report archive; free, massive and respected across the research community. Used by malware researchers studying live collections; the free sample and paper archive with no commercial gate. (free service) |
| [ZDI advisories](https://www.zerodayinitiative.com/advisories/published/) | — | — | — | — published zero-day advisories from the Zero Day Initiative; the disclosure record for enterprise-software flaws. Used by patch-priority teams tracking pre-disclosure zero-days; the free advisory stream competing with vendor feeds. (free service) |

---
*This page is auto-audited from the GitHub API on every monthly verification pass. Stars, ages and push dates are re-snapshotted; the main list only changes when a tool dies or a better one takes its place. See the [editorial standards](../README.md#-editorial-standards).*
