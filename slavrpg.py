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
#@client.event
#async def on_message_delete(message):
#        avtor = message.author
#        content = message.content
#        channel = message.channel
#        await client.send_message(channel, '{} deleted a message. It was: \n**`{}`**'.format(avtor, content))
#        await client.process_commands(message)
@client.command()
async def help():
        embed = discord.Embed(
        title = 'SlavRPG Bot - Help',
        decription = 'Help',
        colour = discord.Colour.red()
        )
        embed.set_footer(text='SlavRPG Bot - GameKiller02BG - 2019')
        embed.add_field(name=':game_die:**Game**',value='**`.game`**', inline=True)
        embed.add_field(name=':gear:**Settings**',value='**`.settings`**', inline=True)
        embed.add_field(name=':thumbsup:**Vote**',value='**`.vote`**', inline=True)
        embed.add_field(name=':call_me:**Random**',value='**`.random`**', inline=True)
        await client.say(embed=embed)
@client.command()
async def game():
        embed = discord.Embed(
        title = 'SlavRPG Bot - Game Help',
        decription = 'Game Help',
        colour = discord.Colour.green())
        embed.set_footer(text='SlavRPG Bot - GameKiller02BG - 2019')
        embed.add_field(name=':up:**Ranks**',value='**`Shows RankUp costs`**', inline=True)
        await client.say(embed=embed)
@client.command()
async def random():
        embed = discord.Embed(
        title = 'SlavRPG Bot - Random Help',
        decription = 'Random',
        colour = discord.Colour.green())
        embed.set_footer(text='SlavRPG Bot - GameKiller02BG - 2019')
        embed.add_field(name=':ping_pong:**Ping**',value='**`Replies Pong!`**', inline=True)
        embed.add_field(name=':middle_finger:**Ligma**',value='**`Surprise!`**', inline=True)
        embed.add_field(name=':speaking_head:**Clear (amount)**',value='**`Clears the choosen amount of messages.`**', inline=False)
        embed.add_field(name=':envelope:**Am (@user#1234) (message)**',value='**`Sends anonimous message to choosen user`**', inline=False)
        await client.say(embed=embed)
@client.command()
async def settings():
        embed = discord.Embed(
        title = 'SlavRPG Bot - Settings',
        decription = 'Settings',
        colour = discord.Colour.blue())
        embed.set_footer(text='SlavRPG BOT - GameKiller02BG - 2019')
        embed.add_field(name=':gear:Soon!',value='Soon!', inline=True)
        await client.say(embed=embed)
@client.command()
async def vote():
        await client.say('```Vote link: ```')
@client.command()
async def ligma():
        await client.say('```Ligma Balls!```')
@client.command()
async def ping():
        await client.say('```Pong!```')
@client.command(pass_context=True)
async def clear(ctx, amount=100):
        channel = ctx.message.channel
        messages = []
        async for message in client.logs_from(channel, limit=int(amount)+1):
                        messages.append(message)
        await client.delete_messages(messages)
        await client.say('```%s Messages deleted!```'%amount)
@client.command(pass_context=True)
async def am(ctx, member: discord.Member, *msg):
    await client.send_message(member, '```Anonimous user sent you a message```')
    await client.send_message(member, " ".join(msg[0:]))
    await client.say("Anonimous message has been sent")
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit = int(2)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('%s Messages deleted' %(amount))
@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()
client.run('NTM4NzY0NTM1OTk0MjUzMzQ4.XEyRkw.b_PUoWFZ7FqEmUB5IZmOZLK57w8')
