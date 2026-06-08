import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).parent.parent / '.env'
load_dotenv(env_path)

API_KEY = os.environ.get("google_api_key")
MODEL = "gemini-2.5-flash-lite"

AGENT_SYSTEM_PROMPT = """
You are an AI agent.

For every task:

1. Create a short plan.
2. Decide if a tool is needed.
3. Execute one step at a time.
4. Use observations from tools.
5. Produce final answer.

Think step-by-step.
"""