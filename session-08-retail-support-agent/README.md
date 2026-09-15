# Session 08 — Retail Support Agent: Idea to Prototype

This is a simple hands-on Python lab inspired by the business-scenario structure used in Microsoft's official `foundry-samples` enterprise-agent tutorial, but rebuilt with an original retail support use case.

## What you build

```text
Customer
   ↓
Retail Support Prompt Agent
   ↓
Policy reasoning
   ↓
Conversation context
   ↓
Safe answer / escalation
```

The lab intentionally has **no order-system tool yet**. That makes the boundary clear:

- explain policy → yes
- remember conversation → yes
- issue refund → no
- check real order status → no
- change account → no

## Hands-on flow

```text
Create Agent
   ↓
Single-turn Test
   ↓
Multi-turn Support
   ↓
Run Scenario Suite
   ↓
Interactive CLI
   ↓
Create V2 with Escalation
   ↓
Compare Behavior
```

## Structure

```text
session-08-retail-support-agent/
├── README.md
├── requirements.txt
├── .env.example
├── knowledge-check.md
├── data/
│   └── support_scenarios.json
├── src/
│   ├── 01_create_support_agent.py
│   ├── 02_single_turn.py
│   ├── 03_multi_turn_support.py
│   ├── 04_run_scenarios.py
│   ├── 05_interactive_chat.py
│   └── 06_create_v2_escalation_agent.py
└── lab/
    ├── 01-prerequisites.md
    ├── 02-business-scenario.md
    ├── 03-create-agent.md
    ├── 04-single-and-multi-turn.md
    ├── 05-run-scenarios.md
    ├── 06-interactive-chat.md
    ├── 07-version-2-escalation.md
    ├── 08-validation.md
    └── 09-troubleshooting.md
```

## Quick start

```bash
pip install -r requirements.txt
az login
python src/01_create_support_agent.py
python src/02_single_turn.py
python src/03_multi_turn_support.py
python src/04_run_scenarios.py
```

## Microsoft reference

Official samples:
https://github.com/microsoft-foundry/foundry-samples

Reference pattern:
`samples/python/enterprise-agent-tutorial/1-idea-to-prototype/main.py`

The Microsoft example uses `AIProjectClient`, `PromptAgentDefinition`, Responses API conversation handling, business scenarios, graceful degradation, and a progression toward evaluation and monitoring. This module keeps the supported pattern but simplifies it for a community workshop.

## Next session

Add an authoritative retail/order API with OpenAPI tools so the agent can move from policy guidance to verified enterprise data.
