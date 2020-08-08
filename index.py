import random
import time
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'db-')
client.load_extension("jishaku")
token = "your token here"

@client.event
async def on_ready():
    print('Logged in as {}!'.format(client.name))

@client.command(help = "Repeats what you say.")
async def echo(ctx,*,message):
    await ctx.send(message)

@client.command(help = "Flips a coin, heads or tails.")
async def coinflip(ctx, times: Int=1):
    flips=[]
    if times == 1:
        await ctx.send(random.choice(["Heads!", "Tails!"]))
    elif times >= 2:
        for i in range(times):
            flips.append(random.choice(['H','T']))
        await ctx.send("Flipped {} times and got {}".format(times,str(flips)))

@client.command(help = "Displays info about the bot.")
async def info(ctx):
    embedVar = discord.Embed(title="Info", description="Information for this simple Discord bot that I'm creating for my server.", color=0xffa200)
    embedVar.set_thumbnail(url="https://i.imgur.com/KiWIsp9.jpg")
    embedVar.add_field(name="Creator:", value="ゴKillerDuckゴ#8805", inline=False)
    embedVar.add_field(name="Purpose:", value="To learn about discord.py and python in general and have a fun bot for my discord", inline=False)
    await ctx.send(embed = embedVar)

@client.command(help = "Forces the bot to leave the server.")
async def leaveserver(ctx):
    if ctx.author.guild_permissions.manage_server:
        await ctx.guild.leave()
    else:
        await ctx.send("You need the manage server permission to do that!")

@client.command(help = "Gets the invite for the current server.")
async def invite(ctx):
    invite = await ctx.channel.create_invite()
    await ctx.send(invite)
    
##Thank you to ♿nizcomix#7532 for the code for the ping command here's his repo https://github.com/niztg/CyberTron5000
@client.command(help = "Checks the bot's ping.")
async def ping(ctx):
    websocket = round(client.latency * 1000, 3)
    start = time.perf_counter()
    embedVar3 = discord.Embed(title=f"**Pong!**", description=f"Websocket Latency: \n**{websocket}**")
    msg = await ctx.send(embed = embedVar3)
    end = time.perf_counter()
    duration = round((end - start) * 1000, 3)
    embedVar3.description += f"\nResponse Time: \n**{duration}**"
    await msg.edit(embed = embedVar3)
    

@client.event
async def on_message(message):
    if message.content == "kwhfibwuhvhwu":
        embedVar2 = discord.Embed(title="Congrats!", description="Congratulations on finding this easter egg! You only had to type 5 trillion words!", color=0x00ff2a)
        embedVar2.set_thumbnail(url="https://d1e3z2jco40k3v.cloudfront.net/-/media/mccormick-us/recipes/mccormick/t/800/two-toned-easter-eggs.jpg?vd=20200628T035528Z&hash=2BC177C2F5D80BEC1E1F3705BD8679BC")
        await message.channel.send(embed = embedVar2)
    await client.process_commands(message)

client.run(token)
