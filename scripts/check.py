"""Report missing / unknown / unchanged / placeholder-mismatched entries in lang/zh-TW.ini."""
import re
from arcdps_lang import read_ini, read_official

official = read_official()
active, commented = read_ini()

PH = re.compile(r'@\d|%[-0-9.lL]*[a-zA-Z]|\\n')


def ph(s):
    return sorted(PH.findall(s))


missing = [(i, k, en) for i, (k, en) in sorted(official.items()) if i not in active and i not in commented]
skipped = [i for i in sorted(commented) if i in official]
unknown = [i for i in sorted(active) if i not in official]
same = [i for i in sorted(active) if i in official and active[i].strip() == official[i][1].strip()]
badph = [i for i in sorted(active) if i in official and ph(active[i]) != ph(official[i][1])]

print(f'official {len(official)} | translated {len(active)} | skipped(;) {len(skipped)}')
print(f'\n[missing] {len(missing)}')
for i, k, en in missing:
    print(f'  {i}\t{k}\t{en!r}')
print(f'\n[placeholder mismatch] {len(badph)}')
for i in badph:
    print(f'  {i}\n    en: {official[i][1]!r}\n    zh: {active[i]!r}')
print(f'\n[same as english] {len(same)}: {same}')
print(f'\n[id not in official default.c] {len(unknown)}: {unknown}')
