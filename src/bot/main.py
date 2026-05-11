import os
import random
import discord
import asyncio
from discord.ext import commands, tasks
from dotenv import load_dotenv
from src.utils.utils import *

load_dotenv(".env")
DISCORD_TOKEN: str = os.getenv("DISCORD_TOKEN")
STATUS_LIST = read_file("src/utils/status_strings.txt")

client = commands.Bot(command_prefix="$", intents=discord.Intents.all())

@tasks.loop(minutes=3)
async def change_bot_status():
    await client.change_presence(activity=discord.Game(random.choice((STATUS_LIST))))

@client.event
async def on_ready():
    print("Connected to Discord")
    change_bot_status.start()

async def load():
    for filename in os.listdir("./src/cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"src.cogs.{filename[:-3]}")
            print(f"{filename[:-3]} module found...")

async def main():
    async with client:
        await load()
        await client.start(DISCORD_TOKEN)

asyncio.run(main())


