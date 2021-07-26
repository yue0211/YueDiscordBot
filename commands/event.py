import discord
import json 
from discord.ext import commands
from core.classes import  Cog_Extension 


with open('setting.json',mode='r',encoding='utf-8') as inFile: 
    data=json.load(inFile)


class Event(Cog_Extension):
    @commands.Cog.listener() 
    async def on_member_join(self,member):  #成員加入頻道
        if member.guild.id==(int(data["Yue"])):
            channel=self.bot.get_channel(int(data["Yue_channel"]))  
            await channel.send(f'歡迎{member}已加入妹子家庭,新人請多邀妹子進群!!') 
            await member.send(f"{member.name} 尚未領取越哥中的伺服器的身份組,請盡早領取")
        elif member.guild.id==(int(data["Rabbit"])):
            channel=self.bot.get_channel(int(data["Rabbit_channel"]))
            await channel.send(f'{member}已加入,太草了') 
            role = discord.utils.get(member.guild.roles,id=(int(data["RabbitNormalPeople"]))) 
            await member.add_roles(role)
            await member.send(f"{member.name} 程式討論區中有提供不同程式的身份組,如有需要可點按表情領取")
        elif member.guild.id==(int(data["TaleRunner"])):
            channel=self.bot.get_channel(int(data["TaleRunner_channel"]))
            await channel.send(f'{member}已加入,悠悠沒洗頭')
            await member.send(f"{member.name} 尚未領取跑online群中的伺服器的身份組,請盡早領取")


    @commands.Cog.listener()
    async def on_member_remove(self,member): #成員離開頻道
        if member.guild.id==(int(data["Yue"])):
            channel=self.bot.get_channel(int(data["Yue_channel"]))  
            await channel.send(f'{member}已離開妹子家庭,太敗類了吧') 
        elif member.guild.id==(int(data["Rabbit"])):
            channel=self.bot.get_channel(int(data["Rabbit_channel"]))
            await channel.send(f'{member}已離開,哭阿') 
        elif member.guild.id==(int(data["TaleRunner"])):
            channel=self.bot.get_channel(int(data["TaleRunner_channel"]))
            await channel.send(f'{member}已離開,悠悠沒小哥哥、小姐姐了')  
        

     # 新增反應貼圖獲取身份組
    @commands.Cog.listener()                    
    async def on_raw_reaction_add(self,payload): 
        guild=self.bot.get_guild(payload.guild_id)
        if guild.id == (int(data["Yue"])):
            if payload.message_id == (int(data["YueRoleMessage"])):
                if str(payload.emoji)==data["YueRoleLowestEmoji"]: 
                    role=guild.get_role((int(data["YueRoleLowest"]))) 
                    await payload.member.add_roles(role) 
                    await payload.member.send(f"你取得了 {role}身份組!!")
                elif str(payload.emoji)==data["YueRoleMiddleEmoji"]: 
                    role=guild.get_role((int(data["YueRoleMiddle"]))) 
                    await payload.member.add_roles(role) 
                    await payload.member.send(f"你取得了 {role}身份組!!")
                elif str(payload.emoji)==data["YueRoleHighEmoji"]: 
                    role=guild.get_role((int(data["YueRoleHigh"]))) 
                    await payload.member.add_roles(role) 
                    await payload.member.send(f"你取得了 {role}身份組!!")
        elif guild.id == (int(data["Rabbit"])):
            if payload.message_id == (int(data["RabbitRoleMessage"])):
                if str(payload.emoji)==data["RabbitC++Emoji"]: 
                    role=guild.get_role((int(data["RabbitC++"])))
                    await payload.member.add_roles(role) 
                    await payload.member.send(f"你取得了 {role}身份組!!")
                elif str(payload.emoji)==data["RabbitPythonEmoji"]: 
                    role=guild.get_role((int(data["RabbitPython"]))) 
                    await payload.member.add_roles(role) 
                    await payload.member.send(f"你取得了 {role}身份組!!")
                







     # 取消反應貼圖取消身份組
    @commands.Cog.listener()                   
    async def on_raw_reaction_remove(self,payload): 
        guild=self.bot.get_guild(payload.guild_id) 
        if guild.id == (int(data["Yue"])):
            if payload.message_id == (int(data["YueRoleMessage"])):
                if str(payload.emoji)== data["YueRoleLowestEmoji"]: 
                    role=guild.get_role((int(data["YueRoleLowest"]))) 
                    member=guild.get_member(payload.user_id) 
                    await member.remove_roles(role)
                    await member.send(f"你移除了{role}身份組!!")
                elif str(payload.emoji)==data["YueRoleMiddleEmoji"]:  
                    role=guild.get_role((int(data["YueRoleMiddle"]))) 
                    member=guild.get_member(payload.user_id)
                    await member.remove_roles(role) 
                    await member.send(f"你移除了{role}身份組!!")
                elif str(payload.emoji)==data["YueRoleHighEmoji"]:  
                    role=guild.get_role((int(data["YueRoleHigh"]))) 
                    member=guild.get_member(payload.user_id)
                    await member.remove_roles(role) 
                    await member.send(f"你移除了{role}身份組!!")
        elif guild.id == (int(data["Rabbit"])):
            if payload.message_id == (int(data["RabbitRoleMessage"])):
                if str(payload.emoji)== data["RabbitC++Emoji"]: 
                    role=guild.get_role((int(data["RabbitC++"]))) 
                    member=guild.get_member(payload.user_id) 
                    await member.remove_roles(role)
                    await member.send(f"你移除了{role}身份組!!")
                elif str(payload.emoji)==data["RabbitPythonEmoji"]:  
                    role=guild.get_role((int(data["RabbitPython"]))) 
                    member=guild.get_member(payload.user_id)
                    await member.remove_roles(role) 
                    await member.send(f"你移除了{role}身份組!!")
               

        





def setup(bot): #運行bot時,會呼叫 setup => 註冊 cog
    bot.add_cog(Event(bot))