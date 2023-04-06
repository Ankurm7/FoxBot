import discord
from discord.ext import commands
from apikey import *


class flames_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def generate_flames(self, name1, name2):
        Dict = {1: 'Friends', 2: 'Lovers', 3: 'Affection',
                4: 'Married', 5: 'Enemy', 0: 'Siblings'}

        name1 = name1.lower()
        name1 = list(name1)
        name2 = name2.lower()
        name2 = list(name2)

        for i in range(len(name1)):
            for j in range(len(name2)):
                if name1[i] == name2[j]:
                    name1[i] = '/'
                    name2[j] = '/'
                    break

        name1_count = 0
        name2_count = 0

        for i in name1:
            if i != '/':
                name1_count += 1
        for i in name2:
            if i != '/':
                name2_count += 1

        ans = (name1_count+name2_count) % 6
        return Dict[ans]

    @commands.command(name='flames')
    async def generate(self, ctx, name1, name2):
        word = self.generate_flames(name1, name2)
        await ctx.send("%s and %s are %s." % (name1, name2, word))

    # @commands.command(name="button")
    # async def button(self, ctx):
    #     view = discord.ui.View()
    #     button = discord.ui.Button(label="Click")
    #     view.add_item(button)
    #     await ctx.send(view=view)
