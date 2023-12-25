#import discord package & import commands package 
import discord
import token
from discord.ext import commands
#define prefix for calling bot commands
client = commands.Bot(command_prefix= '!')

#events 
@client.event 
async def on_ready():
    print("Geany, mare")
    print("----------------------")

@client.command()
async def summon(ctx):
    await ctx.send("Mare, Geanyy")

@client.command()
async def banish(ctx):
    await ctx.send("Mareee")

#add the token from dicord  
client.run(token.token_discord)


