import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import wikipedia
import datetime
import PIL
import sqlite3
import terrabot
from terrabot import TerraBot
from terrabot.events import Events

#Client = discord.Client()
client = commands.Bot(command_prefix=commands.when_mentioned_or("c!"), activity=discord.Activity(name="you xdddddddddd", type=discord.ActivityType.watching))
client.remove_command("help")

@client.event
async def on_ready():
    print("spiker prepared!")

devs = [476770711562747905]

@client.event
async def on_reaction_add(reaction):
    if reaction.message.id == 582149346737258501:
        role = reaction.guild.get_role(server.roles, id=581442708942487563)
        await member.add_roles(reaction.message.author, role)


@client.event
async def on_message(message):
    if message.content.lower() == "hello there" and random.randint(1, 1000) == 1:
        await message.channel.send("General Kenobi")
        await message.channel.send("You are a bold one")
        m = await message.channel.send(file=discord.File('General Kenobi.png'))
        await asyncio.sleep(10)
        await m.delete()
    if "cactus" in message.content.lower() and "is" and "should" and "?" in message.content:
        messages = ["Yes.", "No.", "Sure.", "No...", "Yeah sure...", "Maybe"]
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
        await message.channel.send("durk idot big nub")
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
        if message.author == client.user:
            return
        else:
            r = message.content
        embedreddit = discord.Embed(
            title="<:reddit:581088652759662592> Here's your subreddit!",
            color=0xed6a07
        )

        embedreddit.add_field(name="https://www.reddit.com/" + r, value="epic subreddit", inline=False)
        await message.channel.send(embed=embedreddit)
    if message.content.lower() == "hi rap" and random.randint(1, 4) == 1:
        if message.author == client.user:
            return
        else:
            await message.channel.send("hi rap")
    if random.randint(1, 1000) == 1:
        await message.channel.send("die")
        await message.channel.send(file=discord.File('santa.PNG'))
    await client.process_commands(message)

@client.command()
async def kill(ctx):
    if ctx.author.id in devs:
        messages = ["***Literally Dying...***", "***__Liege North touched me so im dying__***", "***being snapped from the universe...***"]
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
    else:
        await ctx.send("<:cactusfailed:580834469842386975> What an idiot tried to use this command knowing its developer only!")

@client.command(pass_context = True)
async def ping(ctx):
    async with ctx.typing():
        t1 = ctx.message.created_at
        m = await ctx.send('**Pong!**')
        time = (m.created_at - t1).total_seconds() * 1000
        await m.edit(content='**Pong! Took: {}ms**'.format(int(time)))

@client.command()
async def say(ctx, *, arg):
    async with ctx.typing():
        if "@everyone" in ctx.message.content or "@here" in ctx.message.content or ctx.message.role_mentions != [] or ctx.author.id == 401044899568287744:
            await ctx.send("no no!")
            await ctx.message.delete()
        else:
            await ctx.send(arg)
            await ctx.message.delete()

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

embedfun.add_field(name="ping", value="shows you your ping", inline=False)
embedfun.add_field(name="say <message>", value="says the message you want", inline=False)
embedfun.add_field(name="freerobux", value="gives free robux legit way", inline=False)
embedfun.add_field(name="8ball <question> [no prefix]", value="tells you what to do", inline=False)
embedfun.add_field(name="servers", value="shows servers you idots invited him in    ᶜʳᵉᵈᶦᵗˢ ᵗᵒ ʳᵃᵖ", inline=False)
embedfun.add_field(name="hackrbx", value="hacks roblox", inline=False)
embedfun.add_field(name="snap", value="perfectly balanced as all things should be", inline=False)
embedfun.add_field(name="murder <message>", value="kills someone you don't like", inline=False)
embedfun.add_field(name="wiki <search>", value="searches wikipedia", inline=False)
embedfun.add_field(name="gay", value="somebody is gay here", inline=False)
embedfun.add_field(name="r/<subreddit> [no prefix]", value="shows you subreddit you want", inline=False)
embedfun.add_field(name="remindme <time period in seconds> <reminder>", value="reminds you of something", inline=False)
embedfun.add_field(name="howgay <member>", value="tells you how gay you are", inline=False)
embedfun.add_field(name="<:greg:581569386461003787> howgreg <member>", value="shows you how shit you ar...i mean how greg you are!", inline=False)
embedfun.add_field(name="askrap <question>", value="why ask 8ball when u can ask rap?", inline=False)
embedfun.add_field(name="help", value="shows this message", inline=False)

@client.group(name="helpfun")
@commands.cooldown(1, 60, commands.BucketType.user)
async def helpfun(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(embed=embedfun)

embedfun2 = discord.Embed(
    title="<:cactusbot:581412557152190464> CactusBot",
    description="**All of fun commands page 2 are:**",
    url="https://cdn.discordapp.com/attachments/580784963272704020/581414254029307904/sm_5aaa3579e4d62.png",
    color=0x0da323
)

embedfun2.add_field(name="rps <rock, paper or scissors>", value="play rock paper scissors with the bot", inline=False)
embedfun2.add_field(name="wikidonate", value="donate to wikipedia", inline=False)

@client.command(aliases=["helpfunpage2", "helpfun page 2"])
@commands.cooldown(1, 60, commands.BucketType.user)
async def helpfun2(ctx):
    await ctx.send(embed=embedfun2)

embednerd = discord.Embed(
    title="<:cactusbot:581412557152190464> CactusBot",
    description="**All of ~~nerd~~ math commands are:**",
    url="https://cdn.discordapp.com/attachments/580784963272704020/581414254029307904/sm_5aaa3579e4d62.png",
    color=0x4e8ef4
)

embednerd.add_field(name="add <number 1> <number 2>", value="adds 1 number to other one", inline=False)
embednerd.add_field(name="minus <number 1> <number 2>", value="takes 1 number from other one", inline=False)
embednerd.add_field(name="square <number>", value="squares the number", inline=False)
embednerd.add_field(name="helpmath", value="shows this message", inline=False)


@client.command(name="helpmath", aliases=["helpnerd", "helpmatt"])
@commands.cooldown(1, 60, commands.BucketType.user)
async def helpmath(ctx):
    async with ctx.typing():
        await ctx.send(embed=embednerd)

embedmoderation = discord.Embed(
    title="<:cactusbot:581412557152190464> CactusBot",
    description="**All of moderation commands are:**",
    url="https://cdn.discordapp.com/attachments/580784963272704020/581414254029307904/sm_5aaa3579e4d62.png",
    color=0xdd0f0f
)

embedmoderation.add_field(name="clear <amount>", value="purges the amount of messages you specify(plus self message)", inline=False)
embedmoderation.add_field(name="info <member>", value="tells you everything about the user", inline=False)
embedmoderation.add_field(name="serverinfo", value="shows you info about the server", inline=False)
embedmoderation.add_field(name="helpmoderation", value="shows this message", inline=False)


@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def helpmoderation(ctx):
    async with ctx.typing():
        await ctx.send(embed=embedmoderation)

@client.command()
async def clear(ctx, *, number:int=None):
    if ctx.message.author.guild_permissions.manage_messages or ctx.author.id == 476770711562747905:
            if number is None:
                 await ctx.message.channel.purge(limit=1)
            else:
                deleted = await ctx.message.channel.purge(limit=number)
                clear = await ctx.send("<:cactusdone:580753069009010710> spiked those messages **epically**")
                await asyncio.sleep(5)
                await clear.delete()
    else:
        await ctx.send("<:cactusfailed:580834469842386975> you dont have permission for this...and that's gay!")

@client.command(name="servers", aliases=["guilds"])
@commands.cooldown(1, 60, commands.BucketType.user)
async def servers(ctx):
        msg = "**some shitos invited me in**\n"
        for server in client.guilds:
            if "@everyone" in server.name.lower() or "@here" in server.name.lower():
                msg += "{0}\n".format(server.id)
            else:
                msg += "{0}(`{1}`)\n".format(server.name, server.id)

        await ctx.send(msg)

@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def hackrbx(ctx):
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

@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def snap(ctx):
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

@client.command(name ="murder", aliases=["die"] )
async def murder(ctx, *, arg):
    async with ctx.typing():
        if "@everyone" in ctx.message.content or "@here" in ctx.message.content or ctx.message.role_mentions != []:
            await ctx.send("no no!")
            await ctx.message.delete()
        else:
            await ctx.send("<:cactusdone:580753069009010710> " + arg + " was murdered by " + ctx.author.name)

@client.command(name="invite", aliases=["inv"])
async def invite(ctx, server_id):
    if ctx.author.id in devs:
        server = client.get_guild(int(server_id))
        invite = await server.text_channels[0].create_invite(max_age=60, max_uses=1)
        await ctx.send("{0}".format(invite.url))
    else:
        ctx.send("no idot,no invite for u")

@client.command(name="wiki", aliases=["wikipedia"] )
async def wiki(ctx, arg1, arg2: int = 2048):
    async with ctx.typing():
        try:
            page = wikipedia.page(arg1)
            wiki = discord.Embed(title="**{0}**".format(page.title), url=page.url, description=page.content[:arg2], color=0xffffff)
            await ctx.send(embed=wiki)
        except Exception as error:
            await ctx.send('{}'.format(error))

@client.command()
async def gay(ctx):
    async with ctx.typing():
        membr = random.choice(ctx.guild.members).name
        await ctx.send(membr + " is gay")

@client.command(name="remindme", aliases=["reminder", "setreminder"])
async def rmd(ctx, sec: int, arg):
    if sec > 3600:
        counter = 3600
    else:
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

@client.command(aliases=["howgay"])
async def howmuchgay(ctx, *, user: discord.Member = None):
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

@client.command(aliases=["howgregur"])
async def howgreg(ctx, *, user: discord.Member = None):
    async with ctx.typing():
        if user is None:
            user = ctx.author
        random.seed()
        r = random.randint(1, 100)
        greg = r / 1.17
        await ctx.send(f"<:greg:581569386461003787> **{user.name}** is `{greg:.2f}%` greg!")

@client.command()
@commands.has_any_role("Admin", "Administator", "Mod", "Moderator", "mod", "moderator", "admin", "administator", 476770711562747905)
async def mute(ctx, member: discord.Member):
        await member.add_roles(member.server.roles, name="Muted")
        embedmute=discord.Embed(title="<:cactusdone:580753069009010710> mute hammer used!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xa6f409)
        await ctx.send(embed=embedmute)

@client.command()
async def info(ctx, user: discord.Member):
    async with ctx.typing():
        embedinfo = discord.Embed(title="{}'s user-info".format(user.name), description='epic info!!!11', color=ctx.message.author.color)
        embedinfo.add_field(name='Name', value='{}'.format(user.name))
        embedinfo.add_field(name='ID', value='{}'.format(user.id), inline=True)
        embedinfo.add_field(name='Status', value='{}'.format(user.status), inline=True)
        embedinfo.add_field(name='Highest Role', value='<@&{}>'.format(user.top_role.id), inline=True)
        embedinfo.add_field(name='Joined at', value='{:%d/%h/%y at %H:%M}'.format(user.joined_at), inline=True)
        embedinfo.add_field(name='Created at', value='{:%d/%h/%y at %H:%M}'.format(user.created_at), inline=True)
        embedinfo.add_field(name='Discriminator/Tag', value='{}'.format(user.discriminator), inline=True)
        embedinfo.add_field(name='Default avatar', value="{}".format(user.default_avatar_url))
        embedinfo.set_footer(text="{}'s epic Info".format(user.name), icon_url='{}'.format(user.avatar_url))
        embedinfo.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embedinfo)

@client.command()
async def serverinfo(ctx):
    try:
        embedserver = discord.Embed(title="{}'s info".format(ctx.message.guild.name), description="epic server i see", color=ctx.message.author.color)
        embedserver.add_field(name="Name", value="**{}**".format(ctx.message.guild.name))
        embedserver.add_field(name="Server ID", value="`{}`".format(ctx.message.guild.id))
        embedserver.add_field(name="Members", value="`{0}`".format(ctx.guild.member_count))
        embedserver.add_field(name="Roles", value='{}'.format(len(ctx.message.guild.roles)))
        embedserver.set_thumbnail(url=ctx.message.guild.icon_url)
        embedserver.set_footer(text="Requested by idot called {}".format(ctx.message.author.name) + "#{}".format(ctx.message.author.discriminator), icon_url='{}'.format(ctx.message.author.avatar_url))
        await ctx.send(embed=embedserver)
    except Exception as error:
        await ctx.send('{}'.format(error))

@client.command(pass_context=True)
async def square(ctx, number):
    if len(number) > 10:
        await ctx.send('enter number less than 10 characters spam idot')
    else:
        squared_value = int(number) * int(number)
        await ctx.send(str(number) + " squared is " + str(squared_value))

@client.command(aliases=['Add', 'ADD'])
async def add(ctx, left : int, right : int):
    await ctx.send(left + right)

@client.command(aliases=['Minus', 'MINUS', 'Subtract', 'subtract', 'SUBTRACT'])
async def minus(ctx, left : int, right : int):
    await ctx.send(left - right)

@client.command(pass_context=True)
async def help(ctx):
    try:
        Help = discord.Embed(title="<:cactusbot:581412557152190464> Here are all categories for help commands", description="more commands being added every day!", color=0x0072ff)
        Help.add_field(name='Currency Commands', value='`c!helpcurrency`')
        Help.add_field(name='Fun Commands', value='`c!helpfun`')
        Help.add_field(name='Math Commands', value='`c!helpmath`')
        Help.add_field(name='Moderation Commands', value='`c!helpmoderation`')
        await ctx.send(embed=Help)
    except Exception as error:
        await ctx.send('{}'.format(error))

@client.command()
async def helpcurrency(ctx):
    await ctx.send("this command is work in `pro`gress")

@client.command()
async def askrap(ctx, arg):
    rap = ["sphere!", "xd", "eggs!", "are you f retarded?", "make mech", "make mech...but less retarded this time", "ex pro"]
    askrap = discord.Embed(color=ctx.message.author.top_role.color)
    askrap.add_field(name=ctx.message.author.name + ": " + arg, value="Rap: " + random.choice(rap))
    await ctx.send(embed=askrap)

@client.group(name="rps")
async def rps(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send("say rock/paper/scissors nub")

@rps.command(name="rock", aliases=["paper", "scissors", ":hand_splayed:", ":v:", ":fist:"])
async def rock(ctx):
    answer = [":v:", ":fist:", ":hand_splayed:"]
    await ctx.send(random.choice(answer))

@client.command(aliases=["wikidon"])
async def wikidonate(ctx):
    await ctx.send("donate wikipedia to feel good")
    await ctx.send("`donation page link will be sent in 10 seconds in meanwhile DIE`")
    await asyncio.sleep(10)
    await ctx.send("https://donate.wikimedia.org/wiki/Special:LandingPage")

client.run("NDg4MzI3MDk1MDQzMjI3NjU4.XOLJaA.6zpenwjh_GpcDNlGBavJdd1wx4I")
