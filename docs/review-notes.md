# 審閱備忘

## 已確認

2026-10-23 確認下列條目的現行譯文可以,不需修改:

| 編號 | 官方英文 | 譯文 |
|---|---|---|
| 200 | Chat Stats | 聊天統計 |
| 240 | Chat Skills | 聊天技能 |
| 718 | Colours | 顏色 |
| 733 | stats | 統計 |
| 1044 | target bar | 目標長條 |
| 1045 | cleave bar | 範圍長條 |
| 1047 | hide zero buff columns | 隱藏增益為 0 的欄 |

`;1174=a` 以註解保留英文,與其他單字母縮寫的慣例一致。

## 保留的編號

以下 12 個編號在官方 `enum.c` 有定義,但 `default.c` 沒有預設字串,也沒有 `_DEFUNC` 標記,無法確認是否仍在使用,所以保留譯文:
130–132(SKILLS_TOTAL/H/F)、343、345(TGADPSOUT/IN)、376、377(DETAILS_PHYS/COND)、710(LOGSINVALID)、
781(SHOWADVANCEDFUNCOPTS_TOOLTIP)、782(DRAWCOMPAT)、785(SHOWTARGETINFO)、811(FONTSIZE_DEFAULT)。
另有被註解的 `;786`(TARGETINFOTARGET)同樣保留。

## 已移除

已棄用(`_DEFUNC`)的 19 條已於 2026-10-23 移除:138–140、147、370、373、382、522、543、691、830、878、902、963、1169–1172、1312。
