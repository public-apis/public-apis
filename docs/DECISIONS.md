# 維護決策

## 2026-08-22：建立 Windows-first 維護型 fork

**決定**：fork `public-apis/public-apis`，保留 MIT 授權與完整歷史，預設分支維持 `master` 以降低與上游同步摩擦。本線聚焦 Windows 開發 gate、fork CI，以及逐筆審查的上游追蹤。目錄本體不翻譯。

**理由**：這份清單是查 API 的單一入口，上游仍在更新（fork 當下 HEAD 為 2026-08-20 的 `#6962`）。缺的是 Windows 11 上可重現的驗證骨架，以及「上游有沒有新 commit」的明確失敗訊號。直接盯上游網頁無法留下審查紀錄。

**限制**：

- 不把 fork 包裝成原創專案，不移除原作者與 MIT 標示。
- `README.md` 保持上游英文目錄，不建繁中／英文雙檔。
- `CONTRIBUTING.md` 與 `scripts/validate/` 以上游為準。
- 上游更新必須逐筆審查。
- 不啟用對 `scripts/requirements.txt` 的 Dependabot：那些 2021 pin 是上游 Ubuntu 3.8 CI 契約，本線不代為升級。

## 2026-08-22：日常 gate 不拿上游目錄檢查當硬閘門

**決定**：`tools/dev_check.ps1` 與 fork CI 不跑 `scripts/validate/format.py README.md`，也不跑 `links.py` 的重複連結／活連結掃描。改跑上游 `scripts/tests` unittest，以及本 fork 的 pytest／連結檢查。

**理由**：fork 當下對上游 `master` 實測，`format.py README.md` 因 APILayer 贊助表（3 欄而非 5 欄）、表格分隔列被當成 entry、多個分類未按字母排序而失敗；`--only_duplicate_links_checker` 至少打出 `isitdownstatus.com` 與 `tastedive.com/read/api` 兩組重複。上游自己的 `Validate links` workflow 在 2026-08-22 也是 `failure`。本線不代為修 1000+ 筆目錄來換綠燈。

完整活連結掃描留給上游官方 repo 的 `validate_links.yml`。本 fork 把那三個上游 workflow 加上 `if: github.repository == 'public-apis/public-apis'`，避免 fork 上每日紅燈。合併上游 workflow 變更時，`tests/test_docs.py` 會對非 fork 自有的 `*.yml` 檢查這條 guard。

## 2026-08-22：修 fork 審查項，不改上游產品

**決定**：R-06～R-10（連結掃描、upstream checker 例外包裝、路徑邊界、workflow 測試、CI 3.14）在本線修。R-01～R-05（目錄格式、重複連結、`format.py` 跳脫、上游 Action pin、`scripts/requirements.txt`）不修、不回貢。

**理由**：那些不是本 fork 維護骨架的缺陷，改了會跟上游目錄或 3.8 CI 契約打架。

