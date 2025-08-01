from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import requests

from dotenv import find_dotenv, get_key

set_tracing_disabled(disabled=True)
GEMINI_API_KEY= get_key(find_dotenv(), "GOOGLE_API_KEY")
WEATHER_API_KEY= get_key(find_dotenv(), "WEATHER_API_KEY") 

@function_tool
def get_weather(city: str) -> str:
    """
    Fetches weather data for a given city from OpenWeatherMap.
    """
    result = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}")

    if result.status_code == 200:
        data = result.json()
        # Process the data here and return the desired string
        weather = data["weather"][0]["description"]
        
        return f"The weather in {city} is {weather}."  
    else:   
        return "sorry, I could't fetch the weather data"
    
agent:Agent=Agent(
    name="hello",
    instructions="You are a helpful assistant.",
    model=LitellmModel(model="gemini/gemini-2.0-flash",api_key=GEMINI_API_KEY),
    tools=[get_weather],
)

def run(message:str)->str:
    print("Run message",message)
    result=Runner.run_sync(
        agent,
        f"{message}?",  
    )
    return result.final_output