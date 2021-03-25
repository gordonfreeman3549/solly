import discord
import os
import random
from keep_alive import keep_alive
from discord.ext import commands


#i fixed it

client = commands.Bot(command_prefix = ']')
client.remove_command("help")

@client.group(invoke_without_command=True)
async def help(ctx):
  
  em=discord.Embed(title="VOX Help", description="Use ]help <command> for more info")
  em.set_thumbnail(url="https://media.discordapp.net/attachments/772417751540170792/813431331019030578/type.gif")
  em.add_field(name="RNG", value="4 commands")
  em.add_field(name="Test", value="6 commands")
  em.add_field(name="Bot", value="3 commands")
  
  await ctx.send(embed = em)

@help.command()
async def rng(ctx):
  em = discord.Embed(title = "Random", description = "Commands that use random scripts")
  em.set_thumbnail(url="https://media.discordapp.net/attachments/772417751540170792/813431331019030578/type.gif")
  em.add_field(name = "hldm, deathmatch, killmessage ", value = "Returns a random kill message")
  em.add_field(name = "yomama", value = "Returns a yo mama joke")
  em.add_field(name = "yesno, 8ball", value = "Answers your questions")
  em.add_field(name = "inter, intercourse", value = "sex someone")
  await ctx.send(embed = em)

@help.command()
async def test(ctx):
  em = discord.Embed(title = "Test", description = "Commands that is for testing")
  em.set_thumbnail(url="https://media.discordapp.net/attachments/772417751540170792/813431331019030578/type.gif")
  em.add_field(name = "e", value = "test command 1")
  em.add_field(name = "mvm", value = "test command 2")
  em.add_field(name = "yourmom", value = "test command 3")
  em.add_field(name = "everyone", value = "test command 4")
  em.add_field(name = "r34", value = "test command 5")
  em.add_field(name = "funny", value = "test command 6")

  await ctx.send(embed = em)
  
@help.command()
async def bot(ctx):
  em = discord.Embed(title = "Bot", description = "Commands that has to do with the bot")
  em.set_thumbnail(url="https://media.discordapp.net/attachments/772417751540170792/813431331019030578/type.gif")
  em.add_field(name = "ping", value = "Returns latency")
  em.add_field(name = "lines", value = "Returns number of lines")
  em.add_field(name = "ver", value = "Returns version")

  await ctx.send(embed = em)

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
async def yourmom(ctx):
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
  await ctx.send("Currently `174` lines of code has been written")
 
@client.command(aliases =["deathmatch", "killmessage"])
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
#NSFW
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

#You've been Trolled!
#You've been Trolled!
#You have probably been told.
#Don't reply, to this guy;
#he is just getting a rise, 
#out of you! Yes it's true, 
#you respond and thats his cue
#to start trouble on the double
#while he strokes his manly stubble

#You've been Trolled!
#You've been Trolled!
#You should probably just fold
#When the only winning move is not to play
#And yet you keep on trying,
#Mindlessly Replying.
#You've been Trolled.
#You've been Trolled.
#Have a Nice Day! 

#https://cdn.discordapp.com/attachments/809454878316822528/823990025531818034/video08.mp4

@client.command(pass_context=True)
async def yomama(ctx):
  yomjoke = ["Yer mum is so Bri'ish, she went to hell",
             "Yo mama so lesbian, she couldn't give birth to a guy",
             "Yo mama so small, she rode Pickle Rick's pickle'd dick",
             "Yo mama so fat, that she was a TF2 map (a good map btw)",
             "Your mother is so morbidly obese, that she has high blood pressure and type 2 diabetes",
             "Yo mama so fat, she out chungus'd, BIG CHUNGUS!",
             "Yo mama so stupid, she couldn't think of a yo mama joke",
             "Yo mama so fat, she is the most upvoted post on r/chonkers"]
  await ctx.send((random.choice(yomjoke)))

@client.command(aliases=["8ball"])
async def yesno(ctx, *, question):
  yesno = ["Yes",
           "No",
           "Maybe",
           "Why?",
           "Ask that to your mom!",
           "Wtf man, I cannot answer that...",
           "I am not the right person to answer this question",
           "There is a high chance",
           "There is a low chance",
           "Fuck off.",
           "If you beat Half-Life in hard, i will answer the question",
           "The answer is in the toilet bowl",
           "Trolled!"]
 
  await ctx.send(content=f'stupid ass question: {question}\nstupid ass answer: {random.choice(yesno)}')

@client.command(aliases=["intercourse"])
async def inter(ctx, *, chr):
  sexrate=random.randint(0,100)
  await ctx.send(content=f'Chance to sex {chr}: {sexrate}%')

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
