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
| eManager 改版 | Notion/系統分析文件…md（6/17）| 未定 | 待人工：Notion 匯出檔，是否回灌待定 |
| Budget Platform | BudgetPlatform_分析報告.html、OPTIMIZATION_PLAN.md（6/23）| 未定（GitHub/Notion）| 待人工：四層程式碼分析＋六階段優化計畫；含 SQL 注入確切位置(Repository.cs:2338、_RBU.cs:51/752/1033/1055)與缺 [Authorize] 端點，對外發佈敏感安全細節之取捨待 Hyman 定。Obsidian 工作紀錄已寫 |
| Budget Platform | 優化執行計畫.html、整體規劃流程.html、測試操作指南.html（6/23–6/24）| 未定（GitHub/Notion）| 待人工：前二者含安全弱點細節引用，併入 Budget Platform 對外待決集；Obsidian 工作紀錄已寫 |
| eManager / MSU Scorecard | ATMC自動化_SP修正交接_20260624（Notion 部分）| 未定（Notion 子頁）| 待人工：MSU Scorecard 歸屬「後續再定」、尚無 Notion 子頁，未自動建頁。GitHub HTML 已發、Obsidian 已寫；待 Hyman 決定 Notion 歸屬後補 SA 摘要+連結 |

> ℹ️ 完整盤點與已建結構見 `D:\Obsidian Note\專案盤點對照表.md`。
> 小項待補：eManagerReport 既有連結補 SA 摘要。（TCP 3 個舊 DB 連結 SA 已於 6/12 補齊）

---

## ✅ 已同步記錄

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
