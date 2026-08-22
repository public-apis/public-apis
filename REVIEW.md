# Repository review（Windows-first）

- Review date: 2026-08-22
- Review baseline: `c045a2eb505f0f8b7992bb4af53cc020f25003fd`
- Upstream reviewed through: `c045a2eb505f0f8b7992bb4af53cc020f25003fd`
- Primary environment: Windows 11、PowerShell、Python 3.14.7（本機）、CI Windows / Ubuntu 3.12
- Status: 維護骨架可用；API 目錄與 `scripts/validate/` 未改寫；官方仍是上游 `public-apis/public-apis`

## 結論

這個 fork 適合作為 Windows 本機查詢、並追蹤上游目錄更新的維護線。產品是 `README.md` 裡 1000+ 筆免費 public API，行為跟隨上游。本線只加治理骨架：上游檢查、Windows gate、fork CI。

現階段的主要風險不是「fork 把目錄改壞」，而是：

1. 上游自己的 `format.py README.md` 與重複連結檢查，在 fork 當下的 `master` 已經失敗。
2. 上游每日活連結 workflow 在 2026-08-22 也是 `failure`。
3. `scripts/validate/format.py` 在 Python 3.14 會對非法跳脫發出 `SyntaxWarning`。

不把 fork 當成第二個官方產品 repo。目錄、貢獻規則與驗證腳本的版權與行為仍屬上游。不翻譯 `README.md`。

## 本輪實證

### 本機

```text
pwsh -NoProfile -File tools\dev_check.ps1
→ compileall / ruff E9+F（tests、tools）/ pytest / 上游 unittest / check_links 全綠
→ 13 passed
→ 上游 validate package：31 tests OK
→ check_links：12 份維護文件，0 斷連結

python tools/check_upstream_updates.py
→ No new upstream commits.
```

抽查上游目錄檢查（**不列入本 fork 硬閘門**）：

| 指令 | exit | 觀察 |
|---|---|---|
| `python scripts/validate/format.py README.md` | 1 | APILayer 贊助表只有 3 欄、表格分隔列被當成 entry、多個分類未按字母排序 |
| `python scripts/validate/links.py README.md --only_duplicate_links_checker` | 1 | 重複：`isitdownstatus.com`、`tastedive.com/read/api` |

### GitHub Actions

fork 第一次 push 後補上 run URL。預期：

| Workflow | 預期 | 說明 |
|---|---|---|
| CI | success | Ubuntu py3.12 + Windows `dev_check.ps1` |
| Upstream check | success | 無未審查上游 commit |
| 上游三個 catalog workflow | skipped | `if: github.repository == 'public-apis/public-apis'` |

## 開放 findings

| ID | 嚴重度 | Finding | 證據 | 建議 |
|---|---|---|---|---|
| R-01 | P2 | 上游 `format.py` 無法通過當前 `README.md`。贊助區塊與目錄契約不一致。 | 本機實測 exit 1；L043–L055 報 3 欄（需要 5 欄）；多個 ` :---: ` 分隔列被當 entry | 不在本 fork 修目錄。若要回貢，先對準贊助表要不要納入 format 契約。 |
| R-02 | P2 | 目錄有重複連結，上游 `--only_duplicate_links_checker` 失敗。 | `https://isitdownstatus.com`、`https://tastedive.com/read/api` | 可回貢去重。本線不為了綠燈改 1000+ 筆清單。 |
| R-03 | P3 | `format.py` 正則用非 raw 字串，Python 3.14 發 `SyntaxWarning`（`\s`、`\*`、`\[`）。 | compileall / 直接執行時印出 SyntaxWarning | 回貢改 raw string。現況仍能跑。 |
| R-04 | P3 | 上游 workflow 仍用 `actions/checkout@v2`、`setup-python@v2`、Python 3.8。 | `.github/workflows/test_of_*.yml` | 本線不升級那些 pin，避免每次上游同步都衝突。fork CI 用 checkout v7 / Python 3.12。 |
| R-05 | P3 | `scripts/requirements.txt` 鎖在 2021 的 requests 2.27.1 等。本機改用 `requests>=2.32`。 | `scripts/requirements.txt` vs `requirements-dev.txt` | 不幫上游升 pin。Dependabot 不開 pip。 |

## 已檢查、不列為 finding

- 本 fork `tools/check_upstream_updates.py` 以 argv 列表呼叫 `git`，無 `shell=True`。
- `README.md` 未翻譯、無 `README.en.md`／`README.zh-Hant.md`。
- `origin` = `SanHsien/public-apis`，`upstream` = `public-apis/public-apis`，分支 `master`。
- Baseline `reviewed_through` 等於 clone 時 HEAD `c045a2eb505f0f8b7992bb4af53cc020f25003fd`。
- 無 `.env`、金鑰。venv 已被 `.gitignore` 排除。

## 尚未宣稱範圍

- **沒有**對 1000+ 個 API 做活連結或免費額度抽樣。
- **沒有**宣稱上游 catalog validator 在當前 `master` 是綠的。反證是 R-01／R-02。
- `dev_check.ps1` **不含** Bandit、CodeQL、完整 `links.py`。
- **不宣稱** fork 有自己的 GitHub Release 或獨立版號。

## 建議下一步（未動手）

1. 第一次 push 後確認 GitHub Actions 的 CI 與 Upstream check 為綠，上游三個 workflow 為 skipped。
2. 若要回貢：重複連結去重（R-02）比修贊助表格式（R-01）小。
3. 每週一 03:00 UTC 的 `upstream-check.yml` 失敗時，依 [`docs/UPSTREAM.md`](docs/UPSTREAM.md) 審查後再推進 baseline。
