# Legacy Vault — Archived Classics

> These nine tools are archived upstream but remain historically significant or widely referenced.
> The main list only carries actively maintained tools, so archived classics live here.
> [← Back to the main list](README.md) · Archive status verified **2026-10-22** via the GitHub API.

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
