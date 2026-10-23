# 待確認的譯文

2026-10-23 逐條對照官方 `default.c` 時發現,以下條目與官方英文的語意可能不同,但無法僅從文字判斷,
需要對照遊戲內畫面。尚未修改。鍵名取自官方 `enum.c`。「建議譯文」是依官方英文直譯的提案,確認後再套用。

| 編號 | 鍵名 | 官方英文 | 目前譯文 | 疑點 | 建議譯文 |
|---|---|---|---|---|---|
| 136 | SKILLS_HITSCOMPRESS | hits (not-aoe) | 擊中(脈衝) | 「脈衝」與 not-aoe 不同 | 擊中(非範圍) |
| 200 | WINDOW_DPS_HEADER | Chat Stats | 個人統計 | 官方是 Chat(聊天輸出)統計 | 聊天統計 |
| 240 | WINDOW_SKILLS_HEADER | Chat Skills | 個人技能 | 同上 | 聊天技能 |
| 428 | WINDOW_LOG_CBTACTIVATION | activation | 戰鬥啟用 | 可能是「技能啟用」 | 技能啟用 |
| 506 | WINDOW_OPTIONS_SAVELOGS | save boss logs | 對目標保存戰鬥日誌 | 「目標」與 boss 的對應 | 儲存 Boss 日誌 |
| 542 | WINDOW_OPTIONS_OPENLOGSFOLDER | open | 開啟日誌的儲存目錄 | 官方只是按鈕上的「開啟」 | 開啟 |
| 697 | COMMON_LABELS | default title | 標籤 | 英文是「預設標題」 | 預設標題 |
| 718 | COMMON_SHOWADVANCEDSTYLEOPTSPREC | Colours | 載入時,設定檔(.ini)定義的顏色會優先使用 | 官方只有「顏色」 | 顏色 |
| 733 | COMMON_SORTSTATS | stats | DPS進階排序 | | 統計 |
| 762 | COMMON_OPTSTYLE_DATA | Data | 傷害統計顯示 | | 數據 |
| 794 | COMMON_BUFFTOTAL | buffs total | Buff 總計算時間 | | 增益總計 |
| 831 | COMMON_DODGEUPTIME | dodge uptime | 翻滾率 | 「覆蓋率」較貼近 uptime | 閃避覆蓋率 |
| 832 | COMMON_SORTADV_STRIPPERSIST | Strips | 移除增益平均值 | 「平均值」是否為 normalized | 拔增益 |
| 887 | | Unsupported | 不支持,不能使用 Shift | 比官方多出說明 | 不支援 |
| 922 | COMMON_OPTSHISTORICALINFO | Fights | 歷史記錄 | | 戰鬥 |
| 949 | | don't highlight selected player colour | 不要修改選擇的顏色 | | 不突顯所選玩家的顏色 |
| 1005 | COMMON_USEHITSBOSS | use hits boss | 被擊打 Boss | | 使用對 Boss 的擊中 |
| 1007 | | save instanced map logs | 每次切換地圖後儲存日誌 | 「副本地圖」被省略 | 儲存副本地圖日誌 |
| 1044 | COMMON_TARGETBAR | target bar | 不顯示目標總傷害條形圖 | 官方沒有「不顯示」 | 目標長條 |
| 1045 | COMMON_CLEAVEBAR | cleave bar | 不顯示範圍總傷害條形圖 | 同上 | 範圍長條 |
| 1174 | COMMON_TIMERANGEFULL_SHORT | a | f | 單字母縮寫,英文是 a | `;1174=a`(照慣例以 `;` 註解,保留英文) |
| 1267 | | Secondary target\nWill not start new logs but will be included in vs target stats | 次要目標 | 缺少第二行說明 | 次要目標\n不會開始新的日誌,但會計入 vs 目標統計 |

備註:
- 733、762 的鍵名不足以判斷畫面位置,建議譯文只是直譯;762 與 696(`Data` → 數據)對齊。
- 1044、1045 若遊戲中這兩項是「隱藏」類核取方塊,原譯文的「不顯示」可能是對的,建議看畫面再決定。
- 200、240 若實際是顯示在聊天輸出的視窗標題,「聊天統計」才正確;若是個人統計視窗,保留現狀。

以下 12 個編號在官方 `enum.c` 有定義,但 `default.c` 沒有預設字串,也沒有 `_DEFUNC` 標記,無法確認是否仍在使用,所以保留譯文:
130–132(SKILLS_TOTAL/H/F)、343、345(TGADPSOUT/IN)、376、377(DETAILS_PHYS/COND)、710(LOGSINVALID)、
781(SHOWADVANCEDFUNCOPTS_TOOLTIP)、782(DRAWCOMPAT)、785(SHOWTARGETINFO)、811(FONTSIZE_DEFAULT)。
另有被註解的 `;786`(TARGETINFOTARGET)同樣保留。

已棄用(`_DEFUNC`)的 19 條已於 2026-10-23 移除:138–140、147、370、373、382、522、543、691、830、878、902、963、1169–1172、1312。
