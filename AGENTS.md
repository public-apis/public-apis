# AGENTS.md

給 Codex、Claude Code、Cursor 與其他自動化代理在本專案工作時的指引。目錄本體先讀 [`README.md`](README.md)；開發與驗收細節見 [`docs/DEVELOPMENT.md`](docs/DEVELOPMENT.md)。

## 專案定位

這是 [`public-apis/public-apis`](https://github.com/public-apis/public-apis) 的 MIT fork。
核心價值是一份人工整理的免費 public API 目錄：每筆標好 Auth、HTTPS、CORS。複製說明文件網址就能用。

`origin` 是 `SanHsien/public-apis`，`upstream` 是原作者 repo，預設分支皆為 `master`。
保留上游作者、MIT 授權與 `README.md` 目錄。本 fork 的維護差異記在 [`FORK.md`](FORK.md) 與 [`docs/DECISIONS.md`](docs/DECISIONS.md)。

主要開發與完整驗收環境是 **Windows 11 + PowerShell**；Ubuntu CI 補跨平台相容性。

## 硬性邊界

- **不要翻譯或改寫 `README.md` 目錄。** 那是上游產品，不是本 fork 的維護索引。1000+ 筆條目若做成繁中鏡像，每週上游更新會無法審查。維護規則以本檔為準。
- 不要改 `CONTRIBUTING.md` 的欄位規則（Auth / HTTPS / CORS / 描述長度），除非要回貢上游。
- 不提交 API key、cookie、帳號資料，或把付費／行銷向 API 塞進目錄。
- 不推送到 `upstream`。上游同步先跑 `python tools/check_upstream_updates.py`，逐筆審查後再 merge / cherry-pick；不盲目覆蓋 fork 文件與 Windows gate。
- 不把本 repo 做成 API gateway、代理層或「一鍵呼叫所有 API」的後端。它是目錄，不是執行時。

## 技術與資料流

- Python 3.9+（本機與 fork CI 以 3.12 為準）；上游 GitHub Actions 仍跑 3.8，不要去改那些 workflow 的版本，除非回貢。
- `README.md`：API 目錄。
- `scripts/validate/`：格式與連結檢查（以上游為準）。
- `tools/`：fork 維護工具（上游檢查、相對連結檢查、Windows gate）。
- `tests/`：pytest，鎖的是 fork 骨架，不是把 1000+ API 當測試資料。
- 完整活連結掃描（`scripts/validate/links.py README.md` 不帶 `-odlc`）很慢且不穩定；日常 gate 不拿它當硬條件。上游 `format.py README.md` 在 fork 當下的 `master` 自己就失敗（贊助表格式），本線不代為修目錄。

## 開發原則

- 一般修改使用 **branch → PR → CI → merge**，不要直接在 `master` 做正常維護。
- 修 bug 先補可重現失敗測試，再做最小修正。
- 上游公開目錄格式、`CONTRIBUTING.md` 與 `scripts/validate/` 視為相容性契約。
- 不為了套格式而大改上游程式；Ruff 只閘本 fork 的 `tests/` 與 `tools/`（E9 + F）。上游 `scripts/` 的 F541／F401 留給上游。
- 使用繁體中文回覆；維護文件用繁中。目錄本體維持英文。
- PR 標題建議 Conventional Commit；合併前先讀 `gh pr diff <編號>`。
- `REVIEW.md` 是風險快照，不是每個一般 bug 的流水帳。

## 上游處理

1. `git fetch upstream master`
2. `python tools/check_upstream_updates.py --strict`
3. 逐筆判斷是否與 Windows gate、fork 文件或測試衝突。
4. 可同步的提交用 merge；只需要部分修正時 cherry-pick 或最小重做。
5. 跑 `pwsh -NoProfile -File tools\dev_check.ps1`
6. 採用／略過寫進 `docs/DECISIONS.md`，驗證後才推進 `tools/upstream_baseline.json`

Baseline 代表「已審查」，不代表「全部已合併」。

`README.md` 的新條目直接 merge 進來即可，不必翻譯。

## 驗證

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install --upgrade pip
.venv\Scripts\python -m pip install -r requirements-dev.txt
pwsh -NoProfile -File tools\dev_check.ps1
```

沒有實際跑過 Windows gate，不要宣稱本機開發環境已可用。

## 文件責任

- `README.md`：上游 API 目錄（不改寫）。
- `FORK.md`：與上游的關係、差異、同步方式。
- `NOTICE.md`：授權與 attribution。
- `docs/UPSTREAM.md`：upstream remote 與審查清冊。
- `docs/DEVELOPMENT.md`：本機開發與驗收指令。
- `docs/DECISIONS.md`：長期取捨。
- `CONTRIBUTING.md`：上游貢獻規則；新增 API 請往上游送。
- `SECURITY.md`：本 fork 的安全回報流程。
