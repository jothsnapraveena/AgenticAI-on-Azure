# Agentic AI on Azure — Learning Repository

A structured, hands-on learning repository built to take learners from Azure's generative AI foundations to production-grade agentic AI: orchestration, memory, observability, evaluation, safety, and enterprise governance.

This repository is built as a course-first, lab-driven learning system.
It is not a notes repository and not a demo collection.
Every module is designed to teach:

- what the topic is
- why it matters in real agentic systems
- how it fits into the full agent lifecycle
- how to practice it step by step
- how to validate, trace, and explain it confidently

## Course Vision

This repository is designed to help learners build a job-ready understanding of:

- Azure OpenAI and grounding with Azure AI Search
- Building agents with Foundry Agent Service, Agent Framework, and Semantic Kernel
- Multi-agent orchestration and connected agent workflows
- Agent memory and state with Cosmos DB and Azure Cache for Redis
- Tracing agent behavior with OpenTelemetry GenAI conventions
- Evaluating agent quality, safety, and reliability
- Monitoring and alerting with Azure Monitor and Application Insights
- Content safety and adversarial red-teaming for agents
- Identity and governance with Microsoft Entra Agent ID and MCP
- Enterprise agent governance with Microsoft Agent 365
- Scaling agent workloads on AKS

The learning journey progresses in a structured way so that each module builds naturally on the previous one.

## Repository Design Philosophy

This repository follows four principles:

**1. Course-first structure**
Every folder is designed like a proper learning module, not just a technical dump.

**2. Hands-on workflow orientation**
Every module contains a practical lab flow that explains implementation, validation, troubleshooting, and cleanup.

**3. Real-world relevance**
Each topic is positioned in the context of actual agentic system design, not only theory.

**4. Step-by-step progression**
The repository starts with foundations and moves toward production-grade observability, safety, and governance maturity.

## Learning Phases

### Phase 1 — Generative AI Foundations
This phase builds the core understanding of prompting, grounding, and retrieval on Azure.

Modules included:
1. Azure OpenAI Foundations
2. Azure AI Search: Grounding + Retrieval Patterns

### Phase 2 — Building Agents
This phase applies foundation-model concepts to building actual agents on Azure's native tooling.

Modules included:
3. Foundry Agent Service: Hosted Agent Basics
4. Agent Framework + Semantic Kernel Orchestration
5. Connected Agents: Multi-Agent Workflows
6. Agent Memory and State: Cosmos DB + Azure Cache for Redis

### Phase 3 — Observability, Evaluation, and Safety
This phase covers what separates a demo agent from a production one.

Modules included:
7. OpenTelemetry GenAI Tracing for Agents
8. Foundry Evaluators + Continuous Evaluation
9. Azure Monitor + Application Insights Dashboards
10. Content Safety + AI Red Teaming Agent

### Phase 4 — Identity, Governance, and Scale
This phase connects agent platforms into enterprise-grade governance and delivery.

Modules included:
11. Entra Agent ID, RBAC, and MCP Authentication
12. Microsoft Agent 365: Enterprise Control Plane
13. AKS: Scaling and Cost/Token Tracking for Agent Workloads
14. Capstone: End-to-End Agentic Reference Architecture

## What Each Module Contains

Every module folder in this repository is designed to contain:

**README.md**
A course-facing module overview explaining what the topic is, why it matters, and what the learner will gain.

**lab/**
A structured hands-on workflow containing:
- lab overview
- architecture flow
- prerequisites
- implementation steps
- validation checks
- troubleshooting
- cleanup
- proof-of-execution (commands, outputs, and evidence links)

This makes the repository easy to follow, consistent, and professional.

## Who This Repository Is For

This repository is designed for:

- engineers who want a structured path into Azure's agentic AI stack
- learners who prefer workflow-based practical understanding
- practitioners comparing Azure-native agent tooling against open-source stacks
- candidates who want strong project and interview explanation ability
- anyone who wants a high-quality, course-ready reference

## How to Use This Repository

Recommended flow for every module:

1. Read the module README.md
2. Understand why the topic matters
3. Open the lab/README.md
4. Follow the lab in order
5. Validate outcomes using validation-checks.md
6. Use troubleshooting.md if needed
7. Complete cleanup before moving to the next module

## Expected Learning Outcome

By the end of this repository, the learner should be able to:

- explain the Azure generative AI and agent lifecycle clearly
- build and orchestrate agents using Foundry Agent Service, Agent Framework, and Semantic Kernel
- instrument agents with OpenTelemetry and interpret Foundry traces
- design evaluation and continuous-monitoring loops for agent quality and safety
- apply identity, RBAC, and governance controls to agent-to-tool access
- explain where Microsoft Agent 365 fits in enterprise agent governance
- scale agent workloads reliably on AKS
- present a complete end-to-end agentic AI platform story with confidence

## Evidence and Validation Standards

To strengthen real-world credibility and portfolio quality, each module should include a lab/proof-of-execution.md file with:

- exact commands used
- key output snippets or status checks
- screenshots or links to execution evidence
- short notes on what was validated

This keeps the repository practical, reviewable, and suitable for interview or community demonstration.

## Repository Standards

To keep the repository clean and consistent:

- every module follows the same core structure
- file names remain consistent across folders
- explanations stay outcome-oriented
- labs remain practical and validation-driven
- advanced modules include real-world positioning and operational understanding
- late-stage modules connect tracing, evaluation, governance, and scale into one coherent story

## Final Goal

The final goal of this repository is not only learning.
It is to build a clear, practical, and project-ready understanding of Azure's agentic AI stack — from a single model call to an observable, governed, production-shaped agent platform.

## License

MIT
