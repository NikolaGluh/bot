import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import wikipedia
import datetime
import PIL
from PIL import Image, ImageDraw, ImageFont
import firebase
from firebase import firebase
import math
import time
import joke.jokes
from joke.jokes import *
from random import choice
import requests
from io import BytesIO

#Client = discord.Client()
client = commands.Bot(command_prefix="c!", activity=discord.Activity(name="you xdddddddddd", type=discord.ActivityType.watching))
client.remove_command("help")

@client.event
async def on_ready():
    print("spiker prepared!")

fb = firebase.FirebaseApplication("https://yesn-t-399e9.firebaseio.com/", None)
devs = [476770711562747905, 429213502813503488, 373626824963391489]

@client.event
async def on_raw_reaction_add(payload):
    react = payload.emoji
    guild = client.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    if payload.message_id == 582149346737258501:
        if str(react) == "🌵":
            role = guild.get_role(581442708942487563)
            await member.add_roles(role)

@client.event
async def on_raw_reaction_remove(payload):
    react = payload.emoji
    guild = client.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    if payload.message_id == 582149346737258501:
        if str(react) == "🌵":
            role = guild.get_role(581442708942487563)
            await member.remove_roles(role)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("You are on cooldown, please retry in {}s.".format(math.ceil(error.retry_after)))
        return

@client.event
async def on_command(ctx):
    if fb.get(f"cactus/profile/", str(ctx.author.id), None) is None:
        userdata = {
        "Name": ctx.author.name,
        "Coins": 0,
        "Exp": 0,
        "Lvl": 1,
        "Description": "default description",
        }

        fb.put(f"cactus/profile/", str(ctx.author.id), userdata)

@client.event
async def on_message(message):
    messagecount = fb.get(f"cactus/Count", "messagecountglobal")
    messageadd = fb.put(f"cactus/Count", "messagecountglobal", int(messagecount + 1))
    if message.content.lower() == "hello there" and random.randint(1, 10) == 1:
        await message.channel.send("General Kenobi")
        await message.channel.send("You are a bold one")
        m = await message.channel.send(file=discord.File('General Kenobi.png'))
        await asyncio.sleep(10)
        await m.delete()
    if message.content.lower() == "owo" and random.randint(1, 3) == 1:
        await message.channel.send("What's this?")
    if "ba" in message.content.lower():
        if message.author == client.user:
            return
        else:
            await message.channel.send("ba defames us!")
    cactus = ["are", "?", "should", "why", "how", "is", "!", "im", "you"]
    response_check = []
    for word in cactus:
        response_check.append(word in message.content.lower())
    if any(response_check) and " " in message.content.lower() and random.randint(1, 4) == 1:
        if message.author == client.user:
            return
        else:
            messages = ["Never", "Yes.", "No.", "Sure.", "No...", "Probably.", "Pro", "I Don't Think So."]
            await message.channel.send(random.choice(messages))
    if "8ball" in message.content.lower():
        messages = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
        await message.channel.send(random.choice(messages))
    if message.content.lower() == "happens":
        await message.channel.send(file=discord.File('HAPPENS.png'))
    if message.content.lower() == "cactus":
        await message.channel.send("wat?")
    if random.randint(1, 100) == 1 and "babft" in message.content.lower() in message.content:
        await message.channel.send("baft*")
    if message.author.name == "durkdekurk" and random.randint(1, 100) == 1:
        await message.channel.send("durk pro")
    if message.content.lower() == "hi cactus xd":
        await message.channel.send("hi cactus xddddddddddddddddddddddddddddddddddddddddddddddddddddddd")
    if message.content.lower() == "you remind me of the babe":
        await message.channel.send("What babe?")
    if message.content.lower() == "the babe with the power":
        await message.channel.send("What power?")
    if message.content.lower() == "the power of voodoo":
        await message.channel.send("Who do?")
    if message.content.lower() == "you do":
        await message.channel.send("Do what?")
    if message.content.lower() == "remind me of the babe":
        await message.channel.send("What babe?")
    if "r/" in message.content.lower() in message.content:
        banned = fb.get("cactus/banned", str(author.id))
        if banned is None:
            if message.author == client.user:
                return
            r = message.content
            embedreddit = discord.Embed(
                title="<:reddit:581088652759662592> Here's your subreddit!",
                color=0xed6a07
            )

            embedreddit.add_field(name="https://www.reddit.com/" + r, value="epic subreddit", inline=False)
            await message.channel.send(embed=embedreddit)
        else:
            await message.channel.send("You are banned from the bot!")
    if message.content.lower() == "hi rap" and random.randint(1, 4) == 1:
        if message.author == client.user:
            return
        else:
            await message.channel.send("hi rap")
    if random.randint(1, 1000) == 1:
        await message.channel.send("die")
        await message.channel.send(file=discord.File('santa.PNG'))
    no_u_variants = ["no u", "no you", "no yesn't", "no you.", "no ya"]
    if message.content.lower() in no_u_variants and random.randint(1, 5) == 1:
        if message.author == client.user:
            return
        else:
            await message.channel.send("no u")
    msgs = ["im", "Im", "IM", "i am", "I am", "I AM", "i m", "I m", "I M"]
    for msg in msgs:
        try:
            if message.content.startswith(msg, 0, 10) and random.randint(1, 5) == 1:
                words = message.content[len(msg):].split(" ")
                await message.channel.send(f'Hi {words}, im dad')
        except:
            pass
    #r = random.randint(1, 5)
#    getexp = fb.get(f"cactus/profile/{message.author.id}", "Exp")
    #expgive = fb.put(f"cactus/profile/{message.author.id}", "Exp", int(getexp + r))
    #lvl = fb.get(f"cactus/profile/{message.author.id}", "Lvl")
    #lvl_end = int(getexp ** (0.8))
    #if lvl > lvl_end:
    #    await message.channel.send(f"Congratulations {message.author.mention} you leveled up to level {lvl_end}!")
    #    lvlgive = fb.put(f"cactus/profile/{message.author.id}", "Lvl", lvl_end)
    await client.process_commands(message)

@client.command()
async def kill(ctx):
    if ctx.author.id in devs:
        messages = ["***__Oladencola looked at me so i had a stroke and died__***", "***Literally Dying...***", "***__Liege North touched me so im dying__***", "***being snapped from the universe...***"]
        await ctx.message.channel.send(random.choice(messages))
        await client.logout()
    else:
        await ctx.send("<:cactusfailed:580834469842386975> You don't have permission st00pid!")

@client.command(name="dm", aliases=["directmessage", "directmsg", "dirmsg", "dirmessage"])
async def directmessage(ctx, user: discord.User, msg):
    if ctx.author.id in devs:
        await ctx.message.delete()
        async with user.typing():
            await asyncio.sleep(len(msg) / 10)
            await user.send(msg)
            await ctx.message.channel.send("i did it master")
            usr = client.get_user(476770711562747905)
            await usr.send("**" + ctx.message.author.name + ": **" + msg + " TO " + "***" + user.name + "***")
    else:
        await ctx.send("<:cactusfailed:580834469842386975> What an idiot tried to use this command knowing its developer only!")

@client.command(pass_context = True)
async def ping(ctx):
    async with ctx.typing():
        banned = fb.get("cactus/banned", str(ctx.author.id))
        if banned is None:
            t1 = ctx.message.created_at
            m = await ctx.send('**Pong!**')
            time = (m.created_at - t1).total_seconds() * 1000
            await m.edit(content='**Pong! Took: {}ms**'.format(int(time)))
        else:
            await ctx.send("You are banned from the bot!")

@client.command()
async def say(ctx, *, arg):
    async with ctx.typing():
        banned = fb.get("cactus/banned", str(ctx.author.id))
        if banned is None:
            if "@everyone" in ctx.message.content or "@here" in ctx.message.content or ctx.message.role_mentions != [] or ctx.author.id == 401044899568287744:
                await ctx.send("no no!")
                await ctx.message.delete()
            else:
                await ctx.send(arg)
                await ctx.message.delete()
        else:
            await ctx.send("You are banned from the bot!")

embedtest = discord.Embed(
    title="**Click For Robux**",
    url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    color=0xef1313
)

@client.command(aliases=["freeroux"])
async def freerobux(ctx):
    async with ctx.typing():
        await ctx.send(embed=embedtest)

embedfun = discord.Embed(
    title="<:cactusbot:581412557152190464> CactusBot",
    description="**All of fun commands are:**",
    url="https://cdn.discordapp.com/attachments/580784963272704020/581414254029307904/sm_5aaa3579e4d62.png",
    color=0x0da323
)

embedfun.add_field(name="ping", value="shows you your ping.", inline=False)
embedfun.add_field(name="say <message>", value="says the message you want.", inline=False)
embedfun.add_field(name="freerobux", value="gives free robux legit way.", inline=False)
embedfun.add_field(name="8ball <question> [no prefix]", value="tells you what to do.", inline=False)
embedfun.add_field(name="servers", value="shows servers you idots invited him in.    ᶜʳᵉᵈᶦᵗˢ ᵗᵒ ʳᵃᵖ", inline=False)
embedfun.add_field(name="hackrbx", value="hacks roblox.", inline=False)
embedfun.add_field(name="snap", value="perfectly balanced as all things should be.", inline=False)
embedfun.add_field(name="murder <message>", value="kills someone you don't like.", inline=False)
embedfun.add_field(name="wiki <search>", value="searches wikipedia.", inline=False)
embedfun.add_field(name="gay", value="somebody is gay here.", inline=False)
embedfun.add_field(name="r/<subreddit> [no prefix]", value="shows you subreddit you want.", inline=False)
embedfun.add_field(name="remindme <time period in seconds> <reminder>", value="reminds you of something.", inline=False)
embedfun.add_field(name="howgay <member>", value="tells you how gay you are.", inline=False)
embedfun.add_field(name="<:greg:581569386461003787> howgreg <member>", value="shows you how shit you ar...i mean how greg you are!", inline=False)
embedfun.add_field(name="askrap <question>", value="why ask 8ball when u can ask rap?", inline=False)
embedfun.add_field(name="helpfun", value="shows this message.", inline=False)

@client.group(name="helpfun")
@commands.cooldown(1, 60, commands.BucketType.user)
async def helpfun(ctx):
    if ctx.invoked_subcommand is None:
        banned = fb.get("cactus/banned", str(ctx.author.id))
        if banned is None:
            await ctx.send(embed=embedfun)
        else:
            await ctx.send("You are banned from the bot!")

embedfun2 = discord.Embed(
    title="<:cactusbot:581412557152190464> CactusBot",
    description="**All of fun commands page 2 are:**",
    url="https://cdn.discordapp.com/attachments/580784963272704020/581414254029307904/sm_5aaa3579e4d62.png",
    color=0x0da323
)

embedfun2.add_field(name="rps <rock, paper or scissors>", value="play rock paper scissors with the bot.", inline=False)
embedfun2.add_field(name="wikidonate", value="donate to wikipedia.", inline=False)
embedfun2.add_field(name="bug", value="report a bug to the dev.", inline=False)
embedfun2.add_field(name="idea", value="send idea to the dev.", inline=False)
embedfun2.add_field(name="profile", value="shows you your profile or someone elses profile, use c!setprofile to setup your profile.", inline=False)
embedfun2.add_field(name="poll <message>", value="makes a voting pole.", inline=False)
embedfun2.add_field(name="info", value="shows all info about the bot.", inline=False)
embedfun2.add_field(name="worlddestroy", value="shows you how much you have left to live.", inline=False)
embedfun2.add_field(name="spotify", value="spotify info for you or the person you select.", inline=False)
embedfun2.add_field(name="messages", value="shows the amount of messages that were said while bot was running", inline=False)
embedfun2.add_field(name="joke", value="sends a random generated joke, you can also specify what type of joke you want if you put `dadjoke`,`geek`,`icndb` or `chucknorris`", inline=False)
embedfun2.add_field(name="helpfun2", value="shows this message.", inline=False)

@client.command(aliases=["helpfunpage2", "helpfun page 2"])
@commands.cooldown(1, 60, commands.BucketType.user)
async def helpfun2(ctx):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        await ctx.send(embed=embedfun2)
    else:
        await ctx.send("You are banned from the bot!")

embednerd = discord.Embed(
    title="<:cactusbot:581412557152190464> CactusBot",
    description="**All of ~~nerd~~ math commands are:**",
    url="https://cdn.discordapp.com/attachments/580784963272704020/581414254029307904/sm_5aaa3579e4d62.png",
    color=0x4e8ef4
)

embednerd.add_field(name="add <number 1> <number 2>", value="adds 1 number to other one.", inline=False)
embednerd.add_field(name="minus <number 1> <number 2>", value="takes 1 number from other one.", inline=False)
embednerd.add_field(name="square <number>", value="squares the number.", inline=False)
embednerd.add_field(name="helpmath", value="shows this message.", inline=False)


@client.command(name="helpmath", aliases=["helpnerd", "helpmatt"])
@commands.cooldown(1, 60, commands.BucketType.user)
async def helpmath(ctx):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        async with ctx.typing():
            await ctx.send(embed=embednerd)
    else:
        await ctx.send("You are banned from the bot!")

embedmoderation = discord.Embed(
    title="<:cactusbot:581412557152190464> CactusBot",
    description="**All of moderation commands are:**",
    url="https://cdn.discordapp.com/attachments/580784963272704020/581414254029307904/sm_5aaa3579e4d62.png",
    color=0xdd0f0f
)

embedmoderation.add_field(name="clear <amount>", value="purges the amount of messages you specify(plus self message).", inline=False)
embedmoderation.add_field(name="userinfo <member>", value="tells you everything about the user.", inline=False)
embedmoderation.add_field(name="serverinfo", value="shows you info about the server.", inline=False)
embedmoderation.add_field(name="kick <member>", value="kicks a selected member.", inline=False)
embedmoderation.add_field(name="ban <member>", value="bans a selected member.", inline=False)
embedmoderation.add_field(name="role <member> <role name>", value="gives/removes a role from selected member.", inline=False)
embedmoderation.add_field(name="helpmoderation", value="shows this message.", inline=False)


@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def helpmoderation(ctx):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        async with ctx.typing():
            await ctx.send(embed=embedmoderation)
    else:
        await ctx.send("You are banned from the bot!")

@client.command()
async def clear(ctx, *, number:int=None):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        if ctx.message.author.guild_permissions.manage_messages or ctx.author.id == 476770711562747905:
                if number is None:
                     await ctx.message.channel.purge(limit=1)
                else:
                    deleted = await ctx.message.channel.purge(limit=1 + number)
                    clear = await ctx.send("<:cactusdone:580753069009010710> spiked those messages **epically**")
                    await asyncio.sleep(5)
                    await clear.delete()
        else:
            await ctx.send("<:cactusfailed:580834469842386975> you dont have permission for this...and that's gay!")
    else:
        await ctx.send("You are banned from the bot!")

@client.command(name="servers", aliases=["guilds"])
@commands.cooldown(1, 60, commands.BucketType.user)
async def servers(ctx):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        msg = "**some shitos invited me in**\n"
        for server in client.guilds:
            if "@everyone" in server.name.lower() or "@here" in server.name.lower():
                msg += "{0}\n".format(server.id)
            else:
                msg += "{0}(`{1}`)\n".format(server.name, server.id)
        await ctx.send(msg)
    else:
        await ctx.send("You are banned from the bot!")

@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def hackrbx(ctx):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        await ctx.send(ctx.author.mention + " is hacking Roblox!")
        m = await ctx.send(":black_small_square::black_small_square::black_small_square::black_small_square::black_small_square:")
        await asyncio.sleep(2)
        await m.edit(content=':white_small_square::black_small_square::black_small_square::black_small_square::black_small_square:')
        await asyncio.sleep(2)
        await m.edit(content=':white_small_square::white_small_square::black_small_square::black_small_square::black_small_square:')
        await asyncio.sleep(2)
        await m.edit(content=':white_small_square::white_small_square::white_small_square::black_small_square::black_small_square:')
        await asyncio.sleep(2)
        await m.edit(content=':white_small_square::white_small_square::white_small_square::white_small_square::black_small_square:')
        await asyncio.sleep(2)
        await m.edit(content=':white_small_square::white_small_square::white_small_square::white_small_square::white_small_square:')
        await asyncio.sleep(1)
        roblox = ["<:cactusdone:580753069009010710> **Roblox** has been hacked!You stole 1000000 roux!", "<:cactusfailed:580834469842386975> David Bazooka protected roblox with big boi bazooka you get nothing except for termination from robloc", "<:cactusfailed:580834469842386975> No one was there but the robux wasn't there either hm....."]
        await ctx.send(random.choice(roblox))
    else:
        await ctx.send("You are banned from the bot!")

@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def snap(ctx):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        await ctx.send("***i don't feel so good***")
        m = await ctx.send(":black_small_square::black_small_square::black_small_square::black_small_square::black_small_square:")
        await asyncio.sleep(2)
        await m.edit(content=':white_small_square::black_small_square::black_small_square::black_small_square::black_small_square:')
        await asyncio.sleep(2)
        await m.edit(content=':white_small_square::white_small_square::black_small_square::black_small_square::black_small_square:')
        await asyncio.sleep(2)
        await m.edit(content=':white_small_square::white_small_square::white_small_square::black_small_square::black_small_square:')
        await asyncio.sleep(2)
        await m.edit(content=':white_small_square::white_small_square::white_small_square::white_small_square::black_small_square:')
        await asyncio.sleep(2)
        await m.edit(content=':white_small_square::white_small_square::white_small_square::white_small_square::white_small_square:')
        await asyncio.sleep(1)
        await ctx.send("Congratulations the universe is now **perfectly balanced**!")
        gif = await ctx.send(file=discord.File('perfectlybalanced.gif'))
        await asyncio.sleep(20)
        await gif.delete()
    else:
        await ctx.send("You are banned from the bot!")

@client.command()
async def murder(ctx, *, user: discord.Member):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        async with ctx.typing():
            if "@everyone" in ctx.message.content or "@here" in ctx.message.content or ctx.message.role_mentions != []:
                await ctx.send("no no!")
                await ctx.message.delete()
            else:
                responses = ["got hit by a bus while yelling 'I'M GONNA BE SOMEBODY!!'.", "died while making a list of the 'Top 10 funniest ways to die'.", "accidently beated himself up.", "attempted to poop but they're head exploded due to too much pressure.", "got machine gunned to death by a cheesecake.", "died by laughing too hard.", "divided 0 by 0 on a calculator, which created a black hole and got them sucked in where Justin Beiber is the best singer in the new universe and they committed suicide.", "is that stupid that they gave their address and now they are watching some guy going to their house with gun.", "starved while eating.", "thought they can walk on water.", "choked on oxygen.", "got punched in the face by an egg.", "got stabbed by their three year old kid", "fell from a chair","forgot to turn the toaster off", "took a bath in a boiler", "ran into KFC screaming 'what's up my n****' and hoping they don't get shot.But they do.Everyone does.", "fortnite danced in public", "ate sand", "ate shit and died"]
                await ctx.send(f"**{user.name}** " + random.choice(responses))
    else:
        await ctx.send("You are banned from the bot!")

@client.command(name="invite", aliases=["inv"])
async def invite(ctx, server_id):
    if ctx.author.id in devs:
        server = client.get_guild(int(server_id))
        invite = await server.text_channels[0].create_invite(max_age=60, max_uses=1)
        await ctx.send("{0}".format(invite.url))
    else:
        await ctx.send("no idot,no invite for u")

@client.command(name="wiki", aliases=["wikipedia"] )
async def wiki(ctx, arg1, arg2: int = 2048):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        async with ctx.typing():
            try:
                page = wikipedia.page(arg1)
                wiki = discord.Embed(title="**{0}**".format(page.title), url=page.url, description=page.content[:arg2], color=0xffffff)
                await ctx.send(embed=wiki)
            except Exception as error:
                await ctx.send('{}'.format(error))
    else:
        await ctx.send("You are banned from the bot!")

@client.command()
async def gay(ctx):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        async with ctx.typing():
            membr = random.choice(ctx.guild.members).name
            await ctx.send(membr + " is gay")
    else:
        await ctx.send("You are banned from the bot!")

@client.command(name="remindme", aliases=["reminder", "setreminder"])
async def rmd(ctx, sec: int, arg):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        counter = sec

        msg = await ctx.send("`{0}`".format(counter))

        while counter > 0:
            await asyncio.sleep(1)
            counter -= 1
            await msg.edit(content="`{0}`".format(counter))

        await msg.edit(content="`Done.`")
        m = ctx.author.mention
        await ctx.send(m)
        embedreminder = discord.Embed(
            title=":alarm_clock: Your reminder is over!",
            color=0x79e506
        )

        embedreminder.add_field(name="`" + arg + "`", value="   ‍   ", inline=False)
        await ctx.send(embed=embedreminder)
    else:
        await ctx.send("You are banned from the bot!")

@client.command(aliases=["howgay"])
async def howmuchgay(ctx, *, user: discord.Member = None):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        async with ctx.typing():
            if user is None:
                user = ctx.author
            random.seed()
            r = random.randint(1, 100)
            gay = r / 1.17

            emoji = "👨"
            if gay > 25:
                emoji = "🌈"
            if gay > 50:
                emoji = "👬"
            if gay > 75:
                emoji = "‍🏳️‍🌈"
            await ctx.send(f"**{user.name}** is `{gay:.2f}%` gay {emoji} and that's a fact!")
    else:
        await ctx.send("You are banned from the bot!")

@client.command(aliases=["howgregur"])
async def howgreg(ctx, *, user: discord.Member = None):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        async with ctx.typing():
            if user is None:
                user = ctx.author
            random.seed()
            r = random.randint(1, 100)
            greg = r / 1.17
            await ctx.send(f"<:greg:581569386461003787> **{user.name}** is `{greg:.2f}%` greg!")
    else:
        await ctx.send("You are banned from the bot!")

@client.command(aliases=["userinfo"])
async def user(ctx, user: discord.Member):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        async with ctx.typing():
            embedinfo = discord.Embed(title="{}'s user-info".format(user.name), description='epic info!!!11', color=ctx.message.author.color)
            embedinfo.add_field(name='Name', value='{}'.format(user.name))
            embedinfo.add_field(name='ID', value='{}'.format(user.id), inline=True)
            embedinfo.add_field(name='Status', value='{}'.format(user.status), inline=True)
            embedinfo.addield(name='Highest Role', value='<@&{}>'.format(user.top_role.id), inline=True)
            embedinfo.add_field(name='Joined at', value='{:%d/%h/%y at %H:%M}'.format(user.joined_at), inline=True)
            embedinfo.add_field(name='Created at', value='{:%d/%h/%y at %H:%M}'.format(user.created_at), inline=True)
            embedinfo.add_field(name='Discriminator/Tag', value='{}'.format(user.discriminator), inline=True)
            embedinfo.add_field(name='Default avatar', value="{}".format(user.default_avatar_url))
            embedinfo.set_footer(text="{}'s epic Info".format(user.name), icon_url='{}'.format(user.avatar_url))
            embedinfo.set_thumbnail(url=user.avatar_url)
            await ctx.send(embed=embedinfo)
    else:
        await ctx.send("You are banned from the bot!")

@client.command()
async def serverinfo(ctx, server_id=None):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        if server_id is None:
            embedserver = discord.Embed(title="{}'s info".format(ctx.guild.name), description="epic server i see", color=ctx.message.author.color)
            embedserver.add_field(name="Owner", value="{0}#{1}".format(ctx.guild.owner.name, ctx.guild.owner.discriminator))
            embedserver.add_field(name="Region", value="{}".format(ctx.guild.region))
            embedserver.add_field(name="Name", value="{}".format(ctx.guild.name))
            embedserver.add_field(name="Server ID", value="`{}`".format(ctx.guild.id))
            embedserver.add_field(name="Members", value="{}".format(ctx.guild.member_count))
            embedserver.add_field(name="Roles", value='{}'.format(len(ctx.guild.roles)))
            embedserver.set_thumbnail(url=ctx.guild.icon_url)
            embedserver.set_footer(text="Requested by idot called {}".format(ctx.message.author.name) + "#{}".format(ctx.message.author.discriminator), icon_url='{}'.format(ctx.message.author.avatar_url))
            await ctx.send(embed=embedserver)
        else:
            server = client.get_guild(int(server_id))
            embedserver = discord.Embed(title="{}'s info".format(server.name), description="epic server i see", color=ctx.message.author.color)
            embedserver.add_field(name="Owner", value="{0}#{1}".format(server.owner.name, server.owner.discriminator))
            embedserver.add_field(name="Region", value="{}".format(server.region))
            embedserver.add_field(name="Name", value="{}".format(server.name))
            embedserver.add_field(name="Server ID", value="`{}`".format(server.id))
            embedserver.add_field(name="Members", value="{}".format(server.member_count))
            embedserver.add_field(name="Roles", value='{}'.format(len(server.roles)))
            embedserver.set_thumbnail(url=server.icon_url)
            embedserver.set_footer(text="Requested by idot called {}".format(ctx.message.author.name) + "#{}".format(ctx.message.author.discriminator), icon_url='{}'.format(ctx.message.author.avatar_url))
            await ctx.send(embed=embedserver)
    else:
        await ctx.send("You are banned from the bot!")

@client.command(pass_context=True)
async def square(ctx, number):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        if len(number) > 10:
            await ctx.send('enter number less than 10 characters spam idot')
        else:
            squared_value = int(number) * int(number)
            await ctx.send(str(number) + " squared is " + str(squared_value))
    else:
        await ctx.send("You are banned from the bot!")

@client.command(aliases=['Add', 'ADD'])
async def add(ctx, left : int, right : int):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        await ctx.send(f"{left} + {right} = {left+right}")
    else:
        await ctx.send("You are banned from the bot!")

@client.command(aliases=['Minus', 'MINUS', 'Subtract', 'subtract', 'SUBTRACT'])
async def minus(ctx, left : int, right : int):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        await ctx.send(f"{left} - {right} = {left-right}")
    else:
        await ctx.send("You are banned from the bot!")

@client.command(pass_context=True)
async def help(ctx):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        try:
            Help = discord.Embed(title="<:cactusbot:581412557152190464> Here are all categories for help commands", description="more commands being added every day!", color=0x0072ff)
            Help.add_field(name='Currency Commands', value='`c!helpcurrency`')
            Help.add_field(name='Fun Commands', value='`c!helpfun and c!helpfun2`')
            Help.add_field(name='Math Commands', value='`c!helpmath`')
            Help.add_field(name='Moderation Commands', value='`c!helpmoderation`')
            Help.add_field(name='Developer Commands', value='`c!helpdev`')
            await ctx.send(embed=Help)
        except Exception as error:
            await ctx.send('{}'.format(error))
    else:
        await ctx.send("You are banned from the bot!")

embedcurrency = discord.Embed(
    title="<:cactusbot:581412557152190464> CactusBot",
    description="**All of currency commands are:**",
    url="https://cdn.discordapp.com/attachments/580784963272704020/581414254029307904/sm_5aaa3579e4d62.png",
    color=0xebce10
)

embedcurrency.add_field(name="beg", value="gives a random amount of spikes(between 1 and 100).", inline=False)
embedcurrency.add_field(name="bal", value="shows you your balance with spikes, you can also check other peoples balance.", inline=False)
embedcurrency.add_field(name="share", value="shares amount of spikes to other user", inline=False)
embedcurrency.add_field(name="spiker ritual <amount>", value="gambles amount of money for a chance to get double of the amount or lose the amount", inline=False)
embedcurrency.add_field(name="helpcurrency", value="shows this message.", inline=False)

@client.command()
async def helpcurrency(ctx):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        await ctx.send(embed=embedcurrency)
    else:
        await ctx.send("You are banned from the bot!")

embeddev = discord.Embed(
    title="<:cactusbot:581412557152190464> CactusBot",
    description="**All of dev commands are:**",
    url="https://cdn.discordapp.com/attachments/580784963272704020/581414254029307904/sm_5aaa3579e4d62.png",
    color=0x656e6c
)

embeddev.add_field(name="directmessage <user>", value="dms a selected user.", inline=False)
embeddev.add_field(name="invite <server>", value="creates a 1 use invite to any server cactus bot is in.", inline=False)
embeddev.add_field(name="botban <user>", value="bans a selected user from the bot.", inline=False)
embeddev.add_field(name="unbotban <user>", value="unbans a selected user from the bot.", inline=False)
embeddev.add_field(name="adduser <user>", value="adds a selected user to database.", inline=False)
embeddev.add_field(name="coin <user> <amount>", value="shares unlimited amount of money to user.", inline=False)
embeddev.add_field(name="take <user> <amount>", value="takes away amount of coins from user.", inline=False)
embeddev.add_field(name="helpdev", value="shows this message.", inline=False)

@client.command(aliases=["helpdeveloper"])
async def helpdev(ctx):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        await ctx.send(embed=embeddev)
    else:
        await ctx.send("You are banned from the bot!")

@client.command()
async def askrap(ctx, *, arg):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        rap = ["hi rap", "sphere!", "xd", "eggs!", "are you f retarded?", "make mech", "make mech...but less retarded this time", "ex pro"]
        askrap = discord.Embed(color=ctx.message.author.top_role.color)
        askrap.add_field(name=ctx.message.author.name + ": " + arg, value="Rap: " + random.choice(rap))
        await ctx.send(embed=askrap)
    else:
        await ctx.send("You are banned from the bot!")

@client.group(name="rps")
async def rps(ctx):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        if ctx.invoked_subcommand is None:
            await ctx.send("say rock/paper/scissors nub")
    else:
        await ctx.send("You are banned from the bot!")

@rps.command(name="rock", aliases=["paper", "scissors", ":hand_splayed:", ":v:", ":fist:"])
async def rock(ctx):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        answer = [":v:", ":fist:", ":hand_splayed:"]
        await ctx.send(random.choice(answer))
    else:
        await ctx.send("You are banned from the bot!")

@client.command(aliases=["wikidon"])
async def wikidonate(ctx):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        await ctx.send("donate wikipedia to feel good")
        await ctx.send("`donation page link will be sent in 10 seconds in meanwhile DIE`")
        await asyncio.sleep(10)
        await ctx.send("https://donate.wikimedia.org/wiki/Special:LandingPage")
    else:
        await ctx.send("You are banned from the bot!")

@client.command()
async def profile(ctx, user: discord.Member=None):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        if user is None:
            profiledesc = fb.get(f"cactus/profile/{ctx.author.id}", "Description")
            getcoins = fb.get(f"cactus/profile/{ctx.author.id}", "Coins")
            getlvl = fb.get(f"cactus/profile/{ctx.author.id}", "Lvl")
            getexp = fb.get(f"cactus/profile/{ctx.author.id}", "Exp")
            if profiledesc is None:
                profiledesc = "default description, use `c!setprofile description` to change your description"
            embedprofile = discord.Embed(title=ctx.author.name, description=profiledesc, color=ctx.message.author.color)
            embedprofile.add_field(name="Spikes <:spike:594243507200458765>", value=int(getcoins))
            embedprofile.add_field(name="Level", value=int(getlvl))
            embedprofile.add_field(name="Experience Points", value=int(getexp))
            embedprofile.set_footer(text="Requested by idot called {}".format(ctx.author.name), icon_url='{}'.format(ctx.author.avatar_url))
            embedprofile.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embedprofile)
        else:
            profiledesc = fb.get(f"cactus/profile/{user.id}", "Description")
            getcoins = fb.get(f"cactus/profile/{user.id}", "Coins")
            getlvl = fb.get(f"cactus/profile/{user.id}", "Lvl")
            getexp = fb.get(f"cactus/profile/{user.id}", "Exp")
            if profileuserdesc is None:
                profileuserdesc = "default description, use `c!setprofile description` to change your description"
            embedprofile = discord.Embed(title="{}".format(user.name), description=profileuserdesc, color=ctx.message.author.color)
            embedprofile.add_field(name="Spikes <:spike:594243507200458765>", value=int(getcoins))
            embedprofile.add_field(name="Level", value=int(getlvl))
            embedprofile.add_field(name="Experience Points", value=int(getexp))
            embedprofile.set_footer(text="Requested by idot called {}".format(ctx.author.name), icon_url='{}'.format(ctx.author.avatar_url))
            embedprofile.set_thumbnail(url=user.avatar_url)
            await ctx.send(embed=embedprofile)
    else:
        await ctx.send("You are banned from the bot!")
@client.group(name="setprofile")
async def setprofile(ctx):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        if ctx.invoked_subcommand is None:
            await ctx.send("What do you wish to set?\n`description       name`")
    else:
        await ctx.send("You are banned from the bot!")

@setprofile.command(aliases=["desc"])
async def description(ctx, *, arg):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        desc = fb.put(f"cactus/profile/{ctx.author.id}", "Description", str(arg))
        name = fb.put(f"cactus/profile/{ctx.author.id}", "Name", str(ctx.author.name))
        await ctx.send(f"I set your description to `{arg}`|**{ctx.author.name}**")
    else:
        await ctx.send("You are banned from the bot!")

@client.command(aliases=["bugreport", "reportbug"])
async def bug(ctx, *, msg):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        await ctx.message.delete()
        usr = client.get_user(476770711562747905)
        await asyncio.sleep(len(msg) / 10)
        await usr.send(ctx.message.author.name + ":" + msg)
        await ctx.message.channel.send("Thanks for reporting the bug!\n`Every non-serious message will get person banned from the bot`")
    else:
        await ctx.send("You are banned from the bot!")

@client.command(aliases=["giveidea", "sendidea"])
async def idea(ctx, *, msg):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        await ctx.message.delete()
        usr = client.get_user(476770711562747905)
        await asyncio.sleep(len(msg) / 10)
        await usr.send(ctx.message.author.name + ":" + msg)
        await ctx.message.channel.send("Thanks for for the idea!\n`Every non-serious message will get person banned from the bot`")
    else:
        await ctx.send("You are banned from the bot!")

@client.command(aliases=["pollstart", "startpoll"])
async def poll(ctx, *, arg):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        await ctx.message.delete()
        embedpoll = discord.Embed(title="{}'s Poll".format(ctx.author.name), description=arg, color=ctx.message.author.color)
        embedpoll.set_footer(text="Poll by {}".format(ctx.author.name), icon_url='{}'.format(ctx.author.avatar_url))
        msg = await ctx.send(embed=embedpoll)
        emojis = [580753069009010710, 580834469842386975]
        for e in emojis:
            emoji = client.get_emoji(e)
            await msg.add_reaction(emoji)
    else:
        await ctx.send("You are banned from the bot!")

@client.command()
async def info(ctx):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        eminfo = discord.Embed(color=discord.Color.green())
        eminfo.title = 'Bot Info'
        eminfo.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        eminfo.add_field(name="Servers", value=len(client.guilds))
        eminfo.add_field(name="Online Users", value=str(len({m.id for m in client.get_all_members() if m.status is not discord.Status.offline})))
        eminfo.add_field(name='Total Users', value=len(client.users))
        eminfo.add_field(name='Channels', value=f"{sum(1 for g in client.guilds for _ in g.channels)}")
        eminfo.add_field(name="Library", value=f"discord.py")
        eminfo.add_field(name="Bot Latency", value=f"{client.ws.latency * 1000:.0f} ms")
        eminfo.add_field(name="Invite", value=f"[Click Here](https://discordapp.com/oauth2/authorize?client_id={client.user.id}&scope=bot&permissions=268905542)")
        eminfo.add_field(name="Join Our Support Server!", value=f"[Click here](https://discord.gg/9N7Kv7n)")
        eminfo.set_footer(text="CactusBot | Created by Nik#0054 | Powered by discord.py")
        await ctx.send(embed=eminfo)
    else:
        await ctx.send("You are banned from the bot!")

@client.command()
async def worlddestroy(ctx):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        random.seed()
        r = random.randint(1, 100)
        await ctx.send(f"You have `{r}` more days to live!")
    else:
        await ctx.send("You are banned from the bot!")

@client.command()
async def kick(ctx, user: discord.Member, *, reason = "No Reason Provided"):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        if ctx.author == client.user:
            return
        if ctx.message.author.guild_permissions.kick_members or ctx.message.author.id in devs:
            if reason is None:
                await ctx.guild.kick(user = user, reason = "No Reason Provided")
                await ctx.send(f"**{user} has been kicked**")
                await user.send(f"You were kicked from {ctx.guild.name}, {reason}")
            else:
                await ctx.guild.kick(user = user, reason = reason)
                await ctx.send(f"**{user} has been kicked, {reason}**")
                await user.send(f"You were kicked from {ctx.guild.name}, {reason}")
        else:
            await ctx.send("You have no permission to use this idot")
    else:
        await ctx.send("You are banned from the bot!")

@client.command()
async def ban(ctx, user: discord.Member, *, reason = "No Reason Provided"):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        if ctx.author == client.user:
            return
        if ctx.message.author.guild_permissions.ban_members or ctx.message.author.id in devs:
            if reason is None:
                await ctx.guild.ban(user = user, reason = "No Reason Provided")
                await ctx.send(f"**{user} has been banned, {reason}**")
                await user.send(f"You were banned from {ctx.guild.name}, {reason}")
            else:
                await ctx.guild.ban(user = user, reason = reason)
                await ctx.send(f"**{user} has been banned, {reason}**")
                await user.send(f"You were banned from {ctx.guild.name}, {reason}")
        else:
            await ctx.send("You have no permission to use this idot")
    else:
        await ctx.send("You are banned from the bot!")

@client.command()
async def spotify(ctx, user: discord.Member = None):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        if isinstance(user.activity, discord.Spotify):
            embedspotify = discord.Embed(title=f"<:spotify:592829167587033109> Spotify Info for {user.name}", description=f"**Song: {user.activity.title}\nArtist: {user.activity.artist}\nAlbum: {user.activity.album}**", color=0x1eba10)
            embedspotify.set_thumbnail(url=user.activity.album_cover_url)
            await ctx.send(embed=embedspotify)
    else:
        await ctx.send("You are banned from the bot!")

@client.command()
async def role(ctx, member: discord.Member, role: discord.Role):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        if ctx.message.author.guild_permissions.manage_roles or ctx.author.id in devs:
            if role in member.roles:
                await member.remove_roles(role)
                await ctx.send("<:cactusdone:580753069009010710> Removed **{0}** role from **{1}**".format(role.name, member.name))
            else:
                await member.add_roles(role)
                await ctx.send("<:cactusdone:580753069009010710> Added **{0}** role to **{1}**".format(role.name, member.name))
        else:
            await ctx.send("You need **Manage Roles** permission to use this!")
    else:
        await ctx.send("You are banned from the bot!")

@client.command()
async def botban(ctx, user:discord.Member):
    if ctx.author.id in devs:
        ban = fb.put("cactus/banned", str(user.id), str(user))
        await ctx.send(f"Banned **{user.name}** from the bot!")
    else:
        ctx.send("hehe nice try.")

@client.command()
async def unbotban(ctx, user:discord.Member):
    if ctx.author.id in devs:
        ban = fb.delete("cactus/banned", str(user.id), str(user))
        await ctx.send(f"Unbanned **{user.name}** from the bot!")
    else:
        await ctx.send("hehe nice try.")

@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def beg(ctx):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        r = random.randint(1, 100)
        getcoin = fb.get(f"cactus/profile/{ctx.author.id}", "Coins")
        coin = fb.put(f"cactus/profile/{ctx.author.id}", "Coins", int(getcoin) + r)
        await ctx.send(f"Hey, come here and take this `{r}` <:spike:594243507200458765> {ctx.author.name}.")
        guild = client.get_guild(580748210142838794)
        channel = client.get_channel(594143775983534083)
        await channel.send(f"**{ctx.author.name}** used **c!beg command** today at `{ctx.message.created_at}` in **{ctx.guild.name}/#{ctx.channel.name}**")
    else:
        await ctx.send("You are banned from the bot!")

@client.command(aliases=["balance", "bank"])
async def bal(ctx, user: discord.Member=None):
    if user is None:
        getcoins = fb.get(f"cactus/profile/{ctx.author.id}", "Coins")
        await ctx.send(f"You got `{int(getcoins)}` <:spike:594243507200458765> {ctx.author.name}!")
    else:
        getcoins = fb.get(f"cactus/profile/{user.id}", "Coins")
        await ctx.send(f"{user.name} has `{int(getcoins)}` <:spike:594243507200458765>!")

@client.command()
async def adduser(ctx, user: discord.Member):
    if ctx.author.id in devs:
        desc = fb.put(f"cactus/profile/{user.id}", "Description", str("default description"))
        name = fb.put(f"cactus/profile/{user.id}", "Name", str(user.name))
        coins = fb.put(f"cactus/profile/{user.id}", "Coins", 0)
        getlvl = fb.put(f"cactus/profile/{user.id}", "Lvl", 0)
        getexp = fb.put(f"cactus/profile/{user.id}", "Exp", 0)
        await ctx.send(f"**{user.name}** was successfully added to database!")
    else:
        await ctx.send("You dont have permission to do this!")

@client.command(aliases=["give"])
@commands.cooldown(1, 30, commands.BucketType.user)
async def share(ctx, user: discord.Member, number:int):
    getcoin = fb.get(f"cactus/profile/{ctx.author.id}", "Coins")
    getcoinuser = fb.get(f"cactus/profile/{user.id}", "Coins")
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        if number > int(getcoin):
            return await ctx.send("You don't have that much Spikes!")
        if number < 0:
            return await ctx.send("You can't give minus Spikes!")
        if ctx.author.id == user.id:
            return await ctx.send("You can't give yourself money...")
        else:
            coin = fb.put(f"cactus/profile/{ctx.author.id}", "Coins", int(getcoin) - number)
            coinuser = fb.put(f"cactus/profile/{user.id}", "Coins", int(getcoinuser) + number)
            await ctx.send(f"You gave `{number}` <:spike:594243507200458765> to {user.name}!")
            await user.send(f"{ctx.author.name} gave you `{number}` <:spike:594243507200458765>!")
    else:
        await ctx.send("You are banned from the bot!")

@client.command()
async def coin(ctx, user: discord.Member, number:int):
    getcoinuser = fb.get(f"cactus/profile/{user.id}", "Coins")
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        if ctx.author.id in devs:
            if number < 0:
                return await ctx.send("You can't give minus Cactus Coins!")
            else:
                coinuser = fb.put(f"cactus/profile/{user.id}", "Coins", int(getcoinuser) + number)
                await ctx.send(f"You gave `{number}` <:spike:594243507200458765> to {user.name}!")
                await user.send(f"{ctx.author.name} gave you `{number}` <:spike:594243507200458765>!")
    else:
        await ctx.send("You are banned from the bot!")

@client.command()
async def take(ctx, user: discord.Member, number:int):
    getcoinuser = fb.get(f"cactus/profile/{user.id}", "Coins")
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        if ctx.author.id in devs:
            if number < 0:
                return await ctx.send("You can't take minus Spikes!")
            else:
                coinuser = fb.put(f"cactus/profile/{user.id}", "Coins", int(getcoinuser) - number)
                await ctx.send(f"You took away `{number}` <:spike:594243507200458765> from {user.name}!")
                await user.send(f"{ctx.author.name} took away your `{number}` <:spike:594243507200458765>!")
    else:
        await ctx.send("You are banned from the bot!")

@client.command()
async def spikeritual(ctx, number:int):
    getcoin = fb.get(f"cactus/profile/{ctx.author.id}", "Coins")
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        if number > int(getcoin):
            return await ctx.send("You don't have that much Spikes!")
        elif random.randint(1, 5) == 1:
            await ctx.send("You are doing the spike ritual to get twice amount you specified...")
            await ctx.send("...")
            await asyncio.sleep(5)
            ritual = fb.put(f"cactus/profile/{ctx.author.id}", "Coins", int(getcoin) + (number * 2))
            await ctx.send(f"The ritual was a success!You were given {number * 2} for your effort")
        else:
            await ctx.send("You are doing the spike ritual to get twice amount you specified...")
            await ctx.send("...")
            await asyncio.sleep(5)
            ritual = fb.put(f"cactus/profile/{ctx.author.id}", "Coins", int(getcoin) - number)
            await ctx.send(f"The ritual failed.You lost your {number} <:spike:594243507200458765>!")
            if random.randint(1, 100) == 1:
                await ctx.send("`THE HOUSE ALWAYS WINS...`")
    else:
        await ctx.send("You are banned from the bot!")

@client.command()
async def messages(ctx):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        messagecount = fb.get("cactus/Count", "messagecountglobal")
        await ctx.send(f"I started counting messages on 6/29/2019 at 7:25 GMT+2.There are currently `{messagecount}` messages counted!")
    else:
        await ctx.send("You are banned from the bot!")

@client.command()
async def joke(ctx, *, arg=None):
    if arg == "chucknorris" or arg == "chuck norris":
        await ctx.send(chucknorris())
    elif arg == "dadjoke":
        await ctx.send(icanhazdad())
    elif arg == "geek":
        await ctx.send(geek())
    elif arg == "icndb":
        await ctx.send(icndb())
    else:
        await ctx.send(choice([geek, icanhazdad, chucknorris, icndb])())


@client.command()
async def gulag(ctx, user: discord.Member):
    if ctx.guild.id == 529499552177192980:
        banned = fb.get("cactus/banned", str(ctx.author.id))
        if banned is None:
            if ctx.author == client.user:
                return
            if ctx.message.author.guild_permissions.manage_roles or ctx.message.author.id in devs:
                await user.edit(roles=[])
                role = ctx.guild.get_role(574722256878567441)
                await user.add_roles(role)
                ticket = await ctx.send(file=discord.File('TicketGulag.png'))
                await asyncio.sleep(3)
                await ticket.delete()
                await user.send(f"You were gulaged in {ctx.guild.name}")
            else:
                await ctx.send("You dont have permission to gulag people!")
        else:
            await ctx.send("You are banned from the bot!")

@client.command()
async def ungulag(ctx, user: discord.Member):
    if ctx.guild.id == 529499552177192980:
        banned = fb.get("cactus/banned", str(ctx.author.id))
        if banned is None:
            if ctx.author == client.user:
                return
            if ctx.message.author.guild_permissions.manage_roles or ctx.message.author.id in devs:
                remvrole = ctx.guild.get_role(574722256878567441)
                await user.remove_roles(remvrole)
                adrole = ctx.guild.get_role(553005916480471083)
                await user.add_roles(adrole)
                await user.send(f"You were ungulaged in {ctx.guild.name}")
            else:
                await ctx.send("You dont have permission to ungulag people!")
        else:
            await ctx.send("You are banned from the bot!")

@client.command()
async def spamping(ctx, user: discord.Member=None):
    if ctx.author.id in devs:
        if user is None:
            await ctx.send("Specify user!")
        else:
            while 3 > 2:
                await ctx.send(user.mention)

@client.command(aliases=["toplist"])
async def top(ctx):
    banned = fb.get("cactus/banned", str(ctx.author.id))
    if banned is None:
        user_dic = fb.get("cactus/profile/", None)
        users = []
        for id, u in user_dic.items():
            user = u
            user["id"] = id
            for user in users:
                users.append(user)
                embedtop = discord.Embed(color=discord.Color.green())
                embedtop.add_field(name="Top Cactus Bot Users", value="{0}(`{1}`)      {2} <:spike:594243507200458765>\n".format(user["Name"], user["id"], user["Coins"]))
                await ctx.send(embed=embedtop)
    else:
        await ctx.send("You are banned from the bot!")

client.run("NDg4MzI3MDk1MDQzMjI3NjU4.XOLJaA.6zpenwjh_GpcDNlGBavJdd1wx4I")
