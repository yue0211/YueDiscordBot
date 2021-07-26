import discord,random,json,pytz
import datetime 
import psycopg2
from discord.ext import commands
from core.classes import  Cog_Extension 

with open('setting.json',mode='r',encoding='utf-8') as inFile: 
    data=json.load(inFile)



# record = ('ODY3OTUzOTU1MDc2OTkzMDU1.YPonHA.wBBOZyGcVnmGtlIF-WOEQxBCJEU', '730790532565172304', '849131366221873162', '791934397880205332','752200039862108170','849131366221873164','791934397880205335','867977477170032661','868086216439001148','867980086085820466','867980731337560084','867981199249907723','868082350762905610','868094320929030154','868088456113455134','<:fucku:852271663180546090>','<:bruh:852271625675341854>','<:nlnlAyaya:852271836947021824>','<:c_:868091497336172574>','<:python:868085404153303060>','1535','2468','5487')
# table_columns = '(token, Yue, Rabbit, TaleRunner,Yue_channel,Rabbit_channel,TaleRunner_channel,YueRoleMessage,RabbitRoleMessage,YueRoleLowest,YueRoleMiddle,YueRoleHigh,RabbitNormalPeople,RabbitC,RabbitPython,YueRoleLowestEmoji,YueRoleMiddleEmoji,YueRoleHighEmoji,RabbitCEmoji,RabbitPythonEmoji,time,id,code)'
# postgres_insert_query = f"""INSERT INTO discord_Yue {table_columns} VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s);"""

# cursor.execute(postgres_insert_query, record)
# conn.commit()

#delete_table_query = '''DROP TABLE IF EXISTS discord_yue'''

#cursor.execute(delete_table_query)
#conn.commit()




#cursor.close()
#conn.close()



class Main(Cog_Extension):
    
    @commands.command()  # 清除資料
    async def clean(self,ctx,num:int): 
        await ctx.channel.purge(limit=num+1) 


    @commands.command() # 看個人身份
    async def who(self,ctx,name:str):
        for member in ctx.guild.members:
            if  member.name==name or member.nick==name:
                embed=discord.Embed(title="人頭", description="個人資訊", color=0xa85dd0,timestamp=datetime.datetime.now(pytz.timezone('Asia/Taipei')))
                embed.set_author(name="幹幹的", icon_url="https://imgur.dcard.tw/tn729YT.gif")
                embed.set_thumbnail(url=member.avatar_url)
                embed.add_field(name="名稱：", value=f"{member}", inline=False)
                embed.add_field(name="目前的狀態：", value=member.status, inline=False)
                await ctx.channel.send(embed=embed)

    @commands.command() # 隨機產生id
    async def atid(self,ctx):
        box=""
        for i in range(4):
            box+=str(random.randrange(10))
        await ctx.channel.send(box)

        id = self.all[0][22]
        temp="'"+box+"'"
        postgres_update_query = f"""UPDATE discord_yue SET id = {temp} WHERE id =%s """
        self.cursor.execute(postgres_update_query, (id,))
        self.conn.commit()
        


    @commands.command() # 確認驗證碼
    async def check(self,ctx,code):
        if str(self.all[0][23])!=code:
           await ctx.channel.send("驗證碼錯誤")
        else:
           await ctx.channel.send("驗證碼正確")



def setup(bot): #運行bot時,會呼叫 setup => 註冊
    bot.add_cog(Main(bot))

