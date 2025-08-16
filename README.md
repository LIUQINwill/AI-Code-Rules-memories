
## to be followed
👇1. you should build your project structure like this, if you wanna use sub-agent in your project but not globally(refered by the claude code official)
```angular2html
--------------
your_project/
|---.claude
|---|---your_agent1.md
|---|---your_agent2.md
|---CLAUDE.md
```

🔥2. your sub-agent .md file should be started like this:
```angular2html
---
name: your-sub-agent-name
description: Description of when this subagent should be invoked
tools: tool1, tool2, tool3  # Optional - inherits all tools if omitted
---

Your subagent's system prompt goes here. 
```

🐩3. how to ask your sub-agent to work for you :
- method1:
  - `/your-sub-agent-name`
- method2:
  - `ask your-sub-agent-name to do something`

🍷4.what is CLAUDE.md?
- a memory file to make sure the agent remember the rules you set before.
- **for example**, you can write something like this:
```angular2html
- all the test file should be mounted under the `tests` folder.
```

👏5.tips about how to define a agent
- accurate profile description
- goals
- list todo
- tools it can use
- input
- output
- restrictions