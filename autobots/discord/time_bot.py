from discord.ext import commands
from time import sleep
from bot_tokens import BOT_TOKEN


bot = commands.Bot(command_prefix='!')

@bot.command(name='wait')
async def wait(ctx, time):
    sleep(int(time))
    await ctx.send("время Х наступило!")


bot.run(BOT_TOKEN)
