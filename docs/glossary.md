# 術語表

`scripts/check.py` 會依 `docs/glossary.tsv` 檢查「應避免的寫法」(大陸用語、錯字、拼寫不一致),`--fix` 可自動套用。
下表是目前譯文實際採用的詞,以及還沒決定的項目。

## 已採用

| 英文 | 譯法 | 備註 |
|---|---|---|
| squad | 團隊 | 例:團隊統計、團隊日誌 |
| subgroup | 小隊 | 例:小隊顏色、置頂小隊 |
| party | 隊伍 | 只出現在 364、768 |
| window | 視窗 | ArcDPS 的視窗一律稱視窗;遊戲本身的面板(1328、1329)稱面板 |
| scroll / rolling | 捲動 / 滾動 | 畫面捲動用「捲動」;rolling(滾動式統計區間)用「滾動」 |
| condition | 症狀 | 與官方遊戲用語是否一致尚未確認,見下方待決定 |
| barrier | 屏障 | |
| defiance | 蔑視 | 例:蔑視條、CC 蔑視量 |
| crowd control | CC | 例:CC 次數、CC 時長 |
| minion | 召喚物 | |
| cleanse | 清除症狀 | 不與 strip 混用 |
| revive / revival / resurrect | 復活 | 例:復活觸發次數、復活時長、按 F 復活;不使用「救人」 |
| log(名詞) | 日誌 | 動詞或「紀錄行為」用「記錄」;「紀錄」一律寫「記錄」 |
| style | 樣式 | |
| filter | 篩選 | |
| extension | 擴充插件 | |
| buff | 增益 | 一律用「增益」,不留英文 Buff;與中文相連時不留空格,例:增益視窗、增益 ID |
| strip | 拔增益 | 例:拔增益、被拔增益;不再用「移除增益」 |
| condition | 症狀 | 簡中、繁中的 ArcDPS 社群譯本都用「症狀」;查不到官方繁中用語,「狀態」只用於 status(868、1249) |
| squad / subgroup | 團隊 / 小隊 | 同上,社群譯本一致;查不到官方繁中用語 |
| restart | 重新啟動 | 不使用「重啟」 |
| addon / extension | 外掛 / 擴充插件 | addon 指 ArcDPS 本身(1218「外掛模式」);extension 指其擴充,單獨的「插件」不使用 |
| 統計數值 / 一般資料 | 數據 / 資料 | 統計數值用「數據」;資料夾、詳細資料、ImGui 資料用「資料」 |
| profession / elite specialization | 職業 / 專業特化 | |
| relic | 古物 | 例:Relic of the Thief = 潛行者古物(1179);thief 一律用「潛行者」 |

## 待決定

目前沒有。若實測後發現遊戲內的繁中用語與上表不同(尤其是 condition、squad、subgroup),直接在 `docs/glossary.tsv` 加規則,再用 `python scripts/check.py --fix` 套用。
