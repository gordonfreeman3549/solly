
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()

#failed attempt at command
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith("hlgaming"):
    await message.channel.send("gaming")

#this part is fixed now it shows an epic status i guess?
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you"))


#triggers
@client.event
async def on_message(msg):
	if("sex" in " "+msg.content.lower()+" "):
		await msg.add_reaction("<:sex:803720888175820891>")
	if("sus" in " "+msg.content.lower()+" "):
		await msg.add_reaction("<:sus:803587570260770887>")

keep_alive()
client.run(os.getenv('TOKEN'))
