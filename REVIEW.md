# Repository review（Windows-first）

- Review date: 2026-08-22
- Review baseline: `98dd7bf1687a69ab596625f7b9223fd2bd0c013c`
- Upstream reviewed through: `c045a2eb505f0f8b7992bb4af53cc020f25003fd`
- Primary environment: Windows 11、PowerShell、Python 3.14.7（本機）、CI Windows / Ubuntu 3.12
- Status: 維護骨架可用；API 目錄與 `scripts/validate/` 未改寫；官方仍是上游 `public-apis/public-apis`
- Tracked files: 41（`git ls-files`）

## 結論

這個 fork 適合作為 Windows 本機查詢、並追蹤上游目錄更新的維護線。產品是 `README.md` 裡 1000+ 筆免費 public API。本線只加治理骨架：上游檢查、Windows gate、fork CI。

現階段的主要風險不是「fork 把目錄改壞」，而是上游 catalog validator 在官方 `master` 已經紅，以及本 fork 幾處測試／錯誤處理不夠硬。沒有 CRITICAL／HIGH。沒有秘密、沒有把目錄變成 gateway。

不把 fork 當成第二個官方產品 repo。不翻譯 `README.md`。

## 本輪實證

### 本機（`98dd7bf`）

```text
pwsh -NoProfile -File tools\dev_check.ps1
→ compileall / ruff E9+F（tests、tools）/ pytest / 上游 unittest / check_links 全綠
→ pytest 13 passed
→ 上游 validate package：31 tests OK
→ check_links：12 份文件，0 斷連結（沒有掃到 scripts/README.md，見 R-06）

python tools/check_upstream_updates.py
→ No new upstream commits.

python -m bandit -q -r tools --severity-level high --confidence-level medium
→ exit 0（High = 0）

python -m bandit -q -r tools -ll
→ exit 0（Medium+ = 0）
```

抽查上游目錄檢查（**不列入本 fork 硬閘門**）：

| 指令 | exit | 觀察 |
|---|---|---|
| `python scripts/validate/format.py README.md` | 1 | APILayer 贊助表只有 3 欄、表格分隔列被當成 entry、多個分類未按字母排序 |
| `python scripts/validate/links.py README.md --only_duplicate_links_checker` | 1 | 重複：`isitdownstatus.com`、`tastedive.com/read/api` |

`python -c "import check_links; ..."` 印出的文件清單沒有 `scripts/README.md`：`SKIP_NAMES` 用 `path.name`，任何叫 `README.md` 的檔都會被丟掉。

### GitHub Actions

| Workflow | 結果 | 說明 |
|---|---|---|
| [CI @ 2ca3aae](https://github.com/SanHsien/public-apis/actions/runs/32555198499) | success | Ubuntu py3.12、Windows py3.12 `dev_check.ps1` |
| [CI @ 98dd7bf](https://github.com/SanHsien/public-apis/actions/runs/32555325757) | success | docs 提交後再綠一次 |
| [Upstream check @ 2ca3aae](https://github.com/SanHsien/public-apis/actions/runs/32555198427) | success | 無未審查上游 commit |
| [Tests of push & pull](https://github.com/SanHsien/public-apis/actions/runs/32555325756) | skipped | `if: github.repository == 'public-apis/public-apis'` |
| [Tests of validate package](https://github.com/SanHsien/public-apis/actions/runs/32555325742) | skipped | 同上 |

`98dd7bf` 只改 `REVIEW.md`，沒觸發 `upstream-check.yml` 的 `paths:` 過濾，屬預期。

## 開放 findings

| ID | 嚴重度 | Finding | 證據 | 建議 |
|---|---|---|---|---|
| R-01 | P2 | 上游 `format.py` 無法通過當前 `README.md`。贊助區塊與目錄契約不一致。 | 本機 exit 1；L043–L055 報 3 欄（需要 5 欄）；多個 ` :---: ` 分隔列被當 entry | 不在本 fork 修目錄。若要回貢，先對準贊助表要不要納入 format 契約。 |
| R-02 | P2 | 目錄有重複連結，上游 `--only_duplicate_links_checker` 失敗。 | `https://isitdownstatus.com`、`https://tastedive.com/read/api` | 可回貢去重。本線不為了綠燈改 1000+ 筆清單。 |
| R-03 | P3 | `format.py` 正則用非 raw 字串，Python 3.14 發 `SyntaxWarning`（`\s`、`\*`、`\[`）。 | 直接執行時印出 SyntaxWarning | 回貢改 raw string。現況仍能跑。 |
| R-04 | P3 | 上游 workflow 仍用 `actions/checkout@v2`、`setup-python@v2`、Python 3.8。 | `.github/workflows/test_of_*.yml` L17–19 | 本線不升級那些 pin。fork 三檔已加 repo guard；fork CI 用 checkout SHA / Python 3.12。 |
| R-05 | P3 | `scripts/requirements.txt` 鎖在 2021 的 requests 2.27.1 等。本機 `requirements-dev.txt` 用 `requests>=2.32`。 | 兩個 requirements 檔 | 不幫上游升 pin。`requests` **不是**死依賴：`scripts/tests/test_validate_links.py` 會 `import validate.links`，而 `links.py:8` 需要它。 |
| R-06 | P3 | `check_links.py` 宣稱會掃 `scripts/README.md`，實際因 `SKIP_NAMES` 含 `"README.md"` 被檔名過濾掉。 | `iter_documents()` 實測 12 份，無 `scripts/README.md`；`check_links.py` L23–26、L36–42 | 改成比對相對路徑，只跳過根目錄 `README.md`。 |
| R-07 | P3 | `collect_new_commits` 的 `split("\x1f", 2)` 與 `run_git` 的 `FileNotFoundError` 不是 `UpstreamCheckError`。異常時 `main()` 寫不出 report，CI `cat upstream-review-report.md` 會再失敗一次。 | `tools/check_upstream_updates.py` L36–47、L82 | 包成 `UpstreamCheckError`。日常 git 輸出正常時不會踩到。 |
| R-08 | P3 | `check_links.py` 解析相對連結後沒確認仍在 repo 內，`../../...` 會對 repo 外路徑做 `.exists()`。 | `tools/check_links.py` L55–64 | `resolved.is_relative_to(ROOT)` 失敗就記問題。只洩漏存在性，不讀內容。 |
| R-09 | P3 | workflow guard 測試是三個檔名白名單。上游若再加第四個 workflow，測試不會紅。 | `tests/test_docs.py` L60–68；`docs/DECISIONS.md` 已寫要人工重套 guard | 改成掃 `.github/workflows/*.yml`，排除 `ci.yml` 與 `upstream-check.yml`。 |
| R-10 | P3 | CI 矩陣停在 3.12；本機是 3.14.7。3.14 本機 13 passed，Ubuntu job 沒跑 3.14。 | `.github/workflows/ci.yml`；`python --version` | 下次改 CI 時可加一格 3.14。非阻斷。 |

## 已檢查、不列為 finding

- 本 fork `tools/check_upstream_updates.py` 以 argv 列表呼叫 `git`，無 `shell=True`。Bandit High／Medium 對 `tools/` 為 0。
- `README.md` 未翻譯，無 `README.en.md`／`README.zh-Hant.md`。
- `origin` = `SanHsien/public-apis`，`upstream` = `public-apis/public-apis`，分支 `master`。
- Baseline `reviewed_through` 等於 clone 時上游 HEAD `c045a2eb505f0f8b7992bb4af53cc020f25003fd`。
- 無 `.env`、金鑰、`.pem`。`git ls-files` 41 檔。venv 與 `upstream-review-report.md` 已被 `.gitignore` 排除。
- `ci.yml` / `upstream-check.yml`：`permissions: contents: read`、`persist-credentials: false`、checkout／setup-python 釘 SHA。
- `test_upstream_catalog_workflows_stay_on_official_repo` 已鎖現有三個上游 workflow 的 repo guard（F-03「完全沒測試」不成立）。
- 日常 gate **不會**跑 `scripts/validate/links.py` 的 HTTP 探活；`validate_links.yml` 在本 fork skip。
- `requirements-dev.txt` 的 `requests` 給上游 unittest 用，不是 check_links 用。

## 尚未宣稱範圍

- **沒有**對 1000+ 個 API 做活連結或免費額度抽樣。
- **沒有**宣稱上游 catalog validator 在當前 `master` 是綠的。反證是 R-01／R-02。
- `dev_check.ps1` **不含** Bandit、CodeQL、完整 `links.py`。Bandit 只在本輪本機抽查。
- **不宣稱** fork 有自己的 GitHub Release 或獨立版號。
- **沒有**修 R-06～R-10。這份文件是審查快照，不是修復紀錄。

## 建議下一步（未動手）

1. 若要動 fork 程式：先修 R-06（連結掃描漏檔）與 R-09（未來上游 workflow 沒 guard）。兩項都小、都有測試可鎖。
2. R-07／R-08 可順手包進同一 PR。
3. 每週一 03:00 UTC 的 `upstream-check.yml` 失敗時，依 [`docs/UPSTREAM.md`](docs/UPSTREAM.md) 審查後再推進 baseline。
4. 回貢上游的話，重複連結去重（R-02）比修贊助表格式（R-01）小。
