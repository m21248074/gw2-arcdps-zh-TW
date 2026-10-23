"""Shared helpers: parse official enum.c / default.c and the translation ini."""
import ast
import re
import sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    _s.reconfigure(encoding='utf-8', errors='replace')

ROOT = Path(__file__).resolve().parent.parent
OFFICIAL = ROOT / 'official'
SRC_INI = ROOT / 'lang' / 'zh-TW.ini'
DIST_INI = ROOT / 'dist' / 'arcdps_lang.ini'


def read_official():
    """Return {id: (key, english)} for every entry that has a default string."""
    num, cur = {}, -1
    for line in (OFFICIAL / 'enum.c').read_text(encoding='utf-8', errors='replace').splitlines():
        line = re.sub(r'/\*.*?\*/', '', line.split('//')[0]).strip()
        m = re.match(r'(LANG_\w+)\s*(?:=\s*(\d+))?\s*,?$', line)
        if m:
            cur = int(m.group(2)) if m.group(2) else cur + 1
            num[m.group(1)] = cur
    text = (OFFICIAL / 'default.c').read_text(encoding='utf-8', errors='replace')
    out = {}
    for m in re.finditer(r'lang\[(LANG_\w+)\]\s*=\s*("(?:[^"\\]|\\.)*"|0)\s*;', text):
        key, val = m.groups()
        text_val = '' if val == '0' else ast.literal_eval(val)
        if key in num and text_val:
            # the ini stores a newline as the two characters backslash + n
            out[num[key]] = (key, text_val.replace('\n', '\\n'))

    return out


def read_ini(path=SRC_INI):
    """Return ({id: text}, {id: text} for commented-out `;id=text` lines)."""
    active, commented = {}, {}
    for line in Path(path).read_text(encoding='utf-8').splitlines():
        m = re.match(r'^(;?)(\d+)=(.*)$', line)
        if m:
            (commented if m.group(1) else active)[int(m.group(2))] = m.group(3)
    return active, commented
