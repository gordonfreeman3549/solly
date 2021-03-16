import discord
import os
from keep_alive import keep_alive
from discord.ext import commands

#i fixed it

client = commands.Bot(command_prefix = 'hl-')

#this is a latency command?
@client.command()
async def ping(ctx):
  await ctx.send(f'latency gaming {round(client.latency * 1000)}ms')

#this part is fixed now it shows an epic status i guess?
#but yeah, this will crash the bot later for some fucking reason,

@client.event
async def on_ready():
  print ('My body is ready')
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="at Game and Watch"))

#triggers
#i have removed the triggers because, there is a conflict, i will fix it later

keep_alive()
client.run(os.getenv('TOKEN'))
