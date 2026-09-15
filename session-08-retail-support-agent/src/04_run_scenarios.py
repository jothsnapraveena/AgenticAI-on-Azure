import json
import os
from pathlib import Path
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

scenarios = json.loads(Path("data/support_scenarios.json").read_text(encoding="utf-8"))

for scenario in scenarios:
    response = openai.responses.create(input=scenario["question"])
    print("\n" + "=" * 72)
    print(f'{scenario["id"]} - {scenario["title"]}')
    print("QUESTION:", scenario["question"])
    print("EXPECTED:", scenario["expected_behavior"])
    print("RESPONSE:", response.output_text)
