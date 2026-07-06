# Sync Log

記錄每次文件同步的內容與狀態。

---

## ❌ 待同步

| 專案 | 檔案 | 目標位置 | 備註 |
|------|------|---------|------|
| eManagerReport | 既有連結 | Notion eManagerReport 頁 | 補 SA 摘要（小項）|
| SBU Scorecard | （無設計文件，僅 SP） | Notion SBU 子頁已註明 | 待撰寫設計文件後再發 |
| TCP 改版 | BuildLog.md（6/9）| — | 待人工：屬建置「紀錄」非主要設計文件，是否發佈待定 |
| TCP 改版 | 同步舊版資料表.sql（6/9）| — | 待人工：SQL 位於改版根（非 03_DB_Migration），是否比照 DB 變更記錄發佈待定 |
| TCP 改版 | README.md（6/5）| — | 待人工：專案 README，一般不列入發佈集 |
| eManager 改版 | docs/Notion報表框架.html、Notion報表框架_vs_共用框架.html、SA與框架差異分析.html（6/17）| 未定 | 待人工：框架分析文件，發佈集是否納入、放 eManagerReport 還是新區待你定 |
| eManager 改版 | docs/補充內容_報表框架與首頁(給SA).md/.html（6/23）| 未定 | 待人工：供 SA 補入 Notion〈系統分析文件〉之框架/首頁設計補充；同屬上列框架文件群，placement 未定 |
| eManager 改版 | Notion/系統分析文件_最新_20260625.md（6/25 抓取）、docs/比對_補充內容vs Notion最新_20260625.md、比對與衝突解法_補充vsNotion_20260625.html、待補進Notion_對齊草稿_20260625.md（6/25）| 未定（Notion 回灌 / GitHub） | 待人工：補充內容 vs Notion 最新版逐段比對，浮現**七個待拍板衝突 C1–C7**（KPI 顏色模型/狀態態數/用詞/篩選器/小分類做法/布告欄記憶）；對齊草稿標【待拍板後定稿】。拍板＋placement 定後才能回灌 Notion。Obsidian 工作紀錄已寫 |
| eManager 改版 | docs/設定架構對照_首頁登錄vs報表內容_20260626.html、全框架對照_現行為主_差異標註_20260626.html（6/26）| 未定 | 待人工：給 SA 的現行 vs 改版框架對照；同屬框架文件群，placement 待定。Obsidian 工作紀錄已寫 |
| Budget Platform | BudgetPlatform_分析報告.html、OPTIMIZATION_PLAN.md（6/23）| 未定（GitHub/Notion）| 待人工：四層程式碼分析＋六階段優化計畫；含 SQL 注入確切位置(Repository.cs:2338、_RBU.cs:51/752/1033/1055)與缺 [Authorize] 端點，對外發佈敏感安全細節之取捨待 Hyman 定。Obsidian 工作紀錄已寫 |
| Budget Platform | 優化執行計畫.html、整體規劃流程.html、測試操作指南.html（6/23–6/24）| 未定（GitHub/Notion）| 待人工：前二者含安全弱點細節引用，併入 Budget Platform 對外待決集；Obsidian 工作紀錄已寫 |
| Budget Platform | 優化規劃_PM報告.html（6/25）| 未定（GitHub/Notion）| 待人工：PM 面向高階簡報，**不含敏感安全細節**，為 Budget Platform 對外待決集中最低風險、最適合先對外之候選；是否發佈仍待 Hyman 連同整體取捨決定。Obsidian 工作紀錄已寫 |
| Budget Platform | 年度改造_盤點清單.html（6/26，6/29 隨實作微調）| 未定（GitHub/Notion）| 待人工：動態年度／去分年度庫依賴範圍底稿（3 叢集 View/ETL SP/C#＋Snapshot+UNION 殼設計）。含程式碼物件名/行號但**無資安弱點細節**，仍歸 Budget Platform 對外待決集，待 Hyman 連同整體取捨決定。Obsidian 工作紀錄已寫 |
| Budget Platform | 年度改造_第一輪完成小結.html（6/29）| 未定（GitHub/Notion）| 待人工：3 張 Denodo View 動態年度+凍結快照改造**實際完成**（2 新表+2 新 SP+2 View flip 成 UNION 殼，零行為變化）。**無資安弱點細節**（僅 View/SP/表物件名與年度硬編），低風險；但第一輪未收尾（凍結 orchestrator/第二刀未做），仍歸對外待決集待 Hyman 連同整體取捨決定。Obsidian 工作紀錄已寫 |
| Budget Platform | 優化進度總覽.html（6/29）＋ 年度改造第二輪 ETL SP 年度參數化/synonym + 凍結 orchestrator 腳本（6/29~6/30）| 未定（GitHub/Notion）| 待人工：第二輪收尾叢集② ETL SP（@Year=NULL 自動推導+synonym 去分年度庫）與凍結 orchestrator。**無資安弱點細節**；SP 腳本屬程式碼不逐一發佈，HTML 為進度儀表板。整體年度改造對外發佈仍待 Hyman 連同整體取捨決定（第二刀多年度存取仍待答）。Obsidian 工作紀錄已寫 |
| eManager 改版 | 交付_Notion批改稿_20260701\（對照版/全文標註/摘要卡 HTML + Notion線上圖對照/圖片對照 HTML + Notion修改清單.xlsx + Notion現況vs需求規格書_差異報告.md，7/1）| 未定（回灌 Notion / GitHub） | 待人工：以需求規格書為格式基準、抓 Notion 6/30 現況（51 圖）逐段比對之批改稿交付包。**未直接修改線上 Notion**。待決策：結構方向 (A) 保留 Notion SA 格式補模組 /(B) 重整 9 模組 /(C) 併存；整模組缺失（匯出/申請權限/LOG/登入/權限管理/寄信）待補 SA 草稿；報表狀態四態 vs 兩態；是否由 AI 直接改線上 Notion 或先出對照稿。F1 篩選列已釐清為非衝突、D1 使用者已修。placement 未定。Obsidian 工作紀錄已寫 |
| Budget Platform | 待確認_Denodo用途問題.md（7/1）| 未定（外部確認）| 待人工：年度改造第二刀唯一缺的外部答案——Denodo 消費端是否有報表讀「已結案年度」`vw_BudgetPlatformCurrentData`，期望 (A) 送審當下固定值（＝現行凍結，符合）或 (B) 隨匯率重算即時值（需保留即時路徑）。**需向 Denodo 平台負責人（非本專案 C# 範圍）確認**。取得答案前第二刀不動、無風險。Obsidian 工作紀錄已寫 |
| eManager 改版 | 本次資料_Notion批改稿_20260706\（成品_給組員看＝內嵌圖自包含批改稿+修改清單xlsx；_編輯用＝來源HTML+build.py+51圖；7/6）| 未定（回灌 Notion / GitHub）| 待人工：7/1 批改稿包重整為乾淨交付結構（來源／成品分離、build.py 一鍵重生內嵌版、lightbox 不斷圖）＋批改稿新增 5 條共用元件建議（Last/Next Update 元件+API、切換角色模糊查詢共用元件、通知信共用寄信服務併 S6），合計 56 條批註。內容版本仍 7/1、**未直接修改線上 Notion**；結構方向 A/B/C、S1–S6 缺失模組補草稿、批改稿如何套用（手貼 vs AI 寫入）皆待拍板，placement 未定。Obsidian 工作紀錄已寫 |
| Budget Platform | 查證_MSU_Average除數疑點.md（7/1）| 未定（需業務拍板）| 待人工：`BudgetPlatformService.cs Get_BasicData` MSU 分支「當年平均前推」除數 bug（高信心）——case 10 應 `/9` 卻 `/11`、case 11 應 `/10` 卻 `/11`（case 12/13 正確）。**2026 循環 MSU FCST_Month=11 → case 11 正觸發 → Others 家族 Nov/Dec 預估目前實際低估約 9%**。**未自行修改**（動到已顯示/可能已據以編列的數字），待 Hyman 拍板 (a) 直接修正（改除實際月數）或 (b) 保留現狀僅記錄；若修正建議先跑修正前後 MSU 樣本 CC 比對。屬計算/業務邏輯問題，不對外發佈。Obsidian 工作紀錄已寫 |

> ℹ️ 完整盤點與已建結構見 `D:\Obsidian Note\專案盤點對照表.md`。
> 小項待補：eManagerReport 既有連結補 SA 摘要。（TCP 3 個舊 DB 連結 SA 已於 6/12 補齊）

---

## ✅ 已同步記錄

### 2026-07-06

> （本次排程於 2026-07-06 執行，掃到自 6/30 以來的落差＝7/1 產出的檔案 + 6/30 起待認證的 MSU push。）

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| eManager / MSU Scorecard | ATMC自動化_初版.html（E15 年月動態，commit `e9ee35a`）＋ SYNC_LOG 修正（`d0dc8ce`）| it-documents/msu-scorecard/功能模組/：**6/30 起待認證的 push 本次完成**——`git push` 成功 `7529d77..d0dc8ce main -> main`（credential 阻擋已排除），GitHub Pages 已發佈。Obsidian「開發記錄\MSU Scorecard.md」同步狀態更新為「E15 push 已完成」 |
| eManager 改版 / 框架 | Notion 批改稿交付包（7/1，交付_Notion批改稿_20260701\）| Obsidian「eManager Maintain Notes\開發記錄\eManager 改版框架與系統分析.md」新增「Notion 批改稿交付包（2026-07-01）」段＋修改歷程列＋待決策更新。GitHub/Notion 對外待人工（見待同步） |
| Budget Platform | 待確認_Denodo用途問題.md ＋ 查證_MSU_Average除數疑點.md（7/1）| Obsidian「Budget Platform Notes\Budget Platform 概覽.md」新增「待確認文件與 MSU 平均除數疑點（2026-07-01）」段＋修改歷程列＋同步狀態。對外/修正決策待人工（見待同步） |
| eManager 改版 / 框架 | 批改稿交付結構重整 ＋ 5 條共用元件建議（`本次資料_Notion批改稿_20260706\`，7/6 午後）| Obsidian「eManager Maintain Notes\開發記錄\eManager 改版框架與系統分析.md」新增「批改稿重整為交付結構 ＋ 共用元件建議（2026-07-06）」段＋修改歷程列（07/06）＋同步狀態更新至 7/6。GitHub/Notion 對外待人工（見待同步） |

> 本次（自動排程同步）掃 `D:\Work\專案` 比對三目的地，自 6/30 同步後落差為：(a) **MSU E15 的待認證 push 本次成功排除**（credential 阻擋解除，`e9ee35a`+`d0dc8ce` 已 push，GitHub Pages 發佈）；(b) eManager 改版 7/1 新增 Notion 批改稿交付包（對照 Notion 6/30 現況 vs 需求規格書，浮現結構 A/B/C 與整模組缺失，未改線上 Notion）→ Obsidian；(c) Budget Platform 7/1 兩份查證/待確認（Denodo 用途問題單、MSU `Get_BasicData` 除數 bug 查證）→ Obsidian。
> **7/6 午後追加一次掃描**：新增落差＝eManager 改版把 7/1 批改稿包重整為乾淨交付結構（`本次資料_Notion批改稿_20260706\`：成品/編輯用來源成品分離、build.py 一鍵重生內嵌圖版、lightbox 縮圖放大不斷圖）並在批改稿新增 5 條共用元件建議 🟢（Last/Next Update 元件+API、切換角色模糊查詢共用元件、通知信共用寄信服務併 S6，合計 56 條批註）；內容版本仍 7/1、**未改線上 Notion**。屬批改/待拍板材料（結構方向 A/B/C、S1–S6 補草稿、套用方式皆未定、placement 未定）→ 僅 Obsidian 工作紀錄，GitHub/Notion 列待人工。
> 本次唯一對外動作＝MSU E15 GitHub push（屬先前已 commit、僅待認證之主要設計文件改版）。eManager 批改稿（含 7/6 重整）與 Budget 兩份查證皆待拍板（結構方向／Denodo 外部答案／MSU 除數修正動到已顯示數字），故僅 Obsidian 工作紀錄，無其他 git push，Notion 均未動。

### 2026-06-30

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| eManager / MSU Scorecard | ATMC自動化_初版.html（**更新**：新增 E15 年月動態——SP `uSP_MSUScorecard2026_N_Data_TW` 由寫死 `@Year=2026,@Month=3` 改為 `@Year/@Month=NULL` 預設、不帶參數時以 `GETDATE()` 自動採當下年月；備份 `..bak_20260630`）| it-documents/msu-scorecard/功能模組/（**git commit `e9ee35a` 完成；push 待認證**——credential 解析問題，待 Hyman 重登後 `git push`，ahead 1）；Obsidian「開發記錄\MSU Scorecard.md」新增 06-30 E15 修改歷程列＋同步狀態。**Notion 暫不動**（E15 為執行方式調整、文件仍標「初版尚未正式啟用」，KPI/邏輯/資料未對既有系統說明實質變動；待 SP 正式上線拍板後再評估） |
| Budget Platform | 優化進度總覽.html + 年度改造第二輪（ETL SP 年度參數化/synonym + 凍結 orchestrator，6/29~6/30）| Obsidian「Budget Platform Notes\Budget Platform 概覽.md」新增「年度改造 第二輪」段＋修改歷程列＋同步狀態。GitHub/Notion 對外待人工（見待同步） |

> 本次（自動排程同步）掃 `D:\Work\專案` 比對三目的地，自 6/29 同步後落差為：(a) MSU 初版 `.md` 6/30 更新（E15 年月動態）→ 已重生 GitHub HTML（commit `e9ee35a`，**push 待認證**）+ Obsidian；(b) Budget Platform 6/29 晚~6/30 年度改造第二輪（ETL SP 年度參數化 + 凍結 orchestrator + 進度總覽 HTML）→ 對外待人工，僅 Obsidian 工作紀錄。
> MSU E15 唯一對外動作為 GitHub HTML 更新（屬主要設計文件改版），commit 已建但 push 受 credential 阻擋（同 6/25 前情形，待 Hyman 重登）；Notion 因系統仍 pre-production 且僅執行方式調整，暫不更新系統說明。Budget 第二輪無資安弱點細節但整體年度改造對外發佈待 Hyman 拍板，故無 git push（Budget 部分）。

### 2026-06-29

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| Budget Platform | 年度改造_第一輪完成小結.html（6/29，3 張 Denodo View 動態年度+凍結快照改造實際完成：2 新表+2 新 SP+2 View flip 成 UNION 殼，零行為變化 Prod==基準 0/0）＋盤點清單隨實作微調 | Obsidian「Budget Platform Notes\Budget Platform 概覽.md」新增「年度改造 第一輪完成（2026-06-29）」段＋修改歷程列＋同步狀態更新。GitHub/Notion 對外待人工（見待同步） |

> 本次（自動排程同步）掃 `D:\Work\專案` 比對三目的地，自 6/26 同步後唯一落差為 Budget Platform 6/29 兩份檔案（年度改造第一輪完成小結＝實作完成、盤點清單隨實作微調）。兩者對外（GitHub/Notion）發佈皆**待 Hyman 連同 Budget Platform 整體取捨拍板**，故本次實際同步動作僅 Obsidian 工作紀錄。無自動 git push。
> 完成小結無資安弱點細節（僅 View/SP/表物件名），低風險；但改造第一輪尚未收尾（凍結 orchestrator/第二刀多年度存取未做），系統行為仍在變動中，Notion 暫不更新系統說明（待收尾且 Hyman 拍板）。

### 2026-06-26

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| Budget Platform | 年度改造_盤點清單.html（6/26，動態年度／去分年度庫依賴範圍底稿：3 叢集＋Snapshot+UNION 殼設計） | Obsidian「Budget Platform Notes\Budget Platform 概覽.md」新增「年度改造盤點清單（2026-06-26）」段＋修改歷程列。GitHub/Notion 對外待人工（見待同步） |
| eManager 改版 / 框架 | 6/23 補充內容 + 6/25 比對·衝突解法·對齊草稿·系統分析抓取 + 6/26 兩份框架對照（彙整） | Obsidian「eManager Maintain Notes\開發記錄\eManager 改版框架與系統分析.md」**新建**：系統位置/原始文件/工作內容/七個待拍板衝突 C1–C7/Notion 仍缺清單/修改歷程/待人工。GitHub/Notion 因內容與 placement 均待拍板，列待人工 |

> 本次（自動排程同步）掃 `D:\Work\專案` 比對三目的地，落差全數落在 eManager 改版框架文件群與 Budget Platform —— 兩者對外（GitHub/Notion）發佈皆**待 Hyman 拍板**，故本次實際同步動作僅 Obsidian 工作紀錄（含新建 eManager 改版框架開發記錄）。無自動 git push。
> eManager 改版框架文件群（6/17~6/26 共 ~10 份）先前無任何 Obsidian 工作紀錄 → 本次補建彙整開發記錄，填補工作紀錄缺口。

### 2026-06-25

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| eManager / MSU Scorecard | ATMC自動化_初版.html（整合交接 + 新增 2026-06-25 E14 MOPEX-ES 拆分：拆 ES-SMT(LG09)/ES-Labor(LG10) + 新增 Hourly Rate-ES，0625-1 守恆驗收） | it-documents/msu-scorecard/功能模組/（GitHub 已推送 5ece429+5db97e7，2026-06-25 重登 HymanJiang 後成功） |
| eManager / MSU Scorecard | （Notion）子頁 SA 摘要 + GitHub 連結 | Notion MSU 子頁 `375b60a1-adfe-819d-a12a-eaacac3f4c68`：歸屬定案移入 eManager → 將「GitHub Pages 文件（待補連結）」placeholder 就地更新為交接 HTML 連結，並補 7 條 SA 摘要 bullets（範圍/改了什麼/為什麼/影響/E14/狀態） |
| eManager / MSU Scorecard | （工作紀錄）開發記錄更新 | Obsidian「eManager Maintain Notes\開發記錄\MSU Scorecard.md」：新增 06-25 E14 修改歷程列、ES 拆分與 Notion 歸屬兩項待確認標記為已解、補初版檔路徑與同步狀態 |
| Budget Platform | 優化規劃_PM報告.html（6/25，PM 高階簡報） | Obsidian「Budget Platform Notes\Budget Platform 概覽.md」補「PM 報告（2026-06-25）」段 + 修改歷程列（GitHub/Notion 對外待人工，見待同步） |

> MSU Scorecard 歸屬於 2026-06-25 定案（移入 eManager，Notion 子頁 `375b60a1-…`），原 6/24「Notion 待人工」項目已解除。
> 初版 HTML 接續 6/24 交接（後者仍在 GitHub Pages），兩者並存：交接＝交接快照、初版＝含 E14 整合設計文件。
> Budget Platform PM 報告不含敏感細節，但 GitHub/Notion 對外仍歸整體待決集，待 Hyman 定。

### 2026-06-24

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| eManager / MSU Scorecard | ATMC自動化_SP修正交接_20260624.html（ATMC 自動化 SP 修正交接：17 項 N+12 項未計算 → 修正 13 類 + 對照表 1 筆，0624-6 M03 驗收通過） | it-documents/msu-scorecard/功能模組/（GitHub Pages） |
| eManager / MSU Scorecard | （工作紀錄）開發記錄 | Obsidian「eManager Maintain Notes\開發記錄\MSU Scorecard.md」新建（系統位置/架構/修改歷程/待業務拍板/部署備忘） |
| Budget Platform | 優化執行計畫.html / 測試操作指南.html（6/23）＋ 整體規劃流程.html（6/24） | Obsidian「Budget Platform Notes\Budget Platform 概覽.md」補「後續產出」段＋修改歷程列 |

> MSU Scorecard SP 系列（uSP_MSUScorecard2026*.sql，6/24）屬程式碼，依發佈集規則不逐一發佈，已於交接文件說明。
> MSU Scorecard 尚無 Notion 子頁（歸屬「後續再定」），本次未自動建頁 → 列待人工。
> Budget Platform 三份新文件含敏感安全細節引用，對外（GitHub/Notion）發佈待 Hyman 決定，本次僅 Obsidian 工作紀錄。

### 2026-06-23

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| Budget Platform | BudgetPlatform_分析報告.html ＋ OPTIMIZATION_PLAN.md（6/23 四層程式碼分析＋六階段優化計畫） | Obsidian「Budget Platform Notes\Budget Platform 概覽.md」新增「程式碼分析與優化計畫（2026-06-23）」段＋修改歷程表（維運視角工作紀錄） |

> 本次 Obsidian 為唯一實際同步動作。GitHub/Notion 對外發佈因分析報告含敏感安全細節（SQL 注入確切位置、缺授權端點），列入「待同步／待人工」由 Hyman 決定。
> eManager 改版「補充內容_報表框架與首頁(給SA)」（6/23）屬框架文件群、placement 未定，亦列待人工。

### 2026-06-17

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| Budget Platform（新專案） | BudgetPlatform.html | it-documents/budget-platform/ ＋ Notion 新頁(SA 摘要+連結) ＋ Obsidian「Budget Platform Notes\Budget Platform 概覽.md」|
| TCP / eManager | （補同步 Obsidian） | TCP DB變更總覽、HC Dashboard 開發記錄寫入 Obsidian；台帳 Obsidian 欄補上 |

### 2026-06-16

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| eManager / HC Dashboard | ChangeLog.html（6/15+6/16 改版變更記錄） | it-documents/hc-dashboard/ ＋ Notion 子頁 ChangeLog SA 摘要（8 項）+連結 |
| eManager / HC Dashboard | （更新既有）Notion 子頁「待確認」block | ScorecardMap（原待 Amber）/CIS(AURES) 拆分/Total HC 來源/Operation budget rpt_type/Last Year HC 維度欄 等已解，移出待確認；剩 Turnover% 雙色、YTM 欄定義（待 Tina）|

> ChangeLog.md（2026-06-16 15:42 更新）為 HC Dashboard 改版的逐日設計變更記錄，屬「主要設計文件」→ 發佈。
> 同資料夾 SQL（sp_DSB_HC_New.sql、framework_HC_KPIFormat.sql、framework_HC_Dimensions.sql 等）屬程式碼/SP，依發佈集規則不逐一發佈，已於 ChangeLog SA 摘要提及。
> 來源檔：`D:\Work\專案\eManager\HC Dashboard\ChangeLog.md`。

### 2026-06-15

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| eManager / HC Dashboard | 名稱對齊_KPI.html | it-documents/hc-dashboard/ ＋ Notion 子頁連結+SA 摘要 |
| eManager / HC Dashboard | 名稱對齊_Hierarchy.html | it-documents/hc-dashboard/ ＋ Notion 子頁連結+SA 摘要 |
| eManager / HC Dashboard | （更新既有）Notion 子頁「待確認」block | AURES 保留、Operation Turnover% IDL/DL 分母已確認 → 移出待確認、補新待評估 |

> 兩份 worksheet 為 6/12 設計同步後當天新增（13:29 / 13:40），故當次未涵蓋，本次補上。
> 來源檔：`D:\Work\專案\eManager\HC Dashboard\名稱對齊_KPI.md`、`名稱對齊_Hierarchy.md`。

### 2026-06-12

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| TCP 改版 | DB_Migration_Currency.html | it-documents/tcp/DB變更記錄/ ＋ Notion 連結+SA 摘要 |
| TCP 改版 | DB_Migration_History_Tables.html | 同上 |
| TCP 改版 | DB_View_Quota_By_SalesId.html（合併重複的 DB_View_Quota.sql） | 同上 |
| TCP 改版 | DB_View_Quota_Salesperson.html | 同上 |
| TCP 改版 | 需求確認書 v1.1（12 項確認） | Notion TCP 頁就地更新（版本行+清單標題+12 問題→✅結論）|
| eManager | （結構）eManager 總頁 + 模組子頁 | Notion：eManagerReport/OSF 移入，新建 HC Dashboard/My Sales Force/SBU |
| eManager / HC Dashboard | 改版設計_HC_Dashboard.html | it-documents/hc-dashboard/ ＋ Notion 子頁 SA 摘要 |
| eManager / My Sales Force | My_Sales_Force_規格文件.html | it-documents/my-sales-force/ ＋ Notion 子頁 SA 摘要 |
| eManager / OSF | OSF_Commerce_Analysis.html | it-documents/osf-commerce-insights/功能模組/ ＋ Notion 子頁 SA 摘要 |
| TCP 改版 | TcpPlatform_建置說明.html | it-documents/tcp/功能開發/ ＋ Notion TCP 頁連結 |
| TCP 改版 | TCP_Upload_SOP_Examples.html | it-documents/tcp/功能開發/ ＋ Notion TCP 頁連結 |

> 源檔重複提醒：`DB_View_Quota.sql` 與 `DB_View_Quota_By_SalesId.sql` 內容相同，建議擇一保留。

---

## ✅ 已同步記錄（更早）

### 2026-06-08

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| TCP 改版 | DB_Migration_OrgHierarchy.html | it-documents/tcp/DB變更記錄/ ＋ Notion TCP 頁（DB 變更記錄）連結 |
| TCP 改版 | DB_Migration_FOB_Columns.html | it-documents/tcp/DB變更記錄/ ＋ Notion TCP 頁連結 |
| TCP 改版 | DB_Migration_Template_Redesign.html | it-documents/tcp/DB變更記錄/ ＋ Notion TCP 頁連結 |
| eManagerReport | 實作做法.html | it-documents/emanager-report/功能模組/ ＋ Notion eManagerReport 頁連結 |

> 備註：eManagerReport.md 先前已以 eManagerReport.html（6/4）發佈並於 Notion 功能模組加連結，視為已涵蓋。

### 2026-06-04

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| TCP 改版 | TCP獎金平台_系統設計文件.html | it-documents/tcp/需求與規格/ |
| TCP 改版 | TCP獎金平台_設定規格說明.html | it-documents/tcp/需求與規格/ |
| TCP 改版 | TCP獎金平台_設定簡化分析.html | it-documents/tcp/需求與規格/ |
| TCP 改版 | TCP_Platform_系統架構文件.html | it-documents/tcp/功能開發/ |
| TCP 改版 | TCP_Platform_操作指南.html | it-documents/tcp/功能開發/ |
| TCP 改版 | TCP_Salesperson_Config_QA.html | it-documents/tcp/功能開發/ |
| TCP 改版 | TCP獎金平台_QA測試記錄.html | it-documents/tcp/功能開發/ |
| TCP 改版 | TCP獎金平台_上傳檔案說明.html | it-documents/tcp/功能開發/ |
| TCP 改版 | TCP獎金平台_設定指南.html | it-documents/tcp/功能開發/ |
| TCP 改版 | TCP_Platform_需求確認書.md | Notion TCP 頁面（需求與規格） |
| eManagerReport | eManagerReport.html | it-documents/emanager-report/功能模組/ |
| eManagerReport | 功能清單.html | it-documents/emanager-report/功能模組/ |
| eManagerReport | 功能清單_SA.html | it-documents/emanager-report/功能模組/ |
| eManagerReport | 功能清單_User.html | it-documents/emanager-report/功能模組/ |
| OSF Commerce Insights | OSF_CommerceInsights_ChangeLog.md | Notion OSF 頁面（Change Log） |
