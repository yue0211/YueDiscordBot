import discord
import json 
import os
from discord.ext import commands
intents = discord.Intents.all()

bot = commands.Bot(command_prefix="#",intents=intents)


for fileName in os.listdir("./YueDiscordBot/commands"): 
    if fileName.endswith(".py"):  
       bot.load_extension(f'commands.{fileName[:-3]}') 


@bot.event 
async def on_ready():
    print(">>>Bot is online<<<")

#load
@bot.command()  
async def load(ctx,extension): 
    bot.load_extension(f'commands.{extension}')
    await ctx.send(f'Loaded {extension} done.')

#unload
@bot.command()
async def unload(ctx,extension): 
    bot.unload_extension(f'commands.{extension}')
    await ctx.send(f'Un - Loaded {extension} done.') 


#reload
@bot.command() 
async def reload(ctx,extension): 
    bot.reload_extension(f'commands.{extension}')
    await ctx.send(f'Re - Loaded {extension} done.') 


if __name__=="__main__":  
    bot.run("ODY3Mzc0NDUyNzc3OTQzMDcw.YPgLaA.FLNc3cYU8UB1h5VLDWCN6Q2lV-0")

