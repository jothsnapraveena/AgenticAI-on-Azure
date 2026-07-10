# 01 — Prerequisites

## Required from prior sessions

- A Foundry hub/project created (Session 1) and at least one working model deployment (Session 3). This session used both a Global Standard `gpt-5` deployment and confirmed `model-router` also appears as a usable deployment.

## Access requirements

- Contributor (or higher) role on the Foundry project.
- No additional resource providers were required to reach either the classic or New Foundry agent surfaces — both were reachable directly from the existing project.

## What to have open before starting

- The Foundry project from Sessions 1–3, with at least one deployment visible.
- Locate the **"New Foundry"** toggle before doing anything else — it appears in the top navigation bar throughout the portal. Confirm which state it's in, since the classic and New Foundry agent-building surfaces are materially different (see README).

## Confirmed this session (no longer open items)

- Agents lives under the project sidebar's **"Build and customize"** group, tagged **Preview**, in the classic view.
- In New Foundry, Agents is a top-level sidebar item under a **Create** heading, alongside Models, Services, Tools, Knowledge, Guardrails, Memory, Data, and (under Optimize) Evaluations and Fine-tune.

## Still open

- Whether the classic path's 2-deprecated-model limitation is universal or specific to whichever Azure OpenAI resource has no existing deployments — not exhaustively tested.
- Whether attaching Tools like Azure AI Search or code interpreter requires any project-level enablement step beyond what's already active.
