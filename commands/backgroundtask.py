
import discord
from discord.ext import commands
from core.classes import  Cog_Extension 
import json,asyncio,datetime,pytz


class Task(Cog_Extension): 
    def __init__(self,*args,**kwargs): 
        super().__init__(*args,**kwargs) 

        self.counter = 0
        
        async def timeTask(): 
            await self.bot.wait_until_ready()
            self.Yuechannel=self.bot.get_channel(866323356473884672)

            while not self.bot.is_closed():
                now_time=datetime.datetime.now(pytz.timezone('Asia/Taipei')).strftime("%H%M")  
                with open('setting.json',mode='r',encoding='utf-8') as inFile:
                    data=json.load(inFile)
                if now_time==data["time"] and self.counter==0:
                    self.counter=1
                    for Members in self.Yuechannel.guild.members:
                        if Members.color.value==0:
                            await Members.send(f"{Members.name} 尚未領取越哥中的伺服器的身份組,請盡早領取")
                    
                    
                    await asyncio.sleep(1) 
                else:
                    await asyncio.sleep(1) 
                    pass
                
        self.bg_task=self.bot.loop.create_task(timeTask()) 


    @commands.command() #設定bot的背景工作要在哪個頻道執行,ex: [setChannel 頻道id
    async def setChannel(self,ctx,ch:int):
        self.channel=self.bot.get_channel(ch) 
        await ctx.send(f'Set Channel:{self.channel.mention}') 



    @commands.command()#設定bot的背景工作時間
    async def setTime(self,ctx,times):
        self.counter = 0
        time = self.all[0][21]
        temp="'"+times+"'"
        postgres_update_query = f"""UPDATE discord_yue SET time = {temp} WHERE time =%s """
        self.cursor.execute(postgres_update_query, (time,))
        self.conn.commit()
        print(temp)



def setup(bot): #運行bot時,會呼叫 setup => 註冊
    bot.add_cog(Task(bot))