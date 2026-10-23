"""Download the latest official default.c / enum.c into official/. Use `git diff official/` to see what changed."""
import urllib.request
from arcdps_lang import OFFICIAL

BASE = 'https://www.deltaconnected.com/arcdps/translations/'
for name in ('default.c', 'enum.c'):
    req = urllib.request.Request(BASE + name, headers={'User-Agent': 'Mozilla/5.0 (gw2-arcdps-zh-TW fetch.py)'})
    data = urllib.request.urlopen(req).read()
    (OFFICIAL / name).write_bytes(data)
    print(name, len(data), 'bytes')
