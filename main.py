import discord
import os
import random
from keep_alive import keep_alive
from discord.ext import commands


#i fixed it

client = commands.Bot(command_prefix=']')
client.remove_command("help")


@client.group(invoke_without_command=True)
async def help(ctx):

	em = discord.Embed(title="VOX Help",
	                   description="Use ]help <command> for more info")
	em.set_thumbnail(
	    url=
	    "https://cdn.discordapp.com/attachments/794531202488598558/837640723750715443/image0-63.gif"
	)
	em.add_field(name="RNG", value="4 commands")
	em.add_field(name="Test", value="7 commands")
	em.add_field(name="Bot", value="3 commands")
	em.add_field(name="Linne", value="Wow! 2 bots in one huh?")

	await ctx.send(embed=em)


@help.command()
async def rng(ctx):
	em = discord.Embed(title="Random",
	                   description="Commands that use random scripts")
	em.set_thumbnail(
	    url=
	    "https://cdn.discordapp.com/attachments/794531202488598558/837650520839159848/ezgif.com-crop.gif"
	)
	em.add_field(name="hldm, deathmatch, killmessage ",
	             value="Returns a random kill message")
	em.add_field(name="yomama", value="Returns a yo mama joke")
	em.add_field(name="yesno, 8ball", value="Answers your questions")
	em.add_field(name="inter, intercourse", value="sex someone")
	await ctx.send(embed=em)


@help.command()
async def test(ctx):
	em = discord.Embed(title="Test",
	                   description="Commands that is for testing")
	em.set_thumbnail(
	    url=
	    "https://media.discordapp.net/attachments/772417751540170792/813431331019030578/type.gif"
	)
	em.add_field(name="e", value="test command 1")
	em.add_field(name="mvm", value="test command 2")
	em.add_field(name="yourmom", value="test command 3")
	em.add_field(name="everyone", value="test command 4")
	em.add_field(name="r34", value="test command 5")
	em.add_field(name="sexed", value="video test")
	em.add_field(name="amongus", value="shows among us")

	await ctx.send(embed=em)


@help.command()
async def bot(ctx):
  em = discord.Embed(title="Bot",description="Commands that has to do with the bot")
  em.set_thumbnail(url="https://cdn.discordapp.com/attachments/783667025565712417/837677710829682699/ezgif.com-resize-2.gif")
  em.add_field(name="ping", value="Returns latency")
  em.add_field(name="source",value="Returns the source code/github")
  em.add_field(name="update", value="change log")
  await ctx.send(embed=em)

@help.command()
async def linne(ctx):
  em = discord.Embed(title = "Linne's stuff", description = "We combined the most used bot among this community to make this bot larger")
  em.add_field(name="pp", value="penis")
  em.add_field(name="butt", value="butt")
  em.add_field(name="thigh", value="thigh")
  em.add_field(name="boob", value="boobs")
  await ctx.send(embed=em)

#the linne thing or something

@client.command()
async def butt(ctx):
  buttran = ["huge", 
             "small", 
             "thicc", 
             "fat", 
             "sloppy", 
             "wet", 
             "dry", 
             "tight"] 
  await ctx.send ("Your ass is " + random.choice(buttran))

@client.command()
async def pp(ctx):
  penis = ["1",
           "2",
           "3",
           "4",
           "5",
           "6",
           "7",
           "8",
           "9",
           "10",
           "11"] 
  await ctx.send ("Your dick is "+ random.choice(penis)+ " inches long") 

@client.command()
async def thigh(ctx):
  tran = ["huge", 
         "small", 
         "thicc", 
         "fat", 
         "sloppy", 
         "wet", 
         "dry", 
         "tight"]
  await ctx.send("Your thigh is "+random.choice(tran))

@client.command()
async def boob(ctx):
  tit = ["flat",
         "small",
         "medium",
         "big",
         "huge",
         "holy shit it's so big, doesn't your back hurt?",
         "wait... are you a guy?",
         "hold on... you are just a obese man with man boobs"]
  await ctx.send("Your boobs are "+random.choice(tit))


#this is a latency command?
@client.command()
async def ping(ctx):
	await ctx.send(f'latency gaming {round(client.latency * 1000)}ms')


@client.command()
async def e(ctx):
	await ctx.send('fuck off this is not TF2')


@client.command()
async def ver(ctx):
	await ctx.send('VOX InDev Version 0.1.7')


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
	await ctx.send("Currently `242` lines of code has been written")


@client.command(aliases=["deathmatch", "killmessage"])
async def hldm(ctx):
	plr = [
	    "Gordon Freeman killed", "Scout killed", "Soldier killed",
	    "Pyro killed", "Demoman killed", "Engineer killed", "Heavy killed",
	    "Medic killed", "Sniper killed", "Spy killed", "Jesus killed",
	    "Agent Jones killed"
	]

	die = [
	    "Gordon Freeman with", "Scout with", "Soldier with", "Pyro with",
	    "Demoman with", "Engineer with", "Heavy with", "Medic with",
	    "Sniper with", "Spy with", "Jesus with", "Agent Jones with"
	]
	#NSFW
	deathreason = [
	    "Crowbar", "Glock 17", ".357 Magnum", "MP5", "SPAS-12", "Crossbow",
	    "Tau Cannon", "Gauss Cannon", "RPG", "Fragmentation Grenade",
	    "Trimpmine", "Satchel Charge", "Fall Damage", "Physics Gun", "Item",
	    "M1 Garand", "AK-47", "The hand of God", "P90", "Minigun", "C4",
	    "USP Match", "MP7", "AR2", "Scattergun", "Pistol",
	    "Double Barrel Shotgun", "Rocket Launcher", "Bat", "Shovel",
	    "Flamethrower", "Fireaxe", "Grenade Launcher", "Stickybomb Launcher",
	    "Bottle", "Fist", "Wrench", "Sentry LVL 1", "Sentry LVL 2",
	    "Sentry Bullet LVL 3", "Sentry Rocket LVL 3", "Nailgun", "Bonesaw",
	    "Sniper Rifle", "UZI", "Sword", "Sapper", "Butterfly Knife",
	    "Butterfly Knife (backstab"
	]
	await ctx.send(random.choice(plr), random.choice(die), random.choice(deathreason))


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
	    "Yo mama so fat, she is the most upvoted post on r/chonkers"
	]
	await ctx.send((random.choice(yomjoke)))


@client.command(aliases=["8ball"])
async def yesno(ctx, *, question):
	yesno = [
	    "Yes", "No", "Maybe", "Why?", "Ask that to your mom!",
	    "Wtf man, I cannot answer that...",
	    "I am not the right person to answer this question",
	    "There is a high chance", "There is a low chance", "Fuck off.",
	    "If you beat Half-Life in hard, i will answer the question",
	    "The answer is in the toilet bowl", "Trolled!"
	]

	await ctx.send(
	    content=
	    f'stupid ass question: {question}\nstupid ass answer: {random.choice(yesno)}'
	)


@client.command(aliases=["intercourse"])
async def inter(ctx, *, chr):
	sexrate = random.randint(0, 100)
	await ctx.send(content=f'Chance to sex {chr}: {sexrate}%')


@client.command()
async def amongus(ctx):
	await ctx.send(
	    "https://cdn.discordapp.com/attachments/794531202488598558/828277315133505606/red-among-us-png.png"
	)


@client.command()
async def source(ctx):
  await ctx.send("https://github.com/gordonfreeman3549/solly")

@client.command()
async def update(ctx):
  await ctx.send("~ Changed the `amogus` command to `sexed`.\n~ Changed how `sexed` functions.")

@client.command()
async def about(ctx):
  await ctx.send("Bot made by Rosa(Headcrab#5562)")

@client.command()
async def sexed(ctx):
  ed = ["https://cdn.discordapp.com/attachments/850565037072056323/853710195988889600/Hangout_Fortress_member_gets_a_lesson_in_meme_culture.mp4", 
         "https://cdn.discordapp.com/attachments/850565037072056323/854320619331518474/We_will_be_talking_about_the_penis_and_vagina..mp4", 
         "https://cdn.discordapp.com/attachments/850565037072056323/851670371581034536/video0.mp4",
         "https://cdn.discordapp.com/attachments/830849943379902505/854326068164689930/video0.mp4",
         "https://cdn.discordapp.com/attachments/830849943379902505/854326168521146368/talkaboutthe.mp4"]
  await ctx.send("Ping Headcrab if you have a `We will talking about` meme."+random.choice(ed))


#this part is fixed now it shows an epic status i guess?
#but yeah, this will crash the bot later for some fucking reason,


@client.event
async def on_ready():
	print('My body is ready')
	await client.change_presence(activity=discord.Activity(
	    type=discord.ActivityType.watching, name="]help"))


#triggers
#i have removed the triggers because, there is a conflict, i will fix it later

keep_alive()
client.run(os.getenv('TOKEN'))
