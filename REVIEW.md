# Repository review（Windows-first）

- Review date: 2026-08-22
- Review baseline: 見本檔「已修」對應 commit；開放項維持不修
- Upstream reviewed through: `c045a2eb505f0f8b7992bb4af53cc020f25003fd`
- Primary environment: Windows 11、PowerShell、Python 3.14.7（本機）、CI Ubuntu 3.12／3.14、Windows 3.14
- Status: 維護骨架可用；API 目錄與 `scripts/validate/` 未改寫；fork 可修的 R-06～R-10 已修

## 結論

這個 fork 適合作為 Windows 本機查詢、並追蹤上游目錄更新的維護線。產品是 `README.md` 裡 1000+ 筆免費 public API。

2026-08-22 審查列出的 R-01～R-10，**fork 能修的都修了**（R-06～R-10）。**沒有**改上游目錄、**沒有**改 `scripts/validate/`、**沒有**升級上游 workflow pin、**沒有**回貢。

## 已修 findings

| ID | 嚴重度 | Finding | 修復 |
|---|---|---|---|
| R-06 | P3 | `check_links.py` 用檔名過濾，掃不到 `scripts/README.md` | `SKIP_RELATIVE` 比對相對路徑，只跳過根目錄 `README.md`；測試鎖 `scripts/README.md in rels` |
| R-07 | P3 | `FileNotFoundError`／畸形 `git log` 行不是 `UpstreamCheckError`，CI 可能沒 report | `run_git` 包裝 `FileNotFoundError`；`collect_new_commits` 包裝 `ValueError` |
| R-08 | P3 | 相對連結可對 repo 外路徑做 `.exists()` | `resolved.is_relative_to(ROOT)` 失敗就記「逃出 repo 根目錄」 |
| R-09 | P3 | workflow guard 測試是三檔白名單 | 掃 `.github/workflows/*.yml`，排除 `ci.yml` 與 `upstream-check.yml` |
| R-10 | P3 | CI 只跑 3.12 | Ubuntu 矩陣 3.12＋3.14；Windows job 改 3.14 |

## 刻意不修

| ID | 嚴重度 | Finding | 理由 |
|---|---|---|---|
| R-01 | P2 | 上游 `format.py` 無法通過當前 `README.md` | 目錄／贊助表是上游產品。本線不代修 1000+ 筆清單。 |
| R-02 | P2 | 重複連結：`isitdownstatus.com`、`tastedive.com/read/api` | 同上，屬目錄內容。不回貢。 |
| R-03 | P3 | `format.py` 非法跳脫 `SyntaxWarning` | 在上游 `scripts/validate/format.py`。改了會跟上游衝突。現況仍能跑。 |
| R-04 | P3 | 上游 workflow 用 `checkout@v2`／Python 3.8 | 不升級那些 pin。本 fork 靠 repo guard 讓它們 skip。 |
| R-05 | P3 | `scripts/requirements.txt` 鎖 2021 pin | 那是上游 Ubuntu 3.8 CI 契約。本線 `requirements-dev.txt` 另裝現代 requests。 |

## 本輪實證

### 本機（修完後）

```text
pwsh -NoProfile -File tools\dev_check.ps1
→ compileall / ruff E9+F / pytest / 上游 unittest / check_links 全綠
→ 17 passed
→ 上游 validate package：31 tests OK
→ check_links：13 份文件（含 scripts/README.md），0 斷連結
```

### GitHub Actions

修補分支 push 後補 run URL。預期：Ubuntu 3.12／3.14 與 Windows 3.14 全綠；上游三個 catalog workflow skipped。

## 已檢查、不列為 finding

- `tools/check_upstream_updates.py` 仍以 argv 列表呼叫 `git`，無 `shell=True`。
- `README.md` 未翻譯。`origin`／`upstream` remote 正確。
- 日常 gate 仍不跑 `format.py README.md` 與 `links.py` HTTP 探活。
- `requests` 仍給上游 unittest 用，不是死依賴。

## 尚未宣稱範圍

- **沒有**對 1000+ 個 API 做活連結抽樣。
- **沒有**宣稱上游 catalog validator 是綠的。
- `dev_check.ps1` **不含** Bandit、CodeQL。
- **不宣稱** fork 有自己的 GitHub Release。
