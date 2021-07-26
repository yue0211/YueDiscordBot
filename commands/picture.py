import discord
import json 
import random
from discord.ext import commands
from core.classes import  Cog_Extension 

with open('setting.json',mode='r',encoding='utf-8') as inFile: 
    data=json.load(inFile)


class Picture(Cog_Extension):

    
    @commands.command() # 傳送網址的網路圖片
    async def webPicture(self,ctx):  
        rand_picture = random.choice(data["url_picture"]) 
        await ctx.send(rand_picture)





def setup(bot): 
    bot.add_cog(Picture(bot))







