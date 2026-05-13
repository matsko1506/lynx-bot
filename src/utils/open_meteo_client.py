import aiohttp

async def call_open_meteo_api(lattitude, longitude):
    params = {
        "latitude": lattitude,
        "longitude": longitude,
        "current_weather": "true",
        "daily": [
            "temperature_2m_max", 
            "temperature_2m_min", 
            "uv_index_max", 
        "precipitation_probability_max"
        ],
        "hourly": ["temperature_2m", "apparent_temperature", "precipitation"],
        "timezone": "auto"
    }

    async with aiohttp.ClientSession() as session:
        site = await session.get("https://api.open-meteo.com/v1/forecast", params=params)
        data = await site.json()

    return data