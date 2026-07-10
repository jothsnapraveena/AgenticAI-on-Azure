# 04 — Validation Checks

## Confirmed this session

- [x] New Foundry toggle successfully switches between classic and `/nextgen/` surfaces.
- [x] Agent creation completes in the New Foundry builder without errors (`firstagent` created, versioned "1").
- [x] Model picker correctly separates **Deployments** (including `model-router`) from **Models** (catalog subset).
- [x] Tool attachment via the "Create a new connection" pattern is reachable and presents resource + Auth Type fields.
- [x] Web search tool is available with no external setup, with a visible compliance-boundary warning.
- [x] Classic path's model restriction is real and reproducible for at least one Azure OpenAI resource (2 deprecated models shown, non-deployable).

## Deliberately not tested (cost-conscious skip, not a gap)

- [ ] Sending a live chat message and getting a model/model-router response.
- [ ] Traces tab populated with a real tool-invoking run.
- [ ] Publish action and its actual effect (endpoint creation, version lock, etc.).

## What "working" looks like if you do choose to test the above

- A sent message produces a response in the Chat pane; if a tool was needed, the Traces tab should show the tool invocation distinctly from the final text.
- Publish should, at minimum, change the agent's status/version indicator — confirm whether it also exposes a new callable endpoint via the "Call agent" view.


