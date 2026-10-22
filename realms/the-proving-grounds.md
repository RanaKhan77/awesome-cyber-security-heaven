# 🎯 The Proving Grounds

> **71 tools** · [← Back to the main list](../README.md) · Data verified **2026-10-22** (re-verified monthly)

## Curator's notes

Legal targets to practice on — vulnerable-by-design apps, CTF platforms, lab ranges. Practice targets are verified live before listing (dead practice apps are worse than none — they teach tool errors, not vulns).

## Maintenance snapshot (2026-10-22)

- **Active in the last 30 days:** 11 of 29 tracked GitHub repos (38%)
- **Quiet classics (no push in 12+ months, still listed):** Metasploitable 3, HEVD, APTSimulator, OWASP NodeGoat, flightsim
- **Earliest entries:** WackoPicko (2010), CryptOMG (2012)

## Flagship picks

| Tool | ★ Stars | Created | Last push | What it does |
|---|---|---|---|---|
| [Vulhub](https://github.com/vulhub/vulhub) | 21.4k | 2017 | 2026-10-17 ✅ | Pre-Built Vulnerable Environments Based on Docker-Compose |
| [OWASP Juice Shop](https://github.com/juice-shop/juice-shop) | 14.2k | 2014 | 2026-10-21 ✅ | OWASP Juice Shop: Probably the most modern and sophisticated insecure web application |
| [DVWA](https://github.com/digininja/DVWA) | 13.9k | 2013 | 2026-10-18 ✅ | Damn Vulnerable Web Application (DVWA) |
| [pwntools](https://github.com/Gallopsled/pwntools) | 13.8k | 2013 | 2026-10-21 ✅ | CTF framework and exploit development library |
| [WebGoat](https://github.com/WebGoat/WebGoat) | 9.4k | 2015 | 2026-10-19 ✅ | WebGoat is a deliberately insecure application |
| [GOAD](https://github.com/Orange-Cyberdefense/GOAD) | 8.5k | 2021 | 2026-03-12 | game of active directory |

## Full inventory (71 tools)

| Tool | ★ Stars | Created | Last push | License / tier |
|---|---|---|---|---|
| [Vulhub](https://github.com/vulhub/vulhub) | 21.4k | 2017 | 2026-10-17 ✅ | — dockerized vulnerable environments: spin up a CVE, test, tear down. Used by learners spinning up vulnerable environments with Docker; the free compose-file library of real CVE setups. (MIT) |
| [OWASP Juice Shop](https://github.com/juice-shop/juice-shop) | 14.2k | 2014 | 2026-10-21 ✅ | — the modern deliberately-vulnerable app with gamified challenges covering the whole OWASP spectrum. Used in corporate trainings and university courses; the de facto standard vulnerable app for web security practice. |
| [DVWA](https://github.com/digininja/DVWA) | 13.9k | 2013 | 2026-10-18 ✅ | — the classic Damn Vulnerable Web Application for safely learning injection basics. Used by instructors teaching web vulnerabilities for years; the classic PHP vulnerable app in every classroom lab. (GPL-3.0) |
| [pwntools](https://github.com/Gallopsled/pwntools) | 13.8k | 2013 | 2026-10-21 ✅ | — the CTF exploit-development library: from sockets to ROP chains, pwn everything. Used by CTF players and exploit developers writing exploits fast; the standard Python library for pwn challenges. |
| [WebGoat](https://github.com/WebGoat/WebGoat) | 9.4k | 2015 | 2026-10-19 ✅ | — OWASP's teaching app: guided lessons with a solution walkthrough for each vulnerability class. Used by Java teams and instructors learning web exploitation; the OWASP teaching app with lessons built in. (GPL-2.0) |
| [GOAD](https://github.com/Orange-Cyberdefense/GOAD) | 8.5k | 2021 | 2026-03-12 | — Game of Active Directory: a three-forest lab purpose-built for safely practicing AD attack techniques. Used by AD red-team trainees practicing real attack paths; the free Game of Active Directory lab commercial courses emulate. (GPL-3.0) |
| [CTFd](https://github.com/CTFd/CTFd) | 6.9k | 2015 | 2026-10-22 ✅ | — the CTF platform that powers thousands of events; self-host your own competition. Used by CTF organizers self-hosting competitions; the open-source platform behind thousands of events. |
| [Metasploitable 3](https://github.com/rapid7/metasploitable3) | 5.8k | 2016 | 2025-02-13 ⏳ | — Rapid7's purpose-built vulnerable target VM; the canonical Metasploit practice range. Used by pentest trainees practicing Metasploit workflows; the Rapid7-blessed free practice target. |
| [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat) | 3.8k | 2018 | 2026-10-14 ✅ | — Rhino Security's "vulnerable by design" AWS scenarios — deploy, attack, tear down. Used by cloud security learners practicing AWS attacks safely; Rhino Security's free vulnerable-by-design deployment. |
| [HEVD](https://github.com/hacksysteam/HackSysExtremeVulnerableDriver) | 3.1k | 2015 | 2025-02-24 ⏳ | — the Windows kernel-driver training target for exploit development. Used by kernel exploit developers learning Windows driver exploitation; the free HackSys training driver with documented vulns. (GPL-3.0) |
| [APTSimulator](https://github.com/NextronSystems/APTSimulator) | 2.8k | 2018 | 2025-09-23 ⏳ | — makes a Windows host look compromised so you can test detections safely. Used by blue teams generating APT-style artifacts for detection testing; the free Windows simulator for purple exercises. (MIT) |
| [Splunk Attack Range](https://github.com/splunk/attack_range) | 2.6k | 2019 | 2026-10-20 ✅ | — builds instrumented detection labs: attack, collect and test in one workflow. Used by detection engineers building full attack/defend labs in the cloud; the free Splunk range that emulates commercial cyber ranges. (Apache-2.0) |
| [OWASP NodeGoat](https://github.com/OWASP/NodeGoat) | 2.1k | 2013 | 2024-06-15 ⏳ | — the Node.js vulnerable-by-design app: the Top 10 in a controllable lab. Used by Node.js teams learning the OWASP Top 10 in their stack; the OWASP training app for JavaScript. (Apache-2.0) |
| [OWASP Mutillidae II](https://github.com/webpwnized/mutillidae) | 1.5k | 2018 | 2026-09-24 ✅ | — deliberately vulnerable app that re-creates every OWASP Top 10 issue, resettable per install. Used by teachers demonstrating nearly every OWASP vulnerability; the deliberately vulnerable training app. (GPL-3.0) |
| [flightsim](https://github.com/alphasoc/flightsim) | 1.4k | 2018 | 2024-04-04 ⏳ | — generates malicious network traffic for IDS/NDR validation; defender-side only. Used by defenders safely generating malicious-looking network traffic; the free attack simulator for testing detections. (CC-BY-4.0) |
| [DIVA Android](https://github.com/payatu/diva-android) | 1.2k | 2016 | 2023-05-19 ⏳ | — Damn Insecure and Vulnerable App: the Android training classic. Used by mobile security students learning Android flaw classes; the classic deliberately vulnerable Android app. (GPL-3.0) |
| [DVIA-v2](https://github.com/prateek147/DVIA-v2) | 1.1k | 2018 | 2024-03-29 ⏳ | — Damn Vulnerable iOS App v2: the mobile testing curriculum as an app. Used by iOS security learners practicing on Swift; the free deliberately vulnerable iOS app. (MIT) |
| [AzureGoat](https://github.com/ine-labs/AzureGoat) | 967 | 2022 | 2024-10-30 ⏳ | — the vulnerable-by-design Azure cloud lab. Used by cloud security learners practicing Azure attacks; the free vulnerable-by-design Azure lab. (MIT) |
| [DSVW](https://github.com/stamparm/DSVW) | 883 | 2015 | 2026-08-19 | — Damn Small Vulnerable Web: the Top 10 in ~100 lines of Python. Used by trainers demonstrating web flaws with a single Python file; the deliberately small vulnerable app. (public domain) |
| [Vulnerable Node](https://github.com/cr0hn/vulnerable-node) | 493 | 2016 | 2026-10-06 ✅ | — the Node.js vulnerable application for testing analysis tools. Used by Node.js teams auditing a realistic vulnerable app; the free Express-based training target. (MIT-style) |
| [DVWS (Web Sockets)](https://github.com/interference-security/DVWS) | 365 | 2017 | 2026-07-24 | — the vulnerable WebSocket app from Interference Security. Used by students practicing WebSocket-specific attacks; the vulnerable websockets lab. (MIT) |
| [0l4bs](https://github.com/tegal1337/0l4bs) | 355 | 2020 | 2021-06-02 ⏳ | — XSS practice labs with progressive difficulty. Used by students practicing SQLi, XSS and command injection individually; the free isolated labs per bug class. (GPL-3.0) |
| [WackoPicko](https://github.com/adamdoupe/WackoPicko) | 354 | 2010 | 2024-05-25 ⏳ | — the vulnerable app built for testing vulnerability scanners — a frozen-by-design calibration target for your tooling. Used by researchers and instructors demonstrating classic web flaws; the free academic vulnerable social network. |
| [lfi-labs](https://github.com/paralax/lfi-labs) | 335 | 2015 | 2024-04-08 ⏳ | — LFI/RFI/commix practice pages: one flaw family, many variants. Used by learners practicing local file inclusion safely; the free PHP lab for LFI classes. (MIT) |
| [Java Vulnerable Lab](https://github.com/CSPF-Founder/JavaVulnerableLab) | 278 | 2015 | 2026-10-09 ✅ | — the Java vulnerable web application from the CSPF crew. Used by Java developers learning exploitable patterns; the free vulnerable Java application. (GPL-2.0) |
| [DVHMA](https://github.com/logicalhacking/DVHMA) | 274 | 2015 | 2018-08-22 ⏳ | — the Damn Vulnerable Hybrid Mobile App: Android+iOS appsec in one codebase. Used by mobile security students practicing hybrid-app flaws; the vulnerable hybrid mobile app lab. (Apache-2.0) |
| [CryptOMG](https://github.com/SpiderLabs/CryptOMG) | 195 | 2012 | 2015-06-25 ⏳ | — cryptographic flaw testbed from SpiderLabs. Used by crypto learners attacking flawed implementations; the free crypto-focused challenge set. (GPL-3.0) |
| [damnvulnerable.me](https://github.com/skepticfx/damnvulnerable.me) | 34 | 2015 | 2019-05-19 ⏳ | — a modern vulnerable webapp for the OWASP Top 10 era. Used by mobile security students learning both Android and iOS flaws; the free vulnerable mobile apps. (MIT) |
| [SentinelTestbed](https://github.com/dobin/SentinelTestbed) | 11 | 2013 | 2016-11-18 ⏳ | — a testbed app for evaluating security instrumentation. Used by engineers testing detection content against a deliberately vulnerable host; the free detection-lab target. (GPL-3.0) |
|---|---|---|---|---|
| [Altoro Mutual](http://demo.testfire.net/) | — | — | — | — the classic demo bank: legal target for appsec training and tool demos. Used by security teams demoing scanners on a safe target; the classic IBM testfire-style demo banking site. (free service) |
| [Arizona Cyber Warfare Range](http://azcwr.org/az-cyber-warfare-ranges) | — | — | — | — free live-fire ranges for defenders and researchers. Used by learners attacking live-fire lab environments; the free volunteer-run range. (free service) |
| [bWAPP](http://www.itsecgames.com/) | — | — | — | — the "buggy web application" with 100+ vulnerability flavors — an old-school playground that still teaches. Used by instructors demonstrating 100+ web bug classes; the free buggy app for classroom labs. |
| [Crackmes.one](https://crackmes.one/) | — | — | — | — the reverse-engineering challenge community: thousands of crackmes, all legal. Used by reverse-engineering learners practicing on thousands of binaries; the free community crackme archive. (free service) |
| [CryptoHack](https://cryptohack.org/) | — | — | — | — learn modern cryptography by breaking it: challenges from classical ciphers to ECC. Used by learners leveling up applied cryptography; the free interactive challenge platform. |
| [Cryptopals](https://cryptopals.com) | — | — | — | — the legendary crypto challenges; finish them and AES is no longer magic. Used by engineers learning real-world cryptography; the free challenge set that trained a generation of crypto implementers. |
| [CTFlearn](https://ctflearn.com/) | — | — | — | — the beginner-friendly CTF platform with a permanent challenge set. Used by absolute beginners solving first flags; the free beginner-friendly CTF platform. (free service) |
| [CTFtime](https://ctftime.org) | — | — | — | — the global CTF calendar, team rankings and writeup index — the hub of the sport. Used by CTF teams tracking events and rankings worldwide; the free calendar of every serious competition. |
| [CyberDefenders](https://cyberdefenders.org/) | — | — | — | — blue-team CTF platform: investigate realistic incidents with the tools a SOC actually uses. Used by aspiring DFIR analysts practicing blue-team cases; the free DFIR CTF platform. (free tier) |
| [ExploitMe Mobile](http://securitycompass.github.io/AndroidLabs/index.html) | — | — | — | — the SecurityCompass mobile labs. Used by mobile security learners practicing iPhone and Android labs; the free mobile range. (free service) |
| [Firing Range](https://public-firing-range.appspot.com/) | — | — | — | — Google's XSS testbed: the original scanner benchmarking target. Used by XSS researchers testing payloads systematically; Google's free testbed for cross-site scripting classes. (Apache-2.0) |
| [Gandalf](https://gandalf.lakera.ai) | — | — | — | — Lakera's free prompt-injection game; learn AI-security attacks hands-on, level by level. Used by teams learning prompt injection hands-on; Lakera's free AI-security game. |
| [Google Gruyere](http://google-gruyere.appspot.com/) | — | — | — | — Google's cheese-themed vulnerable web app: exploit XSS, XSRF and information disclosure in the cloud. Used by beginners hunting their first web bugs; Google's free vulnerable-app tutorial. |
| [Hack The Box](https://www.hackthebox.com) | — | — | — | — the platform for ranked machines, pro labs and active-dir ranges; the industry's proving ground. Used by aspiring OSCP candidates and professional pentesters keeping sharp; the leading freemium training range. (free tier) |
| [Hack This Site](https://www.hackthissite.org/) | — | — | — | — the community wargames veteran: missions, articles and forums since the early 2000s. Used by a generation of learners starting out; the veteran free training community. |
| [Hackertest.net](http://www.hackertest.net/) | — | — | — | — the 20-level hacking simulation for web basics. Used by beginners playing a level-by-level web puzzle; the veteran free challenge series. (free service) |
| [HackThis](https://www.hackthis.co.uk/) | — | — | — | — 50+ levels of web security challenges, from basics to advanced. Used by beginners practicing across 50+ mission levels; the free UK challenge community. (free service) |
| [Hackxor](https://hackxor.net/) | — | — | — | — a realistic web-app hacking game with a story arc — WebGoat with sharper teeth. Used by aspiring web hackers playing a realistic first-person hacking game; the free browser-based range. |
| [LetsDefend](https://letsdefend.io/) | — | — | — | — browser-based SOC simulator: alert queues, playbooks and IR challenges mapped to MITRE ATT&CK. Used by aspiring SOC analysts simulating alert triage; the freemium blue-team range with realistic cases. (free tier) |
| [MASTG Crackmes](https://github.com/OWASP/mastg/tree/master/Crackmes) | — | — | — | — the mobile RE challenges companion to the OWASP MASTG. Used by mobile security learners practicing the OWASP MASTG on real targets; the free crackme suite. (CC-BY-SA-4.0) |
| [Microcorruption](https://microcorruption.com/) | — | — | — | — embedded-security CTF: reverse the lock firmware, level by level. Used by embedded security learners solving lock-firmware puzzles; the free embedded CTF from Matasano lineage. (free service) |
| [MysteryTwister C3](https://www.mysterytwisterc3.org/en/) | — | — | — | — the international cryptography challenge: from Caesar to quantum. Used by crypto enthusiasts solving graded cipher challenges; the free crypto CTF with legendary pedigree. (free service) |
| [OverTheWire](https://overthewire.org) | — | — | — | — Bandit and friends: learn Linux, networking and protocols through SSH wargames. Used by learners mastering Linux and security fundamentals; the classic free wargames every starter list recommends. |
| [OWASP iGoat](https://wiki.owasp.org/index.php/OWASP_iGoat_Tool_Project) | — | — | — | — the iOS learning app from the OWASP mobile family. Used by iOS security learners practicing on Objective-C; the OWASP deliberately vulnerable iOS app. (wiki project) |
| [Pentest-Ground](https://pentest-ground.com/) | — | — | — | — hosted practice playground of intentionally vulnerable apps for security testing. Used by testers practicing against free lab environments; the training range from the Netsparker lineage. (free service) |
| [picoCTF](https://picoctf.org) | — | — | — | — CMU's beginner-friendly CTF — the best first flag anyone can capture. Used by high-school and university students in CMU's free beginner CTF; the on-ramp for countless security careers. |
| [pwnable.kr](https://pwnable.kr/) | — | — | — | — the classic system-hacking wargame: exploit your way from userland to kernel. Used by exploit developers practicing binary pwn; the classic free challenge server. |
| [Reversing.kr](http://reversing.kr) | — | — | — | — the classic Korean reverse-engineering challenge site. Used by RE learners practicing Korean-style binary challenges; the classic free challenge site. (free service) |
| [RingZer0 CTF](https://ringzer0ctf.com/) | — | — | — | — hundreds of challenges across web, crypto, forensics and reversing. Used by learners solving web, crypto and coding challenges; the free online CTF platform. (free service) |
| [Root Me](https://www.root-me.org/) | — | — | — | — hundreds of real-world hacking challenges across dozens of categories, from web to stego. Used by French-speaking and international learners; the free platform with hundreds of hands-on challenges. (free tier) |
| [SmashTheStack](http://smashthestack.org/) | — | — | — | — the wargames network: shellcoding, exploitation and logic puzzles. Used by learners playing classic wargames like Amateria and Blowfish; the veteran free wargame community. (free service) |
| [SocketToMe](https://digi.ninja/projects/sockettome.php) | — | — | — | — Robin Wood's WebSocket testing challenge app. Used by learners practicing network socket exploitation; the free deliberately vulnerable service. (free service) |
| [techlogia Lab](https://techlogia.de/en/lab) | — | — | — | — free browser-based hacking lab for security training. Used by students practicing end-to-end web exploitation; the free vulnerable lab environment. (CC-BY-4.0) |
| [testasp.vulnweb.com](http://testasp.vulnweb.com/) | — | — | — | — the ASP demo target for scanner testing. Used by scanner developers and QA validating detection; Acunetix's free intentionally-vulnerable classic ASP test site. (free service) |
| [testaspnet.vulnweb.com](http://testaspnet.vulnweb.com/) | — | — | — | — the ASP.NET demo target for scanner testing. Used by scanner developers and QA validating detection; Acunetix's free intentionally-vulnerable ASP.NET test site. (free service) |
| [TryHackMe](https://tryhackme.com) | — | — | — | — guided rooms from your first command to advanced red/blue paths — the friendliest on-ramp. Used by newcomers learning security step by step; the guided-labs platform that made entry-level training free. (free tier) |
| [VulnHub](https://www.vulnhub.com) | — | — | — | — downloadable vulnerable VMs; build and break your own home lab offline. Used by students building offline home labs; the free vulnerable-VM library that replaced expensive lab hardware. |
| [Vulnserver](http://www.thegreycorner.com/2010/12/introducing-vulnserver.html) | — | — | — | — the TCP vulnerable server for exploit-dev practice. Used by exploit developers practicing buffer overflows and ROP; the standard free TCP exploitation trainer. (free service) |
| [W3Challs](https://w3challs.com) | — | — | — | — pentest training challenges with a ranking system. Used by learners practicing web, crypto and stego; the free challenge platform. (free service) |
| [WeChall](http://www.wechall.net/) | — | — | — | — the challenge-site aggregator: one profile across all major wargames. Used by CTF players tracking ranks across challenge sites; the free aggregator for wargame rankings. (free service) |
| [XSS Game](https://xss-game.appspot.com/) | — | — | — | — Google's XSS tutorial game: six levels from context basics to DOM tricks. Used by beginners learning XSS exploitation; Google's free reverse-engineering-free XSS CTF. (free service) |
| [Zero Bank](http://zero.webappsecurity.com/) | — | — | — | — demo banking site for web security exercises. Used by learners practicing web vulns on a simulated banking app; the free demo target behind Invicti training material. (free service) |

---
*This page is auto-audited from the GitHub API on every monthly verification pass. Stars, ages and push dates are re-snapshotted; the main list only changes when a tool dies or a better one takes its place. See the [editorial standards](../README.md#-editorial-standards).*
