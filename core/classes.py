# 用來放所有可能會用到的類別
import discord
from discord.ext import commands

class Cog_Extension(commands.Cog): # Cog_Extension 類別 繼承 commands.cog 類別
    def __init__(self,bot):#初始化建構子  
        self.bot = bot



