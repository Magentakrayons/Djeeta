import discord
import asyncio
import requests
import json

client = discord.Client()

@client.event
async def on_ready():
    print('Djeeta is now online!')
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
        await asyncio.sleep(1)
        print(message.content)
        string = message.content.split()
        string = string[1:]
        print(string)
        if len(string) == 1:
            returnval = "https://www.google.com/#safe=off&q=" + string[0] + "&*"
            await client.send_message(message.channel, returnval)
        else:
            returnval = ""
            for i in string:
                returnval += i
                if string.index(i) != len(string)-1:
                    returnval += "+"
            returnval = "https://www.google.com/#safe=off&q=" + returnval + "&*"
            await client.send_message(message.channel, returnval)

    # Help command
    elif message.content.startswith('!help'):
        await asyncio.sleep(1)
        string = message.content.split()
        if len(string) == 1:
            text = "Hi, I'm Djeeta Bot! \n" \
                    "Please use `!help number` to know more about a category. \n \n" \
                    "**Commands**"\
                    "```1. Granblue \n" \
                    "2. General Utilities```"
            await client.send_message(message.channel, text)
        elif len(string) == 2:
            if "1" in string:
                text = "Granblue \n" \
                        "```!wiki - Performs a gbf.wiki search using the given search request.```"
                await client.send_message(message.channel, text)
            elif "2" in string:
                text = "General Utility \n"\
                        "```!google - Performs a Google search using the given search request.```"
                await client.send_message(message.channel, text)


    # Granblue Utilities

    elif message.content.startswith('!wiki'):
        await asyncio.sleep(1)
        string = message.content.split()
        string = string[1:]
        if len(string) <= 1:
            userInput = string[0]
        else:
            userInput = ""
            for i in string:
                userInput += i
                if string.index(i) != len(string) - 1:
                    userInput += "_"
        url = "https://gbf.wiki/api.php?action=opensearch&format=json&formatversion=2&search="+userInput
        t = requests.get(url).json()
        query = t[0]
        fullUrl = t[3]
        await client.send_message(message.channel,str(len(fullUrl)) + " matches for: " + query)
        returnMessage = ""
        for i in fullUrl:
            returnMessage += i + "\n"
        await client.send_message(message.channel, returnMessage)




client.run('BOT TOKEN')
