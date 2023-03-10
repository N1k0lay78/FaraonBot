import discord
from googletrans import Translator


TOKEN = ""


class MyClient(discord.Client):
    async def on_ready(self):
        self.translator = Translator()
        print('READY')

    async def on_message(self, message):
        if message.author.id != self.user.id:
            if message.channel.id != 1067359358452777020:
                if message.author.name in ["Reben", "yaimel", "Ye Cuba", "-SKT-Thomas", "Dx_WITHEFIRE_xD"]:
                    ans = self.translator.translate(message.content, dest="ru").text
                    await message.reply(content=ans)
                else:
                    ans = self.translator.translate(message.content, dest="es").text
                    await message.reply(content=ans)
            else:
                if self.translator.detect(message.content).lang == 'ru':
                    ans = self.translator.translate(message.content, dest="es").text
                    await message.reply(content=ans)
                else:
                    ans = self.translator.translate(message.content, dest="ru").text
                    await message.reply(content=ans)


if __name__ == '__main__':
    intents = discord.Intents.default()
    intents.message_content = True
    bot = MyClient(intents=intents)
    bot.run(TOKEN)
