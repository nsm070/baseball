import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Cog 자동 로드
async def load_cogs():
    for filename in os.listdir("./cog"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cog.{filename[:-3]}")

@bot.event
async def on_ready():
    print(f"{bot.user} 봇 실행 완료!")

async def main():
    async with bot:
        await load_cogs()
        await bot.start("여기에_디스코드봇_토큰")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
