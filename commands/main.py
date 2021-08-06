import discord,random
import datetime # 為了解決 embed 內的時間設定
from discord.ext import commands
from core.classes import  Cog_Extension # 從core資料夾內的classes.py 導入類別

class Main(Cog_Extension):  # Main類別 繼承 Cog_Extension 類別
    

                               # 參數一定要放 ctx
    @commands.command()        # 頻道位置,使用者 , id 都包含在 ctx 參數內,所以不用另外設定
    async def ping(self,ctx):  # ctx參數 代表 context (上下文) => 上文（使用者）,下文（bot）
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')  # {bot.latency*1000} => 當成一個變數,round 用於四捨五入
                                                        # latency 回傳機器人延遲時間
    @commands.command()
    async def hi(self,ctx):
        await ctx.send("5678")

    @commands.command()
    async def em(self,ctx): # google 搜尋 discord embed 可以生成程式碼 ,time 要自己另外設定
        embed=discord.Embed(title="歌單", description="好聽的歌曲", color=0xa85dd0,timestamp=datetime.datetime.now())
        embed.set_author(name="幹幹的", icon_url="https://imgur.dcard.tw/tn729YT.gif")
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJpozH7Fz41uprarazDZUrs7_Wu06uGkUvRw&usqp=CAU")
        embed.add_field(name="1.", value="diamond", inline=True)
        embed.add_field(name="2.", value="king", inline=True)
        embed.add_field(name="3.", value="sugar", inline=True)
        embed.add_field(name="4.", value="faker", inline=True)
        embed.set_footer(text="舒服")
        await ctx.send(embed=embed)

    # 讓機器人輸出訊息,ex: 下指令要寫 [say xxx(msg)
    @commands.command() # 可以利用msg前面的參數*,讓message之間可以輸入空格 ex: 你 好 嗎,如果沒打前面*,只會印出'你'
    async def say(self,ctx,*,msg):# msg 會存放使用者輸入的訊息 
        await ctx.message.delete()
        await ctx.send(msg)

    #清除訊息,ex: 下指令要寫 [clean 5 => 清除5則訊息(不包含下指令的那行,因為有加一了)
    @commands.command() #num 是要清除訊息的數量
    async def clean(self,ctx,num:int): #將傳近來的字串轉成int
        await ctx.channel.purge(limit=num+1) #為了把下指令的那行也刪掉,所以要多加一


    @commands.command() # 將伺服器成員,隨機組隊
    async def randGuild(self,ctx):
        online=[]
        for members in ctx.guild.members:
            if str(members.status)=="online" and members.bot == False: # members.status 的型態是 Status =>利用discord.py 的 API 查詢
                online.append(members.name)
        random_online=[]
        random_online=random.sample(online,k=4) # random.sample 隨機選取4人,且回傳list
        
        total=[]
        for members in range(2): #從4個成員中,隨機挑2人組隊,共挑2組
            temp = random.sample(random_online,k=2)
            total.append(temp)
            for squad in temp:
                random_online.remove(squad)

        embed=discord.Embed(title="分組名單", description="我是天才", color=0xa85dd0,timestamp=datetime.datetime.now())
        embed.set_author(name="幹幹的", icon_url="https://imgur.dcard.tw/tn729YT.gif")
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJpozH7Fz41uprarazDZUrs7_Wu06uGkUvRw&usqp=CAU")

        tag="1."
        bitch=number="1"
        for x in total:
            replace=""
            tag=tag.replace(bitch,number)
            bitch=number
            for y in x:
                replace+=(y+"           ")
            embed.add_field(name=tag, value=replace, inline=False)
            number=int(number)
            number+=1
            number=str(number)
        embed.set_footer(text="舒服")
        await ctx.send(embed=embed)
    

    @commands.group() # group 為了增加執行效率,不用讓程式判斷太多次,將指令分group
    async def codetest(self,ctx):
        pass
    
    @codetest.command() # codetest 的子命令,用法EX:[codetest python
    async def python(self,ctx):
        await ctx.send("Python")

    @codetest.command()
    async def javascript(self,ctx):
        await ctx.send("javascript")
    
    @codetest.command()
    async def cpp(self,ctx):
        await ctx.send("C++")


def setup(bot): #運行bot時,會呼叫 setup => 註冊
    bot.add_cog(Main(bot))




