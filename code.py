import discord.ext.commands as discord
import random    #Literally only used once
import asyncio
blisted = []

with open("discord-token.txt",mode="r") as f:
    token = f.readlines()[0]
bot = discord.Bot("..")

@bot.command()                            
async def ping(ctx):
    """Test command for bot responsiveness"""
    botSpeech = random.randint(1,2)
    if botSpeech == 1:
        await ctx.channel.send("Pong!")
    else:
        await ctx.channel.send("I don't play table tennis. I bet you watched the anime.")

@bot.command()                           
async def lynch_channel(ctx, args):    
    """Instantly deletes the channel the command is
triggered in"""
    await ctx.args.delete()

@bot.command()                           
async def bal(ctx):
    """Will eventually print the user's balance"""
    await ctx.channel.send("0")
    
@bot.command()                    
async def devs(ctx):
    """Print the devs of the bot (Hard coded fight me Bax"""
    await ctx.channel.send("""- Raw-Nozzite for Design and Programming
- ZomBMage for BETTER Programming""")

@bot.command()
async def blist(ctx, userID):
    """Used for stopping users from posting messages"""
    blisted += userID
    print(blisted)

@bot.event
async def on_ready():
    print("Logged in as:")
    print(bot.user.name)
    print(bot.user.id)
    print("~"*50)

bot.run(token)