# 03 — Implementation Steps

**Status: portal-verified for the New Foundry path.** Steps below reflect what was actually walked through this session. The classic path is documented separately at the end for awareness, since it wasn't completed due to model availability limits.

## Step 1 — Switch to New Foundry

1. In the project, locate the **"New Foundry"** toggle in the top navigation bar.
2. Turn it on. The portal navigates to a `/nextgen/` URL with a new top-level nav: **Home, Discover, Build, Operate, Docs**.

## Step 2 — Create a new agent

1. In the left sidebar (under **Create**), select **Agents**.
2. Create a new agent (this session's example was named `firstagent`).
3. You land directly in the **Playground** tab of the agent editor.

## Step 3 — Choose a model

1. Click the **Model** selector at the top of the Playground.
2. The dropdown splits into **Deployments** (your existing deployments, plus `model-router` if you've deployed it) and **Models** (a smaller browsable set — `gpt-4o`, `gpt-4.1`, `gpt-4.1-mini`, `o4-mini` observed, with a "Browse more models" link for the rest).
3. Select either an existing deployment or a model from the list. This session used a Global Standard `gpt-5` deployment; `model-router` was visible as an alternative but not selected, to avoid an untested live run.

## Step 4 — Write instructions

1. In the **Instructions** box, write the system prompt defining the agent's behavior.
2. An **Optimize** button sits below the box — not explored this session; likely an AI-assisted instruction-refinement feature.

## Step 5 — Attach a tool

1. Scroll to the **Tools** section.
2. The built-in **Web search** tool (Bing grounding) can be enabled directly, with no external resource needed. The portal shows a standing notice: it has additional costs, and customer data flows outside the Azure compliance boundary when used.
3. To attach an external tool (e.g. Azure AI Search), use **Add**, which opens a **"Create a new connection"** modal: select or create the backing resource, and choose an **Auth Type** (API Key was the option shown).
4. This session's agent had a tool added via this connection pattern; the resulting live behavior wasn't tested (see below).

## Step 6 — Review the other Playground views

1. **Chat** — the default test conversation pane. Not used for a live message this session (cost-conscious skip).
2. **YAML** — shows the entire agent configuration as text. Worth opening just to see the structure, even without sending a chat message.
3. **Call agent** — expected to show a code/API snippet for invoking the agent programmatically, similar to the deployment "Get Started" panel from Session 3. Not opened this session.

## Step 7 — Version and Publish (not executed)

1. A **Version** control and **Publish** button sit at the top right of the agent editor.
2. Not tested this session — publishing may have consequences (new endpoint, version lock) worth confirming deliberately before doing it on a real agent.

---

## Classic path (for awareness only — not completed)

1. From the project sidebar (toggle off), go to **Build and customize → Agents**.
2. The **"Foundry Agent Service"** landing screen requires selecting an **Azure OpenAI resource** first — this session saw two options, one tied to the original hub, one auto-created during a Session 3 deployment.
3. Depending on which resource is selected, the subsequent **"Deploy a model"** dialog may show a very limited model list. In this session, one resource surfaced only `gpt-4o` and `gpt-4o-mini`, both non-deployable.
4. This path was abandoned in favor of New Foundry once the model list proved too restrictive to proceed.
