# gw2-arcdps-zh-TW

ArcDPS 繁體中文語言檔(`arcdps_lang.ini`)。

## 結構

| 路徑 | 說明 |
|---|---|
| `official/default.c`, `official/enum.c` | ArcDPS 官方語言來源,由 `scripts/fetch.py` 下載 |
| `lang/zh-TW.ini` | 譯文原始檔,UTF-8、LF,日常編輯與 `git diff` 都看這個 |
| `dist/arcdps_lang.ini` | 實際使用的檔案,UTF-16LE + BOM、CRLF,由 `scripts/build.py` 產生 |
| `scripts/check.py` | 檢查漏翻、佔位符(`@1`、`%s`、`\n`)是否一致、與英文相同的條目 |

## 流程

```
python scripts/fetch.py     # 更新官方來源,用 git diff official/ 看官方改了什麼
python scripts/check.py     # 找出漏翻與問題
# 編輯 lang/zh-TW.ini
python scripts/build.py     # 產生 dist/arcdps_lang.ini
```

把 `dist/arcdps_lang.ini` 放進遊戲的 `addons/arcdps/` 或與 `d3d11.dll` 同一資料夾。

以 `;編號=文字` 開頭的行是刻意跳過、保留英文的項目。

## 來源

- https://www.deltaconnected.com/arcdps/translations
- https://github.com/bluelovers/ws-gw2-arcdps
