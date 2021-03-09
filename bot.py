import discord
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    @classmethod
    async def on_message(self, message):
        m = message.content.lower().split(' ')
        me = message.content.lower()
        if me.find('i love you hibot') != -1:
            await message.channel.send(f'<3 {client.user}')
        if (me.find('amogus') != -1 or me.find('among us') != -1) and message.author != client.user:
            await message.channel.send(f'amogus II: **Upon Us**')
        elif ('hi' in m or 'hello' in m or 'heya' in m) and message.author != client.user:
            await message.channel.send(f'hi {message.author.nick}')
        elif (me.find('good morning gamers') != -1) and message.author != client.user:
            await message.channel.send(f'good morning gamer {message.author.nick}')
        elif (me.find('good morning') != -1) and message.author != client.user:
            await message.channel.send(f'good morning {message.author.nick}')
        elif ('goodnight' in m or 'gn' in m) and message.author != client.user:
            await message.channel.send(f'goodnight {message.author.nick}')


client = MyClient()
client.run(TOKEN)
