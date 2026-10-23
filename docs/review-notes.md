# 待確認的譯文

2026-10-23 逐條對照官方 `default.c` 時發現,以下條目與官方英文的語意可能不同,但無法僅從文字判斷,
需要對照遊戲內畫面。尚未修改。鍵名取自官方 `enum.c`。

| 編號 | 鍵名 | 官方英文 | 目前譯文 | 疑點 |
|---|---|---|---|---|
| 136 | SKILLS_HITSCOMPRESS | hits (not-aoe) | 擊中(脈衝) | 「脈衝」與 not-aoe 不同 |
| 200 | WINDOW_DPS_HEADER | Chat Stats | 個人統計 | 官方是 Chat(聊天輸出)統計 |
| 240 | WINDOW_SKILLS_HEADER | Chat Skills | 個人技能 | 同上 |
| 428 | WINDOW_LOG_CBTACTIVATION | activation | 戰鬥啟用 | 可能是「技能啟用」 |
| 506 | WINDOW_OPTIONS_SAVELOGS | save boss logs | 對目標保存戰鬥日誌 | 「目標」與 boss 的對應 |
| 542 | WINDOW_OPTIONS_OPENLOGSFOLDER | open | 打開日誌的保存目錄 | 官方只是按鈕上的「開啟」 |
| 697 | COMMON_LABELS | default title | 標籤 | 英文是「預設標題」 |
| 718 | COMMON_SHOWADVANCEDSTYLEOPTSPREC | Colours | 載入時,配置文件(.ini)定義的顏色會優先使用 | 官方只有「顏色」 |
| 733 | COMMON_SORTSTATS | stats | DPS進階排序 | |
| 762 | COMMON_OPTSTYLE_DATA | Data | 傷害統計顯示 | |
| 794 | COMMON_BUFFTOTAL | buffs total | Buff 總計算時間 | |
| 831 | COMMON_DODGEUPTIME | dodge uptime | 翻滾率 | 「覆蓋率」較貼近 uptime |
| 832 | COMMON_SORTADV_STRIPPERSIST | Strips | 移除增益平均值 | 「平均值」是否為 normalized |
| 887 | | Unsupported | 不支持,不能使用 Shift | 比官方多出說明 |
| 922 | COMMON_OPTSHISTORICALINFO | Fights | 歷史記錄 | |
| 949 | | don't highlight selected player colour | 不要修改選擇的顏色 | |
| 1005 | COMMON_USEHITSBOSS | use hits boss | 被擊打 Boss | |
| 1007 | | save instanced map logs | 每次切換地圖後保存日誌 | 「副本地圖」被省略 |
| 1044 | COMMON_TARGETBAR | target bar | 不顯示目標總傷害條形圖 | 官方沒有「不顯示」 |
| 1045 | COMMON_CLEAVEBAR | cleave bar | 不顯示範圍總傷害條形圖 | 同上 |
| 1174 | COMMON_TIMERANGEFULL_SHORT | a | f | 單字母縮寫,英文是 a |
| 1267 | | Secondary target\nWill not start new logs but will be included in vs target stats | 次要目標 | 缺少第二行說明 |

另有 31 個編號在官方 `default.c` 沒有對應字串(多為已棄用的 `_DEFUNC` 項目),留在檔案中無害:
130–132、138–140、147、343、345、370、373、376、377、382、522、543、691、710、781、782、785、811、830、878、902、963、1169–1172、1312。
