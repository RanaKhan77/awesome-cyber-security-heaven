# 🛡️ The Bastion

> **33 tools** · [← Back to the main list](../README.md) · Data verified **2026-11-01** (re-verified monthly)

## Curator's notes

The mirror image of the Armory: what you install so you never get popped. Kernel-level audit, mandatory-access-control lineages (SELinux, OpenBSD PF), host hardening and firewall tooling — the unglamorous layer that stops real breaches.

## Maintenance snapshot (2026-11-01)

- **Active in the last 30 days:** 22 of 28 tracked GitHub repos (79%)
- **Quiet classics (no push in 12+ months, still listed):** OpenRASP
- **Earliest entries:** Fail2ban (2011), OpenVPN (2012), ClamAV (2012)

## Flagship picks

| Tool | ★ Stars | Created | Last push | What it does |
|---|---|---|---|---|
| [Fail2ban](https://github.com/fail2ban/fail2ban) | 18.9k | 2011 | 2026-10-27 ✅ | Daemon to ban hosts that cause multiple authentication errors |
| [Lynis](https://github.com/CISOfy/lynis) | 16.6k | 2013 | 2026-09-16 | Lynis - Security auditing tool for Linux, macOS, and UNIX-based systems. Assists with compliance testing (HIPA… |
| [CrowdSec](https://github.com/crowdsecurity/crowdsec) | 15.4k | 2020 | 2026-10-30 ✅ | Open-source IDS/IPS, WAF and bot detection for Linux, Windows, Docker and Kubernetes, with a crowdsourced bloc… |
| [OpenVPN](https://github.com/OpenVPN/openvpn) | 14.8k | 2012 | 2026-10-31 ✅ | OpenVPN  is  an open source VPN daemon |
| [OpenSnitch](https://github.com/evilsocket/opensnitch) | 14.2k | 2017 | 2026-07-26 | OpenSnitch is a GNU/Linux interactive application firewall inspired by Little Snitch. |
| [OpenNHP](https://github.com/OpenNHP/opennhp) | 14k | 2014 | 2026-10-30 ✅ | Make your infrastructure invisible to attackers. OpenNHP implements the Network-infrastructure Hiding Protocol… |

| [OpenSnitch](https://github.com/evilsocket/opensnitch) | 14.2k | 2017 | 2026-07-26 | OpenSnitch is a GNU/Linux interactive application firewall inspired by Little Snitch. |
| [OpenNHP](https://github.com/OpenNHP/opennhp) | 13.9k | 2014 | 2026-10-22 ✅ | A lightweight, cryptography-powered, open-source toolkit built to enforce Zero Trust security for infrastructure, applications, and data in the AI-driven world. |

## Full inventory (33 tools)

| Tool | ★ Stars | Created | Last push | License / tier |
|---|---|---|---|---|
| [Fail2ban](https://github.com/fail2ban/fail2ban) | 18.9k | 2011 | 2026-10-27 ✅ | — the classic log-watching IPS that bans brute-forcing IPs; still the default answer on every Linux server. Used by sysadmins on millions of servers to stop brute force; the classic free guard no commercial tool needed to replace. (GPL-2.0) |
| [Lynis](https://github.com/CISOfy/lynis) | 16.6k | 2013 | 2026-09-16 | — agentless system auditing and hardening with CIS/PCI-DSS-aligned findings; runs anywhere in minutes. Used by system auditors running CIS-style hardening checks; the open-source alternative to commercial compliance scanners for Linux/Unix hosts. (GPL-3.0) |
| [CrowdSec](https://github.com/crowdsecurity/crowdsec) | 15.4k | 2020 | 2026-10-30 ✅ | — collaborative behavior-detection engine with a global IP-reputation network; the modern Fail2ban, 60x faster and IPv6-ready. Used by server administrators and hosting providers; the open-source, crowdsourced alternative to commercial WAF and bot-management services. |
| [OpenVPN](https://github.com/OpenVPN/openvpn) | 14.8k | 2012 | 2026-10-31 ✅ | — the industry-standard open-source VPN daemon for site-to-site and remote-access tunnels. Used by IT teams everywhere; the open-source alternative to commercial VPN gateways. (GPL-2.0 core, component exceptions) |
| [OpenSnitch](https://github.com/evilsocket/opensnitch) | 14.2k | 2017 | 2026-07-26 | — interactive application firewall (Little Snitch for Linux): allow/deny every outbound connection per process. Used by Linux power users and admins wanting per-application firewall control; the open equivalent of Little Snitch on macOS. (GPL-3.0) |
| [OpenNHP](https://github.com/OpenNHP/opennhp) | 14k | 2014 | 2026-10-30 ✅ | — go implementation of the Cloud Security Alliance's Network-infrastructure Hiding Protocol: conceals ports, IPs and domains behind a cryptographically signed knock gate — services stay invisible until the client proves trust. Used by zero-trust teams making infrastructure undiscoverable to mass and AI-driven scanning; the reference open implementation of CSA NHP. (Apache-2.0) |
| [Vuls](https://github.com/future-architect/vuls) | 12.3k | 2016 | 2026-11-01 ✅ | — agentless vulnerability scanner for servers and containers, with CVE reporting across Linux and FreeBSD fleets. Used by server admins for agentless vulnerability scanning; the open-source alternative to Nessus for host patch audits. (GPL-3.0) |
| [BunkerWeb](https://github.com/bunkerity/bunkerweb) | 11.2k | 2019 | 2026-10-31 ✅ | — next-gen open WAF built on nginx: HTTPS, bot mitigation and network protections on by default. Used by web admins wanting a next-gen open-source WAF in front of their sites; the self-hosted alternative to Cloudflare's managed WAF. (AGPL-3.0) |
| [testssl.sh](https://github.com/drwetter/testssl.sh) | 9.3k | 2014 | 2026-10-28 ✅ | — command-line TLS/SSL configuration auditor: protocols, ciphers, chains, vulnerabilities, grading — no agent required. Used by TLS auditors and pentesters everywhere; the free command-line alternative to Qualys SSL Labs for server-side TLS grading. (GPL-2.0) |
| [ClamAV](https://github.com/Cisco-Talos/clamav) | 7.5k | 2012 | 2026-10-22 ✅ | — the open-source antivirus engine that powers mail gateways and file-screening pipelines everywhere. Used on countless mail gateways and Linux file screens; the AV engine many commercial mail filters embed. (GPL-2.0) |
| [Fleet](https://github.com/fleetdm/fleet) | 7.1k | 2020 | 2026-11-01 ✅ | — osquery fleet management: device visibility and policy enforcement at scale, open core with a free tier. Used by IT and security teams managing osquery fleets at scale; the open-source alternative to commercial device management and EDR consoles. (MIT, open core) |
| [dev-sec hardening collection](https://github.com/dev-sec/ansible-collection-hardening) | 5.5k | 2015 | 2026-10-22 ✅ | — battle-tested Ansible roles for OS, SSH, nginx and MySQL baselines; hardening as code. Used by DevOps teams enforcing server baselines as code; the open-source alternative to commercial configuration-compliance agents. |
| [OSSEC](https://github.com/ossec/ossec-hids) | 5.1k | 2013 | 2026-10-31 ✅ | — the original open-source HIDS: log analysis, file integrity and rootkit detection (Wazuh's ancestor). Used by SOC teams on a budget for host intrusion detection; the veteran open HIDS that predates commercial EDR. (GPL-2.0) |
| [OPNsense](https://github.com/opnsense/core) | 4.8k | 2014 | 2026-10-31 ✅ | — open-source firewall/router distro with IDS, VPN and reporting — a pfSense successor built on HardenedBSD. Used by network administrators as a full open-source firewall/router; the business-ready free alternative to commercial UTM appliances. (BSD-2) |
| [ssh-audit](https://github.com/jtesta/ssh-audit) | 4.3k | 2017 | 2026-10-17 ✅ | — SSH server configuration auditor: algorithms, keys and best-practice flags in one run. Used by server hardening teams to audit SSH configurations and algorithms; the standard free SSH auditor. (GPL-3.0) |
| [OpenSSH](https://github.com/openssh/openssh-portable) | 4.1k | 2014 | 2026-10-31 ✅ | — the world's default secure remote-access suite: encrypted shells, tunnels and key management. Used on virtually every Linux server on earth; the open standard for secure remote access that commercial SSH servers complement, not replace. (BSD-style) |
| [Coraza](https://github.com/corazawaf/coraza) | 4k | 2020 | 2026-10-31 ✅ | — ModSecurity-compatible WAF engine in Go; the actively developed successor for OWASP CRS deployments. Used by platform teams embedding a WAF engine inside Go services. |
| [OWASP Core Rule Set](https://github.com/coreruleset/coreruleset) | 3.3k | 2020 | 2026-11-01 ✅ | — the world's most-deployed WAF ruleset; battle-tested protection for web servers, tuned for ModSecurity and Coraza. Used by WAF administrators on nginx, Apache and Coraza; the free ruleset protecting more sites than most commercial WAF feeds. |
| [OpenRASP](https://github.com/baidu/openrasp) | 3k | 2017 | 2025-10-02 ⏳ | — runtime application self-protection: instrument the app itself so attacks get blocked from the inside. Used by AppSec teams adding runtime self-protection to apps; the open-source alternative to commercial RASP vendors. |
| [ComplianceAsCode content](https://github.com/ComplianceAsCode/content) | 2.8k | 2014 | 2026-10-31 ✅ | — the open SCAP/Baseline rule corpus for RHEL, Ubuntu and friends; the content that powers OpenSCAP-style audits. Used by compliance and platform teams applying SCAP hardening profiles; the open-source ruleset commercial compliance products build on. |
| [checksec.sh](https://github.com/slimm609/checksec.sh) | 2.4k | 2014 | 2026-10-28 ✅ | — one-shot binary hardening audit: NX, canaries, PIE, RELRO and fortify flags in a single run. Used by exploit developers and binary auditors checking hardening mitigations; the standard free one-liner for this job. (BSD-3-Clause) |
| [Neo23x0 auditd config](https://github.com/Neo23x0/auditd) | 2k | 2018 | 2026-05-04 | — Florian Roth's hardened auditd rule set: the Linux logging baseline used across incident-response teams. Used by blue teams hardening Linux audit collection; the widely-forked open auditd baseline behind many SOC deployments. (Apache-2.0) |
| [open-appsec](https://github.com/openappsec/openappsec) | 1.7k | 2022 | 2026-09-06 | — ML-driven prevention engine that stops OWASP Top 10 and zero-day web attacks without signatures. Used by security teams deploying machine-learning WAF protection; an open-source alternative to commercial ML-based WAF products. |
| [SELinux](https://github.com/SELinuxProject/selinux) | 1.7k | 2014 | 2026-10-30 ✅ | — mandatory access control for Linux: policy-based confinement that survives a compromised application. Used by hardened enterprise Linux deployments; the mandatory access control standard in RHEL-family distributions. (GPL-2.0) |
| [shellfirm](https://github.com/kaplanelad/shellfirm) | 951 | 2021 | 2026-10-29 ✅ | — a pre-execution guard for your shell: challenges dangerous commands (rm -rf, kubectl delete) before they run. Used by engineers protecting themselves from dangerous commands; a lightweight open guardrail before your shell executes rm -rf. (Apache-2.0) |
| [AIDE](https://github.com/aide/aide) | 759 | 2019 | 2026-10-22 ✅ | — Advanced Intrusion Detection Environment: file-integrity monitoring that alerts the moment system files change. Used by hardening teams for file-integrity monitoring; the free open alternative to commercial FIM modules. (GPL-2.0) |
| [stunnel](https://github.com/mtrojnar/stunnel) | 398 | 2015 | 2026-09-17 | — universal TLS wrapper that adds encryption to any TCP service in minutes. Used by admins adding TLS to legacy services; the free universal TLS wrapper. (GPL-2.0) |
| [unmask](https://github.com/unmask-sh/unmask) | 6 | 2026 | 2026-10-31 ✅ | — self-hosted privacy-first bot management gateway with verified-crawler bypass. Used by teams filtering bot traffic without third-party SaaS; the self-hosted bot-defense gateway. (Apache-2.0) |
|---|---|---|---|---|
| [Netfilter/iptables](https://netfilter.org/) | — | — | — | — the Linux kernel's native packet-filtering framework; the foundation every host firewall build starts from. Used by every Linux firewall admin; the kernel-level packet filter that commercial Linux firewalls wrap a UI around. (GPL-2.0) |
| [OpenBSD PF](https://www.openbsd.org/faq/pf/) | — | — | — | — the packet filter famous for correctness and readable rules; the syntax OpenBSD, pfSense and OPNsense share. Used by OpenBSD and firewall admins; the famously audited packet filter behind many security appliances. (ISC) |
| [Qubes OS](https://www.qubes-os.org/) | — | — | — | — the security-by-compartmentalization desktop OS; " reasonably secure" by architecture, not by antivirus. Used by journalists, researchers and high-risk users; the compartmentalized security desktop with no commercial counterpart. (GPL-2.0) |
| [SpamAssassin](https://spamassassin.apache.org/) | — | — | — | — the veteran open-source spam filter; bayesian scoring and rule engine at the mail gateway. Used by mail administrators on countless gateways; the veteran open-source anti-spam engine many commercial filters license. (Apache-2.0) |
| [Tor](https://www.torproject.org/) | — | — | — | — the anonymity network: routed egress through thousands of volunteer relays; the standard for privacy-preserving research access. Used by privacy-focused researchers, journalists and investigators; the free anonymity network with no commercial equivalent. (BSD-3-Clause) |

---
*This page is auto-audited from the GitHub API on every monthly verification pass. Stars, ages and push dates are re-snapshotted; the main list only changes when a tool dies or a better one takes its place. See the [editorial standards](../README.md#-editorial-standards).*
