import discord
from dotenv import load_dotenv
import os
import re

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    @classmethod
    async def on_message(self, message):
        mi = message.content.lower().split(' ')
        if message.author.bot and message.author != client.user:
            await message.channel.send(f'<3 {message.author.nick} is kinda sus :eyes:')
        elif ('amogus' in mi) and message.author != client.user:
            await message.channel.send(f'amogus II: **Upon Us**')
        elif ('hi' in mi or 'hello' in mi or 'hey' in mi or 'shalom' in mi) and message.author != client.user:
            await message.channel.send(f'hi {message.author.nick}')
        elif ('goodnight' in mi or 'gn' in mi) and message.author != client.user:
            await message.channel.send(f'goodnight {message.author.nick}')


client = MyClient()
client.run(TOKEN)
