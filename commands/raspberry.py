import discord,random,json,pytz,requests
import datetime 
import time
from discord.ext import commands
from core.classes import  Cog_Extension

ENDPOINT = "things.ubidots.com"
DEVICE_LABEL = "car-station"
VARIABLE_LABEL = "status"
VARIABLE_LABEL2 = "direction"
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



def post_var(payload, url=ENDPOINT, device=DEVICE_LABEL, token=TOKEN):
    try:
        url = "http://{}/api/v1.6/devices/{}".format(url, device)
        headers = {"X-Auth-Token": token, "Content-Type": "application/json"}

        attempts = 0
        status_code = 400

        while status_code >= 400 and attempts < 5:
            print("[INFO] Sending data, attempt number: {}".format(attempts))
            req = requests.post(url=url, headers=headers,
                                json=payload)
            status_code = req.status_code
            attempts += 1
            time.sleep(1)

        print("[INFO] Results:")
        print(req.text)
    except Exception as e:
        print("[ERROR] Error posting, details: {}".format(e))




class Raspberry(Cog_Extension):


    @commands.command()
    async def forward(self,ctx):  # 控制樹梅派的車子前進
        if get_var() ==1:
            direction = 1
            payload = {VARIABLE_LABEL2: direction}
            post_var(payload)
            await ctx.channel.send("已完成車子的前進指令")
        else:
            await ctx.channel.send("登入失敗，無法操控車子")

    @commands.command()
    async def backward(self,ctx):  # 控制樹梅派的車子後退
        if get_var() ==1:
            direction = 2
            payload = {VARIABLE_LABEL2: direction}
            post_var(payload)
            await ctx.channel.send("已完成車子的後退指令")
        else:
            await ctx.channel.send("登入失敗，無法操控車子")

    @commands.command()
    async def turnleft(self,ctx):  # 控制樹梅派的車子左轉
        if get_var() ==1:
            direction = 3
            payload = {VARIABLE_LABEL2: direction}
            post_var(payload)
            await ctx.channel.send("已完成車子的左轉指令")
        else:
            await ctx.channel.send("登入失敗，無法操控車子")
    
    @commands.command()
    async def turnright(self,ctx):  # 控制樹梅派的車子右轉
        if get_var() ==1:
            direction = 4
            payload = {VARIABLE_LABEL2: direction}
            post_var(payload)
            await ctx.channel.send("已完成車子的右轉指令")
        else:
            await ctx.channel.send("登入失敗，無法操控車子")




def setup(bot): #運行bot時,會呼叫 setup => 註冊
    bot.add_cog(Raspberry(bot))





