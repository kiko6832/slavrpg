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
async def status_task():
        while True:
                await client.change_presence(game=Game(name='the Solviet Union Anthem.',type = 2))
                await asyncio.sleep(10)
                await client.change_presence(game=Game(name='chess with Stalin.',type = 0))
                await asyncio.sleep(10)
                await client.change_presence(game=Game(name='.help',type = 0))
                await asyncio.sleep(10)
                await client.change_presence(game=Game(name='with '+ str(len(client.servers)) +' servers.',type = 0))
                await asyncio.sleep(10)

@client.event
async def on_ready():
        client.loop.create_task(status_task())
        print("SlavRPG Bot | Python 3.6.5 -> ONLINE")
        print(f"Logged in as {client.user}")
    
@client.event
async def on_message_delete(message):
        avtor = message.author
        content = message.content
        channel = message.channel
        await client.send_message(channel, '{} deleted a message. It was: \n**`{}`**'.format(avtor, content))
        await client.process_commands(message)

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
        embed.add_field(name=':call_me:**Random**',value='**`.random`**', inline=False)
        await client.say(embed=embed)
        
@client.command()
async def game():
        embed = discord.Embed(
        title = 'SlavRPG Bot - Game Help',
        decription = 'Game Help',
        colour = discord.Colour.green())
        embed.set_footer(text='SlavRPG Bot - GameKiller02BG - 2019')
        embed.add_field(name=':up:**Ranks**',value='**`Shows RankUp costs`**', inline=False)
        await client.say(embed=embed)
        
@client.command()
async def random():
        embed = discord.Embed(
        title = 'SlavRPG Bot - Random Help',
        decription = 'Random',
        colour = discord.Colour.green())
        embed.set_footer(text='SlavRPG Bot - GameKiller02BG - 2019')
        embed.add_field(name=':ping_pong:**Ping**',value='**`Replies Pong!`**', inline=False)
        embed.add_field(name=':middle_finger:**Ligma**',value='**`Surprise!`**', inline=False)
        await client.say(embed=embed)

@client.command()
async def settings():
        embed = discord.Embed(
        title = 'SlavRPG Bot - Settings',
        decription = 'Settings',
        colour = discord.Colour.blue())
        embed.set_footer(text='SlavRPG Bot - GameKiller02BG - 2019')
        embed.add_field(name=':gear:**Soon!**',value='**`Soon!`**', inline=False)
        await client.say(embed=embed)

@client.command(pass_context=True)
async def clear(ctx, amount=10):
        channel = ctx.message.channel
        messages = []
        async for message in client.logs_from(channel, limit=int(amount)+1):
                messages.append(message)
                await client.delete_messages(messages)
                await client.say((amount)+'Messages deleted')
                await client.say('If you want to delete the confirmation message type `.clearc`')

@client.command(pass_context=True)
async def clearc(ctx):
        channel = ctx.message.channel
        messages = []
        async for message in client.logs_from(channel, limit=int(1)):
                messages.append(message)
                await client.delete_messages(messages)
@client.command()
async def vote():
        await client.say('`Vote link: `')

@client.command()
async def ligma():
        await client.say('`Ligma Balls! `')

@client.command()
async def ping():
        await client.say('`Pong!`')

client.run('NTM4NzY0NTM1OTk0MjUzMzQ4.Dy5cFw.nd6cwfdHPNoYUVGpBgI2TdsPakE')
