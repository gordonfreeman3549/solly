import discord
import os
from replit import db
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('d-old_e'):
        await message.channel.send('Ah, you always like to press E huh? Well I am not healing you anymore Scout.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('d-help'):
        await message.channel.send('This is a prototype bot for Solly, Not all commands are featured, when I have more time, more commands will be added. All commands:`old_e`')

@client.event
async def on_message(msg):
	if("sex" in " "+msg.content.lower()+" "):
		await msg.add_reaction("<:sex:803720888175820891>")
	if("sus" in " "+msg.content.lower()+" "):
		await msg.add_reaction("<:sus:803587570260770887>")
	await bot.process_commands(msg)        
      
keep_alive()
client.run(os.getenv('sex'))
