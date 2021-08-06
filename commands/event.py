import discord
import json 
import random
from discord.ext import commands
from core.classes import  Cog_Extension # 從core資料夾內的classes.py 導入類別

with open('setting.json',mode='r',encoding='utf-8') as inFile: #將一長串資料存到 json , 可讓畫面比較整齊
    data=json.load(inFile)

class Event(Cog_Extension):
    @commands.Cog.listener() # event 的裝飾子 要改成這樣
    async def on_member_join(self,member):  #成員加入頻道
        channel=self.bot.get_channel(int(data["Yue_channel"]))  #抓取頻道的id（對頻道點右鍵,可複製）
        await channel.send(f'{member} join!')  # f'{member} => 可根據 member 的數值不同, 印出不同名稱

    @commands.Cog.listener()
    async def on_member_remove(self,member):  #成員離開頻道
        channel=self.bot.get_channel(int(data["Yue_channel"]))  
        await channel.send(f'{member} leave!') 

    @commands.Cog.listener() # 如果 bot 接收的訊息 和想要送出的訊息一樣的話 => 可以造成洗頻的效果
    async def on_message(self,msg):  # msg => 要傳入的訊息,on_message 用來偵測使用者輸入的訊息 
        if msg.content.endswith("噁男"): # 結尾是 噁男 , 會觸發事件
             await msg.channel.send("刀藤是夯哥")
        if msg.content == "惡魔是渣男" and msg.author!=self.bot.user: # msg.author!=self.bot.user 代表傳送訊息的人不等於機器人
             await msg.channel.send("惡魔是渣男")                # 加上述的條件 => 而不會造成洗頻
        keyWord=["小狗","惡魔"]
        if msg.content in keyWord:
            await msg.channel.send(msg.content+"是噁男")


    @commands.Cog.listener() # isinstance => 實例, error => 輸入的錯誤指令
    async def on_command_error(self,ctx,error):
        if hasattr(ctx.command,"on_error"): #檢查指令是否有專屬的錯誤處理器,如果有就略過
            return
        if isinstance(error,commands.errors.MissingRequiredArgument):
            await ctx.send("遺失指令的參數")
        elif isinstance(error,commands.errors.CommandNotFound):
            await ctx.send("不要亂打,沒這指令")
        

    # 新增反應貼圖獲取身份組
    @commands.Cog.listener()                    #on_reaction_add => bot 下線之後,找不到訊息
    async def on_raw_reaction_add(self,payload): #on_raw_reaction_add => bot 下線之後,仍然找的到訊息
        # 判斷反應貼圖,給予相對應身份組
        if payload.message_id == 867745054108942346:
            if str(payload.emoji)=='<:nlnlAyaya:852271836947021824>': # 找 emoji 的 custom id 必須在 discord 輸入: \:emojiName: 才可得到格式
                guild=self.bot.get_guild(payload.guild_id) #取得當前所在伺服器
                role=guild.get_role(867709334670803004) # 取得伺服器內指定的身份組
                await payload.member.add_roles(role) # 給予該成員身份組
                await payload.member.send(f"你取得了{role}身份組!!")
            elif str(payload.emoji)=='<:fucku:852271663180546090>': # 找 emoji 的 custom id 必須在 discord 輸入: \:emojiName: 才可得到格式
                guild=self.bot.get_guild(payload.guild_id) #取得當前所在伺服器
                role=guild.get_role(867710250307158026) # 取得伺服器內指定的身份組
                await payload.member.add_roles(role) # 給予該成員身份組
                await payload.member.send(f"你取得了{role}身份組!!")
            
        

    # 取消反應貼圖取消身份組
    @commands.Cog.listener()                    #on_reaction_add => bot 下線之後,找不到訊息
    async def on_raw_reaction_remove(self,payload): #on_raw_reaction_add => bot 下線之後,仍然找的到訊息
        # 判斷反應貼圖,給予相對應身份組
        if payload.message_id == 867745054108942346:
            if str(payload.emoji)=='<:nlnlAyaya:852271836947021824>': # 找 emoji 的 custom id 必須在 discord 輸入: \:emojiName: 才可得到格式
                guild=self.bot.get_guild(payload.guild_id) #取得當前所在伺服器
                role=guild.get_role(867709334670803004) # 取得伺服器內指定的身份組
                member=guild.get_member(payload.user_id) # 取得使用者
                await member.remove_roles(role) # 給予該成員身份組
                await member.send(f"你移除了{role}身份組!!")
            elif str(payload.emoji)=='<:fucku:852271663180546090>': # 找 emoji 的 custom id 必須在 discord 輸入: \:emojiName: 才可得到格式
                guild=self.bot.get_guild(payload.guild_id) #取得當前所在伺服器
                role=guild.get_role(867710250307158026) # 取得伺服器內指定的身份組
                member=guild.get_member(payload.user_id)# 取得使用者
                await member.remove_roles(role) # 給予該成員身份組
                await member.send(f"你移除了{role}身份組!!")
        


    @commands.Cog.listener() # 刪除訊息時會觸發,非管理員自己刪除自己的訊息,會有bug
    async def on_message_delete(self,msg):
        counter=1
        async for auditLogs in msg.guild.audit_logs(action=discord.AuditLogAction.message_delete):
            if counter==1:
                await msg.channel.send(auditLogs.user.name+"刪除了訊息")
                break
            


def setup(bot): #運行bot時,會呼叫 setup => 註冊 cog
    bot.add_cog(Event(bot))

