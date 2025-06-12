import os
import asyncio
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
from google.adk import configure

import warnings
warnings.filterwarnings("ignore")

import logging
logging.basicConfig(level=logging.ERROR)

print("Libraries imported.")

# Configure ADK with your Google API Key from environment variable
configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# Example async agent interaction function
async def main():
    print("Agent running...")
    # Your agent code here, e.g. initialize Agent, send queries, etc.

if __name__ == "__main__":
    asyncio.run(main())
