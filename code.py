import discord.ext.commands as discord
import discord.utils as discordutils
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
        await ctx.channel.send("I don't play table tennis. I bet you watched the anime though.")

@bot.command()
async def del_channel(ctx, *args):  
    """Instantly deletes a specified channel"""
    if len(args) == 1:
        await bot.get_channel(int(args[0][2:-1])).delete()
    else:
        await ctx.channel.send("Please specify a channel!")

@bot.command()
async def bal(ctx):
    """Will eventually print the user's balance"""
    await ctx.channel.send("0")
    
@bot.command()
async def devs(ctx):
    """Print the devs of the bot (Hard coded fight me Bax)"""
    await ctx.channel.send("""```- Raw-Nozzite for Design and Programming, and being an excellent person :)
- ZomBMage for BETTER programming```""")

@bot.command()
async def invite(ctx):
    """Return a link to invite the bot, in case of emergency ;)"""
    await ctx.channel.send(discordutils.oauth_url("511255939806920755"))

@bot.command()
async def kys(ctx):
    """Makes bot leave server"""
    await ctx.channel.send("Guess I'll die then")
    await bot.get_guild(ctx.guild.id).leave()

@bot.command()
async def roulette(ctx):
     """Get a surprise!"""
     with open("randomLine.txt") as f:
         allLines = f.readlines()
         await ctx.channel.send(random.choice(allLines))

@bot.event
async def on_ready():
    print("Logged in as:")
    print(bot.user.name)
    print(bot.user.id)
    print("~"*50)
    print("Invite with:",discordutils.oauth_url("511255939806920755"))

bot.run(token)