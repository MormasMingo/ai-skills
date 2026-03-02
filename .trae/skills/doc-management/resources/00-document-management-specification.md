---
doc-id: 00-spec-00-001
version: 1.0.0
status: published
created: 2026-03-02
updated: 2026-03-02
author: AI Assistant
tags: [specification, document-management]
---

# 文档管理规范

## 1. 概述

### 1.1 目的
规范项目中的文档创建、更新和维护流程，确保项目文档的一致性、完整性和可维护性。

### 1.2 适用范围
适用于所有使用本文档管理规范的项目。

### 1.3 术语定义
| 术语 | 定义 |
|------|------|
| Skill | Trae IDE 中的技能，通过 SKILL.md 定义 |
| Checkpoint | 检查点文档，用于记录任务状态和进度 |
| Project Rules | 项目规则文件，位于 .trae/rules/ 目录 |

## 2. 目录结构

```
documents/
├── 00-specification/       # 通用规范文档（可选，可由Skill提供）
├── 01-projects/            # 项目级文档
└── checkpoints/            # 检查点文档
```

## 3. 文档元信息规范

每个规范文档应以 YAML Front Matter 开头：

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

## 4. 检查点文档规范

### 4.1 文件命名
```
YYYY-MM-DD-[序号]-[描述].md
```

### 4.2 必须包含的四个部分
1. **禁止行为** - 必须严格遵守的规范
2. **建议规范** - 建议遵守的最佳实践
3. **待办任务** - 本次需求的任务列表
4. **后续备忘** - 暂不处理但需记录的事项

## 5. 变更记录

| 版本 | 日期 | 变更内容 | 作者 |
|------|------|----------|------|
| 1.0.0 | 2026-03-02 | 初始版本 | AI Assistant |
