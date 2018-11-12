import discord.ext.commands as discord

with open("discord-token.txt",mode="r") as f:
    token = f.readlines()[0]

@command()
async def ping():
    bot.say("Pong")
bot = discord.Bot()
async def on_ready():
    print("Logged in as:")
    print(bot.user.name)
    print(bot.user.id)
    print("~"*50)
asdasdasdasd