import discord
from discord.ext import commands
import aiohttp
from src.utils.nominatim_client import *
from src.utils.open_meteo_client import *
from src.utils.utils import format_weather_message

class DataGatherCommands(commands.Cog):
    def __init__(self, client):
       self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("DataGatherCommands module is ready to use")

    @commands.command()
    async def test_api(self, ctx):
        async with aiohttp.ClientSession() as session:
            site = await session.get("https://api.thecatapi.com/v1/images/search")
            data = await site.json()
            image_url = data[0]['url']
        message = discord.Embed(title="Meow :3")
        message.set_image(url=image_url)
        await ctx.send(embed=message)

    @commands.command()
    async def get(self, ctx, arg):
        lattitude, longitude = await call_nominatim_api(arg)
        print(f"{lattitude},{longitude}")
        data = await call_open_meteo_api(lattitude, longitude)
        await ctx.send(embed=format_weather_message(data, arg))
    
    
        


async def setup(client):
    await client.add_cog(DataGatherCommands(client))