# Contributing

Welcome to the **glibc Public API Index** — a manually curated reference of GNU C Library functions, organized by module with standard compliance and thread-safety annotations.

## Format

所有 glibc API 条目统一使用以下 **5 列** Markdown 表格格式：

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| `[function_name](https://man7.org/linux/man-pages/man3/function_name.3.html)` | `<header.h>` | 简短描述（英文，不超过 200 字符） | 标准版本 | Yes / No |

## Column Guide

### 1. Function

函数名，需链接到 man7 手册页。格式：
- `[function](https://man7.org/linux/man-pages/man[section]/[function].[section].html)`
- section 通常为 2（系统调用）或 3（库函数）

### 2. Header

函数所在头文件，用反引号和尖括号包围。例如：
- `<stdio.h>`
- `<stdlib.h>`
- `<pthread.h>`

### 3. Description

简短英文描述，建议不超过 200 字符，首字母大写，不用句号结尾。

**示例：**
- `Open a file and associate a stream with it`
- `Compute the sine of an angle`

### 4. Standard

标注函数遵循的标准。常见值：
- `C89` - C 标准 1989
- `C99` - C 标准 1999
- `POSIX.1-2001` - POSIX 标准 2001
- `POSIX.1-2008` - POSIX 标准 2008
- `BSD` - BSD 扩展
- `SVID` - System V 接口定义
- `GNU` - GNU 扩展
- `Linux` - Linux 特定
- `POSIX.1-2001, C89` - 多个标准用逗号分隔

### 5. MT-Safe

线程安全标注。值只能是 `Yes` 或 `No`。
- `Yes` - 多线程安全（MT-Safe / MT-Safe locale 等）
- `No` - 存在竞争条件（例如 `tmpnam`, `strtok`, `rand` 等）

> 参考 glibc 手册中每个函数末尾的 `MT-Safe` 标注。若该函数标记为 `MT-Safe` 或 `MT-Safe locale` 等变体，填 `Yes`；若标记为 `MT-Unsafe`，填 `No` 并在括号中注明原因，如 `No (race:strtok)`。

## Table Structure

每个模块使用二级标题 `## Module Name (headers...)`，模块内使用三级标题 `### Subsection` 组织不同功能组。表格前必须有一行表头：

```
### Sub Section

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [func](...) | `<header.h>` | Description | Standard | Yes |
```

模块之间使用 `<br>` 和 `---` 分隔。

## Alphabetical Order

每个小节内的函数按名称字母顺序排列（严格按 ASCII 顺序）。

例如：
```
fclose -> feof -> fflush -> fgetc -> fgetpos -> fgets -> ...
```

## Local Validation

在提交 PR 前，请运行格式校验脚本确认表格无误：

```bash
# 校验 5 列表格格式（列数、链接格式、描述长度等）
python scripts/validate/format.py README.md
```

脚本检查项：
- 每行是否恰好 5 列
- Function 列是否为 `[name](https://man7.org/...)` 格式
- Header 列是否为 `` `<header.h>` `` 格式
- Description 是否以大写开头且不超过 200 字符
- Standard 列格式是否合法
- MT-Safe 列是否为 `Yes` 或 `No`
- 表格行前是否有表头行

## Pull Request Guidelines

- 每个 PR 只添加一个模块或一组相关函数
- 确保格式严格遵循 5 列表格
- 按字母顺序添加新条目
- Description 使用英文，简洁明了
- 确保表格分隔符行有 5 个 `---`
- 运行本地校验脚本确认格式无误

## Header Reference

常用头文件列表供参考：
- `<stdio.h>` - 标准 I/O
- `<stdlib.h>` - 通用工具
- `<string.h>` - 字符串操作
- `<math.h>` - 数学函数
- `<time.h>` - 时间和日期
- `<pthread.h>` - 线程
- `<unistd.h>` - POSIX 系统调用
- `<sys/stat.h>` - 文件状态
- `<errno.h>` - 错误码
- `<signal.h>` - 信号
- `<locale.h>` - 本地化
- `<regex.h>` - 正则表达式
- `<dlfcn.h>` - 动态链接
- `<wchar.h>` - 宽字符
- `<complex.h>` - 复数数学
- `<search.h>` - 搜索/排序
