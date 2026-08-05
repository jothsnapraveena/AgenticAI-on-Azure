# Session 5: Multi-Tool Orchestration

Part of [AgenticAI-on-Azure](https://github.com/Jothsnapraveena/AgenticAI-on-Azure).



## What you're building

A single Foundry agent with three tools attached at once:

- **Code Interpreter** — runs Python in a sandbox for data analysis and chart generation
- **File Search** — retrieval over a vector store built from an uploaded document
- **Function Calling** — a custom Python function the agent can call directly

The point isn't any one tool — it's seeing how the agent picks which tool to use per request, and what changes in the SDK when you go from one tool to several (`ToolSet`, `enable_auto_function_calls`, combined `tools`/`tool_resources`).



## Prerequisites

See `lab/01-multi-tool-agent/prerequisites.md`.

## What's in this session

```
lab/01-multi-tool-agent/
  prerequisites.md       - environment, packages, RBAC role needed
  multi_tool_agent.ipynb - the main notebook
  validation.md           - how to confirm each tool actually fired
  troubleshooting.md      - common SDK/auth errors and fixes
  cleanup.md              - what to delete afterward to avoid charges
```
