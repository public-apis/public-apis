# 安全政策

## 支援範圍

安全修正以本 fork 的最新 `master` 為主；上游版本的問題也會視需要回報原作者。

## 私下回報

請使用 GitHub Security Advisories 的 **Report a vulnerability** 私下回報。若該入口不可用，
請透過 GitHub 個人檔案聯絡維護者，不要先建立公開 Issue。

回報請包含影響範圍、重現步驟、受影響版本與最小必要證據。請勿附上真實 API key、cookie 或帳號。

## 特別注意

- 本專案是 API **目錄**，不是那些 API 的營運方。清單裡某一服務的漏洞，請向該服務回報。
- `scripts/validate/links.py` 會對 README 裡的公開 URL 發 HTTP 請求。不要改成帶認證、不要掃私人網段。
- 第三方 API 的資料處理政策不由本 repo 控制；呼叫前需另行審查其條款與免費額度。
