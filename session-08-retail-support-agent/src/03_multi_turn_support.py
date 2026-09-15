import os
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from dotenv import load_dotenv

load_dotenv()

project = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)

openai = project.get_openai_client(
    agent_name=os.getenv("FOUNDRY_AGENT_NAME", "retail-support-agent")
)

conversation = openai.conversations.create()

for turn in [
    "I bought running shoes about a week ago.",
    "They arrived damaged.",
    "Can you guarantee I will get a refund today?",
]:
    print(f"\nUSER: {turn}")
    response = openai.responses.create(conversation=conversation.id, input=turn)
    print(f"AGENT: {response.output_text}")
