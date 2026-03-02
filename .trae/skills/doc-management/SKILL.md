---
name: "doc-management"
description: "管理项目文档规范，包括创建和初始化project_rules、documents文档体系、检查点机制。当用户需要创建项目规则、初始化文档体系、管理检查点或更新设计文档时调用。"
---

# 文档管理

## 描述
规范项目文档创建、更新和维护流程，确保一致性、完整性和可维护性。

## 触发条件
- 创建/初始化 `.trae/rules/project_rules.md`
- 创建/更新 `design.md`
- 初始化 `documents/` 目录及文档体系
- 创建/管理 `documents/checkpoints/` 检查点
- 新建项目初始化完整文档体系

## 指令

### 1. 初始化完整文档体系
```bash
git init
mkdir -p .trae/rules documents/00-specification documents/01-projects documents/checkpoints
```
创建文件：`.trae/rules/project_rules.md`、`design.md`、`.gitignore`、`documents/README.md`

### 2. 创建 project_rules.md
- 路径固定：`.trae/rules/project_rules.md`
- 包含：检查点管理规范、命令执行规范、项目特定约束
- 引用 `documents/checkpoints/` 目录

### 3. 初始化 documents 目录
- `00-specification/`：存放通用规范文档
- `01-projects/`：存放项目级文档
- `checkpoints/`：存放检查点文档

### 4. 创建检查点文档
- 位置：`documents/checkpoints/`
- 命名：`YYYY-MM-DD-[序号]-[描述].md`
- 必须包含四个部分：禁止行为、建议规范、待办任务、后续备忘

### 5. 文档元信息规范
每个规范文档以YAML Front Matter开头：
```yaml
---
doc-id: 文档编号
version: 版本号
status: draft|review|published
created: YYYY-MM-DD
updated: YYYY-MM-DD
author: 作者
---
```

## 文件清单
| 文件路径 | 用途 |
|---------|------|
| `.trae/rules/project_rules.md` | AI接口提交的项目规则 |
| `documents/00-specification/00-document-management-specification.md` | 文档管理规范 |
| `documents/00-specification/01-checkpoint-management-specification.md` | 检查点管理规范 |
| `design.md` | 项目设计文档 |

## 参考
- 模板：templates/
- 示例：examples/
