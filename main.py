import discord
from googletrans import Translator


TOKEN = ""


class MyClient(discord.Client):
    async def on_ready(self):
        self.translator = Translator()
        print('READY')

    async def on_message(self, message):
        print(message.author.id, message.author.name, message.content, message.channel.id)
        if message.author.id != self.user.id and message.channel.id not in [1087874636307517491, 1071141318862061598]:
            if message.author.id == 1087790399503990785:
                if "destroyed your" in message.content:
                    await message.reply(content="<@925109931122786395>, <@342956494389641216>, <@430382528231112705>, <@829552769009844254>, <@670683687897006103>, <@390963619418079233>, нас фобнули! ¡estamos bajo ataque!")
            else:
                if ((message.content.count('j') == len(message.content) or message.content in [".", '/', '?', '&', ')', '('] or
                        message.content.startswith('https:'))):
                    None
                elif message.channel.id != 1067359358452777020:
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
