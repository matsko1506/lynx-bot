import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv(".env")
DISCORD_TOKEN: str = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix="$", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Connected to Discord")

client.run(DISCORD_TOKEN)

