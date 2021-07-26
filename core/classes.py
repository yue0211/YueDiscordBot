import discord
import psycopg2
from discord.ext import commands

class Cog_Extension(commands.Cog): 
    def __init__(self,bot):
        self.bot = bot
        # 把 Heroku Postgres 的相關資訊寫到下列指令 (database, user, password, host, port)
        self.conn=psycopg2.connect(database="d67e7e41h34ts4",user="vyasdoojomuxan",password="9fcc11824ce326d017922592a9da2547b16336d84c8b7d1f70b4b828eaf9b676",host="ec2-34-228-100-83.compute-1.amazonaws.com",port="5432")
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
                                url_picture VARCHAR (50) ,
                                time VARCHAR (50) ,
                                id VARCHAR (50) ,
                                code VARCHAR (50) 
                                );'''
        self.cursor.execute(self.create_table_query)
        self.conn.commit()
        postgres_select_query = f"""SELECT * FROM discord_Yue"""
        self.cursor.execute(postgres_select_query)
        self.all=self.cursor.fetchall()










