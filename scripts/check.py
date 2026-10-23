"""Check lang/zh-TW.ini against the official language table and docs/glossary.tsv.

    python scripts/check.py          report problems, exit 1 if there are any
    python scripts/check.py --fix    also apply the glossary replacements to lang/zh-TW.ini
"""
import re
import sys
from collections import defaultdict

from arcdps_lang import ROOT, SRC_INI, read_ini, read_official

GLOSSARY = ROOT / 'docs' / 'glossary.tsv'

PH = re.compile(r'@\d|%[-0-9.lL]*[a-zA-Z]')  # newlines are only line wraps, not compared


def ph(s):
    return sorted(PH.findall(s))


def read_glossary():
    rules = []
    for line in GLOSSARY.read_text(encoding='utf-8').splitlines()[1:]:
        if not line.strip():
            continue
        avoid, use, exempt, *_ = line.split('\t') + ['', '']
        ids = {int(x) for x in exempt.split(',') if x.strip()}
        rules.append((re.compile(avoid), use, ids))
    return rules


def apply_glossary(text, i, rules):
    for rx, use, exempt in rules:
        if i not in exempt:
            text = rx.sub(use, text)
    return text


rules = read_glossary()

if '--fix' in sys.argv:
    lines = SRC_INI.read_text(encoding='utf-8', newline='').split('\n')
    changed = 0
    for n, line in enumerate(lines):
        m = re.match(r'^(\d+)=(.*)$', line)
        if m:
            new = apply_glossary(m.group(2), int(m.group(1)), rules)
            if new != m.group(2):
                lines[n] = f'{m.group(1)}={new}'
                changed += 1
    SRC_INI.write_text('\n'.join(lines), encoding='utf-8', newline='')
    print(f'glossary: fixed {changed} lines')

official = read_official()
active, commented = read_ini()

missing = [(i, k, en) for i, (k, en) in sorted(official.items()) if i not in active and i not in commented]
skipped = [i for i in sorted(commented) if i in official]
unknown = [i for i in sorted(active) if i not in official]
same = [i for i in sorted(active) if i in official and active[i].strip() == official[i][1].strip()]
badph = [i for i in sorted(active) if i in official and ph(active[i]) != ph(official[i][1])]
badterm = [(i, active[i], apply_glossary(active[i], i, rules)) for i in sorted(active)
           if apply_glossary(active[i], i, rules) != active[i]]

by_en = defaultdict(lambda: defaultdict(list))
for i, zh in active.items():
    if i in official and len(official[i][1].strip()) > 1:
        by_en[official[i][1].strip().lower()][zh].append(i)
dup = {en: d for en, d in sorted(by_en.items()) if len(d) > 1}

print(f'official {len(official)} | translated {len(active)} | skipped(;) {len(skipped)}')
print(f'\n[missing] {len(missing)}')
for i, k, en in missing:
    print(f'  {i}\t{k}\t{en!r}')
print(f'\n[placeholder mismatch] {len(badph)}')
for i in badph:
    print(f'  {i}\n    en: {official[i][1]!r}\n    zh: {active[i]!r}')
print(f'\n[glossary: avoided terms] {len(badterm)}  (run with --fix to apply)')
for i, old, new in badterm:
    print(f'  {i}\n    now: {old}\n    fix: {new}')
print(f'\n[same English, different translation] {len(dup)}  (info only; often intentional)')
for en, d in dup.items():
    print(f'  {en[:40]!r}: ' + ' / '.join(f'{zh[:18]} {ids}' for zh, ids in d.items()))
print(f'\n[same as english] {len(same)}: {same}')
print(f'\n[id not in official default.c] {len(unknown)}: {unknown}')

sys.exit(1 if missing or badph or badterm else 0)
