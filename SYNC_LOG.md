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

> ℹ️ 完整盤點與已建結構見 `D:\Obsidian Note\專案盤點對照表.md`。
> 小項待補：TCP 既有 3 個 DB 連結（OrgHierarchy/FOB/Template）補 SA 摘要。

---

## ✅ 已同步記錄

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
