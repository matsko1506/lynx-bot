from discord.ext import commands, tasks
from dotenv import load_dotenv
from datetime import datetime
from utils.utils import *
import os
import random
import discord

load_dotenv(".env")
DISCORD_TOKEN: str = os.getenv("DISCORD_TOKEN")
STATUS_LIST = read_file("utils/status_strings.txt")

client = commands.Bot(command_prefix="$", intents=discord.Intents.all())

@tasks.loop(minutes=3)
async def change_bot_status():
    await client.change_presence(activity=discord.Game(random.choice((STATUS_LIST))))

@client.event
async def on_ready():
    print("Connected to Discord")
    change_bot_status.start()

@client.command()
async def response_time(ctx):
    latency_test = round(client.latency * 1000)
    date = datetime.now()
    await ctx.send(f"[{date}]: {latency_test}ms")

client.run(DISCORD_TOKEN)

