# CLAUDE.md

ArcDPS 繁體中文語言檔。結構、流程、檔案格式見 `README.md`,術語見 `docs/glossary.md`。這裡只放容易踩到的地方。

## 修改譯文

- 只改 `lang/zh-TW.ini`(UTF-8、LF)。`dist/arcdps_lang.ini` 是 UTF-16LE + BOM + CRLF 的產物,**不要手改**,一律由 `python scripts/build.py` 產生。
- ini 裡的換行是兩個字元 `\n`(反斜線加 n)。用 shell heredoc 或 `python -c` 寫含反斜線的字串時,它會被轉成真正的換行,留下一行沒有編號的孤立文字(1267 出過這個問題)。含 `\n` 的修改請用編輯工具或腳本檔,改完跑 `check.py`,它會抓格式損壞的行。
- 翻譯以 `official/default.c` 的英文為準,並看 `official/enum.c` 的鍵名判斷它在介面的位置,不要沿用舊譯文的意思。保留 `@1`、`%s` 這類佔位符。
- 用詞先查 `docs/glossary.md`。新的統一規則寫進 `docs/glossary.tsv`(欄位:避免的寫法〔正規表示式〕、採用、例外編號、備註),再執行 `python scripts/check.py --fix`,不要逐條手改。遊戲內用語已確認:症狀、屏障、蔑視、團隊/小隊;relic 是「古物」,thief 是「潛行者」。
- 完成後 `python scripts/check.py` 必須通過(結束碼 0),再 `python scripts/build.py`,把 `dist/` 一起提交。

## 執行腳本

- 不要用 `python -I`:它會把腳本所在資料夾拿掉,同資料夾的 `arcdps_lang` 模組會找不到。
- Windows 終端機編碼是 cp950,輸出簡體字等字元可能報 `UnicodeEncodeError`。專案腳本已重設為 UTF-8;臨時腳本請自行處理。
- 需要 Python 3.10 以上,沒有第三方套件。

## Git

- 一個主題一個 commit,訊息寫明「為什麼」。結尾附 `Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>`。
- 不要自己 push、打 tag、建立 release、改寫已推上去的歷史。這些由使用者執行。
- `official/` 是 ArcDPS 作者的檔案,只用 `scripts/fetch.py` 更新,不要手改。
- 不要把 `d3d11.dll` 等第三方二進位檔放進倉庫(`.gitignore` 已排除 `*.dll`)。
