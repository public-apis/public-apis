# CLAUDE.md

請先完整閱讀並遵守 [`AGENTS.md`](AGENTS.md)。本檔只補充 Claude Code 的最小入口：

- 這是保留上游歷史的 fork；不要移除 `upstream`、原作者或 MIT 授權標示。
- `README.md` 是 API 目錄，不要改寫成本 fork 的維護索引，也不要翻譯成繁中。
- 修改驗證腳本前，先跑對應測試；提交前跑
  `pwsh -NoProfile -File tools\dev_check.ps1`。
- API key、cookie 與帳號資料一律不可提交。
- 使用繁體中文，直接交付可驗證結果，避免冗長背景鋪陳。
