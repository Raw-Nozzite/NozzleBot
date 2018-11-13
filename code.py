import discord
from discord.ext import commands
import asyncio

with open("discord-token.txt",mode="r") as f:
    token = f.readlines()[0]

bot = commands.Bot(command_prefix="..")

@bot.event
async def on_ready():
    print("Logged in as:")
    print(bot.user.name)
    print(bot.user.id)
    print("~"*50)
@bot.command()
async def ping(ctx):
    await bot.say("pong!")
bot.run(token)