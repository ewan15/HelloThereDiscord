# bot.py
import asyncio
import os

import discord
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env_token')
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    # await client.get_channel(759437628729720855).send('Hello There!')bot

connected = False


def loada():
    return connected


def loada2(state):
    global connected
    connected = state


@client.event
async def on_voice_state_update(member, prev, cur):
    if str(member) == 'Obi-Wan Kenobi#7773':
        return
    try:
        if prev.channel == cur.channel:
            return
        print(f"Joining: {member.voice.channel}")
        voice = await member.voice.channel.connect()
        voice.play(discord.FFmpegPCMAudio('obi-wan-hello-there.mp3'))
        await asyncio.sleep(2.5)
        await voice.disconnect()
    except Exception as e:
        print(e)


client.run(TOKEN)
