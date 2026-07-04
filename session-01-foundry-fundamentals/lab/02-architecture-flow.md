# Architecture Flow

## What you're building

```
Azure Subscription
      |
      v
Foundry Hub ("Azure AI hub" on the creation form)
  |
  +--> Deploys 4 resources on creation:
  |      - the hub itself (Microsoft.MachineLearningServices)
  |      - a Cognitive Services account (backs OpenAI/model access)
  |      - a Storage account
  |      - a Key Vault
  |
  +--> Hub-level Management center (accessed via the hub name dropdown
  |     in ai.azure.com) — fleet-level view, previewed only in this session,
  |     used heavily from Session 18 onward
  |
  v
Foundry Project ("Azure AI project" on the creation form)
      |
      +--> Build and customize (Agents, Templates, Fine-tuning, Prompt flow — later sessions)
      +--> Observe and optimize (Tracing, Monitoring — Session 20-21)
      +--> Protect and govern (Evaluation, Guardrails, Risks + alerts, Governance — Session 18-19)
      +--> RBAC (assigned at hub or project level)
```

## Component roles

| Component | Role |
|---|---|
| Hub | Top-level container; shared governance, billing boundary. Creating one deploys four underlying Azure resources, not just one. |
| Project | Workspace where agents, models, and tools actually get built |
| Management center | Hub-level fleet view — users, models + endpoints, connected resources, compute. This is the real "governance at a glance" surface, not a single "Operate tab" as it might first appear. |
| RBAC assignment | Controls who can do what, at hub or project scope |
| Project nav groups | The project's left navigation is organized into three groups — Build and customize, Observe and optimize, Protect and govern — which map directly onto later sessions in this repository |
