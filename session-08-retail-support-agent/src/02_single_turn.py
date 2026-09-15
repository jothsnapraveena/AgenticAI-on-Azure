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

question = "I bought a jacket 18 days ago. Can I still return it?"
response = openai.responses.create(input=question)

print("USER:", question)
print("AGENT:", response.output_text)
