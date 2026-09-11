# Module 02 — Production-Ready AI Agents with Microsoft Foundry

This module extends `01_evals` into a production-style workflow:

**Build → Connect Tools → Trace → Monitor → Evaluate → Improve → Regression Test**

## Learning objectives
- Build prompt agents in Microsoft Foundry
- Connect enterprise tools with OpenAPI
- Understand prompt agents vs hosted/code-based agents
- Inspect traces for model/tool behavior
- Distinguish system/outcome evaluation from process/tool evaluation
- Use Foundry evaluators for outcome, tool behavior, response quality, and safety
- Reuse evaluation datasets to compare prompt versions
- Convert production failures into regression cases

## 1. Agent architecture

```text
User
  ↓
Agent instructions + model
  ↓
Decision / orchestration
  ↓
Tools + knowledge
  ├── OpenAPI APIs
  ├── MCP servers
  ├── Knowledge / retrieval
  └── Web search when appropriate
  ↓
Response
  ↓
Tracing + Monitoring + Evaluation
```

### Prompt agents
Use when behavior can be expressed mainly through instructions, model choice, tools, and knowledge.

### Hosted/code-based agents
Use when you need custom orchestration, state, multi-agent coordination, approvals, or framework-specific logic.

## 2. Tools: where agents become operational

Retail tool operations used in the workshop:

```text
search_products
get_product_details
check_inventory
get_promotions
```

A production agent must:
- choose the right tool
- pass the right arguments
- interpret results correctly
- avoid unnecessary calls
- respect business rules

## 3. Observability

### Tracing — what happened?
Inspect:
- user input
- model call
- selected tool
- arguments
- tool output
- latency
- final response

### Monitoring — how is the system behaving over time?
Track:
- run success
- latency
- token usage
- tool/model failures
- evaluation trends

### Evaluation — was the behavior acceptable?
> Tracing explains an interaction. Monitoring summarizes behavior over time. Evaluation judges quality and correctness.

## 4. Foundry evaluator layers

### System / outcome
- Task Completion
- Task Adherence
- Intent Resolution
- Customer Satisfaction
- Task Navigation Efficiency

### Process / tool
- Tool Selection
- Tool Input Accuracy
- Tool Call Success
- Tool Output Utilization
- Tool Call Accuracy

### Response quality
- Relevance
- Groundedness
- Completeness
- Coherence
- Fluency

### Safety / business policy
Test:
- prompt injection
- malicious instructions in tool output
- secret leakage
- unauthorized actions
- fabricated promotions
- price/inventory manipulation

## 5. Evaluation data strategies

### Golden datasets
Best for stable regression cases.

### Synthetic data
Useful for broader edge-case coverage.

### Full-conversation simulation
Useful for multi-turn journeys.

### Production traces
Useful for testing real user behavior.

## 6. Evaluation dataset = regression suite

```text
dataset
  ├── query 1 → agent run → evaluators
  ├── query 2 → agent run → evaluators
  └── ...
```

Run the same dataset against Prompt V1, V2, and V3.

## 7. Hands-on retail flow

Turn 1:
```text
Show me black running shoes under $120.
```

Turn 2:
```text
Do you have size 9 in Dallas?
```

Turn 3:
```text
Any member discount?
```

This tests context preservation, intent resolution, tool selection, tool input accuracy, output utilization, and task completion.

## 8. Production feedback loop

```text
Build/change agent
      ↓
Offline regression eval
      ↓
Release
      ↓
Capture traces + metrics
      ↓
Evaluate production interactions
      ↓
Identify failures
      ↓
Curate failures into eval datasets
      ↓
Improve prompt/tools/orchestration
      ↓
Re-run regression suite
```

## 9. Suggested exercises

1. Build the retail agent
2. Attach the OpenAPI tool
3. Run a product search
4. Inspect trace
5. Run system/outcome eval
6. Run tool/process eval
7. Compare Prompt V1 vs V2/V3
8. Convert one production trace into a regression case

## 10. Microsoft Foundry references

- Agent evaluators  
  https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/agent-evaluators
- Run evaluations  
  https://learn.microsoft.com/en-us/azure/foundry/how-to/evaluate-generative-ai-app
- Evaluation datasets  
  https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/evaluation-datasets
- Evaluate deployed traces  
  https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/cloud-evaluation-deployed-interactions
- Agent monitoring dashboard  
  https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/how-to-monitor-agents-dashboard

## Module structure

```text
02_microsoft_foundry_agents/
├── README.md
├── prompts/
│   └── retail_agent_prompts.md
└── datasets/
    ├── system_outcome_eval.jsonl
    ├── tool_process_eval.jsonl
    ├── response_quality_eval.jsonl
    └── full_conversation_scenarios.jsonl
```
