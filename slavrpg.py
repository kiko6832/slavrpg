import discord
import asyncio
import time
import os
from discord.ext import commands
from discord import Game

Client = discord.client
client = commands.Bot(command_prefix = '.')
Clientdiscord = discord.Client()
client.remove_command('help')
@client.event
async def on_ready():
    await client.change_presence(game=Game(name='Solviet Union Anthem',type = 2))
    print("SlavRPG Bot | Python 3.6.5 -> ONLINE")
    print(f"Logged in as {client.user}")
@client.command()
async def help():
    embed = discord.Embed(
        title = 'SlavRPG Bot - Help',
        decription = 'Help',
        colour = discord.Colour.red()
        )
    embed.set_footer(text='SlavRPG Bot - GameKiller02BG - 2019')
    embed.add_field(name=':game_die:**Game**',value='**`.game`**', inline=False)
    embed.add_field(name=':gear:**Settings**',value='**`.settings`**', inline=False)
    embed.add_field(name=':thumbsup:**Vote**',value='**`.vote`**', inline=False)
    embed.add_field(name=':moneybag:**Donate**',value='**`.donate`**', inline=False)
    await client.say(embed=embed)
@client.command()
async def game():
    embed = discord.Embed(
        title = 'SlavRPG Bot - Game Help',
        decription = 'Help',
        colour = discord.Colour.green()
        )
    embed.set_footer(text='SlavRPG Bot - GameKiller02BG - 2019')
    embed.add_field(name=':up:**Ranks**',value='**`Shows RankUp costs`**', inline=False)
    await client.say(embed=embed)
@client.command()
async def vote():
    await client.say('`Vote link: `')
    
@client.command()
async def donate():
    await client.say('`Donate link: `')
        
@client.command()
async def settings():
    embed = discord.Embed(
        title = 'SlavRPG Bot - Settings',
        decription = 'Settings',
        colour = discord.Colour.blue()
        )
    embed.set_footer(text='SlavRPG Bot - GameKiller02BG - 2019')
    embed.add_field(name=':gear:**Soon!**',value='**`Soon!`**', inline=False)
    await client.say(embed=embed)

@client.event
async def on_message_delete(message):
    avtor = message.author
    content = message.content
    channel = message.channel
    await client.send_message(channel, '{} deleted a message. It was: \n**`{}`**'.format(avtor, content))

@client.event
async def on_message(message):
    channel = message.channel
    if message.content.startswith('.ping'):
        await client.send_message(channel, '**`Pong!`**')
client.run('NTM4NzY0NTM1OTk0MjUzMzQ4.Dy5cFw.nd6cwfdHPNoYUVGpBgI2TdsPakE')
