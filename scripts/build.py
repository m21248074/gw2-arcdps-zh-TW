"""lang/zh-TW.ini (UTF-8, LF) -> dist/arcdps_lang.ini (UTF-16LE + BOM, CRLF)."""
from arcdps_lang import ROOT, SRC_INI, DIST_INI

text = SRC_INI.read_text(encoding='utf-8').replace('\r\n', '\n').replace('\n', '\r\n')
DIST_INI.parent.mkdir(exist_ok=True)
DIST_INI.write_bytes(b'\xff\xfe' + text.encode('utf-16-le'))
print('wrote', DIST_INI.relative_to(ROOT), DIST_INI.stat().st_size, 'bytes')
