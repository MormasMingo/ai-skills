# 项目设计文档

## 项目概述

- **项目名称**: AI Skills 仓库
- **项目目标**: 存储和管理 Trae IDE 的自定义 Skill，提供文档管理规范 Skill
- **核心功能**: 
  - 文档管理规范 Skill 的创建和维护
  - 项目文档标准化管理

## 功能需求

### 文档管理规范 Skill
- 自动创建和维护项目设计文档 (design.md)
- 规范 README.md 的内容结构
- 管理 .gitignore 的忽略规则
- 提供文档创建和更新的标准流程

### Project Rules 管理
- 创建和初始化 `.trae/rules/project_rules.md`（固定路径、固定文件名）
- 该文件在调用AI接口时自动提交给AI作为规范要求
- 包含检查点管理规范（引用 documents/checkpoints/）
- 包含命令执行规范
- 包含项目特定约束
- 与全局用户规则互补，不重复

### Documents 文档管理规范体系
- 初始化 `documents/` 目录结构
- 创建 `00-specification/` 通用规范文档
- 建立文档编号体系 `[层级]-[模块]-[分类]-[序号]`
- 定义文档元信息 YAML Front Matter 规范
- 项目迭代时自动更新文档内容

### Checkpoints 检查点管理机制
- 检查点目录位于 `documents/checkpoints/`
- 创建检查点文档（四个标准部分：禁止行为、建议规范、待办任务、后续备忘）
- 文件命名规范 `YYYY-MM-DD-[序号]-[描述].md`
- 检查点复读机制（对话开始前、上下文丢失时）
- 检查点状态更新（任务完成时立即更新）

### 项目初始化
- Git 仓库自动初始化
- 基础配置文件创建
- 文档模板生成
- 完整的文档体系初始化

## 技术架构

- **Skill 格式**: Markdown + YAML Frontmatter
- **存储位置**: `.trae/skills/<skill-name>/SKILL.md`
- **版本控制**: Git
- **规则文件**: `.trae/rules/project_rules.md`（固定路径，AI接口自动提交）
- **文档体系**: `documents/` 目录下管理所有项目文档
- **检查点目录**: `documents/checkpoints/` 统一管理检查点

## 文档规范

### Skill 设计标准
- name: 小写字母、数字和连字符，不超过64字符
- description: 第三人称描述，包含功能和触发时机，不超过1024字符
- 内容结构清晰，包含触发条件、执行流程、输出要求

### Project Rules 规范
- **固定路径**: `.trae/rules/project_rules.md`
- **作用**: 调用AI接口时自动提交给AI
- **内容**: 检查点管理规范、命令执行规范、项目特定约束、任务跟进机制、方案生成文档化规范
- **原则**: 与全局用户规则互补，避免重复
- **新增**: 
  - 任务跟进机制：确保始终通过文档管理工具跟进需求、任务进度、待完成事项
  - 方案生成文档化规范：凡是需要生成方案的时候，都必须自动生成文档进行保存

### Documents 文档管理规范
- **根目录**: `documents/`
- **编号体系**: `[层级]-[模块]-[分类]-[序号]`
- **层级**: 00-spec, 01-project, 02-module
- **分类**: 00-index, 01-requirements, 02-design, ...
- **元信息**: YAML Front Matter（doc-id, version, status, created, updated, author）

### Checkpoints 检查点规范
- **目录**: `documents/checkpoints/`
- **文件名**: `YYYY-MM-DD-[序号]-[描述].md`
- **四部分结构**: 禁止行为、建议规范、待办任务、后续备忘
- **状态**: active | completed | archived
- **复读时机**: 对话开始前、上下文丢失时

### 项目文档清单
- design.md: 项目设计描述
- README.md: 项目简介
- .gitignore: Git 忽略规则
- .trae/rules/project_rules.md: AI接口提交的项目规则
- documents/00-specification/: 通用规范文档
- documents/checkpoints/: 检查点文档

## 迭代记录

- 2026-02-27: 初始版本，创建文档管理规范 Skill
- 2026-02-27: 功能增强，新增 Project Rules 管理、Documents 文档管理规范体系、Checkpoints 检查点管理机制
- 2026-02-27: 结构调整，project_rules.md 固定为 `.trae/rules/project_rules.md`，检查点目录调整为 `documents/checkpoints/`
- 2026-02-27: 规则完善，新增任务跟进机制，确保始终通过文档管理工具跟进需求、任务进度、待完成事项
- 2026-02-27: 补充文档规范要求：凡是需要生成方案的时候，都必须自动生成文档进行保存
