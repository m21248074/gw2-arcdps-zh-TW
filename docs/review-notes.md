# 待實測確認的譯文

2026-10-23 逐條對照官方 `default.c` 與 `enum.c` 鍵名後,下列條目已依官方英文直譯,但鍵名無法確認它在畫面上的實際位置。
放進遊戲實測後,若發現不合適再調整。

| 編號 | 鍵名 | 官方英文 | 目前譯文 | 實測時要看什麼 |
|---|---|---|---|---|
| 200 | WINDOW_DPS_HEADER | Chat Stats | 聊天統計 | 若這是個人統計視窗的標題,改回「個人統計」 |
| 240 | WINDOW_SKILLS_HEADER | Chat Skills | 聊天技能 | 同上,改回「個人技能」 |
| 718 | COMMON_SHOWADVANCEDSTYLEOPTSPREC | Colours | 顏色 | 位於進階樣式的警告文字之後,看是否需要補充說明 |
| 733 | COMMON_SORTSTATS | stats | 統計 | 位置不明,看實際畫面 |
| 1044 | COMMON_TARGETBAR | target bar | 目標長條 | 後面接「不影響長條百分比計算」,可能是「不顯示」類選項,原譯文為「不顯示目標總傷害條形圖」 |
| 1045 | COMMON_CLEAVEBAR | cleave bar | 範圍長條 | 同上 |
| 1047 | COMMON_NOHIDEZEROBUFFS | hide zero buff columns | 隱藏增益為 0 的欄 | 鍵名帶 NO,方向可能相反,勾選後看實際效果 |

`;1174=a` 以註解保留英文,與其他單字母縮寫的慣例一致。

以下 12 個編號在官方 `enum.c` 有定義,但 `default.c` 沒有預設字串,也沒有 `_DEFUNC` 標記,無法確認是否仍在使用,所以保留譯文:
130–132(SKILLS_TOTAL/H/F)、343、345(TGADPSOUT/IN)、376、377(DETAILS_PHYS/COND)、710(LOGSINVALID)、
781(SHOWADVANCEDFUNCOPTS_TOOLTIP)、782(DRAWCOMPAT)、785(SHOWTARGETINFO)、811(FONTSIZE_DEFAULT)。
另有被註解的 `;786`(TARGETINFOTARGET)同樣保留。

已棄用(`_DEFUNC`)的 19 條已於 2026-10-23 移除:138–140、147、370、373、382、522、543、691、830、878、902、963、1169–1172、1312。
