author = "Magentakrayons"
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


    # Help command
    elif message.content.startswith('!help'):
        requestMade("!help", message.author)
        string = message.content.split()
        if len(string) == 1:
            text = "Hi, I'm Djeeta Bot! \n" \
                    "Please use `!help number` to know more about a category. \n \n" \
                    "**Commands** \n"\
                    "`1. Granblue Fantasy \n" \
                    "2. General Utilities`"
            await client.send_message(message.channel, text)
        elif len(string) == 2:
            if "1" in string:
                text = "**Granblue Fantasy** \n \n" \
                        "`!wiki - Performs a gbf.wiki search using the given search request. \n" \
                        "   Syntax: !wiki [Search Query] \n" \
                        "!events - Fetches the current events from http://gbf.wiki's front page. \n" \
                        "!exp - Calculates the EXP needed to reach the desired Weapon/Summon Level. Type 'char' in [Char Modifier] to calculate Character EXP instead. \n" \
                        "   Syntax: !exp [Desired Lvl] [Current Lvl] [EXP to next Lvl] [Char Modifier]`"
                await client.send_message(message.channel, text)
            elif "2" in string:
                text = "**General Utility** \n \n"\
                        "`!google - Performs a Google search using the given search request.`"
                await client.send_message(message.channel, text)


    # Granblue Utilities

    elif message.content.startswith('!wiki'):
        requestMade("!wiki", message.author)
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
        query = query.replace("_"," ")
        fullUrl = t[3]
        await client.send_message(message.channel,str(len(fullUrl)) + " matches for: " + query)
        returnMessage = ""
        for i in fullUrl:
            returnMessage += i + "\n"
        await client.send_message(message.channel, returnMessage)

    elif message.content.startswith("!events"):
        requestMade("!events", message.author)
        link = "http://gbf.wiki"
        f = requests.get(link)
        f = f.text.splitlines()
        searchtext = "<td style=\"vertical-align:top;\">"
        eventlist = []
        urls = []
        for line in range(1, len(f) + 1):
            if searchtext in f[line]:
                adding = True
                nextindex = line + 1
                nextline = f[line + 1]
                while adding:
                    templist = []
                    text = ""
                    appending = False
                    for i in nextline:
                        if i == "\"" and appending == False:
                            appending = True
                        elif appending == True and i != "\"":
                            text = text + i
                        elif i == "\"" and len(text) != 0:
                            appending = False
                            templist.append(text)
                            text = ""
                            if len(templist) == 2:
                                break
                    nextindex = nextindex + 1
                    nextline = f[nextindex]
                    if len(templist) > 0:
                        urls.append(templist[0])
                        eventlist.append(templist[1])
                    if "</td>" in nextline:
                        adding = False
            elif len(eventlist) > 0:
                break
        text = "The Current Events include: \n \n"
        for i in range(len(eventlist)):
            text = text + eventlist[i] + "\n" + (link + urls[i]) + "\n" + "\n"
        await client.send_message(message.channel, text)

    elif message.content.startswith("!exp"):
        requestMade("!exp", message.author)
        if "char" in message.content:
            table = open('tables/charexp.txt','r')
        else:
            table = open('tables/exp.txt', 'r')
        text = message.content.split()
        uplvl = int(text[1])
        lowlvl = int(text[2])
        expleft = int(text[3])
        pointer = ""
        for i in range(lowlvl):
            pointer = table.readline()
        pointer = pointer.split()
        additive = int(pointer[1])-expleft
        print(additive)
        currentexp = int(pointer[2]) + additive
        for i in range(uplvl - lowlvl):
            pointer = table.readline()
        pointer = pointer.split()
        upperexp = int(pointer[2])

        exp = upperexp - currentexp
        string = "Amount of EXP needed: " + str(exp)
        await client.send_message(message.channel, string)

    # General Utilities

    elif message.content.startswith('!google'):
        requestMade("!google", message.author)
        string = message.content.split()
        string = string[1:]
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

def requestMade(type, author):
    print(type, "request made by: ", author)


client.run('BOT TOKEN')
