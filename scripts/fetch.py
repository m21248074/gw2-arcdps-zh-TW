"""Download the latest official default.c / enum.c into official/. Use `git diff official/` to see what changed."""
import urllib.request
from arcdps_lang import OFFICIAL

BASE = 'https://www.deltaconnected.com/arcdps/translations/'
for name in ('default.c', 'enum.c'):
    data = urllib.request.urlopen(BASE + name).read()
    (OFFICIAL / name).write_bytes(data)
    print(name, len(data), 'bytes')
