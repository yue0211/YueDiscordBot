import discord,random,json,pytz
import datetime 
from discord.ext import commands
from core.classes import  Cog_Extension 


class Main(Cog_Extension):

    @commands.command() # 隨機產生id
    async def atid(self,ctx):
        box=""
        for i in range(4):
            box+=str(random.randrange(10))
        await ctx.channel.send(box)

        self.cursor.execute(self.postgres_select_query)
        self.all=self.cursor.fetchall()
        id = self.all[0][2]
        temp="'"+box+"'"
        postgres_update_query = f"""UPDATE discord_yue SET id = {temp} WHERE id =%s """
        self.cursor.execute(postgres_update_query, (id,))
        self.conn.commit()

    @commands.command() # 確認驗證碼
    async def check(self,ctx,code):
        self.cursor.execute(self.postgres_select_query)
        self.all=self.cursor.fetchall()
        if str(self.all[0][2])!=code:
           await ctx.channel.send("驗證碼錯誤")
        else:
           await ctx.channel.send("驗證碼正確")







def setup(bot): #運行bot時,會呼叫 setup => 註冊
    bot.add_cog(Main(bot))





