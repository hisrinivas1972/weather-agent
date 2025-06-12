from google.genai.agent.base import BaseAgent

class WeatherAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="weather-agent",
            system_instruction="You provide current weather information based on user queries.",
            tools=[]  # Add APIs or tools later
        )
