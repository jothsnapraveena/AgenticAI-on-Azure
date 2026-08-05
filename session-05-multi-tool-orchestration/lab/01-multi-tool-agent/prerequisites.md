# Prerequisites

## Azure side

- A Foundry project with a deployed chat-capable model (e.g. `gpt-4o`, `gpt-5-mini`). Session 3 covers deployment.
- Your identity needs the **Azure AI User** or **Azure AI Developer** role on the project — not just Owner/Contributor.
  Owner/Contributor grant management actions (create/edit resources) but not the `agents/write` data action agent
  operations need. This is the #1 cause of `AuthorizationFailed` errors in this lab. Confirm your role in the
  Foundry portal under project → Access control, or via `az role assignment list`.
- Your project endpoint, in the form:
  `https://<resource-name>.services.ai.azure.com/api/projects/<project-name>`

## Local environment

```bash
pip install azure-ai-agents azure-identity
az login
```

- Python 3.9+
- Jupyter (`pip install notebook` or run via VS Code's notebook support)

## Environment variables

Set these before running the notebook (or fill them into the first cell):

```bash
export PROJECT_ENDPOINT="https://<resource-name>.services.ai.azure.com/api/projects/<project-name>"
export MODEL_DEPLOYMENT_NAME="<your-model-deployment-name>"
```

## Files needed

- A small CSV for Code Interpreter to analyze (the notebook generates a synthetic one if you don't have one).
- A short `.md` or `.txt` file for File Search to index (the notebook generates a sample one too).

## Cost awareness

Code Interpreter has per-session charges beyond token costs — sessions run up to 1 hour active / 30 min idle.
This lab creates one short-lived session; just don't leave it running unattended. File Search vector store
storage also has a small ongoing cost until you delete it (see `cleanup.md`).
