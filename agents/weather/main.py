import os
import asyncio
from google.genai import configure
from agents.weather.agent import WeatherAgent
from utils.call_agent import call_agent_async

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
configure(api_key=os.environ["GOOGLE_API_KEY"])

async def main():
    agent = WeatherAgent()
    runner = agent.start()
    query = "What's the weather like in New York today?"
    await call_agent_async(query, runner, "user1", "session1")

if __name__ == "__main__":
    asyncio.run(main())
