# DixtinhoBot for Discord by dixtu - https://github.com/dixtu
# Created using discord.py :)

import discord
from ctypes.util import find_library
from discord.ext import commands
import datetime

bot_token = "TOKEN"  # Replace TOKEN with your bot token.

# You can create your bot through here: https://discordapp.com/developers/applications/

bot = commands.Bot(command_prefix='!')  # Prefix for commands


@bot.event
async def on_ready():
    print("Bot {} ({}) connected at {} (Local time) .".format(bot.user.name, bot.user.id, datetime.datetime.now().time()))


@bot.command(name="say")
async def _say(arg):

        await bot.say(arg)


@bot.command(pass_context=True)
async def hello(ctx):
    nick = ctx.message.author
    await bot.say("Hi {0.mention}!".format(nick))


@bot.command(pass_context=True)
async def connect(ctx):
    # ! ctx.message.author = Member object !
    channel_name = ctx.message.author.voice.voice_channel.name
    voice = ctx.message.author.voice.voice_channel
    await bot.join_voice_channel(voice)
    print("Bot has connected to the {} channel".format(channel_name))


@bot.command(pass_context=True, name="disconnect")
async def _disconnect(ctx):
    channel_name = ctx.message.author.voice.voice_channel.name
    await bot.voice_client_in(ctx.message.author.server).disconnect()
    print("Bot has disconnected from the {} channel.".format(channel_name))


@bot.command(pass_context=True, name="exit")
async def _exit(ctx):
    server_name = ctx.message.author.server
    await bot.close()
    print("Bot has been disconnected from the {} server.".format(server_name))


@bot.command(pass_context=True)
async def play(ctx, arg):

    server = ctx.message.author.server
    discord.opus.load_opus(find_library('opus'))  # find_library() used to help linux users
    if discord.opus.is_loaded():
        player = await bot.voice_client_in(server).create_ytdl_player(arg)
        player.start()
        print("Bot started playing {} ({} Seconds)".format(player.title, player.duration))

    else:
        print("I was unable to play due to an error.")


bot.run(bot_token)





