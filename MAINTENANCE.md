# Maintenance Playbook（维护手册）

> 本仓库派生自 [public-apis](https://github.com/public-apis/public-apis)，沿用了其「靠纪律、靠核实、勤清理」的维护传统，并适配到 glibc API 索引场景。本文档把这些实践固化为可执行的标准作业程序（SOP），方便任何贡献者按同一标准维护列表质量。

## 1. 字母序纪律（Alphabetical Order）

**来源**：上游曾手工把 `BuyWhere` 归位到正确的字母序位置，体现「列表必须保持可扫描」的纪律。

**本项目落地**：
- `scripts/validate/format.py` 的 `check_alphabetical_order()` 在每个 `###` 小节内检查函数名是否严格按 ASCII 升序，违规则报 **warning（非致命）**。
- **新提交必须保持字母序**；存量乱序（当前约 305 处）作为渐进修复目标，不阻断 CI。

**命令**：
```bash
python scripts/validate/format.py README.md
# 输出示例: Line   46: [warn] 'fdopen' should come before 'freopen' (subsection 'Stream Open/Close' not in alphabetical order)
```

## 2. 元数据核实（Metadata Verification）

**来源**：上游曾将 `Road511` 的 CORS 字段从 `Yes` 改为 `No`，依据是按实际行为核实，而非照搬旧值。

**本项目落地**：
- 每个条目的 `Standard` / `MT-Safe` 必须对照 [man7.org](https://man7.org) 手册页末尾标注核实后再填写。
- `MT-Safe` 列：`MT-Safe` / `MT-Safe locale` 等变体填 `Yes`；`MT-Unsafe` 填 `No (race:xxx)`。
- `scripts/validate/links.py` 联网校验 man7 链接可达性——**返回 404 即视为元数据失实**。

**命令**：
```bash
python scripts/validate/links.py README.md        # 全量可达性校验（较慢）
python scripts/validate/links.py README.md -odlc   # 仅重复链接检查（快）
```

## 3. 死条目清理（Dead Entry Hygiene）

**来源**：上游删除失效的 `PlaceKitten` 条目，保持列表真实可用。

**本项目落地**：
- 定期跑 `links.py`，凡 man7 返回 404 的函数链接 → 标记为死条目，移除或替换为有效 man 页。
- `Standard` 标注 `removed` / `deprecated` / `Obsolete` 的函数**保留但必须在 Description 开头写明 `(deprecated) ...`**（参考现有 `gets` 条目）。
- `format.py` 对已废弃但未在描述中标注的函数报 warning。

**审查清单**：
- [ ] man7 链接全部返回 200
- [ ] 无重复函数条目
- [ ] 废弃函数均已显式标注

## 4. 描述深度统一（Description Depth）

**来源**：上游补齐 `BuyWhere` 缺失的国家覆盖描述，使条目信息完整一致。

**本项目落地**：每条 `Description` 建议遵循统一模板：

> **[功能简述]** + （关键参数） + （返回值 / 常见错误）

示例对比：
- 弱：`Open a file`
- 强：`Open a file and associate a stream with it (pathname, mode; returns FILE* or NULL on error)`

- `format.py` 对过短（< 10 字符）的描述报 warning，提示补充。

## 定期审计（建议每月一次）

```bash
# 1. 格式与警告（字母序 / 短描述 / 废弃标注）
python scripts/validate/format.py README.md

# 2. 重复链接检查（快）
python scripts/validate/links.py README.md -odlc

# 3. man7 可达性 / 死条目检测（较慢，可排期执行）
python scripts/validate/links.py README.md
```

## 派生声明

本项目以 [public-apis](https://github.com/public-apis/public-apis) 的文档格式规范为起点，已重定位为 **glibc（GNU C Library）公共 API 索引**。我们保留对其维护纪律的敬意，但项目内容与目标已独立演进。感谢 public-apis 社区奠定的列表维护范式。
