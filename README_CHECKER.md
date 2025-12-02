# Public API 可用性检测工具

一个功能强大的Python CLI工具，用于并发检测Public API的可用性并生成详细检测报告。

## 功能特性

- 🚀 **并发检测**: 支持高并发API请求，可灵活配置并发数
- 📥 **多格式输入**: 支持从JSON和CSV文件读取API列表
- 📤 **多格式输出**: 生成JSON或CSV格式的检测报告
- ⏱️ **智能缓存**: 内置本地缓存机制，支持TTL过期策略，可强制刷新
- 🔁 **重试机制**: 自动重试失败请求，带指数退避策略
- 📊 **详细报告**: 记录HTTP状态码、响应时间、错误信息和检查时间
- 📋 **进度显示**: 实时显示检测进度和详细日志
- 🧪 **单元测试**: 完整的pytest单元测试套件，mock网络请求避免实际调用

## 安装依赖

```bash
# 进入scripts目录
cd scripts

# 安装所需依赖
pip install -r requirements-checker.txt
```

## 快速开始

### 基础使用示例

```bash
# 从JSON文件读取API列表，生成JSON格式检测报告
python check_apis.py --input ../data/apis.json --output ../results/apis_report.json

# 从CSV文件读取API列表，生成CSV格式检测报告
python check_apis.py --input ../data/apis.csv --output ../results/apis_report.csv
```

### 高级配置

```bash
# 自定义并发数为20，超时时间15秒，重试次数5次
python check_apis.py \
    --input ../data/apis.json \
    --output ../results/apis_report.json \
    --concurrency 20 \
    --timeout 15 \
    --retries 5

# 强制刷新缓存，忽略已有缓存结果
python check_apis.py \
    --input ../data/apis.json \
    --output ../results/apis_report.json \
    --force

# 设置缓存过期时间为1小时（默认）
python check_apis.py \
    --input ../data/apis.json \
    --output ../results/apis_report.json \
    --cache-ttl 3600
```

## 参数说明

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `--input` | string | 必填 | 输入API列表文件路径（支持JSON/CSV格式） |
| `--output` | string | 必填 | 输出检测报告文件路径（支持JSON/CSV格式） |
| `--concurrency` | int | 10 | 并发请求数 |
| `--timeout` | int | 10 | 单个请求超时时间（秒） |
| `--retries` | int | 3 | 请求失败后的重试次数 |
| `--cache-ttl` | int | 3600 | 缓存过期时间（秒） |
| `--force` | flag | False | 强制刷新缓存，忽略已有缓存结果 |

## 文件格式

### 输入文件格式

#### JSON格式
```json
[
  {
    "name": "GitHub API",
    "description": "GitHub REST API",
    "link": "https://api.github.com",
    "category": "Development"
  },
  {
    "name": "JSONPlaceholder",
    "link": "https://jsonplaceholder.typicode.com"
  }
]
```

#### CSV格式
```csv
name,description,link,category
GitHub API,GitHub REST API,https://api.github.com,Development
JSONPlaceholder,Fake online REST API,https://jsonplaceholder.typicode.com,Testing
```

### 输出报告格式

输出报告将包含原始API信息以及以下检测字段：

- `check_time`: 检测时间（ISO格式）
- `status`: 检测状态（success/error/timeout）
- `status_code`: HTTP响应状态码（仅success时存在）
- `response_time_ms`: 响应时间（毫秒）
- `error`: 错误信息（仅error/timeout时存在）

#### 示例输出
```json
{
  "name": "GitHub API",
  "description": "GitHub REST API",
  "link": "https://api.github.com",
  "category": "Development",
  "check_time": "2024-05-01T12:00:00.000000",
  "status": "success",
  "status_code": 200,
  "response_time_ms": 125,
  "error": null
}
```

## 运行单元测试

```bash
cd scripts

# 运行所有测试
pytest tests/test_check_apis.py -v

# 生成测试覆盖率报告
pytest --cov=check_apis tests/
```

## 项目结构

```
.
├── data/                 # 测试数据目录
│   └── apis.json        # 示例API列表文件
├── scripts/              # 主程序目录
│   ├── check_apis.py    # 主CLI工具
│   ├── requirements-checker.txt # 依赖文件
│   └── tests/           # 测试目录
│       └── test_check_apis.py # 单元测试文件
├── results/              # 报告输出目录
└── README_CHECKER.md     # 项目文档
```

## 缓存机制

工具使用本地内存缓存，避免重复请求相同API：

1. 每个API根据`name`和`link`生成唯一哈希作为缓存键
2. 默认缓存有效期为1小时（3600秒）
3. 使用`--force`参数可以忽略缓存，强制重新检测
4. 缓存结果包含完整的检测信息

## 重试策略

采用指数退避重试策略：
- 第1次重试：等待1秒
- 第2次重试：等待2秒
- 第3次重试：等待4秒
- 以此类推，重试间隔指数增长

## 日志记录

所有检测过程会同时输出到控制台和日志文件`api_checker.log`：

- INFO级别：显示检测进度、统计结果和重要操作
- ERROR级别：记录错误信息和异常堆栈
- DEBUG级别：显示缓存使用详情

## 性能建议

1. **并发数设置**: 根据网络环境合理设置并发数，建议范围5-50
2. **超时设置**: 对于响应较慢的API适当增加超时时间
3. **缓存优化**: 对于频繁检测的API可以合理调整缓存TTL减少重复请求
4. **批量处理**: 对于大规模API列表（>1000个）建议分批处理

## 常见问题

### Q: 遇到 SSL 证书验证错误怎么办？
A: 可以在`fetch_api`方法中添加`ssl=False`参数禁用证书验证（仅限测试环境使用）

### Q: 如何代理环境中使用？
A: 可以在`aiohttp.ClientSession`中配置`connector`参数添加代理设置

### Q: 如何支持更多输入输出格式？
A: 可以扩展`APIReader`和`APIWriter`类添加新的格式支持

## License

MIT License