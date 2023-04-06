import discord
from discord.ext import commands
import requests
import json

from apikey import *


class greetings_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hello", help="Greets you")
    async def hello(self, ctx):
        await ctx.send("Hello! I am Fox bot.")

    @commands.command(name="del")
    @commands.has_permissions(administrator=True)
    async def delete_messages(self, ctx, l: int):
        channel = ctx.channel
        messages = await channel.history(limit=l).flatten()
        await channel.delete_messages(messages)

    @commands.Cog.listener()
    async def on_member_join(member):
        jokeurl = "https://joke3.p.rapidapi.com/v1/joke/%7Bid%7D"
        headers = {
            "X-RapidAPI-Key": rapidAPI_joke_key,
            "X-RapidAPI-Host": "joke3.p.rapidapi.com"
        }
        response = requests.request("GET", jokeurl, headers=headers)
        channel = channel.get_channel(1070368972643516490)
        await channel.send(json.loads(response.text)['content'])
