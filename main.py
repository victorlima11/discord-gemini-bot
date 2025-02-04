import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = "!"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

async def load_cogs():
    await bot.load_extension("src.cogs.gemini")

@bot.event
async def on_ready():
    print(f"{bot.user} is now online!")
    synced = await bot.tree.sync()  
    print(f"✅ {len(synced)} sync commmands!")
    await load_cogs()

bot.run(TOKEN)