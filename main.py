import discord
import os
import random
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

@client.command()
async def ver(ctx):
  await ctx.send('VOX InDev Version 0.1.2b')

@client.command()
async def mvm(ctx):
  await ctx.send('HERE THEY COME! 5, 4, 3, 2, 1 *mvm music*')

@client.command()
async def test(ctx):
  await ctx.send('Nuh huh, your mom')

@client.command()
async def everyone(ctx):
  await ctx.send('`@`evryune!!!')

@client.command()
async def r34(ctx):
  await ctx.send('How about no, you horny fuck.')

@client.command()
async def funny(ctx):
  await ctx.send('bababooey')

@client.command()
async def lines(ctx):
  await ctx.send("Currently `155` lines of code has been written")
 
@client.command(pass_context=True)
async def hldm(ctx):
  plr = ["Gordon Freeman killed",
         "Scout killed",
         "Soldier killed",
         "Pyro killed",
         "Demoman killed",
         "Engineer killed",
         "Heavy killed",
         "Medic killed",
         "Sniper killed",
         "Spy killed",
         "Jesus killed",
         "Agent Jones killed"]
  
  die = ["Gordon Freeman with",
         "Scout with",
         "Soldier with",
         "Pyro with",
         "Demoman with",
         "Engineer with",
         "Heavy with",
         "Medic with",
         "Sniper with",
         "Spy with",
         "Jesus with",
         "Agent Jones with"]

  deathreason = ["Crowbar",
                 "Glock 17",
                 ".357 Magnum",
                 "MP5",
                 "SPAS-12",
                 "Crossbow",
                 "Tau Cannon",
                 "Gauss Cannon",
                 "RPG",
                 "Fragmentation Grenade",
                 "Trimpmine",
                 "Satchel Charge",
                 "Fall Damage",
                 "Physics Gun",
                 "Item",
                 "M1 Garand",
                 "AK-47",
                 "The hand of God",
                 "P90",
                 "Minigun",
                 "C4",
                 "USP Match",
                 "MP7",
                 "AR2",
                 "Scattergun",
                 "Pistol",
                 "Double Barrel Shotgun",
                 "Rocket Launcher",
                 "Bat",
                 "Shovel",
                 "Flamethrower",
                 "Fireaxe",
                 "Grenade Launcher",
                 "Stickybomb Launcher",
                 "Bottle",
                 "Fist",
                 "Wrench",
                 "Sentry LVL 1",
                 "Sentry LVL 2",
                 "Sentry Bullet LVL 3",
                 "Sentry Rocket LVL 3",
                 "Nailgun",
                 "Bonesaw",
                 "Sniper Rifle",
                 "UZI",
                 "Sword",
                 "Sapper",
                 "Butterfly Knife",
                 "Butterfly Knife (backstab"]
  await ctx.send((random.choice(plr), random.choice(die), random.choice(deathreason)))
#troll
@client.command(pass_context=True)
async def yomama(ctx):
  yomjoke = ["Yer mum is so Bri'ish, she went to hell",
             "Yo mama so lesbian, she couldn't give birth to a guy",
             "Yo mama so small, she rode Pickle Rick's pickle'd dick",
             "Yo mama so fat, that she was a TF2 map (a good map btw)",
             "Your mother is so morbidly obese, that she has high blood pressure and type 2 diabetes",
             "Yo mama so fat, she out chungus'd, BIG CHUNGUS!",
             "Yo mama so stupid, she couldn't think of a yo mama joke"]
  await ctx.send((random.choice(yomjoke)))


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
