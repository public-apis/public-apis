# 🏛️ glibc Public API Index — 系统架构设计

> 版本: v1.0 | 状态: 草案 | 作者: Software Architect
> 
> 本文档描述 `ghshhf/public-apis` 项目从静态 Markdown 索引向可扩展系统平台的架构演进路径。

> ⚠️ **草案 / 未落地**：本文档是架构演进的**规划草案**。当前仓库实际状态为 **V1（静态 Markdown 单文件）**。下文中的 **V2 / V3 / V4 均为规划中、尚未落地**的方案；与之对应的 ADR 多数处于「已提议」状态，仅 ADR-004（CI/CD 门禁）已部分实现（见对应条目）。请勿将本文档视为已交付功能。

---

## 目录

1. [现状分析](#1-现状分析)
2. [领域驱动设计（DDD）](#2-领域驱动设计ddd)
3. [系统架构总览（C4 模型）](#3-系统架构总览c4-模型)
4. [数据架构演进方案](#4-数据架构演进方案)
5. [平台分层架构](#5-平台分层架构)
6. [质量属性分析](#6-质量属性分析)
7. [架构决策记录（ADR）](#7-架构决策记录adr)
8. [长期发展规划路线图](#8-长期发展规划路线图)

---

## 1. 现状分析

### 当前架构（V1：静态 Markdown 文档）

```
┌─────────────────────────────────────────────────────────┐
│  README.md (巨型单文件, ~34K tokens, 20 个模块, 600+ API)   │
│  5列 Markdown 表格 (Function | Header | Description       │
│                        | Standard | MT-Safe)              │
├─────────────────────────────────────────────────────────┤
│  scripts/                                                   │
│  ├── validate/format.py   ← 表格格式校验                     │
│  ├── validate/links.py    ← 外部链接健康检查                  │
│  └── tests/              ← 单元测试                         │
├─────────────────────────────────────────────────────────┤
│  .github/workflows/                                         │
│  ├── test_of_push_and_pull.yml    ← Push/PR 格式校验         │
│  ├── test_of_validate_package.yml ← 单元测试                 │
│  └── validate_links.yml            ← 每日链接检查（scheduled） │
└─────────────────────────────────────────────────────────┘
```

### 已识别的问题

| 问题 | 严重性 | 说明 |
|------|--------|------|
| 单文件瓶颈 | P0 | 34K tokens 的 README.md 难以维护、Diff 冲突频繁 |
| 无结构化数据 | P0 | Markdown 不能被程序化查询、无法提供 API |
| 无搜索能力 | P1 | 用户只能浏览器 Ctrl+F，无法按标准/线程安全过滤 |
| 无版本管理 | P1 | glibc 版本演进（2.35→2.38）缺乏追踪机制 |
| 无渲染平台 | P2 | 缺乏 Web Dashboard、交互式浏览体验 |
| 贡献门槛高 | P2 | PR 需手动校验格式，缺乏自动化辅助工具 |
| 无国际化考虑 | P3 | 只有英文描述 |

---

## 2. 领域驱动设计（DDD）

### 2.1 Event Storming — 识别领域事件

```
用户浏览 API  →  用户搜索函数  →  用户查看详情
      ↓               ↓               ↓
 贡献者提交 PR  →  审核合并  →  自动校验格式
      ↓               ↓
  链接失效发现  →  链接修复  →  内容更新发布
      ↓
  标准版本更新  →  MT-Safe 重新标注
```

### 2.2 限界上下文（Bounded Context）

```
┌─────────────────────────────────────────────────────────────┐
│                   glibc API Index System                      │
│                                                              │
│  ┌─────────────────┐  ┌─────────────────┐  ┌──────────────┐  │
│  │   Content Core   │  │   Curation       │  │   Search     │  │
│  │   (API 数据载体)   │  │   (内容治理)       │  │   (搜索索引)   │  │
│  ├─────────────────┤  ├─────────────────┤  ├──────────────┤  │
│  │ - 函数定义        │  │ - PR 审核流程     │  │ - 全文搜索    │  │
│  │ - 头文件映射       │  │ - 格式自动校验    │  │ - 条件过滤    │  │
│  │ - 标准标注        │  │ - 链接健康检查    │  │ - 模糊匹配    │  │
│  │ - MT-Safe 标注    │  │ - 版本追踪       │  │ - 自动补全    │  │
│  └────────┬────────┘  └────────┬────────┘  └──────┬───────┘  │
│           │                    │                    │         │
│  ┌────────▼────────┐  ┌───────▼────────┐  ┌───────▼───────┐  │
│  │   Publishing     │  │   Analytics     │  │  Integration  │  │
│  │   (发布/分发)     │  │   (数据洞察)     │  │  (外部集成)    │  │
│  ├─────────────────┤  ├─────────────────┤  ├──────────────┤  │
│  │ - Web 平台      │  │ - 热门函数统计   │  │ - REST API   │  │
│  │ - 静态站点       │  │ - 标准覆盖度     │  │ - GraphQL    │  │
│  │ - Markdown 快照  │  │ - 贡献者统计     │  │ - GitHub App │  │
│  │ - NPM/Homebrew  │  │ - 链接健康度报告  │  │ - IDE 插件   │  │
│  └─────────────────┘  └─────────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### 2.3 核心聚合（Aggregates）与实体（Entities）

| 聚合根 | 实体 | 值对象 | 不变条件 |
|--------|------|--------|----------|
| **Function** | function_name, section, header | description, standard, mt_safe | 函数名唯一 |
| **Module** | module_name, subsection | functions[] List | 模块内无重名函数 |
| **Standard** | standard_name, version | url, status | 标准名称遵循 glibc 规范 |
| **Contribution** | pr_number, author | changes[], review_status | 每个 PR 至少修改一个函数 |
| **LinkCheck** | url, checked_at | status_code, error_message | 日检一次 |

### 2.4 上下文映射（Context Mapping）

| 上游 | 下游 | 关系类型 | 说明 |
|------|------|----------|------|
| Content Core | Curation | 共享内核 (Shared Kernel) | 数据模型高度耦合 |
| Curation | Publishing | 遵奉者 (Conformist) | Publishing 遵从 Curation 的发布策略 |
| Content Core | Search | 事件发布 (Event-driven) | 内容变更触发搜索索引更新 |
| Publishing | Integration | 开放主机 (Open Host) | Integration 通过 API 获取数据 |
| Publishing | Analytics | 反腐败层 (ACL) | Analytics 将原始数据转换为统计指标 |

---

## 3. 系统架构总览（C4 模型）

### 3.1 Level 1: 系统上下文

> 参见可视化图表 [architecture-context-c4-level1]

**glibc API Index** 作为核心系统，与四类外部角色交互：
- **C 系统程序员**：查询 API 参考、搜索函数、浏览标准兼容性
- **开源贡献者**：通过 PR 提交新函数、修正描述、更新 MT-Safe 标注
- **GitHub Actions**：自动触发 CI 流水线（格式校验、链接检查、单元测试）
- **外部工具/IDE**：通过公开 API 消费结构化数据（LSP 插件、文档生成器等）
- **glibc 上游**：追踪 glibc 版本发布以更新内容

### 3.2 Level 2: 容器架构（部署单元）

```
┌───────────────────────────────────────────────────────────────┐
│                     glibc API Index System                       │
│                                                                  │
│  ┌─────────────────────┐   ┌──────────────────────┐             │
│  │   GitHub Repository   │   │  GitHub Pages / CDN   │             │
│  │   ┌───────────────┐  │   │  ┌────────────────┐  │             │
│  │   │ README.md     │  │   │  │ 静态 Site (SSG) │  │             │
│  │   │ (结构化数据源)  │  │   │  └────────────────┘  │             │
│  │   ├───────────────┤  │   └──────────────────────┘             │
│  │   │ scripts/      │  │   ┌──────────────────────┐             │
│  │   │ (Python 校验)  │  │   │  REST API Server     │             │
│  │   ├───────────────┤  │   │  (FastAPI/Express)    │             │
│  │   │ .github/work  │  │   └──────────────────────┘             │
│  │   │ flows/        │  │   ┌──────────────────────┐             │
│  │   └───────────────┘  │   │  Search Engine        │             │
│  │                      │   │  (MeiliSearch/Tantivy)│             │
│  └─────────────────────┘   └──────────────────────┘             │
└───────────────────────────────────────────────────────────────┘
```

---

## 4. 数据架构演进方案

> 📌 V2 / V3 / V4 在本文档中仅为**规划草案，尚未落地**。当前仓库仍为 V1（静态 Markdown 单文件 + Python 校验脚本），README.md 是单一事实源。

### 4.1 当前：V1 — Markdown Monolith

```yaml
数据格式: README.md (Markdown 5列表格)
范式: 非结构化
查询能力: 仅 Ctrl+F
版本管理: Git log
分发方式: GitHub 直接浏览
```

### 4.2 近期：V2 — 结构化数据层

**分离数据与展示，引入 JSON/YAML 数据源：**

```
public-apis/
├── data/                          # ← NEW: 结构化数据目录
│   ├── modules/
│   │   ├── stdio.yaml             # - Standard I/O
│   │   ├── string.yaml            # - Character & String
│   │   ├── memory.yaml            # - Memory Management
│   │   ├── math.yaml              # - Math Library
│   │   ├── threading.yaml         # - Threading
│   │   └── ... (20 modules)
│   └── index.yaml                 # 模块索引
├── scripts/
│   ├── generate_readme.py         # ← NEW: 从 data/ 生成 README.md
│   └── validate/schema.py         # ← NEW: JSON Schema 校验
├── README.md                      # 保持向下兼容
└── architecture/                  # 架构文档
```

**YAML 数据模型示例（data/modules/stdio.yaml）：**

```yaml
module: Standard I/O
headers: [stdio.h, unistd.h, fcntl.h]
subsections:
  - name: Stream Open/Close
    functions:
      - name: fopen
        header: <stdio.h>
        description: Open a file and associate a stream with it
        standard: "POSIX.1-2001, C89"
        mt_safe: Yes
        man_section: 3
      - name: fclose
        header: <stdio.h>
        description: Flush and close a stream
        standard: "POSIX.1-2001, C89"
        mt_safe: Yes
        man_section: 3
```

**V2 的质量属性权衡：**

| 维度 | 变化 | 权衡 |
|------|------|------|
| 可维护性 | ✅ 显著提升 — 模块化数据，冲突概率降低 90% | ❌ 新增数据 → Markdown 的生成步骤 |
| 贡献友好度 | ✅ PR 可聚焦单个模块，Diff 可读 | ❌ 贡献者需了解 YAML 格式 |
| 数据完整性 | ✅ Schema 校验保证 5 列完备 | — |
| 兼容性 | ✅ README.md 保持自动生成，PR 流程不变 | — |

### 4.3 中期：V3 — 数据库 + API 层

```yaml
数据存储: SQLite (轻量) → PostgreSQL (生产)
搜索引擎: MeiliSearch (全文搜索) 或 Tantivy (Rust)
API 协议: REST + GraphQL
缓存层: Redis (可选, 高流量场景)
```

**核心数据模型（PostgreSQL）：**

```sql
-- 模块表
CREATE TABLE modules (
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(100) NOT NULL UNIQUE,
    slug        VARCHAR(100) NOT NULL UNIQUE,
    headers     TEXT[] NOT NULL,         -- e.g. {'stdio.h', 'unistd.h'}
    sort_order  INT NOT NULL DEFAULT 0
);

-- 函数表（核心表）
CREATE TABLE functions (
    id            SERIAL PRIMARY KEY,
    module_id     INT NOT NULL REFERENCES modules(id),
    subsection    VARCHAR(100) NOT NULL,
    name          VARCHAR(100) NOT NULL,
    header        VARCHAR(50) NOT NULL,
    description   VARCHAR(300) NOT NULL,
    standard      VARCHAR(100) NOT NULL,
    mt_safe       BOOLEAN NOT NULL,
    mt_safe_note  VARCHAR(200),          -- e.g. 'race:strtok'
    man_section   INT NOT NULL DEFAULT 3,
    glibc_version VARCHAR(20),           -- e.g. '2.35'
    deprecated    BOOLEAN DEFAULT FALSE,
    created_at    TIMESTAMP DEFAULT NOW(),
    updated_at    TIMESTAMP DEFAULT NOW(),
    UNIQUE(module_id, name)
);

-- 标准版本跟踪表
CREATE TABLE standards (
    id      SERIAL PRIMARY KEY,
    name    VARCHAR(50) NOT NULL UNIQUE, -- e.g. 'POSIX.1-2001', 'C99'
    status  VARCHAR(20) DEFAULT 'active' -- active | deprecated | superseded
);
```

**REST API 设计：**

```
GET    /api/v1/modules                    # 获取模块列表
GET    /api/v1/modules/:slug              # 获取模块详情
GET    /api/v1/modules/:slug/functions    # 获取模块下的函数
GET    /api/v1/functions                  # 函数列表（分页、过滤）
GET    /api/v1/functions/:name            # 单函数详情
GET    /api/v1/search?q=&standard=&mt_safe=&header=  # 搜索
GET    /api/v1/stats                      # 统计数据
GET    /api/v1/versions                   # glibc 版本追踪
```

**GraphQL 查询示例：**

```graphql
query SearchFunctions($q: String!, $standard: String) {
  search(query: $q, standard: $standard) {
    name
    header
    description
    standard
    mtSafe
    module {
      name
    }
  }
}
```

### 4.4 远期：V4 — 事件驱动 + 分布式

```yaml
架构: 事件驱动微服务 (Event-driven)
消息队列: RabbitMQ / NATS
数据同步: CDC (Change Data Capture)
集成: IDE 插件生态、CI/CD 集成
```

**事件流：**

```yaml
function.updated → Search 索引更新 → CDN 缓存刷新
function.added   → Analytics 统计 → 邮件通知订阅者
link.broken      → 创建 GitHub Issue → 指派修复
glibc.released   → 版本差异检测 → 更新待办清单
```

---

## 5. 平台分层架构

### 5.1 V2 详细架构（近期可落地）

```
┌──────────────────────────────────────────────────────────┐
│                   Presentation Layer                      │
│  ┌───────────────┐  ┌────────────────┐  ┌────────────┐  │
│  │ GitHub README │  │ GitHub Pages   │  │ VSCode     │  │
│  │ (向下兼容)      │  │ (静态站点 SSG)  │  │ Extension  │  │
│  └───────┬───────┘  └───────┬────────┘  └─────┬──────┘  │
└──────────┼──────────────────┼──────────────────┼─────────┘
           │                  │                  │
┌──────────▼──────────────────▼──────────────────▼─────────┐
│                   API Layer (可选, V3 启用)                │
│  ┌────────────────────────────────────────────────────┐  │
│  │  REST API / GraphQL (FastAPI + Strawberry)         │  │
│  │  分页 | 排序 | 过滤 | 搜索代理                      │  │
│  └───────────────────────┬────────────────────────────┘  │
└──────────────────────────┼───────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────┐
│                   Data Layer                               │
│  ┌────────────────────┐  ┌──────────────────────────┐    │
│  │   PostgreSQL        │  │   MeiliSearch             │    │
│  │   (规范化数据)       │  │   (全文搜索引擎)           │    │
│  └────────┬───────────┘  └──────────┬───────────────┘    │
│           │                         │                     │
│  ┌────────▼─────────────────────────▼───────────────┐    │
│  │   Sync Pipeline                                    │    │
│  │   data/*.yaml → DB → Search Index                  │    │
│  │   README.md (自动生成, 与 YAML 互为源)              │    │
│  └────────────────────────────────────────────────────┘    │
└────────────────────────────────────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────┐
│                   Curation Layer                           │
│  ┌────────────────────┐  ┌──────────────────────────┐    │
│  │   CI/CD 流水线      │  │   Schema 校验器            │    │
│  │   (Push/PR 触发)    │  │   (YAML 格式/链接/标准)    │    │
│  └────────────────────┘  └──────────────────────────┘    │
└────────────────────────────────────────────────────────────┘
```

### 5.2 模块边界与依赖方向

```
                   ┌──────────────────┐
                   │     CLI 工具      │
                   │  (contributor)   │
                   └────────┬─────────┘
                            │ 使用
                   ┌────────▼─────────┐
                   │    Validation    │
                   │    模块互不依赖    │
                   └────────┬─────────┘
                            │ 校验
               ┌────────────┼────────────┐
               │            │            │
      ┌────────▼───┐ ┌─────▼─────┐ ┌────▼──────┐
      │  YAML 数据  │ │  DB 模型   │ │  Markdown  │
      │  (data/)   │ │ (schema)  │ │ (README)  │
      └────────┬───┘ └─────┬─────┘ └────┬──────┘
               │            │            │
               └────────────┼────────────┘
                            │ 消费
                    ┌───────▼────────┐
                    │   API / Web    │
                    │   (只读对外)    │
                    └────────────────┘
```

依赖方向：**从外向内核**, 保持内核（数据模型）零外部依赖。

---

## 6. 质量属性分析

### 6.1 可扩展性（Scalability）

| 场景 | V1 现状 | V2 目标 | V3 目标 |
|------|---------|---------|---------|
| API 数量 10x | ❌ README.md 膨胀至 300K tokens | ✅ 分模块 YAML，加载性能恒定 | ✅ PostgreSQL 索引查询，单表 10w 行无压力 |
| 并发查询 100x | N/A（无服务端） | N/A（静态站点） | ✅ API 水平扩展，Redis 缓存 |
| 贡献者 10x | ❌ PR 冲突频繁 | ✅ 分模块 PR，互不干扰 | ✅ Web 编辑器，零冲突 |
| 版本追踪 | ❌ 无 | ❌ 手动管理 | ✅ 自动化版本差异检测 |

### 6.2 可靠性（Reliability）

| 场景 | 策略 | 实现 |
|------|------|------|
| 链接失效 | 自动检测 + Issue | 每日链接验证 workflow |
| 数据损坏 | 双源验证 | YAML ↔ Markdown 双向校验 |
| 格式错误 | CI 前置拦截 | PR 校验通过后不可合并 |
| 数据丢失 | Git 版本控制 | 每次提交历史可回溯 |

### 6.3 可维护性（Maintainability）

| 维度 | V1 | V2 | V3 |
|------|----|----|----|
| 数据修改 | 编辑巨型文件 | 编辑单一 YAML 模块 | Web Management UI |
| 添加 API | 手动对齐表格 | YAML + `validate` 自动完成 | Form 表单提交 |
| 批量更新 | 脚本依赖 | Schema 校验 | API batch endpoint |
| 架构文档 | ❌ 无 | ✅ arch/README.md + ADRs | ✅ 自动架构渲染 |

### 6.4 可观测性（Observability）

| 维度 | 指标 | 工具 |
|------|------|------|
| 链接健康度 | 有效链接百分比 / 总链接数 | 每日 GitHub Action report |
| 内容覆盖率 | 各标准覆盖函数数 / 模块完整度 | Analytics 仪表盘 |
| 贡献活跃度 | PR 数量 / 审核时间 / 贡献者数 | GitHub Insights |
| API 可用性 | 请求延迟 / 错误率 / QPS | Prometheus + Grafana (V3) |

---

## 7. 架构决策记录（ADR）

### ADR-001: 采用 YAML 作为结构化数据格式

**状态**：已提议
**上下文**：当前 README.md 的单文件 Markdown 格式导致了维护困难、Diff 冲突频繁、无法程序化查询等问题。需要一种可扩展、人类可读写、机器可校验的结构化数据格式。
**决策**：采用 YAML 作为数据存储格式（`data/modules/*.yaml`），替代 Markdown 表格作为数据源。README.md 通过脚本自动生成。
**备选方案**：
| 方案 | 优势 | 劣势 |
|------|------|------|
| JSON | 解析快，Python/JS 原生支持 | 人工编辑体验差（无注释，逗号敏感） |
| YAML ✅ | 人类可读性最优，支持注释，Git Diff 清晰 | 缩进敏感，大文件解析略慢 |
| TOML | 简洁，适合配置文件 | 不支持复杂嵌套结构，社区生态较小 |
| SQLite | 可直接查询 | 不适合 Git 版本控制，PR Diff 不可读 |
**后果**：
- **更容易**：数据分模块管理，PR 互不冲突；贡献者编辑体验提升；可添加 YAML Schema 校验
- **更困难**：需要额外的 README.md 生成步骤；非编程背景贡献者需学习 YAML 语法
- **可逆性**：高 — 随时可从 YAML 源码重新生成 Markdown

### ADR-002: 数据与展示分离架构

**状态**：已提议
**上下文**：当前数据存储（README.md）同时也是最终展示产物，导致数据格式受到展示层约束（如 Markdown 表格链接要求）。
**决策**：将数据层（`data/*.yaml`）与展示层（`README.md` 生成、Web 站点、API 响应）彻底分离。数据层作为**单一事实源**（Single Source of Truth），所有展示产物均由数据层派生。
**后果**：
- **更容易**：数据格式可以自由演进，不受展示约束；支持多展示形态（Markdown / Web / JSON API）；解耦开发
- **更困难**：需要维护数据→展示的转换流水线；构建阶段复杂度增加
- **可逆性**：中 — 转换流水线建立后，回退到纯 Markdown 需放弃数据独立性

### ADR-003: 选择 Modular Monolith 作为 V2 架构模式

**状态**：已提议
**上下文**：项目规模较小（~600 API 条目，20 模块），团队规模 1-3 人。微服务架构带来的运维复杂度过高。
**决策**：V2 阶段采用**模块化单体（Modular Monolith）**架构。所有功能（数据校验、README 生成、Web 服务）在单一 repo 内按模块组织，通过清晰的接口边界解耦。
**参见**：Microservices — Use When / Avoid When 对照表
**后果**：
- **更容易**：部署简单，CI/CD 流水线单一；开发迭代速度快；模块间调用零网络开销
- **更困难**：未来若需独立扩展搜索或 API 服务，需拆分出独立服务
- **可逆性**：高 — 模块化设计为后续拆分预留了接口边界

### ADR-004: 自动化 CI/CD 流水线作为质量门禁

**状态**：已落地（部分）— 第 1 层格式门禁（format.py）、第 2 层单元测试门禁（unittest）此前已落地；第 3 层链接检查 + 夜间失效**自动开 Issue** 已于本迭代通过 `validate_links.yml` 的 `actions/github-script` 步骤实现（软性告警）。
**上下文**：手工审查格式错误效率低，链接失效难以主动发现。项目需要自动化质量保障机制。
**决策**：在 GitHub Actions 中构建三层 CI/CD 流水线：
1. **格式门禁**：Push/PR 触发 YAML Schema 校验 + 格式检查 — **硬性阻断**
2. **单元测试**：Push/PR 触发 Python 测试套件 — **硬性阻断**
3. **链接健康**：每日定时运行链接检查，失效自动创建 Issue — **软性告警**
**后果**：
- **更容易**：格式问题在 PR 阶段即被捕获；链接失效自动发现；审核者负担减轻
- **更困难**：CI 失败可能阻塞紧急修复；需要维护 CI 配置和依赖版本
- **可逆性**：高 — 随时可调整 CI 规则

### ADR-005: 引入 MeiliSearch 作为全文检索引擎

**状态**：已提议（V3 阶段）
**上下文**：当 API 条目增长到数千级别后，Markdown 搜索（Ctrl+F）和数据库 LIKE 查询性能不足。需要支持多字段过滤（标准、头文件、线程安全性）和模糊匹配。
**决策**：在 V3 阶段引入 MeiliSearch 作为全文检索引擎。
**备选方案**：
| 方案 | 优势 | 劣势 |
|------|------|------|
| MeiliSearch ✅ | 开箱即用，Rust 编写，性能优异，支持中文分词 | 额外部署组件 |
| Elasticsearch | 功能最全，生态成熟 | 太重（Java 生态），运维成本高 |
| Tantivy | Rust 原生，性能极致 | 需自行封装 API，缺少 Web UI |
| PostgreSQL FTS | 零额外组件 | 中文分词弱，搜索体验不如专用引擎 |
**后果**：
- **更容易**：用户获得即时模糊搜索、过滤器、自动补全；支持多字段精确过滤
- **更困难**：需要额外部署和管理 MeiliSearch 实例；数据同步增加复杂度
- **可逆性**：中 — 引擎和数据结构耦合，切换成本存在但不高

---

## 8. 长期发展规划路线图

### 8.1 分阶段演进总览

| 阶段 | 时间 | 核心目标 | 交付物 |
|------|------|----------|--------|
| V1 | 当前 | 维持稳定 | 现有 README.md + CI 流水线 |
| V2 | 1-2 个月 | 数据结构化 | YAML 数据 + Schema 校验 + README 生成 |
| V2.5 | 3-4 个月 | 交互式平台 | GitHub Pages 静态站点 + 搜索 UI |
| V3 | 5-8 个月 | API + 搜索引擎 | REST API + MeiliSearch + Web UI |
| V4 | 9-12 个月 | 事件驱动 + 生态 | 微服务 + IDE 插件 + 自动版本追踪 |

### 8.2 V2 详细计划（1-2 个月）

**目标**：将数据从 README.md 迁移到 YAML，实现数据与展示分离

- [ ] **第 1 周**：设计 YAML Schema，创建 `data/schema.yaml`
- [ ] **第 1-2 周**：开发 `scripts/validate/schema.py`（YAML 格式校验器）
- [ ] **第 2-3 周**：开发 `scripts/generate_readme.py`（YAML → README.md 生成器）
- [ ] **第 3-4 周**：逐模块迁移（stdio → threading → networking → ...）
- [ ] **第 5-6 周**：迁移所有 20 个模块，验证双向一致性
- [ ] **第 7-8 周**：更新 CI 流水线，完善单元测试，编写贡献者文档

**关键指标**：
- README.md 100% 从 YAML 自动生成（内容一致）
- Schema 校验覆盖所有 5 列约束
- 模块迁移后 PR 冲突率下降 80%+

### 8.3 V2.5 详细计划（3-4 个月）

**目标**：构建交互式 Web 平台，提升用户体验

- [ ] 选择 SSG 框架（VitePress / Docusaurus / Astro）
- [ ] 构建模块浏览页面（按标题/头文件/标准分组）
- [ ] 实现前端搜索（基于 Lunr.js / FlexSearch.js 客户端搜索）
- [ ] 设计响应式布局（移动端适配）
- [ ] 添加 MT-Safe 可视化标记（✅/❌ 图标）
- [ ] 部署到 GitHub Pages，配置自定义域名（可选）

### 8.4 V3 详细计划（5-8 个月）

**目标**：开放 API 接口 + 引入服务端搜索引擎

- [ ] 搭建 PostgreSQL 数据库，设计表结构
- [ ] 开发数据同步脚本（data/*.yaml → PostgreSQL）
- [ ] 部署 MeiliSearch，建立搜索索引
- [ ] 开发 REST API（FastAPI Python 或 Express Node.js）
- [ ] 开发 GraphQL 端点（Strawberry / Apollo Server）
- [ ] Web UI 连接 API 实现动态交互
- [ ] 添加 API 文档（OpenAPI / Swagger）
- [ ] 部署到云平台（Railway / Fly.io / 自建 VPS）

### 8.5 V4 远景（9-12 个月）

**目标**：构建开发者生态，实现自动化版本追踪

- [ ] 事件驱动架构（RabbitMQ/NATS）
- [ ] VSCode 插件 — 在编辑器中直接查询 glibc API
- [ ] CLI 工具 — `glibc-api-cli search strtok`
- [ ] 自动 glibc 版本追踪 — 对比版本间 API 差异
- [ ] 多语言支持（中文/日文/韩文 API 描述）
- [ ] 社区贡献仪表盘（贡献者排行、模块覆盖度热力图）

### 8.6 技术栈建议

| 层 | V2 推荐 | V3 推荐 | 选择理由 |
|---|---------|---------|---------|
| 数据格式 | YAML | PostgreSQL | YAML 人类可读，DB 程序化查询 |
| 校验 | Python + Pydantic | Python + Pydantic | 与现有 scripts/ 一致 |
| CI/CD | GitHub Actions | GitHub Actions | 零成本，与 repo 集成 |
| 静态站点 | VitePress | — | Vue 技术栈，性能优异 |
| API 框架 | — | FastAPI | Python 生态，OpenAPI 自动生成 |
| 搜索引擎 | — | MeiliSearch | 轻量级，Rust 高性能 |
| 前端 | — | Vue 3 + Nuxt | 与 VitePress 技术栈统一 |
| 部署 | GitHub Pages | Railway / Fly.io | 低成本起步，渐进扩展 |

---

## 附录 A：架构演进权衡矩阵

| 决策 | 获得的 | 付出的 |
|------|--------|--------|
| YAML 替代 Markdown | 结构化查询、模块化 | 额外生成步骤 |
| 数据与展示分离 | 多输出格式 | 流水线复杂度 |
| Modular Monolith | 部署简单、迭代快 | 后期拆分成本 |
| 引入 MeiliSearch | 搜索体验质的飞跃 | 运维新组件 |
| 开放 REST API | 生态集成能力 | 安全、速率限制 |

## 附录 B：术语表

| 术语 | 定义 |
|------|------|
| **MT-Safe** | Multi-Thread Safe — glibc 线程安全性标注 |
| **Bounded Context** | DDD 中的限界上下文，定义领域模型的边界 |
| **Modular Monolith** | 代码结构模块化，但部署为单一单体应用 |
| **ADR** | Architecture Decision Record — 架构决策记录 |
| **SSG** | Static Site Generator — 静态站点生成器 |
| **C4 模型** | Context → Container → Component → Code 的四层架构描述模型 |
| **Event Storming** | DDD 中的工作坊式领域建模方法 |
| **ACL** | Anti-Corruption Layer — 反腐败层，保护领域模型不受外部污染 |

---

> 本文档由 Software Architect 自动生成，将持续根据项目演进更新。所有 ADR 接受社区讨论和修订。


