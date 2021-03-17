import discord
import os
import youtube_dl
from keep_alive import keep_alive
from discord.ext import commands


#i fixed it

client = commands.Bot(command_prefix = ']')

players = {}
#this is a latency command?
@client.command()
async def ping(ctx):
  await ctx.send(f'latency gaming {round(client.latency * 1000)}ms')

@client.command()
async def e(ctx):
  await ctx.send('fuck off this is not TF2')
  

#ok so the music doesn't work in repl.it so umm i will do this locally
@client.command(pass_context=True)
async def join(ctx):
  channel = ctx.message.author.voice.voice_channel
  await client.join_voice_channel(channel)

@client.command(pass_context = True)
async def leave(ctx):
  server = ctx.message.server
  voice_client = client.voice_client_in(server)
  await voice_client.disconnect()

@client.command(pass_context=True)
async def play(ctx, url):
  server = ctx.message.server
  voice_client = client.voice_client_in(server)
  player = await voice_client.create_ytdl_player(url)
  players[server.id] = player
  player.start()


#this part is fixed now it shows an epic status i guess?
#but yeah, this will crash the bot later for some fucking reason,

@client.event
async def on_ready():
  print ('My body is ready')
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="]help"))

#triggers
#i have removed the triggers because, there is a conflict, i will fix it later

keep_alive()
client.run(os.getenv('TOKEN'))
