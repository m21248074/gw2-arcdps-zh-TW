# gw2-arcdps-zh-TW

[ArcDPS](https://www.deltaconnected.com/arcdps) 的繁體中文語言檔(`arcdps_lang.ini`),適用於《激戰 2》。

## 安裝

1. 下載 `dist/arcdps_lang.ini`。
2. 放在 ArcDPS 的 `d3d11.dll` 所在的同一個資料夾。
3. 重新啟動遊戲。

`dist/arcdps_lang.ini` 是 UTF-16LE(含 BOM)格式,這是 ArcDPS 要求的編碼,請不要用一般文字編輯器另存,否則會損壞。要修改請改 `lang/zh-TW.ini`,再用下面的方式重新產生。

## 專案結構

| 路徑 | 說明 |
|---|---|
| `lang/zh-TW.ini` | 譯文原始檔,UTF-8、LF。日常編輯與 `git diff` 都看這個 |
| `dist/arcdps_lang.ini` | 實際使用的檔案,UTF-16LE + BOM、CRLF,由 `scripts/build.py` 產生,**不要手改** |
| `official/default.c`、`official/enum.c` | ArcDPS 官方語言來源(英文預設與編號),由 `scripts/fetch.py` 下載 |
| `docs/glossary.md`、`docs/glossary.tsv` | 術語表。`.tsv` 是 `check.py` 會檢查的規則 |
| `docs/review-notes.md` | 審閱備忘:已確認的條目、保留的編號、已移除的棄用編號 |
| `scripts/` | `fetch.py`、`check.py`、`build.py`、`official_diff.py`、`release_notes.py` |

## 編輯流程

需要 Python 3.10 以上,沒有額外套件。

```
python scripts/fetch.py        # 更新官方來源;用 git diff official/ 看官方改了什麼
python scripts/check.py        # 檢查譯文
# 編輯 lang/zh-TW.ini
python scripts/check.py --fix  # 套用術語表的替換(可選)
python scripts/build.py        # 產生 dist/arcdps_lang.ini
```

`check.py` 會檢查:

- 格式損壞的行(不是空行、`;` 註解、`[lang]` 或 `編號=文字`)。
- 漏翻:官方有、譯文沒有的編號。
- 佔位符(`@1`、`%s` 等)是否與官方一致。
- 術語表裡「應避免的寫法」(大陸用語、`Buff`、`復活`/`救人` 混用等)。
- 英文相同卻譯法不同的條目(僅供參考)。

有漏翻、格式損壞、佔位符不一致或違反術語表時,結束碼為 1。

另外還會把 `dist/arcdps_lang.ini` 解碼回來,檢查 UTF-16LE 編碼、BOM、CRLF 換行,以及內容是否與 `lang/zh-TW.ini` 一致。

### 檔案格式

- 一行一條:`編號=譯文`。編號對應官方 `enum.c`。
- 譯文裡的換行寫成兩個字元 `\n`,**不要**輸入真正的換行。
- `;編號=文字` 表示刻意跳過、保留英文的項目(單字母縮寫等)。

## 官方更新

GitHub Actions 每週一會下載官方語言檔。有變動時會自動開一個 issue,列出新增、英文內容改動、已移除的字串(由 `scripts/official_diff.py` 產生),並附上目前譯文,方便你更新。
同一份官方檔案只會開一個 issue。處理完執行 `python scripts/fetch.py` 並提交 `official/`,下週就不會再報。

## 發佈

推一個 `v` 開頭的 tag,GitHub Actions 會自動檢查、建置,並建立**草稿** release、附上 `dist/arcdps_lang.ini`:

```
python scripts/check.py && python scripts/build.py   # 確認通過,且 dist/ 已提交
git tag v1.0.0
git push origin v1.0.0
```

到 GitHub 的 Releases 頁面檢查草稿內容,確認後再按 Publish。發佈說明由 `scripts/release_notes.py` 產生,
「對應 ArcDPS 版本」取自 `docs/arcdps-version.txt`,ArcDPS 更新並重新核對後請一併更新。

## 版本與來源

ArcDPS 與官方語言來源由 deltaconnected 製作:<https://www.deltaconnected.com/arcdps/translations>。
`official/` 底下的檔案屬於 ArcDPS 作者,放在這裡只是為了對照與比對更新,不在本專案的授權範圍內。

譯文參考:

- [Snowy1794/Arcdps-translation-Chinese-simplified](https://github.com/Snowy1794/Arcdps-translation-Chinese-simplified)
- [bluelovers/ws-gw2-arcdps](https://github.com/bluelovers/ws-gw2-arcdps)
- [lonelydragon0122 的翻譯整理](https://hackmd.io/@lonelydragon0122/HyFvmYIcU/%2FVl7TfXcSTHKm0ApagpplBQ)

## 授權

譯文與腳本以 [MIT License](LICENSE) 釋出。
