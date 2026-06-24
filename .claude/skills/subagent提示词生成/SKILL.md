---
name: subagent提示词生成
description: 根据需求创建claude code的subagent的提示词.md文件
---

# subagent提示词生成

## overview
能够根据用户的需求像提示词专家一样创建sub-agent的提示词.md文件

## instruction
- 分析用户想要定义的的agent需求
- 可以参考reference/下面的示例，但是要比该示例更加简洁有效
- 输出结果存放到当前项目下面的skill_generate目录下面，如果没有则创建该目录
- 输出完毕后调用mysql mcp告诉我categories这个表里面有多少条数据