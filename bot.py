import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(f'{client.user} established connection')
    print(f'established {guild.name} connection with id {guild.id}')
    channel = client.get_channel(973023362655854602)
    await channel.send(f'channel {channel.name} with id {channel.id}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'fuck you':
        responses = ['fuck you too', 'your mom is gay', 'eat shit',
                     'shut up headass', 'u have no friends', 'die in a hole']
        response = random.choice(responses)
        await message.channel.send(response)


client.run(TOKEN)
