# The Sentinel Ops

> **47 tools** · [← Back to the main list](../README.md) · Data verified **2026-10-15** (re-verified monthly)

## Curator's notes

The largest realm — detection engineering, ATT&CK-aligned datasets, SIEM labs and DFIR toolkits. The fingerprinting standards (JA3, HASSH) live here: archived upstream, still canonical, still cited in nearly every detection paper.

## Maintenance snapshot (2026-10-15)

- **Active in the last 30 days:** 26 of 46 tracked GitHub repos (57%)
- **Quiet classics (no push in 2+ years, still the standard):** sysmon-config, Revoke-Obfuscation, DeepBlueCLI, HELK
- **Youngest entries:** The Sleuth Kit (2011), Arkime (2012), Zeek (2012)

## Flagship picks

| Tool | ★ Stars | Created | Last push | What it does |
|---|---|---|---|---|
| [osquery](https://github.com/osquery/osquery) | 23.6k | 2014 | 2026-10-14 ✅ | SQL powered operating system instrumentation, monitoring, and analytics. |
| [Wazuh](https://github.com/wazuh/wazuh) | 17.3k | 2015 | 2026-10-15 ✅ | Wazuh - The Open Source Security Platform. Unified XDR and SIEM protection for endpoints and cloud workloads. |
| [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) | 12.7k | 2017 | 2026-10-13 ✅ | Small and highly portable detection tests based on MITRE's ATT&CK. |
| [Sigma](https://github.com/SigmaHQ/sigma) | 11.2k | 2016 | 2026-10-15 ✅ | Main Sigma Rule Repository |
| [awesome-honeypots](https://github.com/paralax/awesome-honeypots) | 10.6k | 2015 | 2026-06-01 | an awesome list of honeypot resources |
| [YARA](https://github.com/VirusTotal/yara) | 9.9k | 2012 | 2026-10-15 ✅ | The pattern matching swiss knife |

## Full inventory (47 tools)

| Tool | ★ Stars | Created | Last push | License / tier |
|---|---|---|---|---|
| [osquery](https://github.com/osquery/osquery) | 23.6k | 2014 | 2026-10-14 ✅ | — operate endpoints as a SQL database: ask security questions, get rows back. |
| [Wazuh](https://github.com/wazuh/wazuh) | 17.3k | 2015 | 2026-10-15 ✅ | — open-source XDR/SIEM: FIM, log analysis, vulnerability detection and compliance reporting in one free platform. (GPL-2.0) |
| [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) | 12.7k | 2017 | 2026-10-13 ✅ | — library of executable detection tests mapped to MITRE ATT&CK; prove your defenses fire. |
| [Sigma](https://github.com/SigmaHQ/sigma) | 11.2k | 2016 | 2026-10-15 ✅ | — vendor-neutral SIEM detection rules — "Snort for logs", convertible to Splunk/Sentinel/Elastic. (DRL 1.1 rules) |
| [awesome-honeypots](https://github.com/paralax/awesome-honeypots) | 10.6k | 2015 | 2026-06-01 | — the curated honeypot directory: deception tech from low to high interaction. (curated list) |
| [YARA](https://github.com/VirusTotal/yara) | 9.9k | 2012 | 2026-10-15 ✅ | — the pattern-matching language for malware identification — if you write detections, you write YARA. (BSD-3) |
| [Awesome Incident Response](https://github.com/meirwah/awesome-incident-response) | 9.5k | 2015 | 2026-10-13 ✅ | — the curated IR toolkit index used across the industry. (Apache-2.0, curated list) |
| [ntopng](https://github.com/ntop/ntopng) | 8.3k | 2015 | 2026-10-15 ✅ | — high-speed web-based traffic monitoring: flows, top talkers and protocols with long historical views. (GPL-3.0) |
| [Zeek](https://github.com/zeek/zeek) | 8.1k | 2012 | 2026-10-15 ✅ | — the network analysis framework that turns raw traffic into structured, queryable intelligence. (BSD-3) |
| [Arkime](https://github.com/arkime/arkime) | 7.5k | 2012 | 2026-10-15 ✅ | — full-packet capture plus indexed search at scale (formerly Moloch); PCAP you can actually query. |
| [Suricata](https://github.com/OISF/suricata) | 6.7k | 2012 | 2026-10-09 ✅ | — high-performance IDS/IPS/NSM engine with full protocol logging and Eve JSON output. (GPL-2.0) |
| [capa](https://github.com/mandiant/capa) | 6.2k | 2020 | 2026-10-15 ✅ | — identifies what malware actually does: maps capabilities and ATT&CK techniques straight from binaries. |
| [pspy](https://github.com/DominicBreuker/pspy) | 6.2k | 2018 | 2026-03-01 | — watch process and file events on any Linux box without root — catch cron-based persistence in the act. (GPL-3.0) |
| [sysmon-config](https://github.com/SwiftOnSecurity/sysmon-config) | 5.7k | 2017 | 2024-07-03 ⏳ | — the battle-tested Sysmon configuration behind thousands of SOC detections; the de-facto starting point for Windows telemetry. |
| [ThreatMapper](https://github.com/deepfence/ThreatMapper) | 5.3k | 2020 | 2026-06-01 | — Deepfence's open runtime threat scanner: finds and ranks exploitable vulnerabilities in cloud and container workloads. |
| [Security Onion](https://github.com/Security-Onion-Solutions/securityonion) | 4.9k | 2018 | 2026-10-14 ✅ | — the free SOC-in-a-box distro: Suricata, Zeek, Elastic, dashboards and detection pipelines. (Elastic License 2.0) |
| [Threat Hunter Playbook](https://github.com/OTRF/ThreatHunter-Playbook) | 4.7k | 2017 | 2026-01-12 | — open hunting playbooks as code: hypotheses mapped to data sources and detections. (MIT) |
| [Volatility 3](https://github.com/volatilityfoundation/volatility3) | 4.5k | 2014 | 2026-10-12 ✅ | — memory forensics framework — RAM malware has nowhere to hide. |
| [Velociraptor](https://github.com/Velocidex/velociraptor) | 4.3k | 2018 | 2026-10-15 ✅ | — endpoint visibility and DFIR at scale: hunt across thousands of machines with one query language. (AGPL-3.0) |
| [Awesome YARA](https://github.com/InQuest/awesome-yara) | 4.3k | 2017 | 2026-06-15 | — curated YARA rules, tooling and research for malware hunting. (CC-BY-4.0, curated list) |
| [HELK](https://github.com/Cyb3rWard0g/HELK) | 3.9k | 2017 | 2024-06-01 ⏳ | — the Hunting ELK: a pre-built Elasticsearch/Kafka/Spark lab for threat-hunting research — a research project with low churn. (GPL-3.0) |
| [CAPEv2](https://github.com/kevoreilly/CAPEv2) | 3.6k | 2019 | 2026-10-14 ✅ | — the maintained Cuckoo sandbox: automated malware detonation, config extraction and reporting. (GPL-3.0) |
| [Snort 3](https://github.com/snort3/snort3) | 3.4k | 2014 | 2026-04-23 | — the next generation of the classic open-source IDS/IPS, rewritten in C++ with multi-threading. (GPL-2.0) |
| [Timesketch](https://github.com/google/timesketch) | 3.4k | 2014 | 2026-10-14 ✅ | — Google's collaborative forensic timeline analysis for multi-investigator cases. |
| [The Sleuth Kit](https://github.com/sleuthkit/sleuthkit) | 3.2k | 2011 | 2026-10-15 ✅ | — the forensic library behind half the DFIR tools you know: disks, filesystems and timelines. (CPL-1.0) |
| [sysmon-modular](https://github.com/olafhartong/sysmon-modular) | 3.2k | 2018 | 2026-10-14 ✅ | — Swiss-army Sysmon configuration: per-ATT&CK-technique logging modules you compose yourself. |
| [Elastic detection-rules](https://github.com/elastic/detection-rules) | 2.7k | 2020 | 2026-10-15 ✅ | — the detection corpus for Elastic Security: hundreds of maintained rules mapped to MITRE. (Elastic-2.0) |
| [Fibratus](https://github.com/rabbitstack/fibratus) | 2.6k | 2016 | 2026-10-14 ✅ | — Windows kernel-event tracing with YARA filtering; a Swiss army knife for endpoint visibility. (Apache-2.0) |
| [Shuffle](https://github.com/Shuffle/Shuffle) | 2.5k | 2020 | 2026-10-12 ✅ | — self-hosted SOAR automation: connect your TIP, SIEM and responders in drag-and-drop workflows. (AGPL-3.0) |
| [DeepBlueCLI](https://github.com/sans-blue-team/DeepBlueCLI) | 2.4k | 2016 | 2023-10-14 ⏳ | — SANS blue-team PowerShell for fast Windows event-log hunting: logons, mutants, suspicious service installs — quiet upstream but still a blue-team staple. (GPL-3.0) |
| [Kismet](https://github.com/kismetwireless/kismet) | 2.2k | 2016 | 2026-10-15 ✅ | — passive wireless detection layer: discovers Wi-Fi and BLE devices, rogue access points and wardrives. (GPL-2.0) |
| [Sysmon for Linux](https://github.com/Sysinternals/SysmonForLinux) | 2.2k | 2020 | 2026-09-14 ✅ | — the Windows-trusted system monitor ported to Linux. (MIT) |
| [Nagios Core](https://github.com/NagiosEnterprises/nagioscore) | 2.1k | 2014 | 2026-08-07 | — the classic infrastructure monitor: availability checks that surface outages and anomalies early. (GPL-2.0) |
| [FIR](https://github.com/certsocietegenerale/FIR) | 2.0k | 2015 | 2026-09-14 ✅ | — Fast Incident Response from Société Générale: ticketing built for IR workflows. (GPL-3.0) |
| [msticpy](https://github.com/microsoft/msticpy) | 2.0k | 2019 | 2026-10-15 ✅ | — SecOps analysis library from Microsoft: pivots, timelines and hunting helpers for Jupyter. (MIT) |
| [Netcap](https://github.com/dreadl0ck/netcap) | 1.8k | 2018 | 2026-10-13 ✅ | — security audit framework over network traffic: sensors, audit and collection from live or captured streams. (GPL-3.0) |
| [go-audit](https://github.com/slackhq/go-audit) | 1.7k | 2016 | 2026-10-14 ✅ | — auditd in JSON for Linux: structured events that pipelines can actually parse. (MIT) |
| [Conpot](https://github.com/mushorg/conpot) | 1.5k | 2013 | 2026-10-12 ✅ | — ICS/SCADA honeypot: emulates the protocols that run factories, safely. (GPL-2.0) |
| [NoScript](https://github.com/hackademix/noscript) | 1.2k | 2018 | 2026-10-05 ✅ | — the browser extension that blocks JavaScript and plugin content by default — client-side hardening's origin story. (GPL-3.0) |
| [ElastAlert2](https://github.com/jertel/elastalert2) | 1.1k | 2020 | 2026-10-09 ✅ | — the maintained successor to ElastAlert: flexible alerting on Elasticsearch data with dozens of rule types. |
| [HijackThis](https://github.com/dragokas/hijackthis) | 817 | 2016 | 2026-07-02 | — the veteran Windows hijack analyzer: scans browser and OS settings for malicious tampering. (GPL-2.0) |
| [Krawl](https://github.com/BlessedRebuS/Krawl) | 783 | 2025 | 2026-10-14 ✅ | — deception-driven defense: a honeypot server framework for research. (MIT) |
| [Revoke-Obfuscation](https://github.com/danielbohannon/Revoke-Obfuscation) | 754 | 2017 | 2023-12-01 ⏳ | — Daniel Bohannon's framework for detecting obfuscated PowerShell at scale; quiet upstream, still the reference. |
| [RITA](https://github.com/activecm/rita) | 657 | 2024 | 2026-10-01 ✅ | — detects C2 beaconing in Zeek logs — traffic analysis that finds the quiet intruders. (GPL-3.0) |
| [Sublime Rules](https://github.com/sublime-security/sublime-rules) | 379 | 2021 | 2026-10-15 ✅ | — the community rule corpus for the Sublime platform. (MIT) |
| [Sublime Platform](https://github.com/sublime-security/sublime-platform) | 275 | 2021 | 2026-10-10 ✅ | — open email threat detection: rules-as-code against phishing and BEC. (MIT) |
| [Sysinternals Suite](https://learn.microsoft.com/en-us/sysinternals/) | — | — | — | — Microsoft's free Windows admin and DFIR toolkit: Process Explorer, Autoruns, Procmon and dozens more. (free, proprietary) |

---
*This page is auto-audited from the GitHub API on every monthly verification pass. Stars, ages and push dates are re-snapshotted; the main list only changes when a tool dies or a better one takes its place. See the [editorial standards](../README.md#-editorial-standards).*
