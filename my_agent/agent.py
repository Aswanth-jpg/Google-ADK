
from google.adk.agents.llm_agent import Agent

from datetime import datetime
import pytz

# Tool implementation
def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city using pytz for timezone conversion."""
    # Simple mapping of city names to pytz timezones
    city_timezone_map = {
        "new york": "America/New_York",
        "london": "Europe/London",
        "paris": "Europe/Paris",
        "tokyo": "Asia/Tokyo",
        "sydney": "Australia/Sydney",
        "delhi": "Asia/Kolkata",
        "mumbai": "Asia/Kolkata",
        "bangalore": "Asia/Kolkata",
        "beijing": "Asia/Shanghai",
        "moscow": "Europe/Moscow",
        "dubai": "Asia/Dubai",
        "singapore": "Asia/Singapore",
        "los angeles": "America/Los_Angeles",
        "san francisco": "America/Los_Angeles",
        "chicago": "America/Chicago",
        "berlin": "Europe/Berlin",
        "cape town": "Africa/Johannesburg",
        "rio de janeiro": "America/Sao_Paulo",
        "toronto": "America/Toronto",
        "istanbul": "Europe/Istanbul",
        # Add more cities as needed
    }
    tz_name = city_timezone_map.get(city.lower())
    if tz_name:
        tz = pytz.timezone(tz_name)
        now = datetime.now(tz)
        current_time = now.strftime("%I:%M %p")
        return {"status": "success", "city": city, "time": current_time}
    else:
        return {"status": "error", "city": city, "message": "City not recognized or supported."}

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description="Tells the current time in a specified city.",
    instruction="You are a helpful assistant that tells the current time in cities. Use the 'get_current_time' tool for this purpose.",
    tools=[get_current_time],
)