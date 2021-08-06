import discord
import json 
import random
from discord.ext import commands
from core.classes import  Cog_Extension # 從core資料夾內的classes.py 導入類別

with open('setting.json',mode='r',encoding='utf-8') as inFile: #將一長串資料存到 json , 可讓畫面比較整齊
    data=json.load(inFile)


class React(Cog_Extension):

    @commands.command() # command 的裝飾子 要改成這樣
    async def picture(self,ctx):
        rand_picture = random.choice(data["picture"]) #告訴程式圖片的電腦路徑,並隨機選取圖片
        pic = discord.File(rand_picture) 
        await ctx.send(file=pic)

    @commands.command()
    async def webPicture(self,ctx):  # 傳送網址的路徑
        rand_picture = random.choice(data["url_picture"]) #告訴程式圖片的網址路徑,並隨機選取圖片
        await ctx.send(rand_picture)

    

def setup(bot): #運行bot時,會呼叫 setup => 註冊 cog
    bot.add_cog(React(bot))



