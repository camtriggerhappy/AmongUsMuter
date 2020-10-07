import discord
from Token import getToken # api key obsfuscation


class MyClient(discord.Client):

    def __init__(self,deadList):
        super().__init__()
        self.deadList:list = deadList
    async def on_ready(self):
        print("Bot has connected to server")

    async def on_message(self, message):
        if "~mute" in message.content:
            Channel = message.author.voice.channel
            if Channel is not None:
                Users = Channel.members
                for person in Users:
                    await person.edit(mute=True)

        elif "~unmute" in message.content:
            Channel = message.author.voice.channel
            if Channel is not None:
                Users = Channel.members
                for person in Users:
                    if person not in self.deadList:
                        await person.edit(mute=False)

        elif "~dead" in message.content:
            self.deadList.append(message.author)


        elif "~reset" in message.content:
            self.deadList.clear()



client = MyClient(deadList=[])
client.run(getToken())
