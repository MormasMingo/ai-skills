---
doc-id: 01-skill-packer-00-001
version: 1.0.0
status: published
created: 2026-03-02
updated: 2026-03-02
author: AI Assistant
tags: [skill-packer, project-doc]
---

# Skill Packer 项目文档

## 项目概述

Skill Packer 是一个用于打包 Trae IDE Skill 的交互式命令行工具。

## 项目结构

```
ai-skills/
├── skill_packer/           # 主程序目录
│   ├── __init__.py
│   ├── types.py            # 数据类型定义
│   ├── scanner.py          # Skill 扫描器
│   ├── packer.py           # 打包器
│   ├── ui.py               # 交互式界面
│   └── main.py             # 主程序
├── documents/
│   ├── 01-projects/        # 项目个性化文档
│   │   └── skill-packer/   # 本项目文档
│   └── checkpoints/        # 检查点文档
├── .trae/rules/            # 项目规则
├── main.py                 # 入口文件
├── start.bat / start.sh    # 启动脚本（自动安装依赖）
├── build.bat / build.sh    # 构建脚本（打包独立可执行文件）
├── start-standalone.*      # 运行独立可执行文件
└── requirements.txt        # 依赖
```

## 核心功能

1. **自动扫描**：扫描 `.trae/skills/`、`skills/`、`.skills/` 目录
2. **交互式选择**：方向键选择，回车确认，绿色背景高亮
3. **打包功能**：支持 ZIP 和 MD 两种格式
4. **依赖管理**：启动脚本自动检测并安装依赖

## 技术栈

- 语言：Python 3.x
- 依赖：
  - `colorama`：跨平台颜色输出
  - `keyboard`：键盘事件处理

## 使用方式

### 方式一：源码运行
```bash
# Windows
start.bat

# Linux/Mac
./start.sh
```

### 方式二：独立可执行文件
```bash
# 先构建
build.bat

# 然后运行
start-standalone.bat
```

## 变更记录

| 版本 | 日期 | 变更内容 | 作者 |
|------|------|----------|------|
| 1.0.0 | 2026-03-02 | 初始版本 | AI Assistant |
