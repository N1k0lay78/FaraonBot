import discord
from googletrans import Translator


TOKEN = ""


class MyClient(discord.Client):
    async def on_ready(self):
        self.channels = {}
        self.chat_members = {}
        self.translator = Translator()
        self.load_channels()
        self.load_chat_members()
        print('READY')

    def load_channels(self):
        with open("channels.stg", "r") as f:
            for line in f.readlines():
                # no - no translate, au - auto translate mode, ru - translate to ru, es - translate to es
                self.channels[int(line.split()[0])] = line.split()[1]

    def load_chat_members(self):
        with open("users.stg", "r") as f:
            for line in f.readlines():
                # no - no translate, ru - to ru, es - to es
                self.chat_members[int(line.split()[0])] = line.split()[1]

    def add_chat_member(self, id):
        self.chat_members[id] = 'es'
        self.save_chat_member()

    def save_chat_member(self):
        with open("users.stg", 'w') as f:
            f.writelines(map(lambda x: f"{x[0]} {x[1]}\n", self.chat_members.items()))

    def add_channel(self, id):
        self.channels[id] = 'au'
        self.save_channel()

    def save_channel(self):
        with open("channels.stg", 'w') as f:
            f.writelines(map(lambda x: f"{x[0]} {x[1]}\n", self.channels.items()))

    async def on_message(self, message):
        if message.author.id not in self.chat_members:
            self.add_chat_member(message.author.id)
        if message.channel.id not in self.channels:
            self.add_channel(message.channel.id)
        # <@&1072787215140270160> - admin
        # check admin
        # any(map(lambda role: role.id == 1072787215140270160, message.author.roles))
        print(self.chat_members[message.author.id], self.channels[message.channel.id], message.content)
        if message.author.id != self.user.id:  # and message.channel.id not in [1087874636307517491, 1071141318862061598]:
            if message.author.id == 1128752754911887420:
                if "destroyed your 'Metal" in message.content or "destroyed your 'Tek" in message.content or "destroyed your 'Heavy" in message.content:
                    await message.reply(content="<@&1093083549915168832>, нас фобнули! ¡estamos bajo ataque!")
            if ((message.content.lower().count('j') == len(message.content) or message.content in [".", '/', '?', '&', ')', '(', "ok", "Ok", "OK", "ок", "Ок", "ОК"] or
                    message.content.startswith('https:'))):
                None
            elif message.content.startswith('.translate') and any(map(lambda role: role.id == 1072787215140270160, message.author.roles)):
                args = message.content.split()[1:]
                if len(args) == 1:
                    if args[0] in ['ru', 'en', 'es', 'no', 'au']:
                        self.channels[message.channel.id] = args[0]
                        self.save_channel()
                    else:
                        await message.reply(content='доступные языки: ru, en, es, no - не переводить, au - автоматический выбор языка\nidiomas disponibles: ru, en, es, no - no traducir, au - selección automática de idioma')
                elif len(args) == 2:
                    if args[0][2:-1].isdigit() and args[1] in ['ru', 'en', 'es', 'no']:
                        self.chat_members[int(args[0][2:-1])] = args[1]
                        self.save_chat_member()
                    else:
                        await message.reply(content='доступные языки: ru, en, es, no - не переводить\nidiomas disponibles: ru, en, es, no - no traducir')
            elif message.content.startswith('.help') and any(map(lambda role: role.id == 1072787215140270160, message.author.roles)):
                await message.reply(
                    content=""".translate @user lang
выбор языка пользователя
доступные языки: ru, en, es, no (не переводить)
selección de idioma del usuario
idiomas disponibles: ru, en, es, no (no traducir)

.translate lang
выбор языка канала
доступные языки: ru, en, es, no (не переводить), au (автоматический выбор языка)
selección de idioma del canal
idiomas disponibles: ru, en, es, no (no traducir), au (selección automática de idioma)""")
            elif self.channels[message.channel.id] == "au" and self.chat_members[message.author.id] != 'no':
                ans = self.translator.translate(message.content, dest=self.chat_members[message.author.id]).text
                await message.reply(content=ans)
            elif self.channels[message.channel.id] != "no":
                ans = self.translator.translate(message.content, dest=self.channels[message.channel.id]).text
                await message.reply(content=ans)


if __name__ == '__main__':
    intents = discord.Intents.default()
    intents.message_content = True
    bot = MyClient(intents=intents)
    bot.run(TOKEN)
