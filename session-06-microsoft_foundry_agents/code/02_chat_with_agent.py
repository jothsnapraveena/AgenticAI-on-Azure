import os
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from dotenv import load_dotenv

load_dotenv()

PROJECT_ENDPOINT = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
AGENT_NAME = os.getenv("AGENT_NAME", "shopping-assistant-code")

project = AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential(),
)

openai = project.get_openai_client(agent_name=AGENT_NAME)
conversation = openai.conversations.create()

prompts = [
    "Show me black running shoes under $120.",
    "Do you have size 9 in Dallas?",
    "Any member discount?",
]

for prompt in prompts:
    print(f"\nUSER: {prompt}")
    response = openai.responses.create(
        conversation=conversation.id,
        input=prompt,
    )
    print(f"ASSISTANT: {response.output_text}")
