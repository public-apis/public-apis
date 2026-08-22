# 上游維護

## Remote

- Fork：`origin` → `https://github.com/SanHsien/public-apis.git`
- 原作者：`upstream` → `https://github.com/public-apis/public-apis.git`
- 追蹤分支：`master`

## 檢查新提交

```powershell
git fetch upstream master
python tools\check_upstream_updates.py --strict
```

工具以 `tools/upstream_baseline.json` 的 `reviewed_through` 為起點，列出所有未審查提交。
有新提交或檢查失敗時，`--strict` 回傳非零；排程 workflow 也會因此明確失敗。

## 審查清冊

每次只做一次批次審查：

1. 讀 commit 主旨與變更檔案。
2. 判斷是否與 Windows gate、fork 文件或測試衝突。
3. 可直接同步的提交用 merge；只需要部分修正時 cherry-pick 或最小重做。
4. 跑 `pwsh -NoProfile -File tools\dev_check.ps1`。
5. 在 `docs/DECISIONS.md` 記錄採用／略過理由。
6. 驗證完成後才把 baseline 推進到已審查的完整 40 字元 SHA。

Baseline 代表「已審查」，不代表「全部已合併」。

`README.md` 新條目直接同步，不必翻譯。若上游改了 `scripts/validate/` 或 GitHub Actions，才需要核對本 fork 的 Windows gate 是否仍能跑。

## 2026-08-22：fork 起點

本 fork 自上游 `master` `c045a2eb505f0f8b7992bb4af53cc020f25003fd`
（`Merge pull request #6962 from ddevetak/add-football-charts`）建立。此 SHA 設為第一個 `reviewed_through`。
之後的上游 commit 才需要進入審查清冊。
