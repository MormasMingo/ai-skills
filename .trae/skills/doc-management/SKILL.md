---
name: "doc-management"
description: "管理项目文档规范，初始化project_rules、documents体系、检查点机制"
---

# 文档管理

## 描述
规范项目文档创建、更新和维护流程，确保一致性、完整性和可维护性。

## 触发条件（以下任一情况）

### 必须触发（高优先级）
- **新建项目** - 需要初始化完整文档体系时
- **缺少 project_rules.md** - 项目根目录下 `.trae/rules/project_rules.md` 不存在
- **缺少检查点** - 对话开始前发现没有检查点文档，或对话过长/上下文丢失
- **明确指令** - 用户明确要求"使用文档工具初始化"、"创建检查点"等

### 建议触发（中优先级）
- **创建/更新 design.md** - 项目设计文档需要维护
- **初始化 documents 目录** - 项目文档体系需要建立
- **任务状态变更** - 需要更新检查点文档中的待办任务

### 触发检查清单
在以下时刻**必须**检查是否需要调用此 Skill：
- [ ] 对话开始时（检查是否有检查点需要查阅）
- [ ] 新需求提出时（检查是否需要创建检查点）
- [ ] 任务完成时（检查是否需要更新检查点）
- [ ] 对话即将结束时（检查是否有未提交的更改）

## 指令

### 1. 初始化完整文档体系
```bash
git init
mkdir -p .trae/rules documents/01-projects documents/checkpoints
```
创建文件：`.trae/rules/project_rules.md`、`design.md`、`.gitignore`

> **注意**：通用规范文档（00-document-management-specification.md、01-checkpoint-management-specification.md）已包含在本 Skill 的 resources/ 目录中，无需在项目 00-specification/ 目录中重复创建。

### 2. 创建 project_rules.md
- 路径固定：`.trae/rules/project_rules.md`
- 包含：检查点管理规范、命令执行规范、项目特定约束
- 引用 `documents/checkpoints/` 目录

### 3. 初始化 documents 目录
- `01-projects/`：存放项目级个性化文档（必需）
- `checkpoints/`：存放检查点文档（必需）
- `00-specification/`：可选，仅当需要覆盖 Skill 提供的通用规范时才创建

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
| 文件路径 | 用途 | 来源 |
|---------|------|------|
| `.trae/rules/project_rules.md` | AI接口提交的项目规则 | 项目创建 |
| `documents/01-projects/` | 项目级个性化文档 | 项目创建 |
| `documents/checkpoints/` | 检查点文档 | 项目创建 |
| `resources/00-document-management-specification.md` | 通用文档管理规范 | Skill内置 |
| `resources/01-checkpoint-management-specification.md` | 通用检查点管理规范 | Skill内置 |

## 参考
- 模板：templates/
- 示例：examples/
- 通用规范：resources/
