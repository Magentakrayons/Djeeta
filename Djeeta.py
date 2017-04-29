__author__ = "Magentakrayons"

import discord
import requests
import json
import asyncio

#import additional functions
from help import *
from granblue import *
from general import *

client = discord.Client()


@client.event
async def on_ready():
    print('Djeeta is now online!')
    print("ID:", client.user.id)
    print("")

@client.event
async def on_message(message):

    # Help command

    if message.content.startswith('!help'):
        requestMade("!help", message.author)
        text = help(message.content)
        await client.send_message(message.channel, text)

    # Granblue Utilities

    elif message.content.startswith('!wiki'):
        requestMade("!wiki", message.author)
        text = wiki(message.content,requests)
        await client.send_message(message.channel, text)

    elif message.content.startswith("!events"):
        requestMade("!events", message.author)
        text = events(message.content, requests)
        await client.send_message(message.channel,text)

    elif message.content.startswith("!exp"):
        requestMade("!exp", message.author)
        text = exp(message.content)
        await client.send_message(message.channel, text)

    elif message.content.startswith('!skill'):
        requestMade("!skill", message.author)
        text = skill(message.content)
        await client.send_message(message.channel, text)

    elif message.content.startswith('!servertime'):
        requestMade("!servertime", message.author)
        text = servertime(datetime,timezone)
        await client.send_message(message.channel,text)
        
    # General Utilities

    elif message.content.startswith('!google'):
        requestMade("!google", message.author)
        text = google(message.content)
        await client.send_message(message.channel,text)

#Misc. functions
def requestMade(type, author):
    """Prints to console for usage tracking purposes."""
    print(type, "request made by: ", author)


client.run('BOT TOKEN')
