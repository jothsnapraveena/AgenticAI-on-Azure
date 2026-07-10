# 05 — Troubleshooting

## Confirmed issue: classic Agents path shows only 2, non-deployable models

**Symptom:** Navigating to Agents via the classic (New Foundry toggle off) path, then through "Foundry Agent Service" → select an Azure OpenAI resource → "Deploy a model," surfaced only `gpt-4o` and `gpt-4o-mini`, both apparently deprecated and not deployable.

**Cause (partially confirmed):** Agent Service in the classic path is scoped to a specific Azure OpenAI resource, chosen explicitly at setup — not the project as a whole. This session had two such resources available; the one selected appears to have had no existing deployments, and the fallback catalog shown was small and stale.

**Resolution used:** Switched to the **New Foundry** toggle instead of troubleshooting further within the classic path. This surfaced the full deployment list (including `model-router` and existing Session 3 deployments) immediately.

**Not yet confirmed:** whether selecting the *other* available Azure OpenAI resource (the one tied to the original hub, with live Session 3 deployments) would have resolved this within the classic path itself. Worth a quick check if the classic path needs documenting further, but not required for this session's flow.

## Anticipated issues (not yet encountered)

**Tool connection fails to authenticate**
If a tool connection's Auth Type (e.g. API Key) is misconfigured or the linked resource lacks correct permissions, expect the connection to fail at the "Connect" step of the modal. Not encountered this session, since a live tool call wasn't tested.

**Publish behaves unexpectedly**
Since Publish wasn't tested, any consequence — new billable endpoint, irreversible version lock — is unknown. Treat as a "test deliberately, not accidentally" action.

## To be filled in after further verification

- [ ] Outcome of retrying the classic path with the hub-tied Azure OpenAI resource
- [ ] Any errors encountered once a live chat message or Publish action is deliberately tested
