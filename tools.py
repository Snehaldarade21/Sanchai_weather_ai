import requests
from langchain.tools import tool

@tool
def get_weather(city: str) -> str:
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    geo_res = requests.get(geo_url).json()

    if "results" not in geo_res:
        return "City not found."

    lat = geo_res["results"][0]["latitude"]
    lon = geo_res["results"][0]["longitude"]

    weather_url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}&current_weather=true"
    )
    weather_res = requests.get(weather_url).json()
    temp = weather_res["current_weather"]["temperature"]

    return f"It's currently {temp}°C in {city}."
