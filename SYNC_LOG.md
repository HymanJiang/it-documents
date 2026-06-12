# Sync Log

記錄每次文件同步的內容與狀態。

---

## ❌ 待同步

| 專案 | 檔案 | 目標位置 | 備註 |
|------|------|---------|------|
| TCP 改版 | docs/改版產出/TCP_Platform_需求確認書.md（0605 更新） | Notion TCP 頁面（需求與規格） | 需人工確認：6/5 更新內容要不要反映到 Notion 既有摘要 |
| OSF Commerce Insights | OSF_Commerce_Analysis.md | 尚未決定（無 HTML 版） | 需人工決定：是否轉 HTML、放哪 |
| MSU Scorecard | （目前無對應本機文件） | — | 待新增 |

> ⚠️ 以下 Notion 端待補（2026-06-12 Notion MCP 斷線時無法寫入，待連線恢復補做）：
> - TCP 需求確認書 **v1.1（0605）** 的 12 項確認狀態更新到 Notion 既有 v1.0 摘要
> - 下方「部分同步」5 個 DB SQL 的 Notion 連結 + SA 摘要
> - 既有 DB 連結（OrgHierarchy/FOB/Template）與 eManagerReport 實作做法 補上 SA 摘要

---

## ⏳ 部分同步（GitHub 已推，Notion 待補）

### 2026-06-12

| 專案 | 檔案 | GitHub | Notion |
|------|------|--------|--------|
| TCP 改版 | DB_Migration_Currency.html | ✅ 已推 | ⏳ 待補連結+SA |
| TCP 改版 | DB_Migration_History_Tables.html | ✅ 已推 | ⏳ 待補連結+SA |
| TCP 改版 | DB_View_Quota_By_SalesId.html（合併重複的 DB_View_Quota.sql） | ✅ 已推 | ⏳ 待補連結+SA |
| TCP 改版 | DB_View_Quota_Salesperson.html | ✅ 已推 | ⏳ 待補連結+SA |

> 這 5 個 DB SQL（6/5）原本**未被列入上方 ❌ 清單**（清單漏記），經實際掃資料夾比對才發現，於 2026-06-12 補推 GitHub。
> 提醒源檔重複：`DB_View_Quota.sql` 與 `DB_View_Quota_By_SalesId.sql` 內容相同，建議擇一保留。

---

## ✅ 已同步記錄

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
