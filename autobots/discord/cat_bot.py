import discord
from bot_tokens import BOT_TOKEN

class qBot(discord.Client):
    async def on_ready(self):
        print("Подключился и готов показать котика!")

    async def on_message(self, msg):
        if msg.author == self.user:
            return
        if "кот" in msg.content.lower():
            with open("cat.jpg", "rb") as f:
                pic = discord.File(f)
                await msg.channel.send(file=pic)
        elif "собака" in msg.content.lower():
            with open("dog.jpg", "rb") as f:
                pic = discord.File(f)
                await msg.channel.send(file=pic)
            
client = qBot()
client.run(BOT_TOKEN)