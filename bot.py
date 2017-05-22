import discord
from discord.ext import commands
import random

description = ''' Some shitty bot made by a hack '''

bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('-------------')

# get token from file
keyfile = open('key.txt')
key = keyfile.readline()
key = key[:-1] # comment out if your text editor doesn't add a new line
bot.run(key)
