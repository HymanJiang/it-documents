# Sync Log

記錄每次文件同步的內容與狀態。

---

## ❌ 待同步

| 專案 | 檔案 | 目標位置 | 備註 |
|------|------|---------|------|
| eManager / **Sales By Product**（新模組）| `SP\SP_Rolling_Forecast_Prod_2026.sql`（8/3 18:15，40.7 KB，UTF-16 LE，`ALTER PROCEDURE` 快照）＋`ASP\Sales_product_2026.asp`（5/20，132 KB）| 未定（GitHub/Notion 歸屬）| 待人工（**08-04 新列**）：**本次掃描首次發現的 eManager 新模組**，先前不在盤點對照表／SYNC_LOG／任何 Obsidian 筆記中。內容＝產品別 Rolling Forecast 報表線，DB 端 `[Global_Fin].[dbo].[SP_Rolling_Forecast_Prod_2026]` 由 Denodo `sap.iv_biprd_ztha_bo_outlook_month` 取 SAP 月別 Outlook → 組三個月滾動 `Forecast1/2/3` → 幣別換算（`fx_dim` 13 幣）→ 產品階層彙總（Prod_Divi／Prod_Group／Grand Total／MD-MD）→ 回寫 `MFG26..Sales_Product_Forecast`／`Scorecard_Prod_N_Rolling`／`Scorecard_Prod_N`。08-03 兩項變更：**① 不再依賴 `Rolling_Date` 控時、改 SP 內部由 `GETDATE()` 推算**；**② 資料來源改 SAP 月別資料、移除 1wk~4wk 週別快照（含佔位列與日期比對更新）**；另新增「FX 取 13 幣全齊之最新月、缺當月自動沿用前月」邏輯。承 07-30 的來源由 CRM 改 SAP（`校正 Hierarchy`／`SBU FOB Rate`／`NTD→TWD` 三段一併註解停用）。**依規則不發佈**：(a) 模組**無任何設計文件**（只有 SP＋ASP 程式碼），SP 屬程式碼不逐一發佈；(b) it-documents 無對應資料夾、Notion「📊 eManager」下無對應子頁 → **不自行建頁/建資料夾**，歸屬待 Hyman 決定。⚠️ 三項待確認：SP **是否已部署正式 `Global_Fin`** 檔案未載明（純 SSMS 匯出快照、無執行/驗證紀錄）；`Rolling_Date` 停用後**補跑歷史月份／跨月夜間執行的行為**未見驗證；讀碼觀察 `UPDATE …Sales_Product_Forecast SET Total=…` 與 `UPDATE Scorecard_Prod_N_Rolling SET YTD=0` **兩處皆無 WHERE**（後者全表歸零但只補回 `@nowYear`，其他年度 YTD 恐被歸零不復原），建議查核。Obsidian 已新建 `eManager Maintain Notes\開發記錄\Sales By Product.md` |
| Quota Platform（新專案）| `docs\QuotaPlatform_程式架構整理.md`（**7/29 擴寫至 18 章**，60.4 KB）＋`docs\QuotaPlatform_白話說明.md`（**7/29 新建，13 章**，22.3 KB）＋各自 `output\...html`＋`output\Quota Platform 白話說明.md`（Notion 匯入版）＋`tools\md2html.py`＋`同步舊平台資料 SP\`（2 SQL 快照，7/29 傍晚）＋`docs\SBU_QuotaForecast_資料搬遷建議.md`（7/25）| 未定（GitHub/Notion 歸屬）＋**部分不自動對外** | 待人工：**新專案**（QPF 模組，原始碼 `D:\Project\eManagerCoreAdmin`）。🆕 **7/29 傍晚增量**：新增第十八章「同步舊平台資料 SP」——QPF 正式結果由 DB 端每日排程「Update 2026 Quota」回灌舊平台 `MFG26`（`InterLock`／`Quota_Forecast_Rate`／`SBU_Quota_Forecast`），兩支 SP **不在程式碼庫內**；7 點觀察含 ⚠️ `QPF_AddSbuQuotaAdjustment` 單獨重跑會累積膨脹、雙寫不對稱（本地 MFG26 永遠缺調整列）、**換年硬路徑再 +2 處且連排程 Job 名稱都含年份**、以及**與 SbuQuota 搬遷案的交叉點（搬遷來源表仍被此鏈路每日覆蓋，切換時點必須一併停用/改寫）**。SP 屬程式碼不逐一發佈。it-documents 無對應資料夾、Notion「📊 eManager」下無對應子頁 → 依規則**不自行建頁/建資料夾**，歸屬待 Hyman 決定（納 eManager 傘下？與 Budget/TCP 平行？）。🔴 **7/29 更新（原記載「不含資安弱點細節」已不適用）**：技術版第十五章載明 **P0 提權漏洞**（`POST Permission` 全鏈路無角色檢查，任何登入者可上傳 Excel 自我提權為 PowerUser）＋確切端點/行號/硬編 RoleIndex GUID，白話版第十三章亦有對應白話陳述 → **依規則不自動對外發佈**，即使歸屬拍板仍需 Hyman 另行核可（或先出去敏感版）。白話版 Notion 匯入版已備好但**使用者未指定放在哪個頁面/資料庫下** → 不自行建頁。Obsidian `Quota Platform Notes\` vault 已更新工作內容。SBU 搬遷建議 8 個業務決策點未答、搬遷未執行 |
| Budget Platform | `執行計畫\安全批_角色矩陣草案_20260724.md`（7/24 傍晚）| —（**不自動對外發佈**）| 🔴 **待人工·含資安弱點細節**：回應 P0-2 Manager 後台安全缺口的角色授權矩陣草案（12 功能群×建議角色），載明「所有寫入 API 只驗登入不驗角色、`CreateBudgetPermission` 可自我提權、`PagesController` 整 class 無 `[Authorize]` 匿名可讀」→ 與 6/23 分析報告、7/23 Manager 盤點同級，**依規則不自動對外發佈**。待 Hyman 核可矩陣＋回答三問（{Region} Finance 是否保留寫入／SBU Finance 是否需額外寫入／TEST 角色是否清掉），核可後估 1-2 天實作。Obsidian 工作紀錄已寫 |
| Budget Platform | `SP\View效能_第二階段\00_說明.md`（定稿）＋`部署04_fn_BudgetPlatform_OverviewRBU.sql`（7/24 傍晚）| 未定（GitHub/Notion）| 待人工：View 效能第二階段收斂——`00_說明.md` 記兩支 ByCC 函數已部署且實測 0.41s/0.45s（原 161.8s/7.9s）、等值 16/16 全 0、C# 分支 `feature/2026h2-view-perf` 六方法改 FROM 函數；`部署04` 著手處理 COM-06 剩餘 99 秒 OverviewRBU。**無資安弱點細節**，惟 SQL 屬程式碼不逐一發佈、且函數是否正式上線／C# 是否 merge 未確認 → 歸 Budget Platform 對外待決集。Obsidian 工作紀錄已寫 |
| it-documents（repo 自身）| `_scripts\notion_sync\`（`notion-sync.mjs` 23.7 KB／`sync.ps1`／`mapping.json`，7/30 12:07 產出，**至今未 commit**）| 未定（是否納入 repo）| 待人工（**08-03 新列**）：把 MD 推上 Notion 的輔助工具（`dry`／`push`／`status` 三模式，`sync.ps1` 負責帶 `NODE_EXTRA_CA_CERTS`＋`--no-use-system-ca` 繞公司 TLS 攔截）。**token 讀自 `C:\Users\hyman.jiang\.claude\notion-token.txt`、未硬編於檔內**。惟 (a) 屬**工具腳本而非模組設計文件**，不在「只發主要設計文件」的發佈集內；(b) `mapping.json` 唯一條目 `qpf-plain` 指向 **Quota Platform 白話說明**（`pageId: null`、`parentPageId` 為 IT 系統文件索引頁），而該專案**歸屬本身未定** → 依規則不自行 commit、不自行建頁，是否納入 repo 待 Hyman 決定 |
| eManagerReport | 既有連結 | Notion eManagerReport 頁 | 補 SA 摘要（小項）|
| eManager / OSF Commerce Insights | `eManagerCore` `develop` commit `0621048`（6 files，第六次修改 C# 變更） | — | 待人工：ChangeLog 自載「**尚未 push**」（紀錄時點 6/11），現況待查——若仍未 push 則 Store 權限功能未進遠端 |
| Budget Platform | `2026H2優化\進度總覽_已完成與待執行.html`（7/17） | 未定（GitHub/Notion）| 待人工：H2 進度儀表板（已完成/待執行對照），屬日誌性質、無資安弱點細節；同歸 Budget Platform 對外待決集，待 Hyman 取捨。Obsidian 工作紀錄已寫 |
| eManager / HC Dashboard | SBU Hierarchy 改版（7/7，31→38 列＋7 Rollup＋重寫 Revenue 對應）| Notion HC Dashboard 子頁 | 待人工：結構性資料/維度變更已 COMMIT，惟 **SBU Total/小計 Revenue 策略（直抓 vs 抓不到退回加總）未定** + **6 個群組 PG 是否存在於 `SCORECARD_PROD_N` 待核對來源**；策略拍板＋來源確認後，再更新 🧩 功能與資料段（維度/資料表）與 📊 衡量指標段。GitHub ChangeLog.html 已更新，Obsidian 已記 |
| SBU Scorecard | （無設計文件，僅 SP） | Notion SBU 子頁已註明 | 待撰寫設計文件後再發 |
| Budget Platform | `執行計畫\00~05_測試腳本_*.md` + `tools\capture.ps1`（7/21）+ 執行結果與 `screenshots\`（7/22）+ **`測試報告_20260722.md`／`.html`（7/23）** + **`06_測試腳本_上傳下載補測.md`＋`測試報告\測試報告_RBU上傳下載補測_20260730.md`＋`README_資料夾說明.md`（7/30）** + 🆕 **`測試報告\20260731報告-1\測試報告_RBU回歸複測_20260731.md`／`_單檔版.html`＋`測試報告\測試報告_RBU完整重跑_20260731.md`／`測試報告_RBU完整測試_20260731_單檔版.html`＋`02`／`06` 腳本結果回填＋`SP\_還原備份\還原_UPUL08_ACZ權限等冪測試_20260731.sql`（7/31）** | 未定（GitHub/Notion）| 待人工：H2 九工項測試站逐項驗收腳本包（【R】/【W】/【X】三級分類、指定 CC）。🆕 **7/31 修復驗證輪**：D1~D7 回歸複測 → 揪出部署後新迴歸 **X1**（CAPEX 範本 500，ClosedXML `SaveAs` 以 app pool 身分重開 UNC 遭拒；本機 probe 測不出）→ 當日修 `a69b6475` 併同 PM#7/#8 與**加碼發現的 BR/Others-Fix 兩頁簽從未被填** → 部署後複測全過 → **RBU-01~13 完整重跑 13/13 全過**（RBU-13 Blocked 結案、RBU-09 升級為實開 Excel 驗證），**PM 8 缺陷 7 修 1 無法重現**。新增 P1 效能觀察（OPKFS01 Summary 範本 196 秒，其中本次修復佔約 35 秒）。⚠️ `a69b6475` **同樣只上測試站**；UPUL-08 存底/還原檔已備但結果欄空白、狀態不明；殘留追加 VA16 `TEST_20260731` 一列。🆕 **7/30 補測輪**：PM 交回 RBU UAT（8 缺陷）後做端點涵蓋盤點（**下載 10 端點測 6、上傳 6 端點僅 1 分支**）→ RBU 全功能補測 2.5 小時完成 → 產出 **D1~D7 七個缺陷並於當晚全數修復**（只推測試站 `BudgetPlatform` `625b3aa9`，另存 `hotfix/2026h2-uat2-bugfix` `d3844e0c`）。屬操作/驗收文件、**無資安弱點細節**，惟含測試站 URL／內部 CC／實際金額 → 同歸對外待決集。⚠️ **殘留測試資料再添一批（`TEST_20260730`）**，且 **PM 第一版測試值 100/500 已被本輪歸零上傳覆蓋**。**✅ 7/22 09:49~22:58 全數執行完畢，7/23 產出測試報告**：58 項＝**50 Pass／3 Fail／2 Blocked／3 Skip**，3 Fail 皆已修復驗證（見下列）。屬操作/驗收文件、**無資安弱點細節**，惟含測試站 URL、內部 CC 代碼與實際預算金額；同歸 Budget Platform 對外待決集，待 Hyman 取捨。⚠️ **殘留測試資料**：MSU VG02 工時費率**已於 7/22 還原**（Total MOE 歸零驗證），其餘 13 筆（`TEST_20260721` 新增列＋既有科目改值）依 7/22 裁示上線前統一清理。Obsidian 工作紀錄已寫 |
| Budget Platform | `執行計畫\優化盤點_信件功能_20260723.md`＋`SP\信件優化_20260723_待部署\`（3 SQL＋執行說明，7/23 晚）| 未定（GitHub/Notion）| 待人工：全平台信件功能唯讀盤點（3 運作中＋1 休眠）＋優化包。🔴 **含 P0 bug 尚未修上線**：`SP_Budget_SendRfcLog` 成敗判斷把 `Success` 列也算成錯誤，**432 批中 287 批純成功卻一律掛 `- Failed` 主旨＝成敗分流從未正確運作過**；修法一行，整包依指示「先不上版」備妥未執行，⚠️ **每次拋轉仍在對所有區 Admin 寄錯主旨，建議儘早安排部署窗口**。**無資安弱點細節**（非授權/注入類），惟含內部收件人信箱與名單規則、SQL 屬程式碼不逐一發佈；同歸 Budget Platform 對外待決集。App 端 `feature/2026h2-mail-batch`（`a4eac56d`）已推遠端未 merge，merge 後需補測試站 `SMTP:SubjectPrefix`。Obsidian 工作紀錄已寫 |
| Budget Platform | `SP\View效能_第二階段\`（2 個 fn 部署腳本＋驗證腳本，7/24）＋還原檔 | 未定（GitHub/Notion）| 待人工：回應 7/23 定案的 161.8 秒 View 瓶頸——**不改既有 View，改新增兩支「先過濾再組裝」TVF**（`fn_BudgetPlatform_BudgetData_ByCC`／`_CurrentData_ByCC`）供消費端改呼叫，關鍵診斷＝Summary View 各自帶 CC 條件時謂詞推得下去（0.3~0.4s），慢在外層 view 全量實體化後才 JOIN，目標 <1s。⚠️ **驗證腳本無執行結果、函數是否已部署正式 `OPEXdb`、C# 六個 RBU Summary 方法是否已切過去皆未載明**（還原檔警示：C# 已切則退函數須連 C# 一起退，否則 Summary 會 500）；**COM-06 剩餘 99 秒的 `vw_BudgetPlatformOverviewRBU` 未納入本次範圍**。屬 SQL 程式碼不逐一發佈，歸對外待決集。Obsidian 工作紀錄已寫 |
| Budget Platform | `執行計畫\測試報告_20260722.md`／`.html` 結案版改寫＋`_單檔版.html`（9.13 MB）＋`_含截圖.zip`（4.58 MB）（7/23 17:02~17:12）| 未定（GitHub/Notion）| 待人工：報告總表改標為 50 Pass／🔧已修正 4／☑非缺陷 1／⏭Skip 3，各原 Fail 加「結案更新」段；另收成**單檔內嵌截圖版可直接轉寄**。承 7/23 之測試報告條目，**無資安弱點細節**惟含測試站 URL／內部 CC 代碼／實際預算金額，同歸 Budget Platform 對外待決集，待 Hyman 取捨。Obsidian 工作紀錄已寫 |
| Budget Platform | `執行計畫\優化盤點_Manager後台_20260723.md`（7/23）| —（**不自動對外發佈**）| 🔴 **待人工·含資安弱點細節**：Manager 後台 8 子頁全模組盤點，載明 `BudgetPlatformManagerPagesController` **整 class 無 `[Authorize]`**（Permission 清單匿名可讀、User 可 query string 冒名）、**`CreateBudgetPermission` 可自我提權綁 Admin RoleID**、`UploadPermission` 可整包覆蓋一區權限，含確切 controller/端點/行號 → 與 6/23 分析報告同級，**依規則不自動對外發佈**。第一批已實作部署（`47a980ca`，17 檔）**但因機房網路中斷尚未實測**；**第二批（安全）需先定角色矩陣才能動、尚未開工**。另盤點註明全模組**未發現 SQL 注入面**。Obsidian 工作紀錄已寫 |
| Budget Platform | `執行計畫\根因調查_Fail與Blocked項_20260722.md`（7/23）| 未定（GitHub/Notion）| 待人工：3 Fail + 2 Blocked 根因調查。**無資安弱點細節**（純效能/邏輯缺陷分析），惟含程式碼路徑與行號、且歸 Budget Platform 對外待決集。⚠️ 內含**尚未解的 DB 端瓶頸**：`vw_BudgetPlatformBudgetData` 單 costcenter 查詢即 161.8 秒（View 每查必整包實體化），View 重構／落地 snapshot 列第二階段、**是否納入 H2 工項待決**。Obsidian 工作紀錄已寫 |
| eManager / MSU Scorecard | `AKMC\修正_AKMC-System_HourlyRate_YTD翻倍_20260720.sql`（7/20 17:29）| —（程式碼不發佈）| 待人工/待確認：對照表 `SCORECARD_MSU_KpiMgr_New` 重複 mapping 列去重腳本，**含對正式對照表的 DELETE**，本輪無法自檔案確認是否已執行；另 STEP 0 的「全表掃其他重複 KPI」結果未見記載，**可能還有別的 KPI 中招**。Obsidian 工作紀錄已寫 |
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

### 2026-08-04

> （本次排程於 2026-08-04 執行。掃 `D:\Work\專案` 六個專案比對三目的地，落差**全部集中在 eManager 單一專案、單一時間帶（08-03 13:49~18:15）**，且兩項皆為程式碼／工作檔性質：**(A) 發現先前完全未追蹤的新模組 `Sales By Product`**（SP 快照 08-03 18:15）；**(B) MSU Scorecard TW 線重啟**（指標規格工作簿整併＋MOPEX 樞紐核對，產出 8 項待確認清單）。**GitHub/Notion 本次無內容動作**：(A) 無設計文件且 GitHub/Notion 皆無對應位置，依規則不自行建立；(B) 唯一產物為核對用 xlsx（原始資料），SP 未動、KPI 定義未變 → **兩者皆僅 Obsidian**。）

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| eManager / **Sales By Product**（新模組） | `SP\SP_Rolling_Forecast_Prod_2026.sql`（08-03 18:15 新增，40.7 KB，UTF-16 LE）；同資料夾另有既有 `ASP\Sales_product_2026.asp`（05-20，本次未異動） | Obsidian **新建**「eManager Maintain Notes\開發記錄\Sales By Product.md」：系統位置（`[Global_Fin].[dbo].[SP_Rolling_Forecast_Prod_2026]`、Denodo 來源、`MFG26` 對照表與三層寫入標的）＋原始文件＋7 步架構摘要＋修改歷程（07-30 來源改 SAP／08-03 去 `Rolling_Date`＋移除週別快照）＋待確認 6 項。並登錄至「開發記錄總覽.md」清單、`專案盤點對照表.md` eManager 模組表新增一列。**GitHub/Notion 不動**（無設計文件＋無對應資料夾/子頁，歸屬待人工） |
| eManager / MSU Scorecard | `MSU Scorecard\TW\MSU-TW 自動化指標_0729.xlsx`（08-03 17:23 更新，9.3 MB／15 分頁）；`TW\.claude\settings.local.json`（08-03 16:33，工具設定不列入） | Obsidian「eManager Maintain Notes\開發記錄\MSU Scorecard.md」：**更新既有「原始文件」段**（新增此工作簿為現行指標規格＋核對主檔，列出 15 分頁組成）＋修改歷程新增「2026/08/03」列（8 張 MOPEX 樞紐＋逐項核對＋`待確認清單_0803` 8 項全文）＋**待確認段新增一項**（8 項全待對方回覆、3 項必問未答前 SP 不宜動）＋同步狀態新增 08-04 段。**GitHub/Notion 不動** |

> 本次（自動排程同步）掃 `D:\Work\專案` 比對三目的地，落差如下：
> **(A) 全域掃描結果**：六個專案（Budget Platform／eManager／Quota Platform／SBU Scorecard／TCP／SAP上雲）中，**08-04 當日零檔案異動**；08-01、08-02 為週末亦零異動。唯一增量落在 **08-03 13:49~18:15 的 eManager**（前一輪排程於 08-03 較早時段執行，故本輪才掃到）。Budget Platform 自 07-31 18:45 後無新異動，Quota Platform／TCP／SBU Scorecard／SAP上雲 均無異動。
> **(B) 🆕 發現未追蹤的新模組 `eManager\Sales By Product\`**：以 `Sales By Product|Sales_product|Rolling_Forecast_Prod` 全文檢索 `SYNC_LOG.md` **零命中**，`專案盤點對照表.md` 亦無此模組，Obsidian 各 vault 無對應筆記 → 確認為**首次進入同步視野**。資料夾內容＝`ASP\Sales_product_2026.asp`（05-20 舊前端，本次未動）＋`SP\SP_Rolling_Forecast_Prod_2026.sql`（08-03 18:15 新增）。SP 為 `[Global_Fin].[dbo].[SP_Rolling_Forecast_Prod_2026]` 的 SSMS `ALTER PROCEDURE` 匯出快照（腳本時戳 2026/8/3 17:33），處理鏈路＝Denodo `sap.iv_biprd_ztha_bo_outlook_month` 取當年 SAP 月別 Outlook（`PG`→Prod_Group、`PD`→Prod_Divi、`SCM_FCST`→預測值）→ 自我 LEFT JOIN `+1/+2` 月組出三個月滾動 `FORECAST1/2/3` → 寫 `Rolling_Forecast_Prod` → 13 幣別換算 → 產品階層彙總（Prod_Divi 小計／Prod_Group／`Grand Total`／MD-MD）→ 動態 SQL 依當月回寫 `MFG26..Sales_Product_Forecast` 的 `{FOB|Local} Rolling Forecast`／`M2`／`M3` 三種 `Tran_Type` → `Scorecard_Prod_N_Rolling`（M01~M12＋YTD 逐月累加）→ `Scorecard_Prod_N`。
> **(C) Sales By Product 的 08-03 變更（SP 註解自載）**：① **「不再依賴 `Rolling_Date` 控制時間，改由 SP 內部自行推算」**——`@intYear/@intMonth` 直接取 `YEAR/MONTH(GETDATE())`，切斷對外部日期控制表的相依；② 新增 **FX 完整月挑選**——從 `fx_dim` 以 `HAVING COUNT(DISTINCT currency_id)=13` 找 13 幣全齊的最新月份，當月匯率未更新時自動沿用最近一個月；③ **「資料來源改為 SAP 月別資料，移除 1wk~4wk 週別快照（含佔位列與日期比對更新）」**。承 07-30 的第一批改動（來源由 CRM `U_PD_POS`／`U_FORECAST_M`／`U_PD_MAPPING` 改 Denodo SAP，並連帶註解停用 `校正 Hierarchy`／`SBU FOB Rate` 換算 FOB 列／`NTD→TWD` 三段）。
> **(D) MSU Scorecard TW 線重啟（07-21 以來首次異動）**：`TW\MSU-TW 自動化指標_0729.xlsx` 於 08-03 13:49~17:23 整併為 15 分頁工作簿——`MSU-TW 自動化指標`（98 列規格：各廠 KPI 的來源 view／取用條件／公式／Q·H·Y 聚合口徑）＋`全部資料_check`（102 列）＋`模擬_改X_9列`＋以 `mopex_明細`（45,524 列）為底的 **8 張 MOPEX 樞紐**（TWM8 及其 ES(SMT、LABOR)／SMT／LABOR 細分、TWM9 及其 MH10／MH14、TWH1）＋`說明`（承 07-15 Config 改 X 檢查表）。核心產物＝新分頁 **`待確認清單_0803` 8 項**：**必問（影響 SP 修改）3 項**——① `Hourly Rate-Assembly` 是否扣 PG Charge（主表公式寫 `MOPEX / SAP產出工時(H)`，但黃底期望值 820.645 須用 `(MOPEX−PG Charge)×1000/工時` 才算得出；**且現行輸出月值有扣 PG、Q1/Q2/H1/YTD 未扣**——泛System Q1 現 974.00／扣 PG 應 1006.84，CTOS Q1 現 660.28／應 677.87）、② ATMC total 的 SMT／Labor 工時**新公式與打 V 現值矛盾**（新公式 SMT M01 應 4,970.14、Labor M01 應 125,856.8，但 check 表對「僅 LA 值」4,779.94／64,123.53 打 V；total SAP 產出工時 130,826.96 恰為新公式兩者相加，與打 V 現值不相容）、③ IC Burning／BCM 的 cost center 定案。**確認項（定義口徑）3 項**——④ LA `MOPEX(K)` 是否含 993024（母子項非子集、M01 差約 243K）、⑤ total `MOPEX-Labor(K)` 之 CTOS 部分是否扣 PG（PG 處理不對稱）、⑥ `MOPEX(K)(Include Outsourcing Cost)` 不含 IC Burning 是否刻意。**筆誤提醒 2 項**——⑦ check 表「產品吸收成本(K)-SMT」備註誤植（數字正確）、⑧ `MOPEX-後段(K)`＝`MOPEX-Labor(K)`／`SAP產出工時-人力(H)` 建議統一名稱。**「對方回覆」欄目前全空白**。
> **本次無任何對外 GitHub/Notion 內容動作**：(A) Sales By Product **無任何設計文件**（只有 SP＋ASP 程式碼），SP 依發佈集規則屬程式碼不逐一發佈；且 it-documents **無對應資料夾**、Notion「📊 eManager」下**無對應子頁** → 依「不自行建頁/建資料夾」規則，歸屬列待人工。(B) MSU 本次唯一產物為核對用 xlsx（原始資料／工作檔），**SP 未動**（`SP\` 最新仍為 07-20 前之版本）、**無新報告文件**（`報告\` 最新 07-08、`比對結果\` 最新 07-15）、**KPI 定義尚未變更**（8 項全待拍板）、SP 仍 pre-production → Notion MSU 子頁維持不動。GitHub 本次僅推 SYNC_LOG 與 sync-log.html。
> 🔴 **GitHub push 持續阻塞（前輪已報，本輪再累積一筆 → 共 12 個未推送 commit，起自 2026-07-17）**。本輪 `git push` 回 `fatal: could not read Username for 'https://github.com'`（憑證助手 `manager` 取不到認證、非互動環境無法輸入）。以 `git log origin/main` 核對，**遠端最後一個 commit 仍是 `bb261c3`（2026-07-17「發佈 OSF Commerce Insights ChangeLog + 同步紀錄 0717」）**，其後 07-20／07-21／07-22／07-23／07-24／07-27／07-29×2／07-30／07-31／08-03／08-04 共 12 次同步紀錄 commit **全部只在本機**。⚠️ 影響：**GitHub Pages 上的 `sync-log.html` 內容停在 07-17**，任何看線上版的人會少掉近三週的紀錄；本機 `SYNC_LOG.md` 與 `sync-log.html` 均為最新、內容無遺失。📌 **需 Hyman 處理**：重新登入 GitHub 認證（過往紀錄顯示憑證可能解析到錯誤帳號 `JHCtw`，須確認以 `HymanJiang` 登入），之後一次 `git push` 即可把 12 個 commit 全部補上。
>
> ⚠️ **本次三項提醒**：(1) 🆕 **`Sales By Product` 歸屬待決**——這是新一個「本機有、GitHub/Notion 皆無位置」的 eManager 模組，需 Hyman 決定是否納入 eManager 傘下建立資料夾/子頁；若要納入對外文件集，**需先撰寫模組設計文件**（現況只有程式碼）。(2) ⚠️ **Sales By Product 三點待查核**：SP **是否已部署正式 `Global_Fin`** 檔案未載明（純匯出快照、無執行/驗證紀錄）；`Rolling_Date` 停用改 `GETDATE()` 推算後，**補跑歷史月份與跨月夜間執行的行為**未見驗證；讀碼觀察 `UPDATE MFG26..Sales_Product_Forecast SET Total=…` 與 `UPDATE Scorecard_Prod_N_Rolling SET YTD=0` **兩處皆無 WHERE**，後者全表歸零但只補回 `@nowYear`，**其他年度 YTD 恐被歸零且不復原**（屬讀碼觀察、非確認缺陷，建議查核）。(3) 🔴 **MSU `待確認清單_0803` 的 3 項「必問」未答前 SP 不宜動**，其中「Hourly Rate-Assembly 月值有扣 PG／Q·H·YTD 未扣」是現行輸出已存在的口徑不一致，值得優先向 tina 確認。**前列所有待人工項目本輪均無進展**：Quota Platform 歸屬與資安細節兩道閘、Budget Platform 對外待決集（Manager 安全批角色矩陣待核可、信件 P0 bug 待部署窗口、H2 各工項待驗收、`20260731報告-2` 單檔版是否寄 PM）、正式站發版（＝2027 開循環絕對前提）、DBA 三件排程、SBU Scorecard SP-only 無設計文件、eManager HC Dashboard SBU Hierarchy 改版待拍板、eManager 改版框架文件群 placement 未定、MSU AKMC 修正腳本是否已執行、it-documents `_scripts\notion_sync\` 是否納入 repo、TCP 零星待人工。

### 2026-08-03

> （本次排程於 2026-08-03 執行。掃 `D:\Work\專案` 六個專案比對三目的地，**08-01～08-03 三天工作區零檔案異動**（週末）。唯一落差＝**07-31 16:10 排程同步後的傍晚增量（18:44~18:45）**：Budget Platform 測試報告資料夾「一輪一包」收尾整理。**純文件整理、無程式碼／DB／系統行為變動 → 僅 Obsidian**；GitHub 本次僅推 SYNC_LOG 與 sync-log.html，Notion 全數不動。）

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| Budget Platform | `執行計畫\測試報告\20260731報告-2\`（18:44 新建資料夾，收入 `測試報告_RBU完整重跑_20260731.md`＋`測試報告_RBU完整測試_20260731_單檔版.html`，**兩檔內容未變、僅由 `測試報告\` 根移入**，經 LastWriteTime 14:33／14:35 比對確認）＋`執行計畫\README_資料夾說明.md`（18:45 改寫） | Obsidian「Budget Platform Notes\Budget Platform 概覽.md」：**更新既有「原始文件」段**（測試線敘述改為 07-31 傍晚「一輪一包」定版，兩檔路徑由 `測試報告\` 根改為 `20260731報告-2\`，並補「寄 PM 用定版／3.46 MB／22 張截圖內嵌」）＋修改歷程新增「2026-07-31（傍晚·收尾）」列＋同步狀態新增 08-03 段。**GitHub/Notion 不動** |

> 本次（自動排程同步）掃 `D:\Work\專案` 比對三目的地，落差如下：
> **(A) 全域掃描結果＝近乎零落差**：六個專案（Budget Platform／eManager／Quota Platform／SBU Scorecard／TCP／SAP上雲）中，**08-01、08-02、08-03 三日無任何檔案新增或修改**（08-01 為週六、08-02 為週日）。工作區最新檔案時戳停在 **2026-07-31 18:45:13**。
> **(B) 唯一增量＝07-31 傍晚的測試報告資料夾收尾（18:44~18:45）**：因前一輪排程於 **16:10** 執行，此增量落在其後、本輪才掃到。內容＝把當日下午產出的 RBU 完整重跑報告由 `測試報告\` 根**移入新建的 `20260731報告-2\`**，與上午的 `20260731報告-1\` 對齊成「一輪一包」；`README_資料夾說明.md` 同步改寫：測試報告樹改列 `20260731報告-2\` 為 ⭐⭐ 最新並標注**「寄 PM 用定版」**（3.46 MB／22 張截圖全內嵌，§1 對照 PM 報告 8 條／§2 RBU-01~13 每項附圖／§3 Excel 佐證／§4 效能觀察／§5 殘留待辦）、`06` 腳本狀態更新為「07-30 RBU 已執行、07-31 回填 PMV-04／UPDL-01，**SBU/MSU/Manager 部分未執行**」、`02` 腳本加註「07-31 全項重跑（部署 20260731.1／`a69b6475`）、RBU-13 由 Blocked 轉 Pass」，並新增**「一輪一包慣例」**（每輪測試自成 `YYYYMMDD報告[-N]\`，截圖統一放 `screenshots\<輪次名>\`，單檔版已內嵌可獨立寄送）與三條判讀速記。
> **(C) 因此更新的是「既有內容」而非新增**：Obsidian 筆記的「原始文件」段原記載那兩個報告檔在 `測試報告\` 根，該路徑已因搬移而失準 → 本輪據實際檔案系統改寫該段，而非只在末尾追加一列。
> **本次無任何對外 GitHub/Notion 內容動作**：屬純文件整理（測試·驗收文件同歸 Budget Platform 對外待決集，含測試站 URL／內部 CC 代碼／實際預算金額），且**報告內容一字未改、系統之功能/KPI/邏輯零異動、修復仍只在測試站** → 僅 Obsidian。Notion「Budget Platform」頁維持 2026-06-17 概覽不動。GitHub 本次僅推 SYNC_LOG 與 sync-log.html。
> ⚠️ **本次兩項提醒**：(1) 📨 **`20260731報告-2\` 的單檔版已是 PM 定版**（README 自身標注「寄 PM 用定版」），內容完備可直接轉寄，**是否寄給 PM 待 Hyman 決定**——一併留意報告中對 PM 的兩點說明（PM#4 Marketing 只解決一半、用上傳「歸零」設計上不可行；PM#6 仍無法重現待 PM 提供原始失敗檔）。(2) 🆕 **it-documents 出現未追蹤的工具腳本 `_scripts\notion_sync\`**（`notion-sync.mjs`／`sync.ps1`／`mapping.json`，07-30 12:07 產出，至今未 commit）＝把 MD 推上 Notion 的輔助工具，token 讀自 `C:\Users\hyman.jiang\.claude\notion-token.txt`（**未硬編於檔內**）；惟 (a) 屬工具腳本而非模組設計文件、不在發佈集規則內，(b) `mapping.json` 唯一條目指向 **Quota Platform 白話說明**（歸屬未定、`pageId: null`）→ **不自行 commit，列待人工**由 Hyman 決定是否納入 repo。**前列所有待人工項目本輪均無進展**：Quota Platform 歸屬與資安細節兩道閘、Budget Platform 對外待決集（Manager 安全批角色矩陣待核可、信件 P0 bug 待部署窗口、H2 各工項待驗收）、正式站發版（＝2027 開循環絕對前提）、DBA 三件排程、SBU Scorecard SP-only 無設計文件、eManager HC Dashboard SBU Hierarchy 改版待拍板、eManager 改版框架文件群 placement 未定、MSU Scorecard 修正腳本是否已執行、TCP 零星待人工。

### 2026-07-31

> （本次排程於 2026-07-31 執行。掃 `D:\Work\專案` 六個專案比對三目的地，落差**全部集中在 Budget Platform 單一專案、單一時間帶（07-31 上午 10:40 ~ 下午 14:35）**：承 07-30 的 D1~D7 修復，本日走完「回歸複測 → 揪出部署後新迴歸 X1 並當日修 → 部署後複測 → RBU 全項完整重跑」，產出**兩份測試報告**（回歸複測輪＋完整重跑輪，各附單檔版 HTML）＋兩份測試腳本回填＋一份還原腳本＋約 25 張截圖與證據檔。**GitHub/Notion 本次無內容動作**：測試/驗收文件含測試站 URL、內部 CC 代碼與實際預算金額（歸 Budget Platform 對外待決集），且**修復仍只上測試站、正式站行為未變** → **僅 Obsidian**。）

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| Budget Platform | `執行計畫\測試報告\20260731報告-1\測試報告_RBU回歸複測_20260731.md`（11:35 新建）＋`_單檔版.html`（11:44）＋`執行計畫\06_測試腳本_上傳下載補測.md`（11:17 回填 PMV-04／UPDL-01 結果）＋`SP\_還原備份\還原_UPUL08_ACZ權限等冪測試_20260731.sql`（12:09 新建）＋`測試用下載檔案\2026073101\`／`2026073102\`（證據檔）＋`測試報告\screenshots\RBU回歸複測_0731\` | Obsidian「Budget Platform Notes\Budget Platform 概覽.md」：修改歷程新增「2026-07-31」列（①上午回歸複測 ②PMV-04 與加碼發現 ③同 pattern 掃描 ④部署後複測）＋**更新既有「原始文件」段**（測試線資料夾補 07-31 兩輪報告、兩個證據檔資料夾、三個截圖資料夾與還原腳本）＋**更新既有待確認第「07-30 新增·UI 抽驗未做」項為已完成**（劃線並註明 X1 迴歸）。**GitHub/Notion 不動** |
| Budget Platform | `執行計畫\測試報告\測試報告_RBU完整重跑_20260731.md`（14:33 新建）＋`測試報告_RBU完整測試_20260731_單檔版.html`（14:35，3.62 MB）＋`執行計畫\02_測試腳本_RBU.md`（13:08 全項結果回填）＋`測試報告\screenshots\RBU完整重跑_0731\`（約 20 張） | Obsidian 同筆記 07-31 列續段（⑤下午 RBU 完整重跑 13/13 ⑥PM 8 缺陷逐條結案 ⑦效能觀察）＋待確認**新增 5 項**（效能項待裁示／MSU 兩處同 pattern 待抽驗／Headcount 頁簽靜態 2024 需動共用範本待裁示／UPUL-08 是否已執行待確認／D4 DV 503 列與 D7 SBU-MSU 分支未同步）＋**更新既有兩項**（殘留清單追加 VA16 `TEST_20260731` 一列；`hotfix` 進正式站待決項追記 `a69b6475` 同樣只在測試站）＋同步狀態新增 07-31 段。**GitHub/Notion 不動** |

> 本次（自動排程同步）掃 `D:\Work\專案` 比對三目的地，落差如下：
> **(A) 上午·D1~D7 修復回歸複測（部署 `625b3aa9`，CC=EAMAR00／CAPEX 用 EFAFA01）**：D2（逛 CAPEX→Mass Data→整本上傳 200／2.5s＋綠 toast＋入庫，`window.URL` 全程完好）／D3（Jul–Dec input=2,416.67 與 Summary 一致）／D5（People Cost 範本 200／9.5s／449KB，原 146–297s）／D6（Total 列 29 格、末格 -68.27%）／D1（Summary 範本 200／26.3s／132KB，原 500）**全部驗過**。
> **(B) ❌ 但揪出部署後新迴歸 X1（D4 的迴歸）**：CAPEX 範本下載在測試站 EAMAR00／EFAFA01 都回 **500**，**本機跑同一段程式（D4 probe）卻通過**。Serilog 直讀定案根因＝`UnauthorizedAccessException: Access to '\\aclemanager-dev\...\CAPEX.xlsx' is denied`，炸點在 `XLWorkbook.SaveAs(Stream)`——**ClosedXML 由檔案路徑載入的活頁簿，`SaveAs` 時會以當下執行身分重開原檔**，而範本載入在 eMgrITD 模擬區塊內、D4 新增的 `SaveAs` 在區塊外 → IIS app pool 身分對 UNC 無權限；本機通過是因開發者帳號本來就有共享權限，**probe 測不出身分差異**。修法＝範本載入改 `new XLWorkbook(new MemoryStream(File.ReadAllBytes(path)))` 使活頁簿不綁檔案路徑。📌 **教訓：涉及模擬身分＋檔案的行為，本機綠燈不等於部署綠燈**。（排錯路徑備忘一併記入報告：測試站 web 主機 aclemanager-dev、`logs\myapp<日期>.txt` 可直讀；驗部署版本用 DLL 內 UTF-16 字串掃描，DLL 時戳因 deterministic build 不可信。）
> **(C) PMV-04：PM#7／#8 皆屬實＋加碼揪出更嚴重問題**：PM#7＝`GetSummaryWorksheet` 兩個 footer（Local／EURO）都漏寫 col 17 → 兩個 Total 列 FSCT GR% 空白；PM#8＝Total 列該格沿用範本**金額格式**，-0.7618 被顯示成「-1」；🔍 **加碼（比 PM 回報嚴重）＝Business Related／Others-Fix Expense 兩個頁簽從未被填資料**——分頁改名後 `DownloadTemplate_Summary` 的 switch 只留舊名 `Others` case，兩頁簽被原樣複製範本（表頭停 2024/2025、內容全 0），**PM 當時只看 GR% 欄所以沒發現**；與整本上傳 `b9bf4103` 同族的「改名遺漏」。三項＋X1 一併修於 **`a69b6475`**。
> **(D) 程式碼同 pattern 殘留掃描（背景 agent 全掃＋DB 查證）**：`SaveHeadcount_RBU` 用舊世代 StepID `4335F5E4`（DB 查證權限表 0 列／Step_Basic 不存在／Stage 0 列，新 GUID `4FEB8F7B` 有 35 列）→ 已修，**惟複驗後嚴重度下修**＝前端無任何呼叫點、People Cost 上傳走 repo 直存（`UploadHeadcount`+`UploadSalary`）不經此 service 方法＝**dead-path 防禦性修復**；`GetBudgetPlatformCurrentData` 空集合 `.Max()`（與 D1 同款例外路徑、API 可直達）補 `DefaultIfEmpty`；**D2 pattern 全站掃描已清零**（其餘約 60 處 `var URL` 皆在函式作用域內）；⏳ **D3 同 pattern 另有兩處 MSU-only 未動**——`GetRDCurrentData`（MSU 分支，FCST 後月份用前月平均覆蓋）與 `Get_BasicData`（MSU 分支，且 case 7–9 缺漏疑 copy-paste 漂移），待 MSU 輪抽一個 CC 對 Summary 核對後再裁定。
> **(E) 中午 `a69b6475` 部署後複測（部署 20260731.1）全過**：CAPEX 範本 **200／1.0s／17KB**（部署前 500），開檔 **DV 5/5**（A5/B5/C5/H5/M5 下拉全在）、「下拉式選單」來源 sheet 完好（B3=Asset Type、B4=Fixed Assets）、既有資產列正常帶出；Summary 範本 200／27.1s，開檔 **BR 頁簽=2026/2027 表頭＋9 列資料、Others-Fix=2026/2027＋34 列**（部署前＝範本原樣）、Summary 兩 Total 列 FSCT GR% **-76%（0% 格式）**（PM#7 結案）、R&D/Freight/T&E Total 列 GR% **-76.2%（0.0% 格式）**（PM#8 結案）。
> **(F) 下午·RBU 完整重跑（使用者指示「只測 RBU、做一次完整測試」，主 CC 改 OPKFS01／AEU-EU35-SEK-Nordic）**：**RBU-01～13 全部 Pass（13/13）**，兩項狀態升級——**RBU-13 Summary Group 由 07-22 的 Blocked 正式結案**（頁面 200／7.7s，EU01 篩選後表格 **408 列／2.0 秒**、`Download_SummaryGroup` 200／2.6s；真因是當時的 View 效能問題，已由 07-24 的 fn 改寫解決）、**RBU-09 由「檔案有下載」升級為實開 Excel 驗證**（下拉 5/5、來源頁完好＝PM Defect#3 結案）。寫入類 RBU-03～07 全走「改值 → DB 驗證 → 還原」**本輪零殘留**；RBU-12 Summary 守恆抽驗通過（Marketing 群組 Jul=649.1 ↔ 步驟頁 plan 649.08）。
> **(G) PM 測試報告 8 缺陷逐條結案：7 項已修復並實測驗證、1 項無法重現**。⚠️ **兩點給 PM 的重要說明**：① **PM#4 的 Marketing 只解決一半**——PM 的情境是「把第一版數字全部歸零再重新更新」，上傳修復後「重新更新」已完全正常（Marketing 6,001／BR 6,002／Others-Fix 6,003 全進畫面，截圖＋DB 時間戳雙證），但**用上傳的方式「歸零」在設計上不可行**（`ConvertFile_Marketing` 把全零列視為「無資料」直接略過，既不生效也不清既有項目），要清項目須用畫面 Delete，此行為已於 D7 訊息加註；**若要支援「上傳即歸零」需另立需求**。② **PM#8 追查時發現的兩頁簽未填比 PM 回報更嚴重**（見 (C)）。**PM#6 仍無法重現**：乾淨檔上傳成功入庫、混入 CAPEX 科目時整批交易性拒絕且訊息明確、**純 People Cost 科目檔反而成功**（與 PM 認知相反）→ 需 PM 提供原始失敗檔比對定案。
> **(H) 新發現＝效能觀察（P1，非缺陷）**：資料量大的 CC（OPKFS01）在下載類端點明顯偏慢——`DownloadTemplate_Summary` **196 秒**（EAMAR00 同日對照 27 秒）、整本範本 **121 秒**、`DownloadOverview` 17.8 秒、單步驟範本各 17.3~17.8 秒、各費用步驟頁各 16.5~16.9 秒（EAMAR00 為 3.0 秒）。拆解指向共用的 `GetRBU_BasicData` → CurrentData 查詢為主成本（每次約 16~17 秒），Summary 範本內含 5 次同類呼叫≈85 秒。📌 **報告誠實揭露：本日修復補上的 BR／Others-Fix 兩頁簽使 Summary 範本增加約 35 秒**（修復前「秒開但沒有資料」→ 修復後「有正確資料但變慢」），扣除後既有基準仍約 161 秒＝**主要慢因不是本次修復，但本次修復確實讓它更慢**。建議比照 07-24 的做法把 `GetRBU_BasicData` 的 CurrentData 查詢改走 `fn_..._ByCC`，或 Summary 組裝時一次查回 5 個步驟的 CurrentData 重用，預估可壓到 30 秒內。
> **本次無任何對外 GitHub/Notion 內容動作**：Budget Platform 測試/驗收文件屬操作性質（**無資安弱點細節**）但含測試站 URL／內部 CC 代碼／實際預算金額，歸對外待決集；且 `a69b6475` 與 07-30 的 `d3844e0c`／`625b3aa9` **一樣只上測試站、正式站行為未變** → **僅 Obsidian**。Notion「Budget Platform」頁維持 2026-06-17 概覽不動（**無任何功能/KPI/邏輯變更**）。GitHub 本次僅推 SYNC_LOG 與 sync-log.html。
> ⚠️ **本次四項提醒**：(1) 📌 **X1 的教訓值得跨專案套用**——涉及「模擬身分 + 檔案存取」的行為，本機 probe 綠燈不代表部署綠燈；D4 在本機 2/2 通過卻在測試站 100% 失敗，只有讀伺服器 Serilog 才定案。(2) 🔴 **`a69b6475` 只在測試站** —— 正式站發版前，Summary 範本的 BR/Others-Fix 兩頁簽在正式站**仍是空的**（且 D1/D2/D3/D5/D6 等舊碼缺陷同樣仍在），`hotfix/2026h2-uat2-bugfix` 是否進正式站待 Hyman 決定。(3) ⚠️ **UPUL-08（Manager `UploadPermission` ACZ 等冪測試）狀態不明**——還原腳本與存底檔（快照 15／7 列）皆已於 12:09~12:16 產出，**但 `06` 腳本的 UPUL-08 結果欄仍空白**，本輪無法自檔案確認是否已執行、是否需執行還原，列待確認。(4) ⚠️ **殘留再添一筆**：範圍收斂前對 SBU **VA16** 的單步驟上傳驗證留下 `Budget_Marketing` 一列（620300／`TEST_20260731`／Jan=731），併入上線前清理清單（`TEST_20260721`／`TEST_20260730` 清單不變）。**前列所有待人工項目仍無進展**：Quota Platform 歸屬與資安細節兩道閘、Budget Platform 對外待決集（Manager 安全批角色矩陣待核可、信件 P0 bug 待部署窗口、H2 各工項待驗收）、正式站發版（＝2027 開循環絕對前提）、DBA 三件排程、SBU Scorecard SP-only 無設計文件、eManager HC Dashboard SBU Hierarchy 改版待拍板、eManager 改版框架文件群 placement 未定、MSU Scorecard 修正腳本是否已執行、TCP 零星待人工。

### 2026-07-30

> （本次排程於 2026-07-30 19:05 執行。掃 `D:\Work\專案` 六個專案比對三目的地，落差集中在**兩個專案、兩個時間帶**：**(A) Quota Platform 07-29 傍晚 18:11~18:49**（前一輪排程 15:36 之後才產出，故本輪才掃到）＝收錄兩支 DB 端同步 SP 快照並補寫技術版第十八章；**(B) Budget Platform 07-30 全日 13:59~18:43**＝PM UAT 報告進來 → 上傳/下載缺口補測 → 7 個缺陷當日全數修復 → 執行計畫資料夾重整。**GitHub/Notion 本次無內容動作**：(A) 歸屬未定＋含資安弱點細節（兩道閘皆未清）、(B) 屬操作/驗收文件且修復只上測試站（正式站對外行為未變）→ **兩者皆僅 Obsidian**。）

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| Quota Platform | `同步舊平台資料 SP\QPF_SyncToOldTable.sql`＋`QPF_AddSbuQuotaAdjustment.sql`（7/29 18:11 新增）＋`docs\QuotaPlatform_程式架構整理.md`（18:45，17→**18 章**，54.3→60.4 KB）＋`docs\QuotaPlatform_白話說明.md`（18:46，補 7.4 節，20.7→22.3 KB）＋三份 `output\` 重生＋`CLAUDE.md`（18:16）＋`memory\sbu-quota-migration-project.md`（新增） | Obsidian「Quota Platform Notes\開發記錄\QuotaPlatform 架構整理.md」：**新增段落**「技術版第十八章：同步舊平台資料 SP」＋「原始文件」段補 `同步舊平台資料 SP\` 與檔案大小/章數**更新既有敘述**（17→18 章、54.3→60.4 KB）＋白話版段補「7.4 節」說明＋修改歷程新增 07-29 傍晚列＋**待確認新增第 7、8 點**（換年硬路徑 +2 且不在程式碼庫／`AddSbuQuotaAdjustment` 不可單獨重跑）＋**更新既有第 5 點**（SBU Quota 搬遷加註與同步鏈的交叉點）＋同步狀態新增 07-30 段。**GitHub/Notion 不動**（歸屬未定＋含資安弱點細節；SP 屬程式碼不逐一發佈） |
| Budget Platform | `PM測試報告\OPEX Budget Platform RBU Testing Report.docx`（13:59，PM 產出）＋`執行計畫\06_測試腳本_上傳下載補測.md`（新建，17:46 回填結果）＋`執行計畫\02_測試腳本_RBU.md`（15:30 追記）＋`執行計畫\00_測試腳本_執行說明.md`（17:47）＋`執行計畫\測試報告\測試報告_RBU上傳下載補測_20260730.md`（18:43 新建）＋`執行計畫\README_資料夾說明.md`（17:50 新建）＋`測試用下載檔案\`／`測試報告\screenshots\RBU補測\` 證據檔 | Obsidian「Budget Platform Notes\Budget Platform 概覽.md」：修改歷程新增「2026-07-30」列（PM UAT 8 缺陷／端點涵蓋盤點／補測結果／D1~D7 修復／資料夾重整）＋**更新既有「原始文件」段**（改寫為 07-30 重整後的測試線資料夾結構）＋待確認**新增 6 項**（修復後 UI 抽驗與 PMV-04、PM#6 索取原始檔、SBU/MSU/Manager 補測未執行＋2 裁定項、`TEST_20260730` 殘留與 PM 值被覆蓋、hotfix 分支是否進正式站）＋同步狀態新增 07-30 段。**GitHub/Notion 不動**（測試文件含測試站 URL／內部 CC／實際金額，歸對外待決集；修復只上測試站） |

> 本次（自動排程同步）掃 `D:\Work\專案` 比對三目的地，落差如下：
> **(A) Quota Platform — 07-29 傍晚增量（第十八章）**：工作區新收 `同步舊平台資料 SP\` 兩支 SP 快照（存於 **OPEXdb**、UTF-16），據以補寫技術版**第十八章**。關鍵事實＝**QPF 不是封閉系統**：它算出的正式結果每天被回灌到舊平台 `MFG26` 的報表表，還在看舊平台報表的單位看到的其實是新平台數字；這兩支 SP **不在 eManagerCoreAdmin 程式碼內**（全庫 grep 無呼叫）、也不屬三支 Console Job，而由 **DB 端每日排程「Update 2026 Quota」**執行（⚠️ Job 名稱本身含年份）。`QPF_SyncToOldTable`：RBU 正式結果（`CNY→RMB` 純改名）＋`QPF_Adjustment` 加總的 IMAX 列 → DELETE+INSERT `InterLock`；IMAX 月占比 → `Quota_Forecast_Rate`；SBU 段改從**人工上傳**的 `SBU_Quota` 彙總 ÷1,000 → `SBU_Quota_Forecast`（**雙寫 Linked＋本地**）——原「由 `QPF_Result` 推導」區塊已註解停用，註明「Phase 3 改為人工上傳」。`QPF_AddSbuQuotaAdjustment`：把 RBU（僅 USD 列）與 SBU 的逐月差額補成一列 `Quota-Adj` 寫回，使兩邊月總數一致（**只寫 Linked，不寫本地**）。**7 點觀察**：⚠️ 執行順序隱含相依（**單獨重跑第二支會不斷累積重複 `Quota-Adj` 列**，要等隔日整批覆蓋才歸正）／雙寫不對稱（本地那份永遠缺調整列）／🔴 **換年硬路徑再 +2 處且不在程式碼庫內**（`@Year=2026` ×2＋`MFG26` 路徑＋排程名稱）／`QPF_Adjustment` 無年份過濾／DELETE→INSERT 無交易包覆（中途失敗停在已刪未插）／單位幣別口徑（÷1000、`CNY→RMB`、只比 USD）**全無文件**／🔗 **與 SbuQuota 搬遷案交叉**——`SBU_Quota_Forecast` 正是搬遷來源表卻仍被此鏈路每日覆蓋，搬遷切換時點必須一併停用/改寫。白話版同步補 **7.4 節「算好的結果怎麼回流到舊平台」**與第十三章第 6 點。
> **(B) Budget Platform — 07-30 全日（PM UAT → 補測 → 當日修復）**：
> **(B-1) PM 交回 RBU 段 UAT 報告**（`PM測試報告\OPEX Budget Platform RBU Testing Report.docx`，4.1 MB）：PM 自行以 OPEX=**EAMAR00**／CAPEX=**EFAFA01** 完成測試，回報 **8 個缺陷**。逐項對照後標註進新腳本 0.5 節——有的是**我方追蹤清單沒有的新 bug**（PM#1 Marketing Plan 月份、PM#2 People Cost GR%）、有的**推翻我方主輪假設**（PM#3 CAPEX 範本下拉 → 主輪「PM 已驗過免開 Excel」前提不成立，已追記 `02_測試腳本_RBU.md`）、有的**疑似測到修復部署前版本**（PM#4/#5）。
> **(B-2) 端點涵蓋盤點揭露測試盲區**（新腳本 `06` 第 0 節）：**下載 10 個端點只實測 6 個**（`DownloadTemplate_Summary` 從未測到——COM-07 實際打的是另一個端點；`Download_SummaryGroup` 在 RBU-13 Blocked 後未補；07-23 新端點 `DownloadUploadSapErrorMessages` 從未 UI 實測），**上傳 6 個端點僅 1 個分支事後補驗**（單步驟 `UploadExcel` 完全未測、整本上傳只驗過 RBU 分支）。結論＝**07-23~24 的修復大量落在上傳路徑上，改過卻沒測的正是風險最高區塊**。
> **(B-3) 當日執行（RBU 全功能，SBU/MSU/Manager 依使用者指示 Skip）**：以加速法（fetch 批發下載＋`file_upload` 直塞 kendo 隱藏 input＋Excel COM 產測試檔＋alert override 捕捉）把原估 6–8 小時壓到 **約 2.5 小時**。通過項：範本下載 8 步驟（7 快 1 慢）、**單步驟上傳 8/8 全過**（含 marker 入庫驗證 5/5）、整本「歸零→重更新」PM 情境完成、`DownloadOverview` 重測 **17.0s**（原 82.6~98.9s，`5e4e9609` 生效）、Mass Data 診斷完成。
> **(B-4) 新缺陷 D1~D7**：🔴 **D1 `DownloadTemplate_Summary` HTTP 500**（2/2 重現；**PM 測時還能下載＝新迴歸**；根因＝RBU Marketing 分支硬編 StepID 在 DB 全年份 0 列 → 空集合 `Max()` 例外）／🔴 **D2 URL 污染**（`RBU_CAPEX.cshtml:172`、`RBU_Mass_Data_Uplaod.cshtml:53` 頂層 `var URL` 隨 partial 全域執行蓋掉 `window.URL` → **先逛 CAPEX/Mass Data 再整本上傳必炸「URL is not a constructor」**）／D3 Marketing Step 頁 2026 Plan 月份被 Jan–Jun 平均值預填（Summary 頁正確）／D4 CAPEX 範本資料驗證全滅（0 個）＋「下拉式選單」sheet 被使用者資料覆蓋／D5 People Cost 範本下載 **146~297 秒**（空參數 >12 分鐘，新發現）／D6 People Cost Total 列缺 GR% 儲存格（28 vs 29 格）／D7 Marketing「零值列＝無資料」語意誤導。**兩項判定**：**PM#4/#5 與我方 07-24 成功的矛盾不是部署時序，是 D2 的動線差異**（PM 先測 CAPEX 再整本上傳必中，我方直接上傳沒踩到）；**PM#6 無法重現「乾淨檔失敗」**（乾淨檔成功入庫、CAPEX 科目明確拒絕，惟**純 People Cost 科目檔可成功上傳**＝與 PM 認知相反，若該擋是規格缺口）。
> **(B-5) D1~D7 當晚全數修復**（使用者指示「只修 bug、不帶新功能上版」）：`hotfix/2026h2-uat2-bugfix`（自 master，收 D1/D2/D3/D5/D6 等正式站也存在的舊碼缺陷，`d3844e0c`）＋`BudgetPlatform`（D4/D7 屬 H2 新功能碼，`625b3aa9`）；兩分支已推遠端，**依裁示只推測試站、不進 master/正式站**。D5 修復 probe **297s → 11.0s**、D4 以 probe＋真 Excel COM 雙驗證（DV=5、選項清單完好）。
> **(B-6) `執行計畫\` 資料夾重整**：報告全部集中 `測試報告\`（一輪一包，07-22 主輪整包歸 `20260722報告\`）、盤點與待核可草案移 `盤點與草案\`、新增 `README_資料夾說明.md`（含「20260722 系列四檔＝同一份報告的四種包裝，不是四份報告」等判讀速記）。
> **本次無任何對外 GitHub/Notion 內容動作**：(A) Quota Platform 歸屬未定＋技術版含資安弱點細節（兩道閘皆未清，且 SP 屬程式碼不逐一發佈）；(B) Budget Platform 測試文件屬操作/驗收（**無資安弱點細節**）但含測試站 URL／內部 CC 代碼／實際預算金額，且**修復只上測試站、正式站行為未變** → 兩者皆僅 Obsidian。Notion 各頁維持不動（**無任何系統之功能/KPI/邏輯變更**）。GitHub 本次僅推 SYNC_LOG 與 sync-log.html。
> ⚠️ **本次三項提醒**：(1) 🔴 **D1/D2/D3/D5/D6 是正式站也存在的舊碼缺陷**，但依裁示 hotfix 分支未進 master → **正式站發版前這些問題持續存在**（尤其 D2 會讓使用者在特定動線下整本上傳必失敗、D5 People Cost 範本下載近 5 分鐘）；`hotfix/2026h2-uat2-bugfix` 是否進正式站待 Hyman 決定。(2) ⚠️ **殘留測試資料再添一批**（`TEST_20260730`，測試站＝正式 DB），且 **PM 第一版測試值 100/500 已被本輪歸零上傳覆蓋** —— PM 若回頭比對需先知悉；上線前清理清單請併計。(3) 📌 **QPF 換年檢查要跨出程式碼庫**——第十八章查明 DB 端還有 2 支寫死 `@Year=2026` 的 SP 與含年份的排程名稱，不在任何 grep 得到的程式碼路徑上。**前列所有待人工項目仍無進展**：Quota Platform 歸屬與資安細節兩道閘、Budget Platform 對外待決集（Manager 安全批角色矩陣待核可、信件 P0 bug 待部署窗口、H2 各工項待驗收）、正式站發版（＝2027 開循環絕對前提）、DBA 三件排程、SBU Scorecard SP-only 無設計文件、eManager HC Dashboard SBU Hierarchy 改版待拍板、eManager 改版框架文件群 placement 未定、MSU Scorecard 修正腳本是否已執行、TCP 零星待人工。

### 2026-07-29（第二次·當日下午排程）

> （當日第二次排程。上午那次（見下段）掃到零落差；之後 11:49~15:36 使用者在 **Quota Platform** 做了一整天文件工作 → 本輪掃到的落差**全部集中在 Quota Platform 單一專案**：技術版架構整理由 13 章擴寫為 **17 章**、**新建 13 章白話版**、新增 `md2html.py` 轉檔工具，並更新專案 `CLAUDE.md` 與 `memory\`。🔴 擴寫的第十五章揪出 **P0 提權漏洞**。**GitHub/Notion 本次無內容動作**：本專案歸屬仍未定（不自行建資料夾/建頁），且文件已含資安弱點細節（依規則不自動對外發佈）→ **僅 Obsidian**。）

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| Quota Platform | `docs\QuotaPlatform_程式架構整理.md`（11:49，13→**17 章**）＋`output\QuotaPlatform_程式架構整理.html`（11:50 重生） | Obsidian「Quota Platform Notes\開發記錄\QuotaPlatform 架構整理.md」：**新增段落**「技術版第十四~十七章深入整理（2026-07-29 新增）」＋修改歷程新增 07-29 列＋**更新既有「待確認」第 1 項**（原記載「不含資安弱點細節」已不適用）＋新增「同步狀態」段。**GitHub/Notion 不動**（歸屬未定＋含資安弱點細節） |
| Quota Platform | `docs\QuotaPlatform_白話說明.md`（15:00，新建 13 章）＋`output\QuotaPlatform_白話說明.html`（15:00）＋`output\Quota Platform 白話說明.md`（15:08，去 H1 的 Notion 匯入版） | Obsidian 同筆記**新增段落**「白話版文件（2026-07-29 新建）」＋修改歷程新增列＋待確認新增「白話版待上傳 Notion（位置未指定）」。**Notion 不動**：匯入版已備好但**使用者未指定放在哪個頁面/資料庫下** → 依規則不自行建頁 |
| Quota Platform | `tools\md2html.py`（13:40 新增）＋`CLAUDE.md`（15:36）＋`memory\MEMORY.md`／`quota-platform-source-and-doc.md`／`qpf-doc-pending-followups.md`（15:35） | Obsidian 同筆記「原始文件」段補上工具與文件更新流程（改 `.md` → `python tools\md2html.py <src> <dst>` 重生 HTML）＋待確認補「使用者本人無 SBU 平台權限」。**GitHub/Notion 不動**（工具/專案設定/AI 記憶檔非設計文件） |

> 本次（自動排程同步）掃 `D:\Work\專案` 六個專案比對三目的地，落差**全部集中在 Quota Platform**（其餘五個專案自上次同步後零檔案異動）：
> **(a) 技術版擴寫 13 章 → 17 章**（`QuotaPlatform_程式架構整理.md`，25 KB → **54.3 KB**）：以 4 個並行 Explore agent 深讀 `D:\Project\eManagerCoreAdmin` 原始碼後補上四章——
> **十四 其他上傳流程（CurrentYearQuota／TopDown／Memo／Adjustment）**：實作品質**遠比 GrowthRate 粗糙**，五種上傳橫向對照顯示驗證逐項遞減。**`Adjustment` 是孤兒功能**——上傳僅 5 行、**驗證 0 道**、寫入為 `truncate table QPF_Adjustment` **不帶 WHERE**（RBU 上傳會清掉 SBU 與所有年度）、未走交易，且**全 codebase 無任何下游消費者**（`RefreshResult` 完全沒引用）→ 上傳的數字不影響任何計算，最該優先處理或直接下架。**Memo 越權刪除不對稱**：下載只給權限範圍內的列、刪除卻整平台整年度全刪 → 部分權限者「下載→改一行→上傳」會把別人的 Memo 全刪。**TopDown 靜默失敗**：純 UPDATE，比不到的列不 INSERT 也不報錯，畫面仍顯示成功。**CurrentYearQuota**：全刪重建但 DELETE 與 INSERT **分屬兩個交易**（INSERT 失敗即整年資料毀）、無稽核表不記 UpdatedBy、SBU 下載疑似 Bug（`#EmptyQuota` 誤從 `#RbuHierarchyNoQuota` 取 → SBU 永遠拿不到新階層空白列）、先解鎖後寄信（寄信失敗不回滾且永不補寄）、`@ThisWednesday` 時間陷阱（週一/二上傳會把全部階層列成 Added）。
> **十五 Permission 權限機制（最重要）**：後端只有 `[Authorize]`（僅驗有登入 eManager），**RoleType 的授權判斷全 codebase 只在前端 `Index.js` 三個 if，後端沒有任何一處用 RoleType 做授權決策**。🔴 **P0 提權漏洞**＝`POST Permission` 全鏈路無角色檢查，任何在 `QPF_Permission` 有一列的登入者（含 RoleType=User）可直打 API 上傳自製 Excel 把自己設為 PowerUser、取得平台完整控制權。🔴 **P0 破壞性上傳無權限限縮**＝CurrentYearQuota／Memo／Permission／Adjustment 皆「全刪重建」，單一 Region 權限者也能影響全平台。另：`GET Permission/Download` 回全公司 Email×角色×階層對照表無角色檢查；`GetUserPermission` 無 ORDER BY → 多列角色不一致時前端有效角色不確定；`CreateRolePermission` 同步 eManager `RolePermission_UsersRole` **只 INSERT 從不 DELETE**（RoleIndex GUID 硬編）→ 移除權限者殘留；`Enum.TryParse` 缺 `IsDefined`；`GetHierarchyByPermission` 缺 PlatformType → 跨平台階層外洩；SwitchToPhase2／Reset 測試端點部署在正式 Controller 且任何登入者可打。
> **十六 每日排程 RefreshSourceAndOthers**：**Job 鎖殘留**（`FinishJob` 補在 try/catch 而**非 finally**，進程被 kill 則 `IsRunning` 永遠留 1，連帶封鎖前台 CurrentYearQuota 上傳且無自動清理）；**19:00 節流早退副作用**（週三/週五分支跑在節流判斷之前 → EAI 失敗當天仍用舊資料判斷「無異動→解凍」並執行改名）；**純改名週永遠不會自動解凍**（比對以名稱為鍵，純改名＝1 Added+1 Deleted）；效能主因＝`RefreshHierarchy` 對 PG/PD 做完全笛卡兒積（CommandTimeout 3600 秒**只設在 ConsoleApp**，Web 端 `SwitchToPhase2`／`Confirm` 走同一批重 SQL 仍是 Dapper 預設 30 秒）；整條鏈路**零通知**（只寫 `logs/myapp.txt`）；四段大交易分離中途失敗即顯示不一致無回滾；換年硬路徑共 **5 處 MFG26＋2 處 MFG25（測試假資料與正式差一年）＋3 處 Service 年份**，其中 3 處 Linked Server 路徑無 Hardcode 註記容易漏改。
> **十七 前端 UI 結構**：**表頭年份 2024~2028 硬編 30 處**（RBU/SBU 各一份）與 `pageConfig.year` 脫鉤＝前端最大維護痛點；凍結用 Bootstrap `.disabled` class，對 `<button>` **只是視覺樣式不會阻止 click** → 前端凍結亦可繞過；兩區共用 `tableConfigByPlatform` 互相汙染（Formal 選 Group ViewType 會讓 Unconfirmed 表格少欄）；頁面**無任何平台/年度切換 UI 也無選單入口**（只能靠 query string）；初始化 8 次 HTTP 往返全序列化；下載一律 `window.open` 被彈窗封鎖器無聲攔截；`showErrorAlert` 缺 optional chaining（網路層錯誤時 error modal 自己拋 TypeError）；上傳無 CSRF token；Reset 是永遠不顯示的死按鈕但端點是活的。
> **(b) 新建白話版文件（13 章）**（`QuotaPlatform_白話說明.md`，20.7 KB）：不含程式碼行號，給非開發人員／不想看程式碼的人，把技術版轉譯成營運語言——平台是什麼／**進入與切換 RBU-SBU＝只能改網址**／三角色能做什麼／**年度四階段時間軸**（準備期→Phase 1 填 GR%→Switch to Fixed Amount 不可逆→Phase 2 填金額）／日常作業流程／結果計算概念版（FCST=max(A+Q, A+B)）／**三支排程 Job 與週三-週五額外任務**／**凍結是刻意設計非故障**／**公司架構變動維護 SOP 五步**（改名與刪除全自動、新增才要人補）／PowerUser 其他工作（含 Adjustment「建議先不要用」）／**權限建立維護＋與 eManager Role Permission 的關係**（11.4 釐清常見誤區：在 Role Permission 加人**不能**讓人進 QPF，同步方向是 QPF→Role Permission 且**只加不減**）／疑難排解對照表／給接手搬遷者的白話提醒。另產 `output\Quota Platform 白話說明.md`＝去掉 H1 的 **Notion 匯入版**。
> **(c) 工具與專案設定**：新增 `tools\md2html.py`（Markdown→HTML，沿用既有版型），文件更新流程定案為「改 `docs\*.md` → `python tools\md2html.py <src> <dst>` 重生 HTML」；`CLAUDE.md` 與 `memory\`（3 檔）同步記錄兩份文件現況與下次接續待辦。
> **本次無任何對外 GitHub/Notion 內容動作**（三重理由）：① Quota Platform 為**新專案、歸屬仍未定**（it-documents 無對應資料夾、Notion「📊 eManager」下無對應子頁）→ 依規則不自行建資料夾/建頁；② 技術版第十五章**含明確資安弱點細節**（P0 提權漏洞的確切端點與行號、硬編 RoleIndex GUID），白話版第十三章亦有對應白話陳述（「繞過畫面直打 API 可把自己升成 PowerUser」）→ 依規則**不自動對外發佈**；③ 白話版 Notion 匯入版雖已備好，但**使用者未指定放在哪個頁面/資料庫下** → 不在不確定位置建頁。故工作內容**僅進 Obsidian**，Notion 各頁維持不動（QPF 系統本身無變更，只是被記錄下來）。GitHub 本次僅推 SYNC_LOG 與 sync-log.html。
> ⚠️ **本次新增三項提醒**：(1) 🔴 **QPF 後端完全沒有角色授權**——`POST Permission` 可自我提權（P0）、四種破壞性上傳無權限限縮（P0）、Confirm/Reject 無 Gatekeeper 後端檢查、測試端點 SwitchToPhase2/Reset 部署在正式 Controller 任何登入者可打。**搬遷/改版設計時務必補後端角色檢查**；是否列為獨立修補工項待 Hyman 決定。(2) 📌 **Quota Platform 對外發佈現在有兩道閘**（原本只有「歸屬未定」一道）：歸屬拍板**之後**仍需就資安弱點細節另行核可，或先產出去敏感版。(3) **白話版 Notion 匯入待指定位置**＋**使用者本人尚無 SBU 平台權限**（其 eManager 角色 E3 與 QPF 無關，需 SBU PowerUser 用 Permission Excel 加入或 DBA 直接 INSERT `QPF_Permission` PlatformType=2），07-29 當天未解決。**前列所有待人工項目仍無進展**：Budget Platform 對外待決集（Manager 後台安全缺口角色矩陣待核可、View 效能第二階段成效未經正式站證實、信件 P0 bug 待部署窗口、H2 各工項待驗收）、正式站發版（＝2027 開循環絕對前提）、DBA 三件排程、SBU Scorecard SP-only 無設計文件、eManager HC Dashboard SBU Hierarchy 改版待拍板、eManager 改版框架文件群 placement 未定、MSU Scorecard 修正腳本是否已執行、TCP 零星待人工。

### 2026-07-29（第一次·當日上午排程）

> （當日第一次排程。掃 `D:\Work\專案`（Budget Platform／eManager／Quota Platform／SAP上雲／SBU Scorecard／TCP 六專案）比對三目的地，並核對 it-documents git 狀態。**結果：自 07-27 同步後，`D:\Work\專案` 底下無任何 `.md/.html/.sql`（實則任何副檔名）檔案異動** → 無新增未發佈、無已改版需更新的設計文件。it-documents git 工作區乾淨、HEAD 即 07-27 同步 commit（`e3765b3`）。**該輪無任何 GitHub/Notion/Obsidian 內容動作**，僅記錄掃描結果。當日 11:49 起才有 Quota Platform 的新工作，見上一段。）

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| （全部） | — 無新異動 — | — 該輪無同步動作 — |

> 該輪（自動排程同步）掃 `D:\Work\專案` 比對三目的地，自 07-27 排程同步後**零落差**：六個專案資料夾中沒有任何檔案的 LastWriteTime ≥ 2026-07-27，代表這兩天沒有新的產出文件或改版。it-documents repo `git status` 乾淨、最新 commit 仍為 07-27 同步紀錄，發佈狀態與檔案系統一致。
> **所有先前列於「❌ 待同步」的項目維持原狀、無進展**（皆為需人工決策者）：Quota Platform 新專案 GitHub/Notion 歸屬未定；Budget Platform 對外待決集（含 Manager 後台安全缺口角色矩陣草案·含資安弱點細節不自動對外、View 效能第二階段成效未經正式站證實、信件 P0 bug 待部署窗口、H2 各工項待驗收）；SBU Scorecard SP-only 無設計文件；eManager HC Dashboard SBU Hierarchy 改版待 Revenue 策略/PG 來源拍板；eManager 改版框架文件群 placement 未定；MSU/TCP 零星待人工。
> **該輪無對外動作**：無系統之功能/KPI/邏輯變更 → Notion 各頁維持不動；無設計文件新增/改版 → GitHub 無新 HTML；Obsidian 各 vault 無新工作內容。GitHub 僅推 SYNC_LOG 與 sync-log.html（記錄一次「無落差」掃描）。

### 2026-07-27

> （本次排程於 2026-07-27 執行。掃 `D:\Work\專案` 比對三目的地，自 07-24 16:05 同步後的落差有兩塊：**(A) Budget Platform 07-24 傍晚增量**（16:05 排程後才產出）＝View 效能第二階段收斂＋Manager 安全批角色矩陣草案；**(B) Quota Platform ＝一個全新專案**（07-25，架構整理＋SBU 搬遷建議）。(A) 屬 SQL 程式碼／含資安弱點細節之安全草案 → 僅 Obsidian，GitHub/Notion 待人工。(B) 為新專案、GitHub/Notion 歸屬未定 → 依規則不自行建頁/建資料夾，列待人工；已建 `Quota Platform Notes\` vault 記工作內容。**GitHub 本次僅推 SYNC_LOG 與 sync-log.html，Notion 各頁不動**（無任何系統之功能/KPI/邏輯變更，且新專案歸屬未定）。）

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| Budget Platform | `SP\View效能_第二階段\00_說明.md`（定稿）＋`部署02` 更新＋`部署04_fn_BudgetPlatform_OverviewRBU.sql`＋`_還原備份\還原_View效能第二階段_fn.sql` 更新（7/24 傍晚）／`執行計畫\安全批_角色矩陣草案_20260724.md`（7/24 傍晚） | Obsidian「Budget Platform Notes\Budget Platform 概覽.md」：修改歷程新增「2026-07-24（傍晚追補）」列（View 效能收斂＋安全批角色矩陣兩筆）＋更新待確認（View 驗證已記實測 0.41/0.45s·16/16 全 0、OverviewRBU 已新增 部署04、新增安全批待核可項）＋同步狀態新增 07-27 段。**GitHub/Notion 不動**（SQL 屬程式碼；角色矩陣草案含資安弱點細節不自動對外；函數是否正式上線／C# 是否 merge 未確認，系統對外行為未變）|
| Quota Platform（新專案）| `docs\QuotaPlatform_程式架構整理.md`＋`output\...html`＋`docs\SBU_QuotaForecast_資料搬遷建議.md`＋`CLAUDE.md`／`memory\*`（7/25） | Obsidian **新建 vault**「Quota Platform Notes\開發記錄\QuotaPlatform 架構整理.md」（維運視角摘要：系統位置／四層架構／GR% 審核流／RefreshResult 計算／Hierarchy Block 凍結／SBU 搬遷建議／待人工）。**GitHub/Notion 待人工**：新專案歸屬未定，依規則不自行建 it-documents 資料夾/Notion 頁 |

> 本次（自動排程同步）掃 `D:\Work\專案` 比對三目的地，自 07-24 16:05 同步後落差為：
> **(A) Budget Platform — 07-24 傍晚兩筆增量**（上次排程 16:05 執行，這兩筆 17:50 前後才產出，故本輪才掃到）：
> **(A-1) View 效能第二階段收斂**（`SP\View效能_第二階段\00_說明.md` 定稿）：延續 07-24 白天開工的「不改既有 View、改新增兩支先過濾再組裝 TVF」路線，`00_說明.md` 補齊實測與部署狀態——`fn_BudgetPlatform_BudgetData_ByCC` **0.41s**（原 161.8s）、`fn_BudgetPlatform_CurrentData_ByCC` **0.45s**（原 7.9s），兩支稱「**已部署 2026-07-24**」；**等值驗證 16/16 全 0**（EAMAR00／OPKFS01／VA16／CTOS製造 ×兩函數×雙向 EXCEPT，BudgetData 閘門改寫後另補 8 項複驗）。C# 消費端於分支 `feature/2026h2-view-perf`（→ BudgetPlatform）把 `BudgetPlatformRepository_RBU.cs` 六個方法改 FROM 函數（簽名不變、順帶 IN 字串內插改參數化 CSV）。**新增 `部署04_fn_BudgetPlatform_OverviewRBU.sql`** ＝著手處理前列標「未納入本次範圍」的 **COM-06 剩餘 99 秒 `vw_BudgetPlatformOverviewRBU`**。教訓記載：mTVF 內逐列 `NOT EXISTS` 對 51.9 萬列 snapshot 表會退化成每列全掃（83.7s），凍結區清單須先落表變數再 `NOT IN`。
> **(A-2) Manager 安全批（P0-2）角色矩陣草案**（`執行計畫\安全批_角色矩陣草案_20260724.md`）：把 7/23 Manager 後台盤點揭露的安全缺口從「等定義」推進到「等核可」。盤現有角色（Admin／Global Finance／SBU Finance／{Region} Finance ×20／Owner ×5／Viewer ×4／SBU HQ／ATW MKT／TEST），提**12 個功能群 × 建議允許角色**矩陣（Costcenter／權限個別維護／Cost Element／FSCT GR%／Average Salary／Plan Rate／Date＝Admin+Global Finance；RoleSetting／UploadPermission＝僅 Admin；Upload SAP 維持 07-17 定版），實作＝泛化 `IsUploadSapAllowed` 成共用 `RequireRoles(...)`＋PagesController 加 class 級 `[Authorize]`＋`User` 改取 Claims、不改資料表不影響前台。三個待 Hyman 拍板問題（{Region} Finance 是否保留任何 Manager 寫入、SBU Finance 是否需 Upload SAP 以外寫入、TEST 角色是否清掉）。
> **(B) Quota Platform — 全新專案**（`D:\Work\專案\Quota Platform\`，7/25）：模組內部代號 **QPF**、原始碼在 `D:\Project\eManagerCoreAdmin`（與 Budget/TCP 同方案）、頁面 `/Admin/QuotaPlatform/Index`。整理出四層架構（Web 22 端點／Service 1,227 行含 Excel／Repository 4,581 行 Dapper 手寫 SQL 無 SP／14 張 `QPF_*` 表／3 Job）＋三章深入（GR% Confirm/Reject 審核流以 `IsFormal` 旗標＋覆蓋式 Confirm、RefreshResult 每次整年全量重算 RBU+SBU 兩平台的效能熱點、Hierarchy Block 階層換版凍結且僅前端擋）。另一份 `SBU_QuotaForecast_資料搬遷建議.md`＝舊 ASP `SBU_Quota_Forecast` 搬到新 `dbo.SBU_Quota` 的維度落差分流與搬遷步驟（8 個業務決策點未答、未執行）。
> **本次無任何對外 GitHub/Notion 內容動作**：(A-1) View 效能為 SQL 程式碼、(A-2) 安全批角色矩陣**含明確資安弱點細節（依規則不自動對外發佈）**、(B) 為新專案且 it-documents/Notion 皆無對應歸屬（依規則不自行建頁/建資料夾）→ 三者皆列待人工，工作內容進 Obsidian。Notion 各頁維持不動（無任何系統之功能/KPI/邏輯變更）。GitHub 本次僅推 SYNC_LOG 與 sync-log.html。
> ⚠️ **三項提醒**：(1) 🔴 **Manager 後台安全缺口仍未修**——角色矩陣草案已備、待 Hyman 核可＋回答三問即可動工（估 1-2 天）；含資安弱點細節故不自動對外。(2) ⚠️ **View 效能第二階段成效仍未經正式站證實**——`00_說明.md` 雖記實測 0.41/0.45s 與 16/16 全 0，但**兩支函數是否已於正式 `OPEXdb` 上線、`部署04` OverviewRBU 是否已部署、C# 分支 `feature/2026h2-view-perf` 是否已 merge/切換皆未載明**（還原檔警示：C# 已切則退函數須連 C# 一起退，否則 Summary 會 500）。(3) 📌 **Quota Platform 歸屬待 Hyman 決定**（納 eManager 傘下 or 平行），決定後才能建 it-documents 資料夾與 Notion 頁對外發佈。**前次列的尾巴仍無進展**：正式站發版（＝2027 開循環絕對前提）、DBA 三件排程、工項3 分時段排程本體待 E3 冪等確認、ZRCO18 上游補檔、Manager 第一批 `47a980ca` 補實測、信件 P0 bug 待部署窗口、`feature/2026h2-mail-batch` 待 merge、SBU-10 Finish 待人工點一次、MSU Scorecard 修正腳本是否已執行/是否還有其他重複 mapping。

### 2026-07-24

> （本次排程於 2026-07-24 執行。掃到自 7/23 同步後的落差仍全在 **Budget Platform**，且測試線收斂後**新開兩條線**：**信件功能全面盤點揪出一個從未正確運作過的 P0 bug 並備妥優化包（未上版）**、**View 效能第二階段開工**（直接回應 7/23 定案卻未解的 161.8 秒瓶頸）；另把測試報告收成可交付成品。屬程式碼／盤點／驗收文件 → **僅 Obsidian**。**GitHub/Notion 本次無內容發佈**，Notion 頁不動（信件包未部署、View 函數未確認上線，系統對外行為未變）。）

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| Budget Platform | `執行計畫\測試報告_20260722.md`／`.html`（7/23 17:02，改寫為結案版）＋`測試報告_20260722_單檔版.html`（9.13 MB，7/23 17:12）＋`測試報告_20260722_含截圖.zip`（4.58 MB）＋`PM測試資料\Overview_EAMAR00.xlsx`（7/23 23:38） | Obsidian「Budget Platform Notes\Budget Platform 概覽.md」：新增段落「信件功能全面盤點與優化包 ＋ View 效能第二階段開工（2026-07-23 晚 ~ 2026-07-24）」之 ①。**GitHub/Notion 不動**（含測試站 URL／內部 CC 代碼／實際預算金額，同歸 Budget Platform 對外待決集）|
| Budget Platform | `執行計畫\優化盤點_信件功能_20260723.md`（7/23 18:06）＋`SP\信件優化_20260723_待部署\`（`00_執行說明.md`／`01_新表_MailLog與收件人設定表.sql`／`02_ALTER_SP_Budget_SendRfcLog.sql`／`03_ALTER_SP_Budget_CostcenterLockMonitor.sql`，7/23 18:18~18:26）＋還原檔 ×3（`還原_信件優化_新表_20260723.sql`／`_SP_Budget_SendRfcLog_`／`_SP_Budget_CostcenterLockMonitor_`） | Obsidian 同上段之 ②③＋修改歷程新增「2026-07-23（晚）」列＋待確認新增 3 項。**GitHub/Notion 不動**（盤點含內部收件人信箱與名單規則、SQL 屬程式碼；**無資安弱點細節**但仍歸對外待決集；包未部署故系統未變）|
| Budget Platform | `SP\View效能_第二階段\部署01_fn_BudgetPlatform_BudgetData_ByCC.sql`／`部署02_fn_BudgetPlatform_CurrentData_ByCC.sql`／`驗證03_等值與計時.sql`（7/24 15:42）＋`SP\_還原備份\還原_View效能第二階段_fn.sql`＋`快照_Timer_20260724_Date抽驗前.txt`（7/24 15:18） | Obsidian 同上段之 ④⑤＋修改歷程新增「2026-07-24」列＋待確認更新（原「View 效能第二階段是否排入 H2」改為已開工）＋同步狀態新增 07-24 段。**GitHub/Notion 不動**（SQL 屬程式碼不逐一發佈；函數是否上線未確認）|

> 本次（自動排程同步）掃 `D:\Work\專案` 比對三目的地，自 7/23 同步後落差為：
> **(a) ❌ 信件功能盤點——挖出一個從未正確運作過的 P0 bug**：應使用者要求做全平台信件唯讀盤點（`優化盤點_信件功能_20260723.md`），範圍＝OPEXdb 的 DB 端寄信 SP ＋ `eManagerCoreAdmin` 應用端 SMTP。盤出 **3 個運作中＋1 個休眠**：① **SAP 拋轉結果信**（`SP_Budget_SendRfcLog` → `SP_SendMail_WithFile` → msdb dbmail，隨每次拋轉）② **SBU 催辦信**（App 端 `SendSbuReminder`＋`SbuReminderHostedService` 每 15 分檢查，⏸ 兩站開關都關——測試站開啟＝會真寄 226 位 Owner）③ **Cost Center Lock 監控信**（每日 08:00 排程，✅ 運作中）④（休眠）**FSCT 重算結果信**（`EXEC SP_SendMail_WithFile` 被註解＝死碼）。**最重要發現**：①的成敗判斷 `@ErrorCount = COUNT(*) FROM BudgetUploadSAPErrorMessages WHERE BatchID=@BatchID` **把 `Success` 列也算成錯誤**——RFC 回寫慣例是成功列也寫進這張表，**實測 432 個批次中 287 個是全部 Success 列**，卻一律掛 `- Failed` 主旨、走錯誤表格與錯誤明細附件 → **成敗分流從未正確運作過**；修法只是一行 `AND LTRIM(RTRIM(ErrorMessages)) <> 'Success'`。另盤出共通問題：收件人／CC **硬編在 SP 本體**（Hyman＋Tina 的 CC、`BI.FA`／`Global.Finance` 散落 SP 與 C# 常數，人員異動要改 SP 本體、離職者殘留前例＝Lilith）、**dbmail 寄信歷史無法自查**（`eManagerSa` 無 msdb 檢視權 → 07-18 Lock 信寄達與否至今無法確認即此因）、`EmailHelper` 的「測試站主旨標註」被註解掉＝**測試站誤觸寄信與正式信無法區分**。優化建議 7 項排序 P0-1 → P1-2/P1-3 → P2-4/P2-5 → P3-6/P3-7。
> **(b) 📦 信件優化待部署包——依指示「做完先不上版」，全部備妥未執行**：`SP\信件優化_20260723_待部署\` 三支 SQL 依序＝新表（`Budget_Mail_Log` 寄信記錄＋`Budget_Mail_Recipients` 收件人設定表，種子＝現行 CC 名單）／`SendRfcLog` **修 P0 成敗判斷**＋Failed 分支表格與 CSV 也排除 Success 列＋CC 讀設定表＋寄後落 log／`CostcenterLockMonitor` 加 **Active↔UploadSAP 單向連動**（Active 變 'X'→自動關 UploadSAP，**恢復 Active 不自動開**以免蓋掉管理者刻意關閉的設定；編輯權不受影響）＋信件加 UploadSAP 欄與 Auto-disabled 標記＋CC 讀設定表＋落 log。三還原檔皆備，⚠️ **退還原時兩支 SP 與新表必須一起退**（新版 SP 讀設定表／寫 log，表不在會炸）。App 端分支 `feature/2026h2-mail-batch`（commit `a4eac56d`，**已推遠端、未 merge**）＝`EmailHelper` 支援 `SMTP:SubjectPrefix`，測試站 appsettings 設 `"[Testing] "` 即全站信件主旨自動加前綴、正式站不設＝零影響。設計決策三則：`Removed`（CC 從 SAP 主檔消失）**不**納入自動關閉（可能是主檔暫時性缺漏，先只通報，觀察一輪再議）；FSCT 死碼信段**刻意不動**（`SP_Budget_FSCT` 是最關鍵 ETL，純美化不值得碰）；SBU 催辦信不落 `Budget_Mail_Log`（已有自己的 `Budget_SBU_Reminder_Log`）。
> **(c) ✅ View 效能第二階段開工——7/23 定案卻未解的 161.8 秒瓶頸，7/24 有解法了**：作法是**不改動既有 View，改新增兩支「先過濾再組裝」的 TVF** 讓消費端改呼叫——`fn_BudgetPlatform_BudgetData_ByCC(@BudgetYear, @CostcenterIDs)` 取代直查 `vw_BudgetPlatformBudgetData`（單 CC **161.8s**）、`fn_BudgetPlatform_CurrentData_ByCC(@CurrentYear, @CostcenterIDs)` 取代 `vw_BudgetPlatformCurrentData`（單 CC 7.9s／IN 批次 18.7s）。**關鍵診斷＝三張 Summary View 各自帶 `Costcenter_ID` 條件時謂詞推得下去（實測 0.3~0.4s），慢的是外層 view 把三張 View 全量實體化後才 LEFT JOIN** → 函數先解析 CC 清單、逐支帶條件拉小結果、記憶體組裝即可繞開，語意與 view 的即時支＋凍結支等值（`σ(A∪B)=σ(A)∪σ(B)`，UNION 去重語意不變），**目標 <1 秒**（註解稱原型已雙向 EXCEPT=0 驗證）。實作細節：相容性等級 100 無 `STRING_SPLIT` → CSV 拆分改用 XML 法；凍結支 snapshot 沒存 `Costcenter_ID`，以「名稱＋區」對回。`驗證03_等值與計時.sql` 備妥四組 case（EAMAR00 RBU-AEU 走 EURO 支／OPKFS01 RBU／VA16 SBU／CTOS製造 MSU group），每組 fn vs view **雙向 EXCEPT 應為 0**，末段附計時查詢。皆全新物件、還原＝DROP。另 `快照_Timer_20260724_Date抽驗前.txt`（07-24 15:18）＝`Budget_Platfom_Timer` 全表快照（2027／2026／2024 共 63 列）＋`Budget_Platfom_Timer_Log` **LogRows=0**（表已建、尚無紀錄），應為補測 07-23 因機房網路中斷未實測的 Manager 第一批而做的前置備份。
> **(d) 📦 測試報告收成可交付成品**：`測試報告_20260722.md`／`.html` **改寫為結案版**——總表由原始「50 Pass／3 Fail／2 Blocked／3 Skip」改標為 **50 Pass／🔧 已修正 4／☑ 非缺陷 1／⏭ Skip 3**，每個原 Fail 項目下加「✅ 結案更新（2026-07-23）」段記錄真因、修法、commit 與驗證數據；另產 `_單檔版.html`（**9.13 MB**，截圖全部以 data URI 內嵌、**單檔可直接轉寄**）＋`_含截圖.zip`（4.58 MB）。`PM測試資料\Overview_EAMAR00.xlsx`（47 KB）＝COM-06 修好後的 Overview 匯出實檔樣本。
> **本次無任何對外 GitHub/Notion 內容動作**：信件盤點含**內部收件人信箱與名單規則**（**無資安弱點細節**，非授權/注入類）、View 效能為 **SQL 程式碼**、測試報告含**測試站 URL／內部 CC 代碼／實際預算金額** → 三者皆歸 Budget Platform 對外待決集 → **僅 Obsidian**。且信件包未部署、View 函數是否上線未確認 → 依 Notion 去日誌化原則 **Notion 頁維持 2026-06-17 概覽不動**（系統對外行為尚未改變）。GitHub 本次僅推 SYNC_LOG 與 sync-log.html。
> ⚠️ **四項提醒**：(1) 🔴 **P0 信件 bug 尚未修上線** — 每次 SAP 拋轉都在對所有區 Admin 寄錯主旨（純成功批掛 `- Failed`），修法僅一行，整包依指示備妥未上版；**建議儘早安排部署窗口**（部署後驗證＝下次拋轉的信主旨應為 `- Success`、`Budget_Mail_Log` 有列）。(2) ⚠️ **View 第二階段成效未經證實** — `驗證03` 的四組雙向 EXCEPT 與計時**無執行結果記載**，**兩支函數是否已部署正式 `OPEXdb`、C# 六個 RBU Summary 方法是否已切過去皆未載明**（還原檔已警示：若 C# 已切，退函數須連 C# 一起退，否則 Summary／Summary Group 會 500）；另 **COM-06 剩餘 99 秒的 `vw_BudgetPlatformOverviewRBU` 本次未納入**，是否比照辦理待決。(3) **`feature/2026h2-mail-batch` 已推遠端未 merge** — merge 後仍需在測試站 appsettings 補 `SMTP:SubjectPrefix` 才有誤寄防護效果。(4) **前次列的尾巴仍無進展**：正式站發版（＝2027 開循環絕對前提）、DBA 三件排程、工項3 分時段排程本體待 E3 冪等確認、ZRCO18 上游補檔、Manager 第一批 `47a980ca` 補實測、Manager 後台安全第二批（需先定角色矩陣）、SBU-10 Finish 待人工點一次；7/21 提的 **MSU Scorecard 修正腳本是否已執行、是否還有其他 KPI 重複 mapping** 亦仍無新進展。

### 2026-07-23

> （本次排程於 2026-07-23 執行。掃到自 7/22 16:05 同步後的落差仍集中在單一主線：**Budget Platform 測試全案跑完並在隔日一口氣收斂**——測試報告出爐、3 Fail 全修、2 Blocked 全定性、Manager 後台全模組盤點且第一批已實作部署。屬操作/驗收＋根因分析文件，其中 **Manager 後台盤點含明確資安弱點細節 → 依規則不自動對外發佈**。**GitHub/Notion 本次無內容發佈**，Notion 頁不動（bug 修復＋資料缺口補齊，系統本身未變）。）

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| Budget Platform | `執行計畫\04_測試腳本_MSU.md`（7/22 22:58）／`05_測試腳本_Manager.md`（7/22 17:37）結果欄回填 ＋ `screenshots\{MSU,MGR}\` 約 26 張截圖 ＋ **`測試報告_20260722.md`／`.html`（7/23 09:58/09:59）** ＋ **`根因調查_Fail與Blocked項_20260722.md`（7/23 08:47）** ＋ **`優化盤點_Manager後台_20260723.md`（7/23 08:18）** ＋ `SP\_還原備份\還原_BudgetFXRate_2026補跑.sql`（7/23 09:35）／`還原_Date後台_TimerLog表.sql`（7/23 15:30） | Obsidian「Budget Platform Notes\Budget Platform 概覽.md」：**更新既有段落**「測試腳本實際執行（2026-07-22）」＝進行中→已跑完、補 MGR/MSU 結果、加註「工具逾時＝原生 confirm」單一假說已被推翻；**新增段落**「Fail／Blocked 根因調查與修復 ＋ Manager 後台優化盤點（2026-07-23）」；修改歷程 07-22 列改寫＋新增 07-23 列；待確認新增 4 項；同步狀態新增 07-23 段。**GitHub/Notion 不動**（見下）|
| eManager | `Hierarchy\SBU\2026 SBU Hierarchy.xlsx`（7/23 09:57） | **無同步動作**——組織階層原始資料 xlsx，依發佈集規則不發佈；無伴隨設計文件變更（同 7/22 之 RBU Hierarchy 處置）|

> 本次（自動排程同步）掃 `D:\Work\專案` 比對三目的地，自 7/22 16:05 同步後落差為：
> **Budget Platform — 測試從「執行中」變成「全案收斂」**：7/22 上午開跑的測試於**當日 17:37 前跑完 MGR、22:58 回填完 MSU**，7/23 上午產出測試報告與兩份分析文件。**最終戰績 58 項＝50 Pass／3 Fail／2 Blocked／3 Skip**（COM 7/1/0/1、RBU 12/0/1/0、SBU 11/0/1/1、MSU 9/1/0/0、MGR 11/1/0/1）。
> **(a) 3 Fail 全數修復並於測試站驗證通過**：① **MGR-08 Default FSCT GR% 下拉全空** ← `GetToolsDefaultFsctGr` 是 Tools 頁中**唯一漏做權限值 `ALL` 特判**者（Admin 的 `ALL` 與 Costcenter 區域值交集為空），修 3-5 行；驗證 Region Type 選 ACZ → Company Code 帶出 EU70 → 表格正常。② **COM-06 Overview Excel Download 完全無檔** ← 逐列 `InsertRowsBelow(1)`（07-15 Summary Group 修過的同款毒 pattern）＋**插入次數基準用錯**（用 view 總列數而非 `costcenter×3`，多插約 13 倍、檔尾多出大量空白列＝正確性 bug）＋迴圈條件 `.Count()` 每圈重排延遲查詢；改一次插足列數，驗證 **HTTP 200／98.9 秒／69,384 bytes 真 xlsx**。③ **MSU-09 MSU Summary 空白凍結** ← **7/22 的「慢查詢」假說被推翻**：用 `window.alert` 捕捉器實測，API **6.8 秒即回 HTTP 500**、前端 error handler 跳原生 `alert(E001)` **把分頁鎖死**＝「空白＋自動化凍結 3 分鐘」的完整解釋；500 真因＝`SBUSummaryDTO` 匯率換算 getter 以金額除以 `CurrentRate` 月值，**匯率缺列→NRE、月值 0→除零**。修法兩層＝三個 getter 全面 SafeDiv＋缺列寫 Serilog Warning（`1a327316`），驗證 **HTTP 200／64,642 bytes**、換算欄帶出實際匯率（USD→NTD 31.53~31.62）。commit `8b89f36b`（①②＋RBU-13）。
> **(b) 2 Blocked 全數定性**：**SBU-10 Finish ＝非產品 bug**——click handler 第一行即原生 `confirm()`，對話框同步阻塞 renderer → CDP 點擊逾時、API 從未發出，故狀態不變無壞資料；**未改碼，待人工點一次 Finish 即結案**。**RBU-13 ＝純查詢效能**（非對話框）——`GetRBUSummaryGroup` 是 07-15 批次化優化**沒改到的路徑**（當時只改下載），Company Code 分支把 EU01 底下全部 CC 拼 IN 清單再打 4 次 view 聚合掃描；改兩次批次掃描＋記憶體聚合後**回 HTTP 200／408 列正確表格**（原本永遠拿不到結果）。**✅「工具逾時家族」全數破案，共三種成因**：①原生 alert 鎖分頁（MSU-09，已修）②原生 confirm() 確認框（SBU-10 與各 Save/Delete，非缺陷）③純慢查詢（RBU-13／COM-06／MGR-11）——7/22 當時「截圖抓不到對話框」的原因即**對話框阻擋了截圖協定本身**。
> **(c) Manager 後台全模組唯讀盤點（8 子頁、前後端並行調查）＋第一批已實作部署**：第一批 commit `47a980ca`（17 檔）＝後端 Date 存檔背景化 `SP_Budget_FSCT`（**＝MGR-11 逾時真因**：存檔後同步等 SP 跑完才回應；含併發守衛＋rerun）＋兩處 `GetPermissionRole` 只取第一筆之殘留；前端 MessageBox **14 處成功/失敗判斷**（原第二參數寫死 `true`，**後端回錯誤字串也顯示綠色成功 toast＝失敗被當成功**）＋7 個 Tools 頁載入錯誤提示＋事件委派改綁 partial 內容器（原綁永久節點致切頁後重複綁定、一次操作打 N 次 API）＋刪除改成功後才移列＋Permission Edit 預選修正。刻意未做：axios 全域 timeout。另一分支新增 `Budget_Platfom_Timer_Log`（Date 後台**僅 Deadline 異動落紀錄、FCST_Month 不記**，使用者定案）。
> **本次無任何對外 GitHub/Notion 內容動作**：`優化盤點_Manager後台_20260723.md` **含明確資安弱點細節**（`BudgetPlatformManagerPagesController` 整 class 無 `[Authorize]`、`CreateBudgetPermission` 可自我提權、`UploadPermission` 可整包覆蓋一區權限，皆附端點與行號）→ **依規則不自動對外發佈、列待人工**；測試報告與根因調查無資安細節，惟含測試站 URL／內部 CC 代碼／實際預算金額，同歸 Budget Platform 對外待決集 → 僅 Obsidian。且本次為 **bug 修復＋資料缺口補齊、非功能/KPI/邏輯變更** → 依 Notion 去日誌化原則 **Notion 頁維持 2026-06-17 概覽不動**。GitHub 本次僅推 SYNC_LOG 與 sync-log.html。
> ⚠️ **四項提醒**：(1) 🔧 **已動到正式 DB** — `Budget_FXRate` **原本完全沒有 2026 列**（全表僅 2025 年 624 列），07-23 於內網 `EXEC SP_Budget_FXRate` 補入 2026 全年 USD/EURO 各 303 列，**1~6 月取自上游 `VRBU_Fx` 實際匯率、7~12 月沿用 6 月值** → 屆時真實匯率出來須留意是否被覆蓋/需重跑；還原檔 `還原_BudgetFXRate_2026補跑.sql`（`DELETE WHERE [Year]=2026`，冪等）。(2) ⚠️ **DB 端 View 瓶頸已定案但未解** — `vw_BudgetPlatformBudgetData` **即使只查 1 個 costcenter（回 178 列）也要 161.8 秒**，即 View 每查必整包實體化、costcenter 過濾推不進去 → RBU-13 修後仍需 170 秒、COM-06 仍需 99 秒；**功能面已修但使用體驗仍待第二階段 View 重構／落地 snapshot，是否納入 H2 工項待決**。(3) 🔴 **Manager 後台安全缺口尚未修**（盤點第二批，需先定各功能開放角色矩陣）；且**第一批 `47a980ca` 因機房網路中斷尚未實測**，需補測試站驗證。(4) **SBU-10 Finish 待人工點一次**即可讓 58 項全數結案；另 `Budget_Platfom_Timer_Log` 退表**必須連同 C# 分支一起退**，否則 repo 寫 log 的 INSERT 會炸掉 Date 存檔/刪除。**前次列的尾巴仍無進展**：正式站發版（＝2027 開循環絕對前提）、DBA 三件排程、工項3 分時段排程本體待 E3 冪等確認、ZRCO18 上游補檔；7/21 提的 **MSU Scorecard 修正腳本是否已執行、是否還有其他 KPI 重複 mapping** 亦未見新進展。

### 2026-07-22

> （本次排程於 2026-07-22 16:05 執行。掃到自 7/21 同步後的落差只有一條主線：**Budget Platform 測試腳本於今日 09:49 實際開跑，執行至本次同步時點仍在進行中**。屬操作/驗收文件＋截圖 → **僅 Obsidian**。**GitHub/Notion 本次無內容發佈**，Notion 頁不動（既有功能之驗收，系統本身未變）。）

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| Budget Platform | `執行計畫\00_測試腳本_執行說明.md`／`01_共用與入口`／`02_RBU`／`03_SBU`／`04_MSU`（7/22 10:08~16:03 陸續回填結果欄）＋`screenshots\{COM,RBU,SBU,MSU}\` 約 57 張截圖 | Obsidian「Budget Platform Notes\Budget Platform 概覽.md」新增「2026 H2 優化 — 測試腳本實際執行（2026-07-22，進行中）」段＋修改歷程列＋同步狀態（含殘留測試資料清單）。**GitHub/Notion 不動**（操作/驗收文件，同歸 Budget Platform 對外待決集；系統本身未變故 Notion 頁維持）|
| eManager | `Hierarchy\RBU\2026 RBU Hierarchy.xlsx`／`Hierarchy\SBU\2026 SBU Hierarchy.xlsx`（7/21 16:36） | **無同步動作**——組織階層原始資料 xlsx，依發佈集規則不發佈；無伴隨設計文件變更 |

> 本次（自動排程同步）掃 `D:\Work\專案` 比對三目的地，自 7/21 同步後落差為：
> **Budget Platform — 測試腳本從「已寫好未執行」變成「執行中」**：7/21 上午寫的腳本包，7/22 09:49 由另一個 Claude Code session 搭 Chrome 自動化開跑。**至 16:05 本次同步時點仍在進行**：COM（9 項）／RBU（13 項）／SBU（13 項）結果欄全數回填，MSU 跑到 MSU-07，**MSU-08~10 與 `05_測試腳本_Manager.md`（MGR 全部）結果欄仍空、`測試報告_YYYYMMDD.md` 尚未產出** → 完整報告預計下次同步才收得到。
> **執行中的兩項協議變更（`00_執行說明.md` 已改寫）**：(1) **【W】改為不用逐項還原**（7/22 使用者裁示；測試資料標 `TEST_20260721`，**正式上線前統一清理一次**，還原失敗不算 Fail；**【X】只截圖不點擊之禁令不受影響**）。(2) **Save／Delete／Finish 點擊前先截圖告知使用者**——本輪多處遇自動化工具（screenshot／click）逾時無回應、須 `navigate` 強制重整才恢復，研判**極可能是網頁跳出瀏覽器原生 confirm/alert 對話框**（會完全阻擋 CDP，自動化看不到也點不掉），**非平台缺陷** → 受影響項目（RBU-13／SBU-05／SBU-06／SBU-10）一律記 **Blocked／待人工確認**而非 Fail。
> **驗證良好的部分**：**工項9（SBU T&E／General Expense 拆分）全綠**——T&E **8 科目**齊、General Expense **18 科目**齊、Business Related 移出後**精準剩 13 分類**、**SBU-09 Summary 總額守恆抽驗逐月零誤差**（T&E Apr/May/Jun＝4,244／16,647／1,193,621、GE 六個月數字皆與步驟頁 Subtotal 完全一致），Group 5／Group 13 兩獨立列均進 Summary；**工項7** Current Allocation Rule 唯讀 **14 欄**且確實在選單最後（Rule Period 2026/6）；**工項6** SBU Overview 單一 Summary Status 欄；**工項1** CAPEX 範本可下載（`CAPEX.xlsx` 12,623 bytes）；**工項3** 入口頁 Last／Next SAP Update 顯示正常；RBU 五個費用頁（Marketing／R&D／T&E／Freight／Others-Fix）**cell-level 即時自動存檔**皆正常並已驗持久化；**MSU-06 Working Hour** 費率 SMT 0%→50%、Labor 連動 50%，存檔後 **Total MOE 由 0.0 變 176,017.0**，證實 `Save_WorkingHourRate` 觸發分攤重算正常。
> **缺陷／待釐清（5 件）**：① ❌ **COM-06 — Overview 的「Excel Download」(`DownloadOverview`) 逾時 90 秒×2 完全無檔案產出**，而同頁「Download Template」可正常下載（45,939 bytes / 20-30 秒）→ **不同後端端點、只有前者壞**，本輪唯一明確 Fail。② ⚠️ **SBU-08 — 「2027 New Capital」彙總框存檔後與整頁重載後皆仍顯示 0.0/0.0**，與明細列 Total Expense=1.0 不一致（前端彙總欄未刷新，小 bug）。③ ⚠️ **RBU-12 — Summary 全頁找不到 Submit／Confirm 按鈕**（用 find 確認不存在），與腳本預期不符，待確認是權限或機制不在此頁。④ ⚠️ **Blocked ×2 待人工實點**：RBU-13（篩 OPKFS01 查得空表原因未明；改篩 Company Code=EU01 後工具全逾時，下載與篩選聯動未及測試）、SBU-10（Finish **點擊指令本身即逾時**，重整後仍 Un-completed）。⑤ ⚠️ **效能偏慢**：Overview 35-40 秒、RBU Summary 20+ 秒、SBU Summary 約 40 秒，疑與 ① 的下載端同源（後端彙總查詢）。
> **設計性發現（皆非缺陷，但腳本假設需修正）**：(a) **Headcount／People Cost 三型全唯讀**（RBU-02／SBU-02／MSU-02 實測輸入不被接受，頁面明寫「You cannot change in platform」），資料由 HR 匯入、整批 Excel 上傳維護 → 「改值→存檔→還原」模式不適用，平均薪資自動帶值也連帶無法驗證（2027 HC 未匯入前恆為 0）。(b) **RBU 沒有獨立「Based on inflation rate」步驟** — 通膨推算是內嵌在 T&E／Freight／R&D／Others／Business Related 各頁 2026 表最後一欄的 **GR%** 機制（逐科目可不同），且推算後的 2027 數字不在這些頁面顯示 → **建議改用 Excel 匯出內容核對此計算**。(c) **MSU-07 General Allocated Expense 唯讀**（頁面明示「Please use the upload function」）。(d) MSU 選單機制為先選 Group 再自動帶出第一個 Costcenter（本輪＝**VG02**），無獨立 Costcenter 下拉。
> **本次無任何對外 GitHub/Notion 內容動作**：測試腳本與截圖屬操作/驗收文件（日誌性質），**無資安弱點細節**，惟含測試站 URL、內部 Cost Center 代碼與實際預算金額，整體歸 Budget Platform 對外待決集 → 僅 Obsidian；且本次為**既有功能之驗收、系統本身未變**，依 Notion 去日誌化原則 **Notion 頁不動**。GitHub 本次僅推 SYNC_LOG 與 sync-log.html。
> ⚠️ **三項提醒**：(1) **殘留測試資料未還原**（7/22 使用者裁示改為上線前統一清理）：`TEST_20260721` 標記散落於 **RBU OPKFS01**（Marketing 新增列、R&D 650700／T&E 620110／Freight 630502／Others 650401 各一格 Jul=1）、**SBU VA16**（Marketing 列、R&D 專案列、**T&E Travel-Accommodation Jan=2.0（刪除步驟未完成）**、GE Overtime meal Jan=1、Capital 一列）、**MSU VG02**（Marketing 列、R&D 專案列、Capital 一列）。**特別注意：MSU VG02 的 Working Hour 費率被改為 SMT 50%／Labor 50%（原 0%／100%）且未還原——這是設定值變更、不帶 `TEST_` 標記難以辨識，且已觸發 MOE 分攤重算（Total MOE 0→176,017），清理清單務必補上**（測試站與正式 DB 共用資料）。(2) **測試尚未跑完** — MSU-08~10 與 Manager 後台（MGR）全部未測，測試報告未產出；Manager 後台是尚未有任何驗證覆蓋的一塊。(3) **前次列的尾巴仍無進展**：正式站發版（＝2027 開循環絕對前提）、DBA 三件排程、工項3 分時段排程本體待 E3 冪等確認、ZRCO18 上游補檔；另 7/21 提的 **MSU Scorecard 修正腳本是否已執行、是否還有其他 KPI 重複 mapping** 亦未見新進展。

### 2026-07-21

> （本次排程於 2026-07-21 執行。**重點：Notion 連線恢復**——自 7/17、7/20 兩度 `certificate signature failure` 後本次連線成功，**積欠的 OSF Commerce Insights 系統說明更新已補完**。另掃到自 7/20 同步後的落差：**MSU Scorecard** AKMC 線 7/20 傍晚找到 YTD 費率翻倍根因並出修正腳本；**Budget Platform** 7/21 上午新開測試腳本包工作線。此二者皆屬程式碼/操作文件 → 僅 Obsidian。）

| 專案 | 檔案 | 目標位置 |
|------|------|---------|
| eManager / OSF Commerce Insights | （無新檔案；補做 7/17 積欠的 Notion 更新） | **Notion** OSF Commerce Insights 頁（`375b60a1-adfe-81c2-be42-dee5db09e9fc`）：① 📊 衡量指標段新增 3 個 bullet——營運效率指標（O2R/O2S/S2A/A2C/C2R 天數指標，**O2S/S2A/A2C/C2R 之 YTM 採 AVG 不可加總**）、`Freight Act. ($)`、`Freight Fee %`（＝`SUM(Freight Act. ($)) ÷ (SUM(CurrentYear Achv. (K)) × 1000)`，分母單位 K 需 ×1000、比率以小數存放前端 ×100 顯示、小數位 3、YTM 型別 RECALC_SUM）；並 **update-a-block 改寫既有 YTM bullet** 為「YTMCalcType 驅動之 SUM／AVG／RECALC_SUM 三型別」。② 🧩 功能與資料段新增資料權限 bullet（專屬權限表 `OSF_CommerceInsightsPermission`、維度為 Store 讀 `HierarchyName='Store'`、`'ALL'`＝看全部）。③ 🔗 相關文件段加 ChangeLog.html 連結。**GitHub 無新內容**（ChangeLog.html 已於 7/17 發佈）|
| eManager / MSU Scorecard | `AKMC\驗算_AKMC-System_HourlyRate_Assembly_YTD_20260720.sql`（7/20 16:39）＋`AKMC\修正_AKMC-System_HourlyRate_YTD翻倍_20260720.sql`（7/20 17:29） | Obsidian「開發記錄\MSU Scorecard.md」新增 07-20（續）修改歷程列＋同步狀態＋待確認。**GitHub/Notion 不動**（驗算/修正 SQL 屬程式碼；且為資料重複造成的計算偏差、非 KPI 定義變更）|
| Budget Platform | `執行計畫\00_測試腳本_執行說明.md`／`01_共用與入口`／`02_RBU`／`03_SBU`／`04_MSU`／`05_Manager`＋`tools\capture.ps1`（7/21 10:50~10:53） | Obsidian「Budget Platform Notes\Budget Platform 概覽.md」新增 07-21 修改歷程列＋同步狀態。**GitHub/Notion 待人工**（操作/驗收文件，同歸 Budget Platform 對外待決集）|

> 本次（自動排程同步）掃 `D:\Work\專案` 比對三目的地：
> **(a) ✅ Notion 連線恢復 — OSF Commerce Insights 系統說明補完**：7/17 與 7/20 兩次排程均因 `certificate signature failure` 停做 Notion，本次 `retrieve-a-page` 成功。依待同步列所載，把**第七次修改（7/17 KPI 邏輯）＋第六次修改（6/11 Store 資料權限）**反映進系統說明——皆屬「系統本身有變」（KPI 計算邏輯與權限維度），符合 Notion 只在系統有變時更新之原則；日誌性內容（改了什麼／commit／狀態）一律未寫入 Notion。技術備忘：`update-a-block` 需把 `bulleted_list_item` 當**最上層參數**傳（包在 `type` 下會 400）。
> **(b) MSU Scorecard（7/20 傍晚）— AKMC YTD 費率翻倍找到根因**：承同日 AKMC 線。`驗算_...YTD_20260720.sql` 以 pooled 口徑 `Σ(MOPEX×1000) ÷ Σ(SAP工時)` 獨立驗算 2026 Jan~Jun（分子 `ZRCO07_SUM.WBTR1` KOSTL KK04/KQ01 對照表 No=7；分母 `ZRPP89_SUM.Activity_To_Conf2` Cost_Center KK04/KQ01/**KQ06**，**分母比分子多一個 cost center**）。`修正_...YTD翻倍_20260720.sql` 確認**根因＝`SCORECARD_MSU_KpiMgr_New` 有兩筆完全相同的 mapping 列**（2026／AKMC-System／`MOPEX(K)-ForHourlyRate`），主 SP LEFT JOIN 把每月列變兩份；**Q1/Q2/H1 用 AVG 免疫、YTD 用 PIVOT SUM ÷ @Month 被灌成 2 倍** → YTD MOPEX 9,581.54（應 4,790.77）、費率 251.95（應 125.97），分母工時只有一筆故剛好 ×2。修法四步：確認重複並全表掃其他重複 → `ROW_NUMBER()` 去重（`BEGIN TRAN` 檢查 rowcount 後才 COMMIT）→ 重跑 `EXEC uSP_MSUScorecard2026`（冪等）→ 驗收 H1/YTD 皆 125.97。
> **(c) Budget Platform（7/21 上午）— 測試腳本包新工作線**：為 H2 九工項測試站驗收，`執行計畫\` 一口氣產出 6 份 MD ＋ `tools\capture.ps1`，設計給另一個 Claude Code session 搭配 Chrome 自動化執行，逐項含操作步驟／預期結果／截圖檔名／結果欄。核心安全設計＝**【R】唯讀／【W】寫入（留原值、標 `TEST_20260721`、測完還原）／【X】高風險只截圖不點擊**三級分類，因**測試站與正式 DB 共用資料、無獨立測試庫**；另立 5 條紅線。指定 CC＝RBU `OPKFS01`、SBU `VA16`（勿用 SA11）、MSU 取第一個有權限者；Budget Year 2027。腳本內已內建已知非缺陷提示。**腳本尚未執行**（結果欄全空、無 screenshots、無測試報告）。
> **本次對外發佈僅 Notion（OSF 系統說明）**：MSU 為驗算/修正 SQL（程式碼），且為資料重複造成的偏差、非 KPI 定義變更 → GitHub/Notion 不動；Budget 測試腳本屬操作/驗收文件、腳本未執行，同歸對外待決集 → 僅 Obsidian。GitHub 本次僅推 SYNC_LOG 與 sync-log.html。
> ⚠️ **三項提醒**：(1) **MSU 修正腳本含對正式對照表 `SCORECARD_MSU_KpiMgr_New` 的 DELETE，是否已執行本輪無法自檔案確認**；且 STEP 0 的「全表掃同 YEAR/PLANT/DESCRIPTION 重複」結果未見記載——**可能還有其他 KPI 同樣中招**，建議補查。(2) **linked server `172.21.214.30` 連線是否已恢復未載明**（7/20 稍早記 Communication link failure，傍晚驗算腳本已寫成可執行形式但無執行結果）。(3) Budget 前次列的尾巴均未見進展：**正式站發版**（＝2027 開循環絕對前提）、DBA 三件排程、工項3 分時段排程本體待 E3 確認 SAP 冪等、ZRCO18 上游補檔。

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
