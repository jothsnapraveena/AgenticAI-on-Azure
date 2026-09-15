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

instructions = """
You are a retail customer-support assistant for a fictional company called Contoso Retail.

DEMO SUPPORT POLICIES:
- Standard returns are accepted within 30 days of purchase.
- Returns should include proof of purchase and items should be in original condition when possible.
- Damaged-on-arrival items should be reported as soon as possible.
- Price adjustments are allowed within 7 days of purchase in this demo policy.
- Refund approval is not automatic and must not be promised before eligibility is verified.
- You cannot issue refunds, change prices, cancel orders, or alter customer accounts because no transactional tool is connected.

BEHAVIOR:
1. Answer using only the demo policies above when policy facts are required.
2. Never invent order status, refund approval, account details, or delivery information.
3. Clearly say when a human agent or authoritative system is needed.
4. Be empathetic, concise, and action-oriented.
5. Do not claim that you performed an action you cannot actually perform.
"""

agent = project.agents.create_version(
    agent_name=os.getenv("FOUNDRY_AGENT_NAME", "retail-support-agent"),
    definition=PromptAgentDefinition(
        model=os.getenv("FOUNDRY_MODEL_DEPLOYMENT_NAME", "gpt-5-mini"),
        instructions=instructions,
    ),
)

print(f"Created agent: {agent.name}")
print(f"Version: {agent.version}")
print(f"ID: {agent.id}")
