# background task
import discord
from discord.ext import commands
from core.classes import  Cog_Extension # 從core資料夾內的classes.py 導入類別
import json,asyncio,datetime,pytz


class Task(Cog_Extension): # *args和**kwargs是可變傳參,為了傳送多個參數
    def __init__(self,*args,**kwargs): #如果在Task類別重新定義初始化建構子
        super().__init__(*args,**kwargs) #則Cog_Extension類別的初始化建構子會消失
                                        #為了不讓父類別(Cog_Extension)中定義的初始化建構子消失
                                        #要打super().__init__(*args,**kwargs),保存父類別的建構子

        self.counter = 0

        # async def interval(): #定義間隔時間
        #     await self.bot.wait_until_ready() # 等bot啟動完成,才執行
        #     self.channel=self.bot.get_channel(866323356473884672)
        #     while not self.bot.is_closed(): #當 bot 沒有關閉時
        #         await self.channel.send("Hi I'm running!!")
        #         await asyncio.sleep(5) #單位是秒

        # self.bg_task=self.bot.loop.create_task(interval()) #創造新的背景作業


        async def timeTask(): #定義間隔時間
            await self.bot.wait_until_ready() # 等bot啟動完成,才執行
            self.channel=self.bot.get_channel(866323356473884672)
            while not self.bot.is_closed():#當 bot 沒有關閉時 
                now_time=datetime.datetime.now(pytz.timezone('Asia/Taipei')).strftime("%H%M")  # 抓取當前時間,並設定時區
                with open('setting.json',mode='r',encoding='utf-8') as inFile:#將一長串資料存到 json , 可讓畫面比較整齊
                    data=json.load(inFile)
                if now_time==data["time"] and self.counter==0:
                    self.counter=1
                    await self.channel.send("Task Working")
                    await asyncio.sleep(1) #為了讓bot有時間準備迴圈中的其他指令
                else:
                    await asyncio.sleep(1) #為了讓bot有時間準備迴圈中的其他指令
                    pass
                
        self.bg_task=self.bot.loop.create_task(timeTask()) #創造新的背景作業







    @commands.command() #設定bot的背景工作要在哪個頻道執行,ex: [setChannel 頻道id
    async def setChannel(self,ctx,ch:int):
        self.channel=self.bot.get_channel(ch) # 在 python 的 物件導向中,上面的self.channel仍然可以使用(是同一個物件)
        await ctx.send(f'Set Channel:{self.channel.mention}') #提示訊息 self.channel.mention => tag channel



    @commands.command()
    async def setTime(self,ctx,time):
        self.counter = 0
        with open('setting.json',mode='r',encoding='utf-8') as inFile:#將一長串資料存到 json , 可讓畫面比較整齊
             data=json.load(inFile)
        data["time"]=time
        with open('setting.json',mode='w',encoding='utf-8') as outFile:#將一長串資料存到 json , 可讓畫面比較整齊
             json.dump(data,outFile,indent=4) # indent設定縮排,沒縮排資料會全部變一行



def setup(bot): #運行bot時,會呼叫 setup => 註冊
    bot.add_cog(Task(bot))


