import discord.ext.commands as discord
import random    #Literally only used once
import asyncio

with open("discord-token.txt",mode="r") as f:
    token = f.readlines()[0]
bot = discord.Bot("..")

@bot.command()                            #Test command for bot responsiveness
async def ping(ctx):
    botSpeech = random.randint(1,2)
    if botSpeech == 1:
        await ctx.channel.send("Pong!")
    else:
        await ctx.channel.send("I don't play table tennis. I bet you watched the anime.")

@bot.command()                           #Instantly deletes the channel the command is
async def lynch_channel(ctx):            #triggered in
    await ctx.channel.delete()

@bot.command()                           #Will eventually print the user's balance
async def bal(ctx):
    await ctx.channel.send("0")
    
@bot.command()                           #Print the devs of the bot (Hard coded fight me Bax)
async def devs(ctx):
    await ctx.channel.send("""- Raw-Nozzite for Design and Programming
- ZomBMage for BETTER programming""")

@bot.event
async def on_ready():
    print("Logged in as:")
    print(bot.user.name)
    print(bot.user.id)
    print("~"*50)

bot.run(token)