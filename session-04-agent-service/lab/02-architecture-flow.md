# 02 — Architecture Flow

## Two surfaces, one underlying agent concept

```
                    [New Foundry toggle]
                     /                \
            OFF (classic)         ON (New Foundry)
                 |                        |
     "Foundry Agent Service"      /nextgen/ Build > Agents
     -> select AOAI resource      -> direct agent builder
     -> "Deploy a model" dialog      (Playground, Details,
        (may be limited to a          Traces, Monitor, Eval)
        small model subset)
```

Both surfaces are expected to produce the same underlying Agent/Thread/Run/Message objects — the difference observed this session was in the creation UX and model availability, not in the object model itself. This is an assumption carried from documentation and prior sessions' patterns, not independently re-confirmed for the classic path since it wasn't usable enough to complete an agent there this session.

## New Foundry agent creation flow (primary path)

```
Model deployment (Session 3)
        |
   New Foundry: Build > Agents > new agent
        |
   [Model picker]
     - Deployments: existing deployments + model-router
     - Models: browsable subset (gpt-4o, gpt-4.1, gpt-4.1-mini, o4-mini...)
        |
   [Instructions] (system prompt)
        |
   [Tools] -- Tools / Toolboxes / Skills (Preview)
     - Web search: built-in, no setup, data-boundary warning
     - External tools (e.g. Azure AI Search): "Create a new connection"
       modal -> select/create resource + Auth Type
        |
   [Playground: Chat / YAML / Call agent]
        |
   Version history <-> Publish
```

## Relationship to Sessions 1–3

```
[Hub/Project]  (Session 1)
     |
[Model Deployment]  (Session 3 — serverless: Standard / Global Standard)
     |                              \
     |                          [model-router deployment]
[Agent]  <- instructions + tools, references a deployment above
     |
[Thread] <-> [Run] <-> [Tool calls]
```

Agent creation itself didn't appear to provision new top-level Azure resources beyond what tool connections require (e.g. an Azure AI Search resource, if you attach that tool) — this held for the New Foundry path tested this session.
