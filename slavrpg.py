import discord
import asyncio
import time
import os
from discord.ext import commands
from discord import Game

Client = discord.client
client = commands.Bot(command_prefix = '.')
Clientdiscord = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(game=Game(name='HardBass',type = 2))
    print("SlavRPG Bot | Python 3.6.5 -> ONLINE")

        
client.run('NTM4NzY0NTM1OTk0MjUzMzQ4.Dy5cFw.nd6cwfdHPNoYUVGpBgI2TdsPakE')
