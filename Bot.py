"""
Created by Meaning[2099129]
Python discord bot
Did it extremely sleep deprived
Which explains why its shit
I also did the read me while sleep deprived
If anyone actually sets this up properly I will be suprised

No modifaction required in this code below
I mean feel free if you want too have fun
but it doesn't need it all you need to do is edit the config.json file
"""



import requests
import discord
from discord.ext import commands
import asyncio
import json
import datetime

client = commands.Bot(command_prefix=commands.when_mentioned)

class Tornid():
    def __init__(self):
        self.val = False

async def check():
    sent = False
    await client.wait_until_ready()
    config = json.loads(open("config.json", "r").read())
    for key in config["APIKeys"]:
        globals()[str(config["APIKeys"][str(key)])] = Tornid()
    while not client.is_closed():
        config = json.loads(open("config.json", "r").read())
        for key in config["APIKeys"]:
            comp = requests.get(f'https://api.torn.com/company/{key}?selections=employees,stock,profile&key={config["APIKeys"][key]}').json()
            embed = discord.Embed(title=str(comp["company"]["name"]), description=f'Run by: **{comp["company"]["employees"][str(comp["company"]["director"])]["name"]}**', url=f'https://www.torn.com/joblist.php#/p=corpinfo&ID={key}', color=discord.Color.gold())
            embed.add_field(name='\n\n**COMPANY INFO**', value="..............", inline=False)
            embed.add_field(name='Star Rating', value=f'{str(comp["company"]["rating"])} :star:')
            embed.add_field(name='Daily Income', value="${:,.2f}".format(comp["company"]["daily_income"]), inline=True)
            embed.add_field(name='Weekly Income', value="${:,.2f}".format(comp["company"]["weekly_income"]), inline=True)
            embed.add_field(name='Employees Needed', value=str(comp["company"]["employees_capacity"]-comp["company"]["employees_hired"]), inline=True)
            embed.add_field(name='\n\n**EMPLOYEES**', value="..............", inline=False)
            for x in comp["company_employees"]:
                employee_name = str(comp["company_employees"][x]["name"])
                last_action_made = str(comp["company_employees"][x]["last_action"]["relative"])
                employee_state = str(comp["company_employees"][x]["status"]["state"])
                employee_position = str(comp["company_employees"][x]["position"])
                employee_effectiveness = str(comp["company_employees"][x]["effectiveness"]["total"])
                final_str = f'Activity: {last_action_made}\nState: {employee_state}\nEffectiveness: {employee_effectiveness}%\nPosition: {employee_position}' if "day" not in last_action_made else f'Activity: {last_action_made}\nState: {employee_state}\nEffectiveness: {employee_effectiveness}%\nPosition: {employee_position}\n**INACTIVE**'
                embed.add_field(name=employee_name, value=final_str, inline=True)
            embed.add_field(name='\n\n**STOCK INFO**', value="..............", inline=False)
            for x in comp["company_stock"]:
                stock_amount = comp["company_stock"][x]["in_stock"]
                stock_sold = comp["company_stock"][x]["sold_amount"]
                final_str = f'In stock: {stock_amount}\nAmount Sold: {stock_sold}' if stock_amount > stock_sold else f'In stock: {stock_amount}\nAmount Sold: {stock_sold}\n**ORDER MORE**'
                embed.add_field(name=str(x), value=final_str, inline=True)
            embed.set_footer(text=str(datetime.datetime.now())[:-7])
            if globals()[str(config["APIKeys"][str(key)])].val:
                await globals()[str(config["APIKeys"][str(key)])].message.edit(embed=embed)
            else:
                globals()[str(config["APIKeys"][str(key)])].val = True
                globals()[str(config["APIKeys"][str(key)])].message = await client.get_channel(config["Channel"]).send(embed=embed)
        await asyncio.sleep(3600.0)

client.loop.create_task(check())

client.run(json.loads(open("config.json", "r").read())["Token"])
