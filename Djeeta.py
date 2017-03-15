import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Djeeta is now online!')
    print("Username:",client.user.name)
    print("ID:", client.user.id)
    print("")

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

    elif message.content.startswith('!google'):
        print(message.content)
        string = message.content.split()
        string = string[1:]
        print(string)
        if len(string) == 1:
            returnval = "https://www.google.com/#safe=off&q=" + string[0] + "&*"
            print(returnval)
            await client.send_message(message.channel, returnval)
        else:
            returnval = ""
            for i in string:
                returnval += i
                if string.index(i) != len(string)-1:
                    returnval += "+"
            print(returnval)
            returnval = "https://www.google.com/#safe=off&q=" + returnval + "&*"
            await client.send_message(message.channel, returnval)




client.run('BOT TOKEN')