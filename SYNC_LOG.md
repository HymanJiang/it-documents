# Sync Log

記錄每次文件同步的內容與狀態。

---

## ❌ 待同步

| 專案 | 檔案 | 目標位置 | 備註 |
|------|------|---------|------|
| eManagerReport | 既有連結 | Notion eManagerReport 頁 | 補 SA 摘要（小項）|
| eManager / OSF Commerce Insights | 第七次修改（7/17 KPI 邏輯）＋ 第六次修改（6/11 Store 資料權限） | Notion OSF Commerce Insights 頁（`375b60a1-adfe-81c2-be42-dee5db09e9fc`）| **待人工／待連線**：2026-07-17 排程執行時 Notion **certificate signature failure 無法連線**，Notion 部分停做。**系統本身確有變、應更新**：① 📊 衡量指標與計算邏輯段 → 補 O2S/S2A/A2C/C2R 之 **AVG** YTM 規則與 **Freight Fee %**＝`SUM(Freight Act. ($)) / (SUM(CurrentYear Achv. (K)) * 1000)`（比例存放、前端 ×100 顯示、DecimalPlaces=3）；② 🧩 功能與資料段 → 補**第六次（6/11）Store 資料權限**（權限維度 Region→Store、報表專屬表 `OSF_CommerceInsightsPermission` 讀 `HierarchyName='Store'`、`'ALL'`＝看全部）；③ 🔗 相關文件 → 加 ChangeLog.html 連結（GitHub 已發佈）。下次連線恢復時處理 |
| eManager / OSF Commerce Insights | `eManagerCore` `develop` commit `0621048`（6 files，第六次修改 C# 變更） | — | 待人工：ChangeLog 自載「**尚未 push**」（紀錄時點 6/11），現況待查——若仍未 push 則 Store 權限功能未進遠端 |
| Budget Platform | `2026H2優化\進度總覽_已完成與待執行.html`（7/17） | 未定（GitHub/Notion）| 待人工：H2 進度儀表板（已完成/待執行對照），屬日誌性質、無資安弱點細節；同歸 Budget Platform 對外待決集，待 Hyman 取捨。Obsidian 工作紀錄已寫 |
| eManager / HC Dashboard | SBU Hierarchy 改版（7/7，31→38 列＋7 Rollup＋重寫 Revenue 對應）| Notion HC Dashboard 子頁 | 待人工：結構性資料/維度變更已 COMMIT，惟 **SBU Total/小計 Revenue 策略（直抓 vs 抓不到退回加總）未定** + **6 個群組 PG 是否存在於 `SCORECARD_PROD_N` 待核對來源**；策略拍板＋來源確認後，再更新 🧩 功能與資料段（維度/資料表）與 📊 衡量指標段。GitHub ChangeLog.html 已更新，Obsidian 已記 |
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
| Budget Platform | 第二刀 多年度存取（設計_多年度存取.md + 部署_vw_*_History.sql，7/8）| 未定（GitHub/Notion）| ✅**閘已清**：Denodo 用途問題（7/1 待確認）設計文件記載**已答 (A) 固定值（2026-07-08）** → 第二刀可部署（新增 `vw_BudgetPlatformCurrentData/BudgetData_History`，純新增撤銷=DROP）。**GitHub/Notion 對外仍待人工**（歸 Budget Platform 整體對外待決集）。⚠️ `待確認事項\README.md` 表格狀態欄仍標「⬜ 待回覆」與設計文件（已答 A）不一致，請 Hyman 留意。Obsidian 工作紀錄已寫 |
| eManager 改版 | 本次資料_Notion批改稿_20260706\（成品_給組員看＝內嵌圖自包含批改稿+修改清單xlsx；_編輯用＝來源HTML+build.py+51圖；7/6）| 未定（回灌 Notion / GitHub）| 待人工：7/1 批改稿包重整為乾淨交付結構（來源／成品分離、build.py 一鍵重生內嵌版、lightbox 不斷圖）＋批改稿新增 5 條共用元件建議（Last/Next Update 元件+API、切換角色模糊查詢共用元件、通知信共用寄信服務併 S6），合計 56 條批註。內容版本仍 7/1、**未直接修改線上 Notion**；結構方向 A/B/C、S1–S6 缺失模組補草稿、批改稿如何套用（手貼 vs AI 寫入）皆待拍板，placement 未定。Obsidian 工作紀錄已寫 |
| Budget Platform | 查證_MSU_Average除數疑點.md（7/1）→ **已在 C# 分支修正（7/8）**| 未定（C# push）| 進度更新：MSU「當年平均前推」除數 bug（case 10/11 應 `/9`·`/10` 卻 `/11`）已於年度改造結案 C# 分支 `feature/budget-optimization` **修正（#3，部署碼用 `/10`，probe 驗證低估精確 9.09%）**——即採決策 (a) 直接修正。**分支維持本地、未 push（使用者決定）**；測試檔 `Fcst_MSU_DivisorProbeTests.cs` 未追蹤。待人工＝C# push/PR 時機。屬計算/業務邏輯，不對外發佈。Obsidian 工作紀錄已寫 |
| SBU Scorecard | uSP_SBUScorecard2026.sql（7/10，NRE-ADM6 MType 正規化）| —（無設計文件）| 待人工：`uSP_SBUScorecard2026` 加一段——2026/6 來源單據 `NRE-ADM6` 的 `MType` 誤設 `ZFIN`(FACT=3)，於 `#tmpITPDetail` 正規化為 `ZSRV`，使下游 8 處 `part LIKE '%NRE%' AND MType='ZSRV'` 的 NRE 判斷落 NRE 桶（來源修正後影響 0 列）。**SP-only、無設計文件、無對應 Obsidian vault**，依發佈集規則不發佈；歸屬／是否建記錄待人工。|
| Budget Platform | 預算匯率自維 開工/實作（設計_預算匯率自維.md 更新 + 部署/補資料/還原 SQL，7/13）| 未定（GitHub/Notion）| 待人工：7/9 設計轉入實作。⓪ **BRL 補列已寫入正式 `Budget_PlanRate`**（`步驟0_補BRL_LinkedServer.sql`，補 2 列 USD/EURO type=5.70、驗證 0 列、附還原檔；⚠️②部署後需冪等重跑）；① 後台 Plan Rate 維護頁 C# 全分層完成（`feature/budget-optimization`、未 commit/push、離線測試 17/17）；② `SP_Budget_FXRate` v3 停推腳本備妥**未部署**（前提＝①先上線，附還原檔）；③ BudgetData flip 未開工。**無資安弱點細節**；C#／SQL 屬程式碼不逐一發佈。歸 Budget Platform 對外待決集，GitHub/Notion 待 Hyman 連同整體取捨決定。Obsidian 工作紀錄已寫。|
| Budget Platform | Plan Rate 多年度主鍵（`部署_BudgetPlanRate_PK加Year.sql` + 還原檔，7/13 下午）| 未定（GitHub/Notion）| 待人工：`PK_Budget_PlanRate` 由 `(CurrencyType,Currency)` 改 `(CurrencyType,Year,Currency)`，解鎖①頁面跨年度並存、宣稱讀取端零影響，附還原檔。屬 DB 變更腳本／程式碼不逐一發佈；✅**已確認於 07-13 執行於正式 DB**（7/14 補確認）。歸 Budget Platform 對外待決集。Obsidian 工作紀錄已寫。|
| Budget Platform | 權限表年度移除 DB 前置（`DB前置_權限表去重備份.sql` + 還原檔，7/13 下午，**新工作線·無設計文件**）| 未定（GitHub/Notion）| 待人工：權限延續制移除年度維度，備份 2058／875 列後 `DELETE [Year]<'2026'`（預期刪 139／331、留 2026 的 1919／544），宣稱正式站零影響，附整表回灌還原檔。✅**已確認於 07-13 執行於正式 DB**（7/14 補確認），且權限去年度 C# 已 commit/push 部署測試站；**尾巴＝正式站發版後 DROP 權限表 Year 欄＋清備份表（屆時出腳本）**、此新工作線**是否需補設計文件待人工**。屬 DB 變更腳本／程式碼不逐一發佈，歸 Budget Platform 對外待決集。Obsidian 工作紀錄已寫。|
| Budget Platform | 預算匯率自維 7/14 結案（`步驟3a/3b_*.sql`＋`部署_SP_Budget_FXRate_v3_*.sql` 更新＋還原檔 2＋`設計_預算匯率自維.md` 結案段＋`測試清單_給PM前驗收.md`，7/14）| 未定（GitHub/Notion）| 待人工：預算匯率自維**全案結案**（②v3 部署含移除 OPEX_PlanRate 複製段、⓪ BRL 在位、③a 驗證 208,812 列 EXCEPT=0/0、③b BudgetData View＋凍結 SP flip 改讀 `Budget_PlanRate`，指紋與基準一致）。**無資安弱點細節**，惟 C#／SQL 部署腳本屬程式碼、且整體歸 Budget Platform 對外待決集，GitHub/Notion 待 Hyman 連同整體取捨決定。未來時點：8 月 3–6 號 FX Rate 排程跑完後須確認 `Budget_PlanRate` 未被覆蓋（證 v3 停推生效）。Obsidian 已含 07-14 結案段。|
| SBU Scorecard | `uSP_SBUScorecard2026_Trigger.sql`＋`Fix_QuotaAchvIncludeDC_DEV_WEB_OneTime.sql`（7/13 晚）| —（無設計文件）| 待人工：Trigger 重算 Quota 及下游 KPI（惟只補 'Quota Achv.%'）；一次性腳本補算 `SCORECARD_PROD_N_DEV_WEB` 漏掉的 'Quota Achv.%(include Double Count)'＝(Revenue(E2E)+Double Count Rev.(E2E))/Quota（例 ARM Computing YTD 155.34%→150.85%）。**⚠️ 一次性腳本非永久——下次跑 Trigger 會覆寫回舊值，SP 本身仍待補相同 include-DC 邏輯才一勞永逸**。**SP-only、無設計文件、無對應 Obsidian vault**，依發佈集規則不發佈；歸屬／是否建記錄待人工。|
| Budget Platform | **2026 H2 開工：8 個工項 DB 部署腳本＋2027 開循環前置**（`SP\2026H2優化\工項1/2/3/4/6/7/8/9_*`、`SP\2027開循環\步驟1/2/3`、`2026H2優化\2027開循環前檢查清單.md`／`工項9_設計與確認清單_TE_GeneralExpense.md`／`工項規劃_RBU_SBU.html`，7/15 傍晚~7/16）| 未定（GitHub/Notion）| 待人工：7/15 定案的 H2 規劃**當晚開工**，一天內 9 工項中 8 項產出腳本（僅工項5 FSCT Month 未動），全附還原檔、皆冪等。**無資安弱點細節**，惟 SQL 部署腳本／C# 屬程式碼不逐一發佈，且 H2 各工項尚在測試站/未驗收 → 歸 Budget Platform 對外待決集，待 Hyman 連同整體取捨決定。⚠️ **待確認：各腳本是否已於正式 `OPEXdb` 執行，本輪無法自檔案確認**（工項3 交接稱設定表「已部署」、工項9 cutover 前提稱 C# 已部署，餘未載明）。⚠️ **2027 開循環：步驟2 建 Timer「執行即生效」（入口年度＝MAX(Timer.Year)，跑完立即切 2027、2026 變唯讀），且硬阻擋 A1＝正式站尚未發版**（正式站舊程式以日期推算年=2027 查權限、權限表已無 2027 概念 → 入口 500／空白）→ 發版為開 2027 絕對前提；D1 建議 CAPEX 改版（W2–W3）上線後再開放，避免舊範本窗口。決策紀錄：工項9 改「預設樣式先行」不等 Lilian/PD，範圍經 Hyman 7/16 擴大為 T&E＋General Expense 兩步驟。Obsidian 工作紀錄已寫 |
| Budget Platform | 2027 開循環「一鍵複製年度基礎資料」建議（`2027開循環前檢查清單.md` B1 去年度化評估，7/15）| —（建議） | 待人工：使用者 7/15 提問「基礎表能否去除年份概念」→ 評估結論**不建議徹底去 Year**（年度版本化設定非名單型；實測 Basic 新增 6 科目+1 改名、Active 整組重建 203→8,626 零重疊、Step 新增 1,411 列；且已結案年度唯讀頁即時 join 當年科目）；**唯 `Budget_AccountCode_Group` 兩年逐列完全相同（0/0）**。建議折衷＝保留 Year＋後台「開啟新年度」一鍵複製鈕，**可列 H2 追加工項待 Hyman 決定是否納入**。另順帶發現清理候選（發版後清備份表時一併）：`Budget_CurrentData_RBU_BK20250611`（**1,938 萬列**）、`Budget_Headcount_20251002`（51 萬）、`Budget_HCM_Actual_HC_20251002`、`BudgetZrco18_2024` |
| Budget Platform | 年度改造 結案總表（結案總表.md，7/8）＋ 預算匯率自維設計（設計_預算匯率自維.md，7/9）| 未定（GitHub/Notion）| 待人工：年度改造**主線結案**（對外 View flip snapshot+殼、Snapshot 基建+Orchestrator+年度參數化 ETL SP 全部署正式 DB；★SQL Agent「每日凍結」交 DBA 建為唯一營運後果尾巴）。**預算匯率自維**（範圍 B、7/9 拍板）＝結案後加值設計，讓預算計劃匯率脫離共用 `OPEX_PlanRate`、改由後台頁維護 `Budget_PlanRate`，**尚未動程式/DB、待審核**。皆無資安弱點細節但歸 Budget Platform 對外待決集，GitHub/Notion 待 Hyman 連同整體取捨決定。Obsidian 工作紀錄已寫 |

> ℹ️ 完整盤點與已建結構見 `D:\Obsidian Note\專案盤點對照表.md`。
> 小項待補：eManagerReport 既有連結補 SA 摘要。（TCP 3 個舊 DB 連結 SA 已於 6/12 補齊）

---

## ✅ 已同步記錄

### 2026-07-20

> （本次排程於 2026-07-20 執行，掃到自 7/17 同步後的落差：**Budget Platform** 工項3 SAP 分時段拋轉的遠端部署交付＋九工項 PM 分項驗收清單＋7/17 權限信箱疑義結案＋進度總覽更新；**MSU Scorecard** 新開 AKMC 一線（linked server ZRCO07_SUM 來源追查＋連線失敗診斷）。**本次無對外 GitHub/Notion 內容發佈**——Budget 全屬程式碼/日誌且歸對外待決集、MSU 為診斷 SQL＋原始資料。**⚠️ Notion 本次仍無法連線（certificate signature failure，同 7/17）→ Notion 部分續停做**。實際同步動作：Obsidian 工作紀錄 ×2 + 台帳/本 SYNC_LOG + sync-log.html 重生。）

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| Budget Platform | `2026H2優化\工項3_部署說明_分時段拋轉.md`（14:53）＋部署包 `工項3_部署包_UploadALL_分時段\`（Release 19 檔含 exe/pdb）＋`SP\_還原備份\還原_工項3_UploadSchedule補HK_IN模式.sql`（14:55）；`2026H2優化\PM分項驗收清單_2026H2.md`（10:29）；`SP\_還原備份\還原_LilithChen權限列.sql`（10:28）；`2026H2優化\進度總覽_已完成與待執行.html`（14:57 更新） | Obsidian「Budget Platform Notes\Budget Platform 概覽.md」新增「工項3 分時段拋轉部署包＋PM 分項驗收清單＋權限信箱結案（2026-07-20）」段＋修改歷程列＋同步狀態更新至 7/20。**GitHub/Notion 待人工**（Console 部署包/SQL 還原腳本屬程式碼、進度總覽/驗收清單屬日誌/操作文件，無資安弱點細節；同歸 Budget Platform 對外待決集）|
| eManager / MSU Scorecard | `AKMC\診斷_ZRCO07_SUM_來源檢查_20260720.sql`（15:29）＋`AKMC\診斷_linkedserver_172214_連線失敗_20260720.sql`（15:46）＋`AKMC\ZRCO07_SUM.xlsx`（15:49，來源資料） | Obsidian「開發記錄\MSU Scorecard.md」新增 07-20 修改歷程列（AKMC 新開一線）＋同步狀態＋待確認（linked server 連線/來源確認）。**GitHub/Notion 不動**（診斷 SQL＋原始 xlsx 屬程式碼/底稿；linked server 連不上、分子來源未確認、SP 仍 pre-production、無新報告文件）|

> 本次（自動排程同步）掃 `D:\Work\專案` 比對三目的地，自 7/17 同步後落差為：
> **(a) Budget Platform（7/20）——工項3 部署交付＋PM 驗收清單＋權限信箱結案**：① **工項3 SAP 分時段拋轉** 產出遠端部署包（原始碼 `D:\Project\BudgetplatformConsole_Upload ALL` 改版、Release 19 檔）＋部署說明——Console 改**啟動參數帶時段**（`...Upload_ALL.exe 07:30`，**無參數＝與舊版全量行為完全相同＝安全回退**），5 點改動：參數帶時段／時段×公司代碼分區（讀 `Budget_SAP_UploadSchedule`，pattern `CN%`/`EU%`）／Deadline 過濾（只拋未過期區、寬限到隔天、天然取 `MAX(Timer.Year)`）／**RBU 回到排程**（舊排程迴圈只跑 SBU＋MSU）／**設定表補漏**（原 34 列漏 HK01/HK05/IN02，補 `HK%`＋放寬 `IN01`→`IN%`，現 36 列全涵蓋，還原檔在）；含遠端機五排程 `schtasks`（07:30/14:30/17:30/20:00/22:00）、驗證與三段回退。冪等背書＝RFC `ZCO_PLAN_KP06` 按鍵值覆寫＋舊制本就一天兩拋。② **九工項 PM 分項驗收清單**（開發側全完成、部署測試站 `dev-emanageradmin-2.advantech.com`），列驗收路徑/預期＋驗收前提醒（部分區 2026 實際數 0＝上游 ZRCO18 缺美國＋10 幣別、SBU 催辦信旗標關閉、工項9 用 VA16）；**工項4 Lock 監控 07-18 首跑偵測 304 筆異動、07-20 持續執行**。③ **✅ 7/17 權限信箱疑義結案**——Liz.Huang／Tammy.Wu 員工主檔查證正式信箱即 `@advantech.com`（有效）；**Lilith.Chen 查無此人（已離職）→ 權限列已移除**（角色列 2＋區域列 19，還原檔 `還原_LilithChen權限列.sql`）。④ 進度總覽 HTML 更新至 7/20。
> **(b) MSU Scorecard（7/20）——AKMC 新開一線**：承 #9 泛System Hourly Rate-Assembly，追 **AKMC-System** 口徑分子 MOPEX 來源 `[172.21.214.30].[iFactoryPlatform].[SAP].[ZRCO07_SUM]`（**SQL Server linked server，非 Denodo**）。產出來源存在性檢查 SQL（連線/物件/樣本/期別涵蓋/接 HierarchyMapping No=7 對 cost center）＋linked server「**Communication link failure / network name no longer available**」連線失敗診斷 SQL（查 data_source/provider、重試 3 次、OPENROWSET 備援、OS 層埠測試）＋來源 `ZRCO07_SUM.xlsx`。**目前卡在 linked server 連不上（暫時性 vs 設定壞待判）、分子來源未確認**。
> **本次無任何對外 GitHub/Notion 內容動作**：Budget 全數為 Console 部署包/SQL 還原腳本（程式碼）＋進度總覽/驗收清單（日誌/操作文件），雖**無資安弱點細節**，仍整體歸 Budget Platform 對外待決集（待 Hyman 取捨）；MSU 為診斷 SQL＋原始 xlsx、SP 仍 pre-production。→ 實際同步動作僅 Obsidian 工作紀錄 ×2 + 台帳/本 SYNC_LOG 對齊 + sync-log.html 重生。
> ⚠️ **兩項提醒**：(1) **Notion 本次仍完全無法連線**（`certificate signature failure`，與 7/17 同）——依規則停做 Notion 部分；**OSF Commerce Insights 頁的 KPI 邏輯更新（第六/七次修改）仍列待人工/待下次連線恢復**（見待同步）。(2) **Budget 工項3 分時段排程本體仍待 E3 確認 SAP 冪等後才於遠端機建立**——在那之前入口頁「Next SAP Update」顯示新時段、實際拋轉仍照舊時段（驗收清單已列為已知落差）；另舊排程 2026-03-19 後停跑且停跑前一路 Error，部署時須順查歷程。

### 2026-07-17

> （本次排程於 2026-07-17 執行，掃到自 7/16 同步後的落差：**OSF Commerce Insights 第七次修改**——Operational Excellence 7 個 KPI 調整，已部署驗證；**Budget Platform H2 進度總覽**＋工項9 第二段＋SAP 閘門角色定版。⚠️ **Notion 本次全程無法連線（certificate signature failure）→ Notion 部分停做、列待人工**。實際同步動作：GitHub 發佈 OSF ChangeLog.html（首次）+ Obsidian 工作紀錄 ×2 + 台帳/本 SYNC_LOG + sync-log.html 重生。）

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| eManager / OSF Commerce Insights | `OSF_CommerceInsights_ChangeLog.md`（7/17 15:59，新增**第七次修改**；另補記先前未同步的**第六次修改**（6/11 Store 資料權限）） | **GitHub**：轉 `osf-commerce-insights\功能模組\ChangeLog.html`（**首次發佈**，比照 hc-dashboard/ChangeLog.html 樣式）。**Obsidian**：「開發記錄\Commerce Performance Insights.md」補第六/七次修改歷程列＋兩段完整工作紀錄、原始文件路徑由舊 `D:\eManager\...` 更正為現行 `D:\Work\專案\eManager\...`、補已發佈連結。**Notion 待人工**（連線失敗，且 KPI 計算邏輯有變需更新 📊 衡量指標段）|
| Budget Platform | `2026H2優化\進度總覽_已完成與待執行.html`（7/17 15:15）＋`2026H2優化\工項9_範本草稿\T&E.xlsx`／`General Expense.xlsx`（7/17 13:11） | Obsidian「Budget Platform Notes\Budget Platform 概覽.md」新增「2026 H2 優化 — 進度總覽（2026-07-17）＋ 工項9 第二段」段＋修改歷程列＋同步狀態更新至 7/17。**GitHub/Notion 待人工**（進度儀表板屬日誌性質；同歸 Budget Platform 對外待決集）|

> 本次（自動排程同步）掃 `D:\Work\專案` 比對三目的地，自 7/16 同步後落差為：
> **(a) OSF Commerce Insights — 第七次修改（7/17，已部署並驗證）**：Operational Excellence 7 個 KPI（O2R／O2S／S2A／A2C／C2R／Freight Act. ($)／Freight Fee %）YTM 規則調整。**根因是三個實質 bug**：① `PBI_OSF_Commerce_Performance` 的 KPI 名稱與 `OSF_CommerceInsightsKPI` 設定表**完全對不上**，SP 原樣寫入 PBI 名稱、前端以設定名稱查找 → 這 7 個 KPI **在報表上完全無資料**（2026 查無任何相關列）；② Freight Fee % 分母 `2026 Achv. (K)` 單位為 K 需 ×1000（同第四次 ROAS 修正之坑）；③ Freight Fee % `DecimalPlaces=0` 使比例值（0.0464）被四捨五入成 0 → 百分比全變 0%。**修法**：SP 三處（`PBI_Data` CTE 加 `CASE` 名稱對應／**新增 `YTMCalcType='AVG'` 區塊**（設定驅動，原 ③④ 改編號 ④⑤）／RECALC_SUM 加 Freight Fee % `[FreightAct] / NULLIF([Revenue] * 1000, 0)`）＋`Update_OSF_CommerceInsightsKPI_YTM.sql`（Step 0 CHECK 約束重建納入 `'AVG'`——DB 實查從未建此約束只有 DEFAULT，故 `IF EXISTS` 判斷；O2S/S2A/A2C/C2R 設 AVG；Freight Fee % 設 RECALC_SUM、DecimalPlaces 0→3）＋`Create_OSF_CommerceInsightsKPI.sql` 同步約束＋`OSF_CommerceInsightsKPI.xlsx` 更新備註/小數位。**部署已完成、結果已驗證**（設定表腳本已跑、SP 已 ALTER 並重算 @HierarchyYear=2026；Jan ALL 驗算 3942.81／131508.6 ≈ 0.030）。⚠️ **後續注意**：PBI 端拼字不一致（`Arrival to Clearnace`、`Clearance to received`），SP 的 CASE 照 **DB 實際名稱**寫，**若 PBI 日後改正拼字，SP 對應需同步更新**，否則該 KPI 會再度無資料。
> **(b) Budget Platform — H2 進度總覽（7/17）**：本輪已完成／待執行對照表，同時**回答了 7/15~16 紀錄留下的多項待確認**——**2027 預算循環已開啟**（Timer 2027／Deadline 2027-03-01／**FCST_Month=7**（非前次暫定期末值）／PlanRate 2027／八表複製，**三支腳本跑完並驗證**）；**RBU 五工項 merge `7ed2cbb1`**（**工項5 由「FSCT Month 後台設定」變為「Date 頁 RBU (All Regions) 一次套用」**——前次紀錄稱工項5 未動，現已完成惟範圍與原規劃不同；CAPEX 正式範本**已上 share**）；工項8 `baa765dd`／工項6 `22f78730`+`c776ea6e`（⚠️ 催辦信旗標**預設關閉**）／工項7 `6651589d` 測試站實測通過／**工項9 兩段完成**（第一段 cutover **守恆自檢 282 個 Cost Center 差異＝0**、頁面實走驗證全過；**第二段（7/17）＝Excel 範本上 share＋下載/上傳（單步驟與整本）＋表頭字樣修正**，「下載→清庫→上傳回存」閉環煙霧測試兩步驟全綠，`e0bc2845`／`987cc3bc`，**照預設樣式（仿 R&D）定稿**＝前次列的 5 項待 Lilian/PD 定稿已按預設樣式走）；**手動拋 SAP 閘門角色 7/17 拍板**＝Admin／Global Finance／SBU Finance 三角色（19 人，**SBU HQ 不開放**），**權限判斷改看使用者全部角色**（原只取第一筆會漏判多角色者），煙霧測試五角色全綠（`aeafe758`+`07e599cc`）；**「2027 不能編列」修復**＝根因 **Monthly Update ETL 排程結束日過期**、已手動補跑，RBU 主要幣別區 2026 基準數字恢復。
> **本次對外發佈僅 OSF ChangeLog.html**（設計文件、無資安弱點細節，且 hc-dashboard/ChangeLog.html 已有同類先例）；OSF 的 SP／設定表 SQL／xlsx 屬程式碼與底稿，依發佈集規則不逐一發佈。Budget 進度總覽屬日誌性質＋整體歸對外待決集 → 僅 Obsidian。TCP `舊版\SP_SALES_TCP_New.sql`（7/17 14:37）屬舊版 SP 程式碼、不發佈。
> ⚠️ **三項提醒**：(1) **Notion 本次完全無法連線**——`certificate signature failure`（連 get-block-children 與 retrieve-a-page 皆失敗），依規則**停做 Notion 部分**；**OSF 頁本應更新**（第七次修改動到 KPI 計算邏輯＝系統本身有變，📊 衡量指標與計算邏輯段需補 O2S~C2R 的 AVG 與 Freight Fee % 公式），**列待人工/待下次連線恢復**。(2) **OSF 第六次修改（6/11 Store 資料權限）先前從未被同步**——台帳「OSF 最後異動」停在 2026-06-04，證實台帳水位線過時；本次已於 Obsidian 補記，Notion 亦需補（🧩 功能與資料段：權限維度由 Region 改 Store、權限表 `OSF_CommerceInsightsPermission` 讀 `HierarchyName='Store'`）。ChangeLog 內另載該次 C# 變更 commit 於 `eManagerCore` `develop`（`0621048`）**當時尚未 push**，現況待查。(3) **Budget A1 硬阻擋「正式站發版」仍未做** → 2027 循環現況應僅測試站生效；新待辦 **Lilith.Chen／Liz.Huang／Tammy.Wu 權限表信箱為 .com 而非 .com.tw 疑似無效帳號、待 PM 確認**。

### 2026-07-16

> （本次排程於 2026-07-16 執行，掃到自 7/15 同步後的落差：**Budget Platform H2 於 7/15 傍晚開工**——一天內 9 工項中 8 項產出 DB 部署腳本，另開 2027 開循環前置線；MSU Scorecard 7/15 傍晚 Config 改 'X' 模擬報表。**本次無對外 GitHub/Notion 內容發佈**——Budget 全數屬程式碼/DB 腳本且歸對外待決集、H2 工項尚在測試站未驗收；MSU 為純模擬查詢 SQL＋核對 xlsx。實際同步動作僅 Obsidian 工作紀錄 + 台帳/本 SYNC_LOG + sync-log.html 重生。）

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| Budget Platform | **H2 開工 8 工項腳本**：`SP\2026H2優化\工項1_部署_CAPEX加欄.sql`（＋4 欄、舊 2 欄保留停寫）／`工項2_部署_SP_Budget_SendRfcLog_v2.sql`（收件人接回 `@Recipients`、BI 改 CC、**移除 `Budget_Permission.[Year]` 過濾＝順解 DROP COLUMN Year 阻擋**、email 欄 30→200、補成功情境、System 防呆）／`工項3_部署_SAP上傳時段設定表.sql`＋`工項3_DBA交接_拋轉排程調整.md`／`工項4_部署_CostcenterLock監控.sql`＋`工項4_建作業_每日Lock監控.sql`／`工項6_部署_SummaryFinish表.sql`＋`工項6_部署_ReminderLog表.sql`／`工項7_部署_AllocationRuleStep註冊.sql`＋`工項7_部署_AllocationRule角色設定.sql`／`工項8_部署_SBU留存Log表.sql`／`工項9_部署_ProjectDataSBU表.sql`＋`工項9_cutover_TE_GE上線切換.sql`＋`2026H2優化\工項9_設計與確認清單_TE_GeneralExpense.md`；**2027 開循環**：`2026H2優化\2027開循環前檢查清單.md`＋`SP\2027開循環\步驟1_複製PlanRate_2026到2027.sql`／`步驟2_建Timer2027_開啟循環.sql`／`步驟3_複製基礎資料_2026到2027.sql`；還原檔 8 份於 `SP\_還原備份\`；`工項規劃_RBU_SBU.html`／`FY27_CAPEX_正式範本_待放share.xlsx` | Obsidian「Budget Platform Notes\Budget Platform 概覽.md」新增「2026 H2 優化 — 開工（2026-07-15 傍晚 ~ 07-16）＋ 2027 開循環前置」段（逐工項內容與決策）＋修改歷程列＋同步狀態更新至 7/16。**GitHub/Notion 待人工**（見待同步，同歸 Budget Platform 對外待決集）|
| eManager / MSU Scorecard | `TW\測試_Config改X_模擬報表_20260715.sql`（純 SELECT 不寫表，取用已跑完的 `Temp_SCORECARD_MSU_N_Data`，比照主 SP 對 `UsingUpload='X'` 的處理模擬 9 列改 X 呈現＋4 列維持 V 上傳對照）＋`TW\ATMC自動化_Config改X_檢查_20260715.xlsx`（核對用）| Obsidian「開發記錄\MSU Scorecard.md」新增 07-15（續）修改歷程列＋同步狀態更新至 7/16。**GitHub/Notion 不動**（純模擬查詢 SQL＋原始 xlsx 屬程式碼/底稿；Config 尚未實際改 'X'、待 tina 核對；SP 仍 pre-production、無新報告文件）|

> 本次（自動排程同步）掃 `D:\Work\專案` 比對三目的地，自 7/15 同步後落差為：(a) **Budget Platform H2 於 7/15 傍晚（17:29 起）開工**——7/15 才定案的工項規劃當晚即動手，至 7/16 15:38 **9 個工項中已有 8 項產出 DB 部署腳本**（僅工項5 FSCT Month 未動），全部附 `SP\_還原備份\` 一鍵還原檔、皆標冪等：工項1 CAPEX 加 4 欄（AssetType/AssetCategory/RequestingDepartment/PurchasePurpose，移除的 SectorCOE/Remark **DB 欄保留停寫**）＋正式範本待放 share；工項2 `SP_Budget_SendRfcLog` v2（v1 收件人邏輯寫好卻沒接上、EXEC 寫死測試名單 → 接回 `@Recipients`；**順修移除 `Budget_Permission.[Year]` 過濾**，既解權限延續制漏人、也解 H1 尾巴 DROP COLUMN Year 的已知阻擋物件；email 欄位截斷修正；補「成功」情境信）；工項3 `Budget_SAP_UploadSchedule` 設定表＋App 側 Last/Next SAP Update 顯示與封鎖區間（**排程本體＋SP 分區執行需 DBA/E3 配合**，過渡＝新時段跑全量、須先問 E3 端 SAP 可否接受重複拋轉）；工項4 Lock 監控三物件（Snapshot/ChangeLog/SP，只監控平台管理 CC）＋每日 08:00 Agent 作業（**無 msdb 權限、需 DBA 建**）；工項6 `Budget_Summary_Finish`（存檔即解除 Finish）＋`Budget_SBU_Reminder_Log`（NULL=正式寄送為每日防重依據）；工項7 唯讀 Allocation Rule Step 註冊（ActionName 不可含空格、角色列複製自 Summary 否則選單不顯示）；工項8 `Budget_SBU_Archive_Log`（NULL 列＝整輪彙總、每循環年只跑一次）；**工項9 改「預設樣式先行」不再等 Lilian/PD**，且**範圍經 Hyman 7/16 補充擴大為 T&E＋General Expense 兩步驟獨立**（新表 `Budget_Project_Data_SBU` 加 `StepID` 與 R&D 舊表隔離、`vw_Budget_Summary_SBU` 加第 4 段、cutover 單一交易＋守恆自檢＋既填數字搬移為「(Moved from Business Related)」專案列）。另新開 **2027 開循環前置**線（檢查清單＋步驟1/2/3 腳本，使用者拍板皆沿用 2026 值起步）。(b) **MSU Scorecard** 7/15 傍晚產出 ATMC MOPEX **Config 改 'X' 模擬報表**（純 SELECT、不寫正式表，取用已跑完的暫存結果模擬改 X 後呈現）＋核對 xlsx，Config 尚未實際改、待 tina 核對。
> **本次無任何對外 GitHub/Notion 內容動作**：Budget H2 全數為 SQL 部署腳本／C#（程式碼，依發佈集規則不逐一發佈），雖**無資安弱點細節**，但各工項尚在測試站/未經 PM 驗收、系統對外行為未定案，整體仍歸 Budget Platform 對外待決集（待 Hyman 取捨）→ Notion 頁維持 2026-06-17 概覽不動；MSU 為模擬查詢 SQL＋原始 xlsx、SP 仍 pre-production。→ 實際同步動作僅 Obsidian 工作紀錄 + 台帳/本 SYNC_LOG 對齊 + sync-log.html 重生。
> ⚠️ **兩項提醒**：(1) **H2 各腳本是否已於正式 `OPEXdb` 執行，本輪無法自檔案確認**（工項3 交接文件稱設定表「已部署」、工項9 cutover 前提稱 C# 已部署，其餘未載明）——其中工項9 cutover 含對 2027 `Budget_BasicData` 的搬移＋刪列（有備份表與還原檔），若已跑即實質營運後果。(2) **2027 開循環：`步驟2_建Timer2027` 執行即生效**（入口年度＝`MAX(Timer.Year)`，跑完立即切 2027、2026 變唯讀已凍循環），而檢查清單自載**硬阻擋 A1＝正式站尚未發版**（正式站舊程式以日期推算年=2027 查權限、權限表已無 2027 概念 → 入口 500／空白；範本下載仍舊密碼）→ **先發版正式站是開 2027 的絕對前提**；另 D1 建議 CAPEX 改版（W2–W3、8/5 收斂）上線後再開放，以免使用者用舊範本上傳 2027 CAPEX。

### 2026-07-15

> （本次排程於 2026-07-15 執行，掃到自 7/14 同步後的落差：MSU Scorecard 7/15 SP 覆蓋改動、Budget Platform H1 結案歸檔＋H2 工項規劃。**本次無對外 GitHub/Notion 內容發佈**——MSU 為 SP＋診斷 SQL＋原始資料且 pre-production；Budget 為規劃/紀錄文件且整體歸對外待決集。實際同步動作僅 Obsidian 工作紀錄 + 台帳/本 SYNC_LOG + sync-log.html 重生。）

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| eManager / MSU Scorecard | `SP\uSP_MSUScorecard2026_N_Data_TW.sql`（**#5 ATMC-LA MOPEX 改「User 上傳覆蓋」**＋`MOPEX %`/`MOPEX %(Excl)` 改比率型 KPI 走 Q/H/YTD 加權）＋`TW\檢查_上傳覆蓋_LA_MOPEX_20260715.sql`（覆蓋前置檢查）＋`TW\0715-1/2/3.xlsx`（驗收）；備份 `..bak_20260715b_qhytd`／`..bak_20260715c_lapv` | Obsidian「開發記錄\MSU Scorecard.md」新增 07-15 修改歷程列＋更新待確認 #5（改採上傳覆蓋、列驗證條件）＋同步狀態。**GitHub/Notion 不動**（SP＋診斷 SQL＋原始資料屬程式碼/底稿、SP 仍 pre-production、KPI 調整未定案、無新報告文件）|
| Budget Platform | H1 結案歸檔：工作目錄重整為 `2026H1優化_已結案\`（規劃/過程紀錄/結案交付）＋`README.md`（索引，記正式站發版後 4 尾巴）；H2 規劃：`2026H2優化\工項規劃_RBU_SBU.md`（自 Notion H2 ticket list 篩 13 張 RBU/SBU 票切 9 個 feature branch，07-16 起估 7–9 週、5 待確認） | Obsidian「Budget Platform Notes\Budget Platform 概覽.md」新增「H1 優化結案歸檔＋H2 工項規劃（2026-07-15）」段＋修改歷程列＋同步狀態。**GitHub/Notion 待人工**（規劃/紀錄文件、無資安弱點細節、尚未動程式，同歸 Budget Platform 對外待決集）|

> 本次（自動排程同步）掃 `D:\Work\專案` 比對三目的地，自 7/14 同步後落差為：(a) **MSU Scorecard** 7/15 於 `uSP_...N_Data_TW.sql` 做 **#5 ATMC-LA MOPEX 改「User 上傳覆蓋」**——不再逐階梯追排除科目（07-09 診斷線久拖未決），改讓 ATMC-LA 的 `MOPEX(K)`/`MOPEX-SMT/Labor` 由上傳表 `SCORECARD_MSU_UploadData_New` 就地覆蓋系統計算值（UNPIVOT M01–M12、上傳→系統命名對應、`UsingUpload='X'` 保留 fallback），連動 `MOPEX %`/`MOPEX %(Exclude Internal PV)` 改為比率型 KPI（`'X'`＋`CountType=0`）走 Q/H/YTD **加權**（期望 ATMC total/MOPEX %/Q1 ≈ 0.06337）；產出覆蓋前置檢查 SQL＋驗收 xlsx，備份 qhytd（比率加權前）/lapv（LA PV 覆蓋前）。(b) **Budget Platform** 上半年優化全案 7/15 **驗收通過並歸檔**（工作目錄重整為 `2026H1優化_已結案\`＋README 索引，記正式站發版後 4 尾巴：發版→驗證範本→`DROP COLUMN Year`×2→清備份表），並**啟動下半年工項規劃**（`工項規劃_RBU_SBU.md`：自 Notion「Platform Issue Ticket List - 2026 H2」篩 13 張 RBU/SBU 票切 9 個 feature branch，快贏優先/外部依賴早發起/大包中段，5 待確認）。
> **本次無任何對外 GitHub/Notion 內容動作**：MSU 7/15 為 SP＋診斷 SQL＋原始 xlsx（程式碼/底稿）、SP 仍 pre-production 且 KPI 定義調整未定案，依發佈集規則不發佈、Notion 系統說明未實質變動；Budget H1 README 為結案索引、H2 為前瞻工項規劃（尚未動程式），皆無資安弱點細節但整體歸 Budget Platform 對外待決集（待 Hyman 取捨）。→ 實際同步動作僅 Obsidian 工作紀錄 + 台帳/本 SYNC_LOG 對齊 + sync-log.html 重生。

### 2026-07-14

> （本次排程於 2026-07-14 執行，掃到自 7/13 下午同步後的落差：Budget Platform 預算匯率自維 7/14 全案結案、SBU Scorecard 7/13 晚間兩支 Quota 相關 SQL。**本次無對外 GitHub/Notion 內容發佈**——Budget 全數歸對外待決集、SBU 為 SP-only 無設計文件；Budget Obsidian 本日已由使用者自行補記至 7/14（含將 9 篇 MD 整理進 vault），故實際同步動作僅台帳/SYNC_LOG 對齊 + sync-log.html 重生。）

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| Budget Platform | 預算匯率自維 7/14 結案：`步驟3a_flip前驗證_BudgetData即時支等值.sql`／`步驟3b_部署_BudgetData_FreezeSP_flip改讀BudgetPlanRate.sql`／`部署_SP_Budget_FXRate_v3_停推BudgetPlanRate.sql`（更新）＋還原檔 2 份＋`設計_預算匯率自維.md`（補結案段）＋`測試清單_給PM前驗收.md` | Obsidian「Budget Platform Notes\Budget Platform 概覽.md」**已含 07-14 結案段＋修改歷程列＋同步狀態＋Vault 筆記索引**（本日使用者自行補記，內容與檔案系統一致，本輪確認無需重寫）。**GitHub/Notion 對外待人工**（見待同步，同歸 Budget Platform 整體對外待決集）|
| SBU Scorecard | `SP\uSP_SBUScorecard2026_Trigger.sql`（7/13 18:56，重算 Quota 及下游 KPI）＋`SP\Fix_QuotaAchvIncludeDC_DEV_WEB_OneTime.sql`（7/13 18:33，一次性補算 include-Double-Count 版）＋`20260713  驗證資料.xlsx`（16:05） | **無同步動作**——SP-only、無設計文件、無對應 Obsidian vault，依發佈集規則不發佈；歸屬/是否建記錄待人工（見待同步）|

> 本次（自動排程同步）掃 `D:\Work\專案` 比對三目的地，自 7/13 下午同步後落差為：(a) **Budget Platform** 預算匯率自維 **7/14 全案結案**（⓪①②③ 全部完成並驗證）——② `SP_Budget_FXRate` v3 部署（含使用者 7/14 拍板加碼**移除 OPEX_PlanRate 分年度庫複製段**，SP 只剩 Budget_FXRate 重建段、分年度庫依賴歸零）；⓪ BRL 確認在位（7/13 補列未被排程洗掉、冪等重跑 0 補）；③a 驗證全過（即時支換匯段 208,812 列新舊雙向 EXCEPT=0/0）；③b `vw_BudgetPlatformBudgetData`＋`SP_FreezeSnapshot_BudgetData` flip 改讀 `Budget_PlanRate`（自檢 0 列、View 指紋 MSU −1226451664／RBU −54054080／SBU 1516615081 與基準一致）。**BudgetData 與 CurrentData 自此完全走 `Budget_PlanRate`、脫離共用 `OPEX_PlanRate` 與分年度庫**；唯一殘留 = FSCT `#Temp_Currency`（可選、未做）。另補 07-13 待確認狀態：Plan Rate PK 加 Year 與權限表年度移除前置**兩腳本確認均已於 07-13 執行於正式 DB**；權限去年度 C# 已 commit/push 部署測試站。並產出 `測試清單_給PM前驗收.md`（本波全改動驗收清單，測試站）。(b) **SBU Scorecard** 7/13 晚 `uSP_SBUScorecard2026_Trigger` 重算 Quota 及下游 KPI（惟只補 'Quota Achv.%'）＋一次性 `Fix_QuotaAchvIncludeDC_DEV_WEB_OneTime.sql` 補算漏掉的 'Quota Achv.%(include Double Count)'（＝(Revenue(E2E)+Double Count Rev.(E2E))/Quota；SP 本身仍待補同邏輯才一勞永逸）＋驗證 xlsx。
> **本次無任何對外 GitHub/Notion 內容動作**：Budget Platform 7/14 結案無資安弱點細節，但整體對外發佈仍待 Hyman 取捨、且 C#／SQL 部署腳本屬程式碼；SBU 為 SP-only 無設計文件、無 vault。Budget Obsidian 工作紀錄本日已由使用者自行補齊至 7/14（含 vault 整理 9 篇 MD），本輪核對內容與檔案系統一致、確認無需重寫。→ 實際同步動作僅台帳/本 SYNC_LOG 對齊 + sync-log.html 重生。

### 2026-07-13（下午追補）

> （同日午後再次排程，掃到自上午同步（截至 ~11:49）後的新落差：Budget Platform 午後 13:46~15:41 新增兩組 DB 腳本 + ①後台頁測試截圖。**本次無對外 GitHub/Notion 內容發佈**——皆屬程式碼／DB 變更腳本且歸 Budget Platform 對外待決集；實際同步動作僅 Obsidian 工作紀錄 + 本 SYNC_LOG + sync-log.html 重生。）

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| Budget Platform | `預算匯率自維\部署_BudgetPlanRate_PK加Year.sql` + `_還原備份\還原_BudgetPlanRate_PK.sql`（7/13 15:41）| Obsidian「Budget Platform Notes\Budget Platform 概覽.md」新增「續（2026-07-13 下午）：Plan Rate 多年度主鍵 + 權限表年度移除 DB 前置」段＋修改歷程列（07-13 下午）＋同步狀態追補。**GitHub/Notion 對外待人工**（見待同步）|
| Budget Platform | `權限年度移除\DB前置_權限表去重備份.sql` + `_還原備份\還原_權限表年度移除前置.sql`（7/13 14:54，新工作線·無設計文件）＋ `測試照片\後台網站測試 0713.png`（13:46）| 同上 Obsidian 段。**GitHub/Notion 對外待人工**（見待同步）|

> 本次（自動排程同步·下午）掃 `D:\Work\專案` 比對三目的地，自上午同步後落差為 Budget Platform 兩組午後 DB 腳本：(a) **Plan Rate 多年度主鍵**——`PK_Budget_PlanRate` 加 `Year`（解鎖①後台頁跨年度並存、宣稱讀取端零影響）；(b) **權限表年度移除 DB 前置**（新工作線、尚無設計文件）——備份後刪 2026 前舊列（宣稱正式站零影響）。兩者皆附一鍵還原檔。另①後台 Plan Rate 頁瀏覽器測試截圖留檔。
> **本次無任何對外 GitHub/Notion 內容動作**：兩組腳本屬 DB 變更／程式碼（依發佈集規則不逐一發佈）、無資安弱點細節但整體歸 Budget Platform 對外待決集（待 Hyman 取捨）。→ 僅 Obsidian 工作紀錄＋本 SYNC_LOG（含 sync-log.html 重生）。⚠️ **提醒：兩腳本是否已於正式環境執行本輪無法確認（設計文件進度段停在上午 11:49）→ 列待確認；權限前置含對正式權限表 `DELETE`（139+331 列），若已跑即實質營運後果。**

### 2026-07-13

> （本次排程於 2026-07-13 執行，掃到自 7/9 同步後的落差：Budget Platform 預算匯率自維 由設計轉入實作、SBU Scorecard SP 修正、MSU 7/9 晚間 LA MOPEX 排除階梯診斷。**本次無對外 GitHub/Notion 內容發佈**——全數落在待決集或屬程式碼/診斷；實際同步動作僅 Obsidian 工作紀錄 + 本 SYNC_LOG + sync-log.html 重生。）

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| Budget Platform | 設計_預算匯率自維.md（7/13 進度段）＋ 部署_SP_Budget_FXRate_v3_停推BudgetPlanRate.sql／步驟0_補BRL(_LinkedServer).sql／還原檔（7/13）| Obsidian「Budget Platform Notes\Budget Platform 概覽.md」新增「預算匯率自維 — 開工/實作（2026-07-13）」段（⓪①②③ 四步驟進度）＋修改歷程列（07-13）＋同步狀態更新至 7/13。**GitHub/Notion 對外待人工**（見待同步）|
| eManager / MSU Scorecard | 診斷_LA_MOPEX_排除階梯_20260709.sql ＋ ATMC自動化_比對／待tina確認_20260709.xlsx（7/9 晚）| Obsidian「開發記錄\MSU Scorecard.md」新增 07-09（續）修改歷程列（#5 LA MOPEX 排除階梯診斷）＋同步狀態更新至 7/13。**GitHub/Notion 不動**（純診斷 SQL＋原始比對資料，屬程式碼/底稿；結論待 tina）|

> 本次（自動排程同步）掃 `D:\Work\專案` 比對三目的地，自 7/9 同步後落差為：(a) **Budget Platform** 預算匯率自維**由設計轉入實作**（`設計_預算匯率自維.md` 補 7/13 進度＋部署/補資料/還原 SQL）——⓪ **BRL 補列已於正式 `Budget_PlanRate` 執行**（Linked Server 版、附還原檔、⚠️②部署後需冪等重跑）＝本輪唯一已落地營運後果；① 後台 Plan Rate 維護頁 C# 全分層完成（`feature/budget-optimization`、未 commit/push、離線 17/17）；② `SP_Budget_FXRate` v3 停推腳本備妥**未部署**（前提＝①先上線）；③ BudgetData flip 未開工。(b) **SBU Scorecard** 7/10 `uSP_SBUScorecard2026` 加 NRE-ADM6 MType 正規化（來源 ZFIN→ZSRV、影響 0 列）——SP-only、無設計文件、無 vault → 待人工。(c) **MSU Scorecard** 7/9 晚 LA MOPEX 排除階梯診斷 SQL＋比對 xlsx → Obsidian。
> **本次無任何對外 GitHub/Notion 內容動作**：Budget Platform 預算匯率自維無資安弱點細節但整體對外發佈待 Hyman 取捨、且 C#／SQL 屬程式碼；SBU SP-only 無設計文件；MSU 為診斷 SQL＋原始資料。→ 僅 Obsidian 工作紀錄＋本 SYNC_LOG（含 sync-log.html 重生）。⚠️ 提醒：Budget ⓪ BRL 補列在②部署前是暫時的（FX Rate 每月排程會洗掉），②部署後須冪等重跑一次。

### 2026-07-09

> （本次排程於 2026-07-09 執行，掃到自 7/8 同步後的落差：Budget Platform 年度改造結案＋第二刀部署就緒＋預算匯率自維設計，MSU 效能瓶頸定位。**本次無對外 GitHub/Notion 動作**——全數落在 Budget Platform 對外待決集或屬程式碼/診斷；實際同步動作僅 Obsidian 工作紀錄 + 本 SYNC_LOG。）

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| Budget Platform | 結案總表.md（7/8）＋ 設計_多年度存取.md（7/8）＋ 設計_預算匯率自維.md（7/9）＋ 部署/探勘/驗證 SQL | Obsidian「Budget Platform Notes\Budget Platform 概覽.md」新增「年度改造結案 + 第二刀部署就緒 + 預算匯率自維設計（2026-07-08~07-09）」段＋修改歷程列（07-08、07-09）＋同步狀態更新至 7/9。**GitHub/Notion 對外待人工**（見待同步）|
| eManager / MSU Scorecard | 效能_整支SP計時_20260709.sql／效能_分段計時_20260709.sql ＋ uSP CTOS PG 調整（bak_20260709_ctospg）| Obsidian「開發記錄\MSU Scorecard.md」新增 07-09 修改歷程列（效能瓶頸定位進行中＋CTOS PG 調整）＋同步狀態。**GitHub/Notion 不動**（診斷/計時 SQL 與 SP 調整屬程式碼、無新報告文件；SP 仍 pre-production、KPI 定義未變）|

> 本次（自動排程同步）掃 `D:\Work\專案` 比對三目的地，自 7/8 同步後落差為：(a) **Budget Platform** 年度改造**主線結案**（`結案總表.md`：對外 View flip snapshot+殼、Snapshot 基建＋`SP_FreezeOrchestrator`＋年度參數化 ETL SP 全部署正式 DB；SQL Agent「每日凍結」交 DBA 建）＋**第二刀多年度存取閘已清可部署**（`設計_多年度存取.md`：Denodo 已答 (A) 固定值 → 新增 `_History` View 純新增）＋**預算匯率自維設計**（`設計_預算匯率自維.md`：範圍 B、7/9 拍板、脫離共用 `OPEX_PlanRate` 改後台維護 `Budget_PlanRate`，尚未動程式/DB 待審）；(b) **MSU Scorecard** 7/9 效能瓶頸定位（分段計時遠端健康 1~2 分 vs 整支曾 13 分，產出整支/分段計時 SQL 一刀切開瓶頸，結論待判讀）＋ CTOS PG SP 調整。
> **本次無任何對外動作**：Budget Platform 全數歸對外待決集（年度改造無資安弱點細節但整體對外發佈待 Hyman 取捨、預算匯率自維為未實作設計；早前分析報告含 SQL 注入等敏感細節）；MSU 7/9 為診斷/計時 SQL 與 SP 調整（程式碼）、無新報告文件，依發佈集規則不發佈、Notion 系統說明未實質變動。→ 僅 Obsidian 工作紀錄。
> 進度亮點（見待同步更新）：7/1 待確認的 **Denodo 用途問題已獲答 (A)**（第二刀解閘）；7/1 查證的 **MSU 平均除數 bug 已在 C# 分支修正**（#3、`/10`、probe 驗證，本地未 push）。⚠️ `Budget Platform\待確認事項\README.md` 狀態欄仍標「待回覆」與設計文件（已答 A）不一致，已於 Obsidian／待同步標註請 Hyman 留意。

### 2026-07-08

> （本次排程於 2026-07-08 執行，掃到自 7/6 以來的落差：HC Dashboard 7/7 SBU Hierarchy 改版、MSU Scorecard 7/7~7/8 ATMC 調整報告。）

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| eManager / HC Dashboard | ChangeLog.html（**更新**：新增 2026-07-07「SBU Hierarchy 改版」段——SBU 31 Leaf → 31 Leaf + 7 Rollup = 38 列、`DSB_HC_Rollup` 0→51 筆、`DSB_HC_ScorecardMap` 重寫 38 列 Revenue 對應 + 加 `FilterExcludePD` 欄、`sp_DSB_HC_New` 3 處守門/排除分支調整；既有環境已跑 `SBU_Change_20260707_Incremental.sql` 並 COMMIT，驗收 Hierarchy 38／Rollup 51／ScorecardMap 38）| it-documents/hc-dashboard/（由 ChangeLog.md 以 python-markdown 重生 → git push）；Obsidian「開發記錄\HC Dashboard.md」新增 07-07 修改歷程列 + 3 項待確認（6 群組 PG 來源、SBU Total Revenue 策略、SP 重灌）+ 同步狀態。**Notion 暫不動**（Revenue 策略/PG 來源未定，見待人工）|
| eManager / MSU Scorecard | ATMC自動化_調整報告_20260708.html（tina 3 月 9 項比對；① 效能：3 支 DENODO-PROD 遠端查詢 `@Year` 下推只抓當年（`#Mopex_Raw`/`#Zrpp89_Raw`/`#Kp27_Raw`），結果不變、附帶修好歷史年重跑撈空；② #1 Hourly Rate-人力 兩個工時字串 bug（LA Labor 多空格、CTOS 字串錯）修後收斂到與 tina 差 −1~2%；③ #6/#7/#9 實跑驗收 PASS；④ MOPEX% NO ROW 根因＝sharepoint 來源 Plant/KPI 欄全 NULL，須來源端修）| it-documents/msu-scorecard/功能模組/（複製 HTML → git push，同 SP 修正交接/初版慣例，無敏感安全細節）；Obsidian「開發記錄\MSU Scorecard.md」新增 07-07~08 修改歷程列 + 待確認（#1 殘差/#5 LA MOPEX 待 tina、MOPEX% 來源標籤）+ 原始文件 + 同步狀態。**Notion 暫不動**（SP 仍 pre-production，效能/bug 修正未動 KPI 定義）|

> 本次（自動排程同步）掃 `D:\Work\專案` 比對三目的地，自 7/6 同步後落差為：(a) **HC Dashboard** ChangeLog.md 7/7 新增「SBU Hierarchy 改版」段（主要設計文件改版，比照 6/16 發佈慣例）→ 重生 ChangeLog.html 推 GitHub + Obsidian；(b) **MSU Scorecard** 7/8 產出 ATMC 調整報告 HTML（效能下推＋#1 工時字串修正＋#6/#7/#9 驗收＋MOPEX% 根因）→ 複製到 GitHub 功能模組 + Obsidian。兩者對外皆為主要設計/報告文件、無敏感安全細節，故 GitHub push；Notion 皆暫不動（HC SBU Revenue 策略/PG 來源未定案、MSU 仍 pre-production）。
> 附帶：eManager 改版 7/6 午後另有 `待續清單_20260706.md`、`今日修改摘要_20260706.html` 等收工檔，屬 7/6 已記錄之批改稿批次（結構方向 A/B/C 未定），仍列待人工，無新增動作。HC Dashboard／MSU 的診斷/測試/設定 SQL 與主改 SP 屬程式碼，依發佈集規則不逐一發佈，已於文件說明。

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
