# Session 4: Agent Service I — Fundamentals

Part of [AgenticAI-on-Azure](https://github.com/jothsnapraveena/AgenticAI-on-Azure)

![Repository architecture](/images/4.png)

## Where this sits in the course

Sessions 1–3 covered Foundry Models: hub/project creation, the model catalog, and deployment (including Model Router as a deployment type). This session moves into Agent Service — the first of four sessions on that surface, covering what an agent is, how to create one, and how tools attach to it.

## Two coexisting experiences

Portal-verified during this session: Foundry currently ships **two parallel agent-building surfaces**, switchable via a **"New Foundry"** toggle present throughout the portal (project overview, Agents section, etc.).



**New Foundry (toggle on)** — a materially different surface at a `/nextgen/` URL path, with its own top-level navigation: **Home, Discover, Build, Operate, Docs**. This is where agent creation actually worked smoothly in this session, and it's the primary path documented below. The classic path is noted for awareness — if you land there first, flipping the toggle is the fix, not troubleshooting the model list.

Both paths are labeled **Preview** as of this session.

## Agent Service concepts (still valid across both surfaces)

- **Agent** — a definition: name, instructions (system prompt), a model or deployment it uses, and attached tools. A template, not a conversation.
- **Thread** — a conversation, holding an ordered list of messages, persisted server-side.
- **Message** — a single entry in a thread.
- **Run** — one execution: agent + thread → next response, including any tool-calling loop.

## What "Model" means in the New Foundry agent builder

The model picker inside agent creation splits into two distinct sections, confirmed via the portal:

- **Deployments** — your project's existing live deployments (e.g. a Global Standard `gpt-5` deployment from Session 3), plus, notably, **`model-router`** listed here as a selectable deployment alongside regular models.
- **Models** — a smaller browsable catalog (`gpt-4o`, `gpt-4.1`, `gpt-4.1-mini`, `o4-mini` observed) with a "Browse more models" link to the full catalog.

The fact that `model-router` appears under **Deployments**, not Models, confirms something worth carrying back into Session 3's documentation: Model Router isn't a model — it's a deployment type that dynamically selects an underlying model per request. Once deployed, it's usable by an agent exactly like any single-model deployment.

### Serverless vs. managed compute (context for deployment choice)

Two fundamentally different ways a model gets hosted, relevant to what shows up in the Deployments list:

- **Serverless (pay-as-you-go)** — Standard and Global Standard deployment types from Session 3. No infrastructure to manage; billed per token/call.
- **Managed compute** — the model runs on dedicated, provisioned compute (VM/GPU capacity you commit to), typically used for Provisioned Throughput (PTU) deployments or open-source models not offered as pay-per-token APIs. Trades cost predictability for guaranteed, low-variance latency.

This session's deployments were all serverless; managed compute deployment wasn't walked through and is a candidate for a later session rather than this one.

## Tools: Toolboxes, Tools, Skills

The Tools section of the New Foundry agent builder has three sub-tabs:

- **Tools** — individual, atomic capabilities (web search, Azure AI Search, a custom function).
- **Toolboxes** — bundles of multiple tools grouped for reuse across agents.
- **Skills (Preview)** — a newer, less-defined concept, likely a higher-level composed capability (tool + instructions + logic packaged together). Not explored in depth this session since it's still in preview and behavior may shift.

**Built-in web search** (Bing grounding) is available with no external setup, but carries an explicit portal warning: it has additional costs, and customer data flows outside the Azure compliance boundary when used. Worth flagging in any org context.

**Connecting an external tool** (e.g. Azure AI Search) follows a consistent pattern: a "Create a new connection" modal requiring you to select or create the backing resource, plus declare an Auth Type (API Key observed; other types may exist).

## Agent editing surface

Once inside an agent, the top-level tabs are:

- **Playground** — the working editor: model picker, Voice mode toggle, Instructions box, Tools section, and a live Chat pane on the right (with **Chat / YAML / Call agent** sub-views — YAML exposes the entire agent config as text, meaning agents can be version-controlled outside the UI).
- **Details (Preview)** — metadata view, not explored in depth this session.
- **Traces** — per-run execution detail (tool calls, reasoning steps).
- **Monitor** — aggregate usage/metrics over time.
- **Evaluation** — structured quality testing against test cases.

Agents carry a **Version** history and a separate **Publish** action, implying a draft/iterate → publish release pattern rather than simple autosave.

## Discover gallery

The **Discover → Agents** tab lists 48 Microsoft-provided starter agent templates (e.g. Internal Policy Q&A, RFP Response Drafter, Trip Itinerary Designer), each tagged with the tools/connectors it demonstrates. Explicitly labeled: templates are for **educational use only**, not production-ready as-is.

