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
print("Retail Support Agent — type exit to stop.")

while True:
    user_input = input("\nYou: ").strip()
    if user_input.lower() in {"exit", "quit"}:
        break
    try:
        response = openai.responses.create(conversation=conversation.id, input=user_input)
        print("Agent:", response.output_text)
    except Exception as exc:
        print("Request failed:", exc)
