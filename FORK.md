# Fork 維護說明

本 repo fork 自 [`public-apis/public-apis`](https://github.com/public-apis/public-apis)，
沿用 MIT License 與完整 Git 歷史。

## 為什麼維護 fork

- 保留社群持續更新的免費 public API 目錄（天氣、金融、加密貨幣、AI、地圖、動漫等）。
- 本機要能在 Windows 11 重跑上游 `scripts/validate` 單元測試，以及本 fork 的開發 gate。
- 建立逐筆審查的上游追蹤：每週自動對 `upstream/master` 列出未審查 commit。
- 不當成第二個官方產品站。目錄本體、欄位規則與貢獻格式以上游為準。

**回貢判準：修的是上游驗證腳本或目錄格式的 bug 就送回去；這裡獨創的文件／Windows 維護骨架留在這裡。**

## 與上游的差異

| 項目 | 說明 |
|---|---|
| `README.md` | **不翻譯、不改寫。** 這份 1000+ API 目錄就是產品，保持上游英文為單一真相源 |
| `AGENTS.md` / `CLAUDE.md` | 本 fork 的 AI 維護單一真相源 |
| `NOTICE.md` / `FORK.md` | 來源、授權與同步說明 |
| `tools/dev_check.ps1` | Windows 本機一鍵 gate |
| `.github/workflows/ci.yml` | 新增 Ubuntu 3.12／3.14 + Windows 3.14：pytest / ruff / 上游 unittest / 維護文件連結 |
| `.github/workflows/upstream-check.yml` | 每週對 `upstream/master` 做未審查 commit 檢查 |
| `docs/DECISIONS.md`、`docs/UPSTREAM.md`、`docs/DEVELOPMENT.md` | fork 維護文件 |
| 上游既有 workflows | 保留，但加上只在官方 `public-apis/public-apis` 執行的 guard |

產品 `README.md` 目錄、`CONTRIBUTING.md` 欄位規則、`scripts/validate/` 以上游為準，除非有已記錄的 fork 修正。

## 分支與 remote

- `origin/master`：SanHsien 維護線。
- `upstream/master`：public-apis 原始專案。
- 功能與修正使用短期分支；驗證通過後再合併到 `master`。

不要 `git push upstream`。同步方式見 [`docs/UPSTREAM.md`](docs/UPSTREAM.md)。

要新增或修正某一個 API 條目：對 [`public-apis/public-apis`](https://github.com/public-apis/public-apis) 開 PR，不要把行銷向、付費牆 API 送進本 fork。

## 換一台電腦怎麼開發

```powershell
git clone https://github.com/SanHsien/public-apis.git
cd public-apis
python -m venv .venv
.venv\Scripts\python -m pip install --upgrade pip
.venv\Scripts\python -m pip install -r requirements-dev.txt
pwsh -NoProfile -File tools\dev_check.ps1
```

只想查 API、不開發時：直接打開 [`README.md`](README.md)。
