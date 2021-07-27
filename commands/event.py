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
            channel=self.bot.get_channel(int(data["YueMainRoom"]))
            await channel.send(f'{member}已加入本群,如要解鎖更多頻道權限請去 #升級會員資格 設定資料') 
            role = discord.utils.get(member.guild.roles,id=(int(data["YueNormalMember"]))) #普通會員身份
            await member.add_roles(role)
            await member.send(f"{member.name} 群內有許多資源,可善加利用,並遵守相關規定,謝謝配合")
        

    @commands.Cog.listener()
    async def on_member_remove(self,member): #成員離開頻道
        if member.guild.id==(int(data["Yue"])):
            channel=self.bot.get_channel(int(data["YueMainRoom"]))  
            await channel.send(f'{member}已離開本群') 
 
        

     # 新增反應貼圖獲取身份組
    @commands.Cog.listener()                    
    async def on_raw_reaction_add(self,payload): 
        guild=self.bot.get_guild(payload.guild_id)
        if guild.id == (int(data["Yue"])):
            if payload.message_id == (int(data["YueRoleMessage"])):
                if str(payload.emoji)==data["YueC++"]: 
                    role=guild.get_role((int(data["YueRoleC++"]))) 
                    await payload.member.add_roles(role) 
                    await payload.member.send(f"你取得了 {role}身份組!!")
                elif str(payload.emoji)==data["YuePython"]: 
                    role=guild.get_role((int(data["YueRolePython"]))) 
                    await payload.member.add_roles(role) 
                    await payload.member.send(f"你取得了 {role}身份組!!")
                elif str(payload.emoji)==data["YuePeko"]: 
                    role=guild.get_role((int(data["YueRolePeko"]))) 
                    await payload.member.add_roles(role) 
                    await payload.member.send(f"你取得了 {role}身份組!!")
                elif str(payload.emoji)==data["YueTalesRunner"]: 
                    role=guild.get_role((int(data["YueRoleTalesRunner"]))) 
                    await payload.member.add_roles(role) 
                    await payload.member.send(f"你取得了 {role}身份組!!")


     # 取消反應貼圖取消身份組
    @commands.Cog.listener()                   
    async def on_raw_reaction_remove(self,payload): 
        guild=self.bot.get_guild(payload.guild_id) 
        if guild.id == (int(data["Yue"])):
            if payload.message_id == (int(data["YueRoleMessage"])):
                if str(payload.emoji)== data["YueC++"]: 
                    role=guild.get_role((int(data["YueRoleC++"]))) 
                    member=guild.get_member(payload.user_id) 
                    await member.remove_roles(role)
                    await member.send(f"你移除了{role}身份組!!")
                elif str(payload.emoji)==data["YuePython"]:  
                    role=guild.get_role((int(data["YueRolePython"]))) 
                    member=guild.get_member(payload.user_id)
                    await member.remove_roles(role) 
                    await member.send(f"你移除了{role}身份組!!")
                elif str(payload.emoji)==data["YuePeko"]:  
                    role=guild.get_role((int(data["YueRolePeko"]))) 
                    member=guild.get_member(payload.user_id)
                    await member.remove_roles(role) 
                    await member.send(f"你移除了{role}身份組!!")
                elif str(payload.emoji)==data["YueTalesRunner"]:  
                    role=guild.get_role((int(data["YueRoleTalesRunner"]))) 
                    member=guild.get_member(payload.user_id)
                    await member.remove_roles(role) 
                    await member.send(f"你移除了{role}身份組!!")






def setup(bot): #運行bot時,會呼叫 setup => 註冊 cog
    bot.add_cog(Event(bot))
