# -*- coding: utf-8 -*-
"""
Generate sync-log.html from SYNC_LOG.md.

SYNC_LOG.md is the single source of truth for the file-level sync history.
This script renders it into a navy-styled HTML page published on GitHub Pages
(https://hymanjiang.github.io/it-documents/sync-log.html).

Run each sync-routine cycle AFTER updating SYNC_LOG.md:
    python _scripts/gen_sync_log_html.py
Output: <repo-root>/sync-log.html  (overwritten every run)
"""

import os
import re
import html
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "SYNC_LOG.md")
OUT = os.path.join(ROOT, "sync-log.html")

CSS = """
  *,*::before,*::after{box-sizing:border-box;}
  body{font-family:"Segoe UI","Microsoft JhengHei",Arial,sans-serif;margin:0;padding:0;background:#f4f6f9;color:#222;font-size:14px;line-height:1.65;}
  .topbar{background:#00315a;color:#fff;padding:20px 32px;}
  .topbar h1{margin:0 0 4px;font-size:21px;font-weight:600;}
  .topbar .sub{font-size:13px;color:#b8d4ea;}
  .wrap{max-width:1080px;margin:0 auto;padding:24px 32px 64px;}
  h2{font-size:17px;color:#00315a;border-bottom:2px solid #e1e6ec;padding-bottom:6px;margin:30px 0 12px;}
  h3{font-size:15px;color:#0a4a86;margin:22px 0 8px;padding:4px 10px;background:#eef3f8;border-left:4px solid #00315a;border-radius:0 4px 4px 0;}
  p{margin:8px 0;}
  code{background:#eef1f5;color:#1e2a38;padding:1px 5px;border-radius:3px;font-family:"Cascadia Code","Consolas",monospace;font-size:12.5px;}
  table{border-collapse:collapse;width:100%;margin:10px 0;font-size:13px;}
  th,td{border:1px solid #d8dee6;padding:6px 10px;text-align:left;vertical-align:top;}
  th{background:#eef3f8;color:#00315a;white-space:nowrap;}
  .meta{background:#fff;border:1px solid #e1e6ec;border-left:4px solid #00315a;border-radius:6px;padding:12px 18px;margin-bottom:20px;font-size:13px;color:#444;}
  .note{background:#fbfcfe;border:1px solid #e6ebf1;border-left:3px solid #9db8d2;border-radius:4px;padding:8px 14px;margin:8px 0;font-size:12.5px;color:#3a4655;}
  hr{border:0;border-top:1px solid #e1e6ec;margin:26px 0;}
  .footer{margin-top:40px;padding-top:14px;border-top:1px solid #e1e6ec;font-size:12px;color:#8a97a6;}
"""


def inline(s):
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s


def cells(line):
    parts = [c.strip() for c in line.strip().strip("|").split("|")]
    return parts


def is_sep(line):
    return bool(re.match(r"^\s*\|?\s*:?-{2,}", line)) and set(line.strip()) <= set("|-: ")


def convert(md):
    lines = md.split("\n")
    out = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()

        # table block
        if stripped.startswith("|") and i + 1 < n and is_sep(lines[i + 1]):
            header = cells(line)
            i += 2  # skip header + separator
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append(cells(lines[i]))
                i += 1
            out.append("<table>")
            out.append("<tr>" + "".join(f"<th>{inline(c)}</th>" for c in header) + "</tr>")
            for r in rows:
                out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            out.append("</table>")
            continue

        # blockquote block (group consecutive)
        if stripped.startswith(">"):
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(inline(lines[i].strip().lstrip(">").strip()))
                i += 1
            out.append('<div class="note">' + "<br>".join(buf) + "</div>")
            continue

        # headings
        if stripped.startswith("### "):
            out.append(f"<h3>{inline(stripped[4:])}</h3>")
            i += 1
            continue
        if stripped.startswith("## "):
            out.append(f"<h2>{inline(stripped[3:])}</h2>")
            i += 1
            continue
        if stripped.startswith("# "):
            i += 1  # title handled in topbar
            continue

        # horizontal rule
        if stripped == "---":
            out.append("<hr>")
            i += 1
            continue

        # blank
        if stripped == "":
            i += 1
            continue

        # plain paragraph
        out.append(f"<p>{inline(stripped)}</p>")
        i += 1

    return "\n".join(out)


def main():
    with open(SRC, encoding="utf-8") as f:
        md = f.read()
    body = convert(md)
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    doc = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>文件同步紀錄 (SYNC_LOG)</title>
<style>{CSS}</style>
</head>
<body>
  <div class="topbar">
    <h1>\U0001F4C4 文件同步紀錄（SYNC_LOG）</h1>
    <div class="sub">由 SYNC_LOG.md 自動產生 · 產生時間 {ts}</div>
  </div>
  <div class="wrap">
    <div class="meta">
      <b>資料來源：</b><code>SYNC_LOG.md</code>（檔案層完整歷史的單一真相）。本頁每次同步排程<b>自動重新產生</b>，內容一律以 <code>.md</code> 為準；請勿手動編輯本 HTML。
    </div>
{body}
    <div class="footer">
      本檔由 <code>_scripts/gen_sync_log_html.py</code> 自 <code>SYNC_LOG.md</code> 產生。專案現況見台帳 <code>專案進度.md</code>；完整盤點見 <code>專案盤點對照表.md</code>。
    </div>
  </div>
</body>
</html>
"""
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(doc)
    print(f"Wrote {OUT} ({len(doc)} bytes) from {SRC}")


if __name__ == "__main__":
    main()
