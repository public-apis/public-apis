# 開發環境

維護者與 AI 接手用的開發文件。查 API 請看 [`README.md`](../README.md)；上游同步在 [`UPSTREAM.md`](UPSTREAM.md)；決策在 [`DECISIONS.md`](DECISIONS.md)。

## 架構

```text
README.md（人工整理的 public API 目錄）
        │
        ├─ scripts/validate/format.py     欄位、排序、描述長度
        ├─ scripts/validate/links.py      重複連結（日常）／活連結（上游排程）
        └─ scripts/tests/                 上游 unittest
```

根目錄其餘檔案（`FORK.md`、`tools/`、`docs/`、`tests/`）是本 fork 的開發與治理骨架。

## 本機開發（Windows）

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install --upgrade pip
.venv\Scripts\python -m pip install -r requirements-dev.txt
$env:PYTHONUTF8 = "1"
pwsh -NoProfile -File tools\dev_check.ps1
```

只查某一類 API 時，打開 `README.md` 對應章節即可，不必建 venv。

手動重跑單項：

```powershell
.venv\Scripts\python scripts\validate\format.py README.md
.venv\Scripts\python scripts\validate\links.py README.md --only_duplicate_links_checker
.venv\Scripts\python tools\check_upstream_updates.py
```

## Canonical gate

`tools\dev_check.ps1` 會依序：

1. `python -m compileall`（`scripts`、`tests`、`tools`）
2. `ruff check`（E9 + F，只掃 `tests`、`tools`；不改上游 `scripts/` 的寫法）
3. `pytest tests/ -q`
4. `python -m unittest discover tests`（在 `scripts/` 目錄）
5. `python tools/check_links.py`

不把 `format.py README.md` 或完整／重複連結掃描當本 fork 硬閘門：上游 `master` 當下自己就過不了。細節見 [`DECISIONS.md`](DECISIONS.md)。

PR CI 在 Ubuntu 跑 3.12 與 3.14，Windows 跑 3.14。上游原有 workflows 加上 `github.repository == 'public-apis/public-apis'`，避免在本 fork 每天紅燈。

## 不要做的事

- 不要翻譯 `README.md`。
- 不要為了 fork 文件去改上游 `CONTRIBUTING.md`。
- 不要在日常 gate 裡做完整活連結掃描。
- 不要提交 API key 或把本目錄當成自己的 API 產品。
- 測試不要去打真實第三方 API；fork 測試只鎖維護骨架。
