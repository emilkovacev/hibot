import discord
import dotenv
import os
import datetime

dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))

bot = discord.Bot()
hi_map = {}

@bot.event
async def on_ready():
    global startup_time
    startup_time = datetime.datetime.now()
    print(f"{bot.user} is connected!")


@bot.slash_command(name="hi")
async def hi(ctx):
    n = hi_map.get(ctx.author, 0) + 1
    hi_map[ctx.author] = n
    await ctx.respond(f"Hi {ctx.author.nick}! You said hi {n} times since startup at {startup_time}.")

bot.run(token)
