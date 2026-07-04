# Architecture Flow

## What you're building

```
Azure Subscription
      |
      v
Foundry Hub (governance container)
      |
      v
Foundry Project (workspace)
      |
      +--> Connections (models, data sources, tools — configured in later sessions)
      +--> RBAC (assigned at hub or project level)
      +--> Operate tab (fleet visibility — previewed only in this session)
```

## Component roles

| Component | Role |
|---|---|
| Hub | Top-level container; shared governance, billing boundary |
| Project | Workspace where agents, models, and tools actually get built |
| Connection | A link from a project to an external resource (model deployment, data source, tool) |
| RBAC assignment | Controls who can do what, at hub or project scope |
| Operate tab | Centralized view across agents/models/tools in a subscription — used heavily from Session 7 onward |
