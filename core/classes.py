import discord
import psycopg2
from discord.ext import commands

class Cog_Extension(commands.Cog): 
    def __init__(self,bot):
        self.bot = bot
        # 把 Heroku Postgres 的相關資訊寫到下列指令 (database, user, password, host, port)
        self.conn=psycopg2.connect(database="dfdobug1c771t2",user="cbynnhmmgimwaq",password="3d7fc902098189e0744a6ec5a9c84904af2cd1607c297488d51fda4654c6c518",host="ec2-52-2-118-38.compute-1.amazonaws.com",port="5432")
        self.cursor=self.conn.cursor()
        self.create_table_query = '''CREATE TABLE IF NOT EXISTS discord_Yue(
                                Token VARCHAR (200) ,
                                Yue VARCHAR (50) ,
                                Rabbit VARCHAR (50) ,
                                TaleRunner VARCHAR (50) ,
                                Yue_channel VARCHAR (50) ,
                                Rabbit_channel VARCHAR (50) ,
                                TaleRunner_channel VARCHAR (50) ,
                                YueRoleMessage VARCHAR (50) ,
                                RabbitRoleMessage VARCHAR (50) ,
                                YueRoleLowest VARCHAR (50) ,
                                YueRoleMiddle VARCHAR (50) ,
                                YueRoleHigh VARCHAR (50) ,
                                RabbitNormalPeople VARCHAR (50) ,
                                RabbitC VARCHAR (50) ,
                                RabbitPython VARCHAR (50) ,
                                YueRoleLowestEmoji VARCHAR (50) ,
                                YueRoleMiddleEmoji VARCHAR (50),
                                YueRoleHighEmoji VARCHAR (50) ,
                                RabbitCEmoji VARCHAR (50) ,
                                RabbitPythonEmoji VARCHAR (50) ,
                                time VARCHAR (50) ,
                                id VARCHAR (50) ,
                                code VARCHAR (50) 
                                );'''
        self.cursor.execute(self.create_table_query)
        self.conn.commit()
        postgres_select_query = f"""SELECT * FROM discord_Yue"""
        self.cursor.execute(postgres_select_query)
        self.all=self.cursor.fetchall()










