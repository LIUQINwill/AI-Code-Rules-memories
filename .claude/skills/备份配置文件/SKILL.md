---
name: 备份配置文件
description: 备份.claude.json配置文件
---

# Skill: 备份 Claude 配置文件

## Description
当用户请求备份 Claude 的本地配置文件（.claude.json）时，执行此技能。该技能会运行本地 Python 脚本，将配置文件复制并添加当前时间戳后缀。

## Usage
当用户提到以下意图时触发：
- "备份配置文件"
- "备份 .claude.json"
- "Backup claude config"

## Implementation
- **Type**: Python Script Execution
- **Script Path**: `scripts/backup_claude.py`
- **执行命令**：`python3 /Users/whitley/pycharmProject/AiCodeRules/.claude/skills/备份配置文件/scripts/backup_claude.py`

## Parameters
无（该脚本自动获取当前时间并处理指定路径）

## Expected Output
脚本将返回成功消息（包含备份路径）或错误消息。请将此结果反馈给用户。