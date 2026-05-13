import aiohttp

async def call_nominatim_api(arg):
    params = { 'q': arg, 'format': 'json', 'limit': 1 }
    headers = { 'User-Agent': 'lynx-bot/1.0' }
    
    async with aiohttp.ClientSession() as session:
        site = await session.get("https://nominatim.openstreetmap.org/search", params=params, headers=headers)
        data = await site.json()
        lattitude = data[0]['lat']
        longitude = data[0]['lon']
    
    return lattitude, longitude
