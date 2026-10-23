"""Compare official/ in the working tree (after fetch.py) with the committed version and print a Markdown report.

    python scripts/fetch.py && python scripts/official_diff.py
"""
import subprocess

from arcdps_lang import ROOT, parse_official, read_ini, read_official


def committed(name):
    out = subprocess.run(['git', 'show', f'HEAD:official/{name}'], cwd=ROOT, capture_output=True, check=True)
    return out.stdout.decode('utf-8', errors='replace')


def cell(text, limit=160):
    text = text.replace('|', '\\|').replace('\\n', ' ⏎ ')
    return text if len(text) <= limit else text[:limit] + '…'


old = parse_official(committed('enum.c'), committed('default.c'))
new = read_official()
active, commented = read_ini()

added = sorted(i for i in new if i not in old)
removed = sorted(i for i in old if i not in new)
changed = sorted(i for i in new if i in old and new[i][1] != old[i][1])
renamed = sorted(i for i in new if i in old and new[i][1] == old[i][1] and new[i][0] != old[i][0])

if not (added or removed or changed or renamed):
    print('官方語言檔的字串沒有變動(可能只有註解或格式不同)。')
    raise SystemExit(0)

print(f'官方語言檔有更新:新增 {len(added)}、改動 {len(changed)}、移除 {len(removed)}、改名 {len(renamed)}。\n')
print('更新步驟:`python scripts/fetch.py`,翻譯下列項目,`python scripts/check.py`,`python scripts/build.py`,提交。\n')

if added:
    print(f'### 新增的字串({len(added)}),需要翻譯\n')
    print('| 編號 | 鍵名 | 英文 |\n|---|---|---|')
    for i in added:
        print(f'| {i} | `{new[i][0].replace("LANG_", "")}` | {cell(new[i][1])} |')
    print()

if changed:
    print(f'### 英文內容改動的字串({len(changed)}),請檢查現有譯文是否仍然正確\n')
    print('| 編號 | 原英文 | 新英文 | 目前譯文 |\n|---|---|---|---|')
    for i in changed:
        print(f'| {i} | {cell(old[i][1])} | {cell(new[i][1])} | {cell(active.get(i, "(未翻譯)"))} |')
    print()

if removed:
    print(f'### 官方已移除的字串({len(removed)}),可從 `lang/zh-TW.ini` 刪除\n')
    print('| 編號 | 原英文 | 目前譯文 |\n|---|---|---|')
    for i in removed:
        print(f'| {i} | {cell(old[i][1])} | {cell(active.get(i, "(未翻譯)"))} |')
    print()

if renamed:
    print(f'### 只改了鍵名的字串({len(renamed)}),英文沒變\n')
    print(', '.join(f'{i}(`{old[i][0].replace("LANG_", "")}` → `{new[i][0].replace("LANG_", "")}`)' for i in renamed))
