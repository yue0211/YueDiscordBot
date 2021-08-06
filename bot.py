import discord
import json 
import random
import os
from discord.ext import commands
intents = discord.Intents.all()

with open('setting.json',mode='r',encoding='utf-8') as inFile: #將一長串資料存到 json , 可讓畫面比較整齊
    data=json.load(inFile)

bot = commands.Bot(command_prefix="[",intents=intents)

@bot.event #async 是異步執行函數,為了讓多個使用者再同一個時間段輸入相同指令時,不會出錯
async def on_ready():
    print("Bot is online")

 
for fileName in os.listdir("./commands"): # ./ 代表相對路徑,fileName => main.py,react.py
    if fileName.endswith(".py"):  # 如果 fileName 的結尾是.py 才導入 => 為了避免導入錯的檔案
       bot.load_extension(f'commands.{fileName[:-3]}') # 類似於 from ... import... => 為了把 fileName的 .py清除,所以結尾要-3

# [help => 可知道目前的所有指令及 指令屬於哪個 cog

@bot.command()  
async def load(ctx,extension): # commands 下的函數,參數一定要有ctx
    bot.load_extension(f'commands.{extension}')
    await ctx.send(f'Loaded {extension} done.') # 確認有被 load

@bot.command()
async def unload(ctx,extension): # commands 下的函數,參數一定要有ctx
    bot.unload_extension(f'commands.{extension}')
    await ctx.send(f'Un - Loaded {extension} done.') # 確認有被 unload


@bot.command() # reload => programmer 如果可以在程式運行中修改程式碼,存檔,然後下 reload cog的名稱 就可直接更新 cog 功能
async def reload(ctx,extension): # commands 下的函數,參數一定要有ctx
    bot.reload_extension(f'commands.{extension}')
    await ctx.send(f'Re - Loaded {extension} done.') # 確認有被 reload

@reload.error #指令個別專用的錯誤處理
async def reload_error(ctx,error):
    if isinstance(error,commands.errors.MissingRequiredArgument):
        await ctx.send("請輸入參數,並指定參數的所屬範圍")



if __name__=="__main__":  # 有引入別的py檔時,為了避免執行到其他py檔,所以要有此判斷式
    bot.run(data["Token"])

