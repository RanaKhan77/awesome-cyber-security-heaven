#!/usr/bin/env python3
"""W160 heaven: add csprecon + sitedorks to the Cartographers realm (verified
active 2026-11-25: pushed 2026-11-24 / 2026-11-23, licenses MIT / GPL-3.0,
both adopted into the 2MNY system this session). Run on server in /root/heaven
on the main branch. Counts: realm 142->144, README census 1421->1423 (x2)."""

results = []

def edit(path, old, new, label):
    s = open(path, encoding="utf-8").read()
    if new in s and old not in s:
        results.append((label, "ALREADY"))
        return
    if old not in s:
        results.append((label, "ANCHOR-MISSING"))
        return
    open(path, "w", encoding="utf-8").write(s.replace(old, new, 1))
    results.append((label, "OK"))

R = "README.md"
C = "realms/the-cartographers.md"

CSPRECON_ROW = (
    "| [csprecon](https://github.com/edoardottt/csprecon) | 569 | 2022 | 2026-11-25 ✅ | "
    "— discover new target domains from Content-Security-Policy headers: fetch a page, parse every "
    "script-src/connect-src/img-src origin, and grow the scope from what the site itself declares "
    "it trusts. Used by bug bounty hunters expanding in-scope host lists from CSP data they already "
    "collect; the one-command CSP-to-scope recon tool from edoardottt. (MIT) |\n"
)
SITEDORKS_ROW = (
    "| [sitedorks](https://github.com/Zarcolio/sitedorks) | 1.1k | 2020 | 2026-11-25 ✅ | "
    "— search Google, Bing, Brave, Ecosia, Yahoo or Yandex across 638 dorkable sites in one command, "
    "from a CSV you can edit per engagement and split into per-category queries. Used by bug bounty "
    "hunters running site-scoped dork sweeps without pasting URLs one by one; the maintained "
    "multi-engine dork launcher. (GPL-3.0) |\n"
)

# --- realm: count + two rows after the findomain row ---
edit(C, "## Full inventory (142 tools)", "## Full inventory (144 tools)", "cartographers-count")
s = open(C, encoding="utf-8").read()
anchor = s.find("| [findomain](https://github.com/Findomain/Findomain)")
if anchor >= 0 and "csprecon" not in s:
    j = s.find("\n", anchor) + 1
    s = s[:j] + CSPRECON_ROW + s[j:]
    open(C, "w", encoding="utf-8").write(s)
    results.append(("cartographers-csprecon", "OK"))
elif "csprecon" in s:
    results.append(("cartographers-csprecon", "ALREADY"))
else:
    results.append(("cartographers-csprecon", "ANCHOR-MISSING"))

s = open(C, encoding="utf-8").read()
if "sitedorks" not in s:
    # insert after the new csprecon row if present, else after findomain
    anchor = s.find("| [csprecon](https://github.com/edoardottt/csprecon)")
    if anchor < 0:
        anchor = s.find("| [findomain](https://github.com/Findomain/Findomain)")
    if anchor >= 0:
        j = s.find("\n", anchor) + 1
        s = s[:j] + SITEDORKS_ROW + s[j:]
        open(C, "w", encoding="utf-8").write(s)
        results.append(("cartographers-sitedorks", "OK"))
    else:
        results.append(("cartographers-sitedorks", "ANCHOR-MISSING"))
else:
    results.append(("cartographers-sitedorks", "ALREADY"))

# --- README: census counts (2 places) ---
edit(R, "**2026 edition** — 1421 tools", "**2026 edition** — 1423 tools", "readme-count-line")
edit(R, "🧭 **1421 curated tools**", "🧭 **1423 curated tools**", "readme-compass")

# --- README: bullet entries in the Cartographers section (after urlfinder bullet) ---
s = open(R, encoding="utf-8").read()
if "csprecon" not in s:
    anchor = s.find("- [urlfinder](https://github.com/projectdiscovery/urlfinder)")
    if anchor >= 0:
        j = s.find("\n", anchor) + 1
        bullet = (
            "- [csprecon](https://github.com/edoardottt/csprecon) - Discover new target domains from "
            "Content-Security-Policy headers: every script-src/connect-src origin on a page becomes a "
            "scope candidate in one command. Used by bug bounty hunters expanding in-scope host lists "
            "from CSP data they already collect; the CSP-to-scope recon tool from edoardottt. (MIT)\n"
        )
        s = s[:j] + bullet + s[j:]
        open(R, "w", encoding="utf-8").write(s)
        results.append(("readme-csprecon-bullet", "OK"))
    else:
        results.append(("readme-csprecon-bullet", "ANCHOR-MISSING"))
else:
    results.append(("readme-csprecon-bullet", "ALREADY"))

s = open(R, encoding="utf-8").read()
if "sitedorks" not in s:
    anchor = s.find("- [csprecon](https://github.com/edoardottt/csprecon)")
    if anchor < 0:
        anchor = s.find("- [urlfinder](https://github.com/projectdiscovery/urlfinder)")
    if anchor >= 0:
        j = s.find("\n", anchor) + 1
        bullet = (
            "- [sitedorks](https://github.com/Zarcolio/sitedorks) - Search Google, Bing, Brave, Ecosia, "
            "Yahoo or Yandex across 638 dorkable sites in one command, driven by an editable CSV with "
            "categories. Used by bug bounty hunters running site-scoped dork sweeps without pasting "
            "URLs one by one; the maintained multi-engine dork launcher. (GPL-3.0)\n"
        )
        s = s[:j] + bullet + s[j:]
        open(R, "w", encoding="utf-8").write(s)
        results.append(("readme-sitedorks-bullet", "OK"))
    else:
        results.append(("readme-sitedorks-bullet", "ANCHOR-MISSING"))
else:
    results.append(("readme-sitedorks-bullet", "ALREADY"))

for label, st in results:
    print(label, "=>", st)
ok = all(st in ("OK", "ALREADY") for _, st in results)
print("ALL-OK" if ok else "HAS-MISSING-ANCHORS")
