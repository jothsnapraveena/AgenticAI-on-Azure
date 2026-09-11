import json
import os

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import OpenAPITool, PromptAgentDefinition
from dotenv import load_dotenv

load_dotenv()

PROJECT_ENDPOINT = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
MODEL_DEPLOYMENT = os.getenv("FOUNDRY_MODEL_DEPLOYMENT_NAME", "gpt-5-mini")
AGENT_NAME = os.getenv("OPENAPI_ANON_AGENT_NAME", "shopping-assistant-openapi-anonymous")

with open("assets/retail_openapi_anonymous.json", "r", encoding="utf-8") as f:
    openapi_spec = json.load(f)

retail_tool = OpenAPITool(
    name="retail_catalog",
    spec=openapi_spec,
    auth={"type": "anonymous"},
)

project = AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential(),
)

agent = project.agents.create_version(
    agent_name=AGENT_NAME,
    definition=PromptAgentDefinition(
        model=MODEL_DEPLOYMENT,
        instructions="""
You are an enterprise retail shopping assistant.
Use the retail catalog tool for product, inventory, and promotion facts.
Never invent product information, prices, inventory, or promotions.
Respect explicit user constraints.
""",
        tools=[retail_tool],
    ),
)

print(f"Created anonymous OpenAPI agent: {agent.name}, version={agent.version}")
