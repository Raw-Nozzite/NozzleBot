import discord.ext.commands as discord
import random
import asyncio

with open("discord-token.txt",mode="r") as f:
    token = f.readlines()[0]
bot = discord.Bot("..")

@bot.command()
async def ping(ctx):
    botSpeech = random.randint(1,2)
    if botSpeech == 1:
        await ctx.channel.send("Pong!")
    else:
        await ctx.channel.send("I don't play table tennis. I bet you watched the anime.")
@bot.command()
async def lynch_channel(ctx):
    await ctx.channel.delete()
@bot.event
async def on_ready():
    print("Logged in as:")
    print(bot.user.name)
    print(bot.user.id)
    print("~"*50)
    for channel in bot.get_all_channels():
        if channel.name == "asdkj":
            await channel.delete()
bot.run(token)