import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import datetime
import PIL
from PIL import Image, ImageDraw, ImageFont
import firebase
from firebase import firebase
import math
from random import choice
import requests
from io import BytesIO
import praw

#Client = discord.Client()
client = commands.Bot(command_prefix=".", activity=discord.Activity(name="fin burn in hell.", type=discord.ActivityType.watching))
client.remove_command("help")

@client.event
async def on_ready():
    print("fin should die!")

devs = [476770711562747905, 312915737398214657, 429213502813503488]

@client.event
async def on_raw_reaction_add(payload):
    react = payload.emoji
    guild = client.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    if payload.message_id == 612588849276780544:
        if str(react) == "<:fingay:612588248413372417>":
            role = guild.get_role(612412468160888833)
            await member.add_roles(role)

@client.event
async def on_raw_reaction_remove(payload):
    react = payload.emoji
    guild = client.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    if payload.message_id == 612588849276780544:
        if str(react) == "<:fingay:612588248413372417>":
            role = guild.get_role(612412468160888833)
            await member.remove_roles(role)

@client.event
async def on_message(message):
    if message.content.lower() == "fin":
        await message.channel.send("should die")
    if "dead dog" in message.content.lower():
        await message.channel.send("epic dog kill")
    await client.process_commands(message)

@client.command(name="dm", aliases=["directmessage", "directmsg", "dirmsg", "dirmessage"])
async def directmessage(ctx, user: discord.User, msg):
    await ctx.message.delete()
    await asyncio.sleep(len(msg) / 10)
    await user.send(msg)
    await ctx.message.channel.send("sent.")
    usr = client.get_user(476770711562747905)
    await usr.send("**" + ctx.message.author.name + ": **" + msg + " TO " + "***" + user.name + "***")

@client.command()
async def say(ctx, *, arg):
    if "@everyone" in ctx.message.content or "@here" in ctx.message.content or ctx.message.role_mentions != []:
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
        await ctx.send("<:fingay:612588248413372417>")
        await ctx.send(embed=embedtest)

embedfun = discord.Embed(
    title="<:fingay:612588248413372417> Fin Hater Bot",
    description="**All commands are:**",
    color=0x0da323
)

embedfun.add_field(name="say", value="says something.", inline=False)
embedfun.add_field(name="dm", value="dms someone.", inline=False)
embedfun.add_field(name="dogkill", value="epic dog kill.", inline=False)
embedfun.add_field(name="add", value="MATHS", inline=False)
embedfun.add_field(name="minus", value="MATHS", inline=False)
embedfun.add_field(name="square", value="MATHS", inline=False)
embedfun.add_field(name="askrap", value="you ask, rap answers.", inline=False)
embedfun.add_field(name="poll", value="creates a poll.", inline=False)
embedfun.add_field(name="ban", value="bans some nerd.", inline=False)
embedfun.add_field(name="role", value="adds/removes a role.", inline=False)
embedfun.add_field(name="spamping", value="spampings someone.", inline=False)

@client.group(name="help")
async def help(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(embed=embedfun)

@client.command()
async def dogkill(ctx):
    membr = random.choice(ctx.guild.members).name
    await ctx.send(membr + " should kill fin's dog")

@client.command(pass_context=True)
async def square(ctx, number):
    if len(number) > 10:
        await ctx.send('enter number less than 10 characters spam idiot')
    else:
        squared_value = int(number) * int(number)
        await ctx.send(str(number) + " squared is " + str(squared_value))

@client.command(aliases=['Add', 'ADD'])
async def add(ctx, left : int, right : int):
    await ctx.send(f"{left} + {right} = {left+right}")

@client.command(aliases=['Minus', 'MINUS', 'Subtract', 'subtract', 'SUBTRACT'])
async def minus(ctx, left : int, right : int):
    await ctx.send(f"{left} - {right} = {left-right}")

@client.command()
async def askrap(ctx, *, arg):
    rap = ["hi rap", "sphere!", "xd", "eggs!", "are you f retarded?", "make mech", "make mech...but less retarded this time", "ex pro", "nicolas cage is very pro", "liege cool and smart"]
    askrap = discord.Embed(color=ctx.message.author.top_role.color)
    askrap.add_field(name=ctx.message.author.name + ": " + arg, value="Rap: " + random.choice(rap))
    await ctx.send(embed=askrap)

@client.command(aliases=["pollstart", "startpoll"])
async def poll(ctx, *, arg):
    await ctx.message.delete()
    embedpoll = discord.Embed(title="{}'s Poll".format(ctx.author.name), description=arg, color=ctx.message.author.color)
    embedpoll.set_footer(text="Poll by {}".format(ctx.author.name), icon_url='{}'.format(ctx.author.avatar_url))
    msg = await ctx.send(embed=embedpoll)
    emojis = ["👍", "👎", 612588248413372417]
    for e in emojis:
        emoji = client.get_emoji(e)
        await msg.add_reaction(emoji)

@client.command()
async def ban(ctx, user: discord.Member, *, reason = "No Reason Provided"):
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
        await ctx.send("*says no permission to do this in nerd language*")


@client.command()
async def role(ctx, member: discord.Member, role: discord.Role):
    if ctx.message.author.guild_permissions.manage_roles or ctx.author.id in devs:
        if role in member.roles:
            await member.remove_roles(role)
            await ctx.send("Removed **{0}** role from **{1}**".format(role.name, member.name))
        else:
            await member.add_roles(role)
            await ctx.send("Added **{0}** role to **{1}**".format(role.name, member.name))
    else:
        await ctx.send("You need **Manage Roles** permission to use this!")

@client.command()
async def spamping(ctx, user: discord.Member=None):
    if ctx.author.id in devs:
        if user is None:
            await ctx.send("Specify user!")
        else:
            while 3 > 2:
                await ctx.send(user.mention)

client.run("NDg4MDA5MDUwMTUyMzcwMTc2.XVkhCQ.023euxRbMFW7zAYtXP47n6oWLbo")
