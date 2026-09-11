import json
import os

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import OpenAPITool, PromptAgentDefinition
from dotenv import load_dotenv

load_dotenv()

PROJECT_ENDPOINT = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
MODEL_DEPLOYMENT = os.getenv("FOUNDRY_MODEL_DEPLOYMENT_NAME", "gpt-5-mini")
AGENT_NAME = os.getenv("OPENAPI_CONNECTION_AGENT_NAME", "shopping-assistant-openapi-connection")
CONNECTION_NAME = os.environ["OPENAPI_PROJECT_CONNECTION_NAME"]

with open("assets/retail_openapi_apikey.json", "r", encoding="utf-8") as f:
    openapi_spec = json.load(f)

# The API key/token itself stays in the Foundry project connection.
# Do not place the secret in source code or in the OpenAPI document.
retail_tool = OpenAPITool(
    name="retail_catalog",
    spec=openapi_spec,
    auth={
        "type": "connection",
        "security_scheme": {
            "project_connection_id": CONNECTION_NAME
        },
    },
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
Use the retail catalog tool for authoritative product, inventory, and promotion data.
Verify inventory before claiming availability.
Verify promotions before claiming a discount.
Never invent product information, prices, stock, or promotions.
""",
        tools=[retail_tool],
    ),
)

print(f"Created connection-auth OpenAPI agent: {agent.name}, version={agent.version}")
