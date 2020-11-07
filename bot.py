
import discord
from discord.ext import commands
import sys
import os
import requests
import json

from io import StringIO  # Python3


bot = commands.Bot(command_prefix='.')
bot.remove_command("help")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def profile(ctx, args):
	c = requests.get("https://api.ashcon.app/mojang/v2/user/"+args)
	c = c.content
	c = json.loads(c)
	try:
		userhist = c["username_history"][0]["username"]
	except:
		userhist = "NONE"
	c = c["uuid"]
	embedVar = discord.Embed(title="Profile", description=args, color=0x00ff00)
	embedVar.add_field(name="uuid", value=c, inline=False)
	
	embedVar.add_field(name="Last username", value=userhist, inline=False)

	urll="https://mc-heads.net/head/"+c+"/left"
	embedVar.set_thumbnail(url=urll)
	await ctx.send(embed=embedVar)

@bot.command()
async def hypixel(ctx, args):


	c = requests.get("https://api.ashcon.app/mojang/v2/user/"+args)
	c = c.content
	c = json.loads(c)
	try:
		userhist = c["username_history"][0]["username"]
	except:
		userhist = "NONE"
	c = c["uuid"]
	data = requests.get("https://api.hypixel.net/player?key=HYPIXEL-KEY&name="+args)
	data = data.content
	data = json.loads(data)
	if "monthlyPackageRank" in data["player"]:
		rank = data["player"]["monthlyPackageRank"]
		if rank == "SUPERSTAR":
			rank = "MVP++"
	elif "rank" in data["player"] and data["player"]["rank"] != "NORMAL":
		rank = data["player"]["rank"]
		if rank == "MVP_PLUS":
			rank = "MVP+"
		if rank == "VIP_PLUS":
			rank = "VIP+"
	elif "newPackageRank" in data["player"]:
		rank = data["player"]["newPackageRank"]
		if rank == "MVP_PLUS":
			rank = "MVP+"
		if rank == "VIP_PLUS":
			rank = "VIP+"
	elif "packageRank" in data["player"]:
		rank = data["player"]["packageRank"]
		if rank == "MVP_PLUS":
			rank = "MVP+"
		if rank == "VIP_PLUS":
			rank = "VIP+"
	else:
		rank = "Non-Donor"

	karma = data["player"]["karma"]
	embedVar = discord.Embed(title="Profile", description=args, color=0x00ff00)
	embedVar.add_field(name="uuid", value=c, inline=False)
	embedVar.add_field(name="Last username", value=userhist, inline=False)
	embedVar.add_field(name="Hypixel Rank", value=rank, inline=False)
	embedVar.add_field(name="Karma", value=karma, inline=False)
	embedVar.add_field(name="Plancke stats", value="https://plancke.io/hypixel/player/stats/"+args, inline=False)
	urll="https://mc-heads.net/body/"+c+"/left"
	embedVar.set_thumbnail(url=urll)
	await ctx.send(embed=embedVar)


@bot.command()
async def bedwars(ctx, args):
	c = requests.get("https://api.ashcon.app/mojang/v2/user/"+args)
	c = c.content
	c = json.loads(c)
	try:
		userhist = c["username_history"][0]["username"]
	except:
		userhist = "NONE"
	c = c["uuid"]
	data = requests.get("https://api.hypixel.net/player?key=1922c369-15e9-4812-b9fe-20eea39dbc89&name="+args)
	data = data.content
	data = json.loads(data)
	try:
		coins = data["player"]["stats"]["Bedwars"]["coins"]
	except:
		coins = "NONE"
	try:
		xp = data["player"]["stats"]["Bedwars"]["Experience"]
	except:
		xp = "NONE"
	try:
		finals = data["player"]["stats"]["Bedwars"]["entity_attack_final_kills_bedwars"]
	except:
		finals = "NONE"
	try:
		wins = data["player"]["stats"]["Bedwars"]["wins_bedwars"]
	except:
		wins = "NONE"
	embedVar = discord.Embed(title="Profile", description=args, color=0x00ff00)
	embedVar.add_field(name="uuid", value=c, inline=False)
	embedVar.add_field(name="Last username", value=userhist, inline=False)
	embedVar.add_field(name="Bedwars Coins", value=coins, inline=False)
	embedVar.add_field(name="Experience", value=xp, inline=False)
	embedVar.add_field(name="wins", value=wins, inline=False)
	embedVar.add_field(name="Finals", value=finals, inline=False)
	urll="https://mc-heads.net/head/"+c+"/left"
	embedVar.set_thumbnail(url=urll)
	await ctx.send(embed=embedVar)

@bot.command()
async def skywars(ctx, args):
	c = requests.get("https://api.ashcon.app/mojang/v2/user/"+args)
	c = c.content
	c = json.loads(c)
	try:
		userhist = c["username_history"][0]["username"]
	except:
		userhist = "NONE"
	c = c["uuid"]
	data = requests.get("https://api.hypixel.net/player?key=1922c369-15e9-4812-b9fe-20eea39dbc89&name="+args)
	data = data.content
	data = json.loads(data)
	try:
		coins = data["player"]["stats"]["SkyWars"]["coins"]
	except:
		coins = "NONE"
	try:
		xp = data["player"]["stats"]["SkyWars"]["Experience"]
	except:
		xp = "NONE"
	try:
		finals = data["player"]["stats"]["SkyWars"]["kills"]
	except:
		finals = "NONE"
	try:
		wins = data["player"]["stats"]["SkyWars"]["wins"]
	except:
		wins = "NONE"
	embedVar = discord.Embed(title="Profile", description=args, color=0x00ff00)
	embedVar.add_field(name="uuid", value=c, inline=False)
	embedVar.add_field(name="Last username", value=userhist, inline=False)
	embedVar.add_field(name="SkyWars Coins", value=coins, inline=False)
	embedVar.add_field(name="Experience", value=xp, inline=False)
	embedVar.add_field(name="wins", value=wins, inline=False)
	embedVar.add_field(name="kils", value=finals, inline=False)
	urll="https://mc-heads.net/head/"+c+"/left"
	embedVar.set_thumbnail(url=urll)
	await ctx.send(embed=embedVar)




@bot.command()
async def render(ctx, args):
	print("run")
	c = requests.get("https://api.ashcon.app/mojang/v2/user/"+args)
	c = c.content
	c = json.loads(c)
	try:
		userhist = c["username_history"][0]["username"]
	except:
		userhist = "NONE"
	c = c["uuid"]
	embedVar = discord.Embed(title="Profile", description=args, color=0x00ff00)
	embedVar.add_field(name="uuid", value=c, inline=False)
	embedVar.add_field(name="Last username", value=userhist, inline=False)
	urll="https://mc-heads.net/body/"+c+"/right"
	embedVar.set_image(url=urll)
	await ctx.send(embed=embedVar)




@bot.command()
async def capes(ctx, args):
	url = "http://s.optifine.net/capes/" + args + ".png";

@bot.command()
async def help(ctx):
	helping='''
.Help - Brings up this page\n
.profile (username) - brings up general stats about a player\n
.hypxiel (username) - brings up sone hypixel stats about a player\n
.render (username) - renders the current skin of the player\n
.bedwars (username) - brings up bedwars stats
.skywars (username) - brings up skywars stats
'''
	embedVar = discord.Embed(title="Help", description="All Features", color=0x00ff00)
	embedVar.add_field(name="Commands", value=helping, inline=False)
	embedVar.add_field(name="Prefix", value="`.`", inline=False)


	await ctx.send(embed=embedVar)



bot.run('DISCORD-TOKEN')


