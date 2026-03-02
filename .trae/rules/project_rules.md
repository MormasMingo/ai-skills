# 项目规则

> 本规则适用于当前项目，与全局用户规则互补。
> 调用AI接口时会自动提交此文件内容作为规范要求。

---

## 一、检查点管理规范

### 1.1 查阅时机
- **每次对话开始前**，查阅 `documents/checkpoints/` 目录下的最新检查点文档
- **当对话过长或被压缩后**，必须重新查阅检查点文档

### 1.2 状态更新
- 任务完成后**立即**更新检查点文档的待办任务状态
- 使用 `[x]` 标记已完成，`[ ]` 标记待完成

---

## 二、命令执行规范

### 2.1 基本原则
- **严禁使用**任何形式的模拟行为、模拟数据、虚拟数据
- 执行命令前**必须确认**命令的安全性和正确性

### 2.2 删除与修改操作
- 涉及删除、修改操作前**必须备份或确认**
- 批量操作前先在测试环境验证

### 2.3 错误处理
- 命令执行失败时**必须分析原因并报告**
- 记录错误信息和解决过程

---

## 三、项目特定约束

### 3.1 技术栈规范
- 语言: Python 3.x
- 依赖管理: pip + requirements.txt

### 3.2 文档管理规范
- 文档目录: `documents/`
- 检查点目录: `documents/checkpoints/`
- 遵循文档编号体系和元信息规范
- 始终通过检查点机制跟进需求、任务进度

### 3.3 任务跟进机制
- **每次对话开始前**必须查阅最新检查点文档
- **任务状态变更时**立即更新检查点文档
- **新需求产生时**立即创建或更新检查点文档
- 使用 `[x]` 标记已完成任务，`[ ]` 标记待完成任务

### 3.4 项目结构规范
```
ai-skills/
├── skill_packer/       # 主程序目录
├── documents/          # 文档目录
├── .trae/rules/        # 项目规则
└── design.md           # 设计文档
```

### 3.5 Git 提交规范

#### 提交信息格式
```
<type>: <subject>

<body>
```

#### Type 类型
| 类型 | 说明 | 示例 |
|------|------|------|
| `feat` | 新功能 | `feat: add skill scanner module` |
| `fix` | 修复bug | `fix: resolve keyboard input issue` |
| `refactor` | 重构代码 | `refactor: optimize UI rendering logic` |
| `docs` | 文档更新 | `docs: update project rules` |
| `style` | 代码格式 | `style: format ui.py` |
| `test` | 测试相关 | `test: add scanner test cases` |
| `chore` | 构建/工具 | `chore: update build scripts` |

#### Subject 规范
- 使用**英文**，首字母小写
- 不超过 50 个字符
- 使用**动词开头**，描述做了什么
- 结尾**不加句号**

**正确示例**：
- `feat: add interactive skill selection UI`
- `fix: resolve arrow key handling on Windows`
- `refactor: optimize terminal width calculation`

**错误示例**：
- ❌ `feat: added new feature` (过去时)
- ❌ `fix: bug fixed.` (有句号)
- ❌ `update` (无类型，无描述)
- ❌ `refactor` (无具体描述)

#### Body 规范（可选）
- 当修改较复杂时，添加 body 说明
- 描述**为什么修改**和**修改了什么**
- 每行不超过 72 个字符

#### 提交时机
- **每个独立功能/修复**单独提交
- **提交前**检查修改内容
- **提交信息**必须准确描述修改内容

### 3.6 其他约束
- 使用 `keyboard` 库处理键盘输入
- 使用 `colorama` 库处理跨平台颜色输出
