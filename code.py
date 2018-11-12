import discord.ext.commands as discord
import random

with open("discord-token.txt",mode="r") as f:
    token = f.readlines()[0]

@command()
async def ping():
    botSpeech = random.randint(1,2)
    if botSpeech == 1:
        bot.say("Pong")
    else:
        bot.Say("I don't play table tennis. I bet you watched the anime.")
bot = discord.Bot()
async def on_ready():
    print("Logged in as:")
    print(bot.user.name)
    print(bot.user.id)
    print("~"*50)
