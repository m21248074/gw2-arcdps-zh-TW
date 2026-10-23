"""Print release notes (Markdown) for dist/arcdps_lang.ini. Usage: python scripts/release_notes.py <tag>"""
import hashlib
import sys

from arcdps_lang import DIST_INI, ROOT, read_ini, read_official

tag = sys.argv[1] if len(sys.argv) > 1 else 'dev'
official = read_official()
active, commented = read_ini()
data = DIST_INI.read_bytes()
compat = (ROOT / 'docs' / 'arcdps-version.txt').read_text(encoding='utf-8').strip()
covered = sum(1 for i in official if i in active or i in commented)

print(f'''ArcDPS 繁體中文語言檔 {tag},適用於《激戰 2》。

### 內容
- 涵蓋官方語言檔的全部 {covered}/{len(official)} 個字串({len(active)} 條已翻譯,其餘為單字母縮寫等刻意保留英文的項目)。
- 對應 ArcDPS 版本:{compat}
- 術語與遊戲內用語一致,詳見 `docs/glossary.md`。

### 安裝
1. 下載附件 `arcdps_lang.ini`。
2. 放在 ArcDPS 的 `d3d11.dll` 所在的資料夾。
3. 重新啟動遊戲。

此檔為 UTF-16LE(含 BOM),請勿用一般文字編輯器另存。要修改請改 `lang/zh-TW.ini` 後執行 `python scripts/build.py`。

### 檔案資訊
- `arcdps_lang.ini`:{len(data):,} bytes
- SHA-256:`{hashlib.sha256(data).hexdigest()}`

### 已知限制
- 少數字串寫死在 ArcDPS 內、不在官方語言檔裡(例如 `Local`、`show old messages`、`(!) some functionality is disabled`),無法透過語言檔翻譯,會維持英文。
- ArcDPS 更新後若新增字串,這些會暫時顯示英文,直到本專案跟進。
''')
