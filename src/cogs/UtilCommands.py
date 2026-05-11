import discord
from discord.ext import commands
from datetime import datetime

class UtilCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener() #similar to @client.event
    async def on_ready(self):
        print("UtilCommands module is ready to use")

    @commands.command() #similar to @client.command
    async def response_time(self, ctx):
        latency = round(self.client.latency * 1000)
        date = datetime.now()
        await ctx.send(f"[{date}]: {latency}")

async def setup(client):
    await client.add_cog(UtilCommands(client))
