import discord,random,json,pytz,requests
import datetime 
import time
from discord.ext import commands
from core.classes import  Cog_Extension

ENDPOINT = "things.ubidots.com"
DEVICE_LABEL = "car-station"
VARIABLE_LABEL = "status"
TOKEN = "BBFF-ZWASr1Yu4iSwu7PdxbA8Wsiw7ib9C0" # replace with your TOKEN


def get_var(url=ENDPOINT, device=DEVICE_LABEL, variable=VARIABLE_LABEL,token=TOKEN):
        try:
            URL = "http://{}/api/v1.6/devices/{}/{}/lv".format(url, device, variable)

            headers = {"X-Auth-Token": token, "Content-Type": "application/json"}

            attempts = 0
            status_code = 400
            while status_code >= 400 and attempts < 5:
                #print("[INFO] Retrieving data, attempt number: {}".format(attempts))
                req = requests.get(url=URL, headers=headers)
                status_code = req.status_code
                attempts += 1
                time.sleep(1)
                #print("[INFO] Results:")
                return int(float(req.text))

        except Exception as e:
            print("[ERROR] Error posting, details: {}".format(e))


class Raspberry(Cog_Extension):


    @commands.command()
    async def forward(self,ctx):  # 樹梅派的登入確認
        if get_var() ==1:
            await ctx.channel.send("登入成功")
            await ctx.channel.send("前進")   
        else:
            await ctx.channel.send("登入失敗")




    


def setup(bot): #運行bot時,會呼叫 setup => 註冊
    bot.add_cog(Raspberry(bot))





