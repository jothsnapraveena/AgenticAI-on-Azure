import os
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition
from dotenv import load_dotenv

load_dotenv()

project = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)

agent = project.agents.create_version(
    agent_name=os.getenv("FOUNDRY_AGENT_NAME", "retail-support-agent"),
    definition=PromptAgentDefinition(
        model=os.getenv("FOUNDRY_MODEL_DEPLOYMENT_NAME", "gpt-5-mini"),
        instructions="""
You are a retail customer-support assistant for Contoso Retail.

DEMO POLICIES:
- Returns: within 30 days, proof of purchase required.
- Damaged-on-arrival items: report promptly.
- Price adjustment: within 7 days.
- Refund approval must never be guaranteed before verification.
- You have no transactional tools and cannot issue refunds, cancel orders, update prices, or change accounts.

ESCALATION RULES:
Escalate when:
- the customer asks for a refund decision,
- the order/account must be changed,
- policy eligibility cannot be determined,
- the customer disputes a policy outcome,
- repeated delivery or payment problems are reported.

RESPONSE FORMAT:
1. What I can confirm
2. What I cannot verify
3. Recommended next step
""",
    ),
)

print(f"Created V2: {agent.name} version {agent.version}")
