# Skill Packer 设计文档

## 项目概述

Skill Packer 是一个用于打包 Trae IDE Skill 的交互式命令行工具。

## 功能需求

### 核心功能
1. 自动扫描当前目录下的 skill
2. 交互式列表选择 skill
3. 支持打包为 ZIP 格式
4. 支持导出为 MD 格式

### 交互特性
1. 方向键上下移动选择
2. 回车键确认
3. Esc 键退出/返回
4. 选中项绿色背景高亮
5. 描述文本自动截断（40字符）

## 技术架构

### 技术栈
- 语言: Python 3.x
- 依赖:
  - `colorama`: 跨平台颜色输出
  - `keyboard`: 键盘事件处理

### 项目结构
```
ai-skills/
├── skill_packer/
│   ├── __init__.py
│   ├── types.py          # 数据类型定义
│   ├── scanner.py        # Skill 扫描器
│   ├── packer.py         # 打包器
│   ├── ui.py             # 交互式界面
│   └── main.py           # 主程序
├── main.py               # 入口文件
├── requirements.txt      # 依赖
└── .gitignore
```

### 模块职责

#### scanner.py
- 扫描 `.trae/skills/`、`skills/`、`.skills/` 目录
- 识别包含 `SKILL.md` 的目录作为 skill
- 提取 skill 名称和描述

#### ui.py
- 渲染交互式列表界面
- 处理键盘输入（方向键、回车、Esc）
- 选中项绿色背景高亮显示
- 描述文本截断处理

#### packer.py
- 打包 skill 为 ZIP 格式
- 导出 skill 为 MD 格式（合并 SKILL.md、examples、templates）
- 输出到 `dist-skills/` 目录

## 迭代记录

### 2026-03-02
- 初始版本开发完成
- 支持 skill 扫描、列表选择、ZIP/MD 打包
- 使用 keyboard 库处理键盘输入
- 添加绿色背景高亮选中项
