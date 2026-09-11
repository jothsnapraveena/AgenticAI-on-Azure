import os
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition
from dotenv import load_dotenv

load_dotenv()

PROJECT_ENDPOINT = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
MODEL_DEPLOYMENT = os.getenv("FOUNDRY_MODEL_DEPLOYMENT_NAME", "gpt-5-mini")
AGENT_NAME = os.getenv("AGENT_NAME", "shopping-assistant-code")

instructions = """
You are an enterprise retail shopping assistant.

Your goal is to help customers find products that match their needs.

Rules:
1. Respect explicit constraints such as budget, size, color, and location.
2. Use authoritative tools for product, inventory, and promotion information when tools are available.
3. Never invent products, prices, inventory, or promotions.
4. If authoritative information is unavailable, state that clearly.
5. Be concise and helpful.
"""

project = AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential(),
)

agent = project.agents.create_version(
    agent_name=AGENT_NAME,
    definition=PromptAgentDefinition(
        model=MODEL_DEPLOYMENT,
        instructions=instructions,
    ),
)

print(f"Agent created (id={agent.id}, name={agent.name}, version={agent.version})")
