import discord, asyncio
from discord.ext import commands
from discord.ext.commands import Bot
import os

Bot = commands.Bot(command_prefix= '.')

global status

@Bot.event
async def on_ready():
    print("Bot is online!")

@Bot.command(pass_context= True)
async def discusson(ctx): # Команда для создания беседы
    await Bot.say("`User {0} has created a {1}!`".format(ctx.message.author,ctx.message.content))
    await Bot.delete_message(ctx.message)

@Bot.command(pass_context= True)
async def Anonym(ctx): # Команда для оставления анонимного сообщения
    await Bot.say("`{0}`".format(ctx.message.content))
    await Bot.delete_message(ctx.message)

@Bot.command(pass_context= True)
async def say_in(ctx): # Команда для оставления сообщения
    await Bot.say("`{0} {1}`".format(ctx.message.author, ctx.message.content))
    await Bot.delete_message(ctx.message)

@Bot.command(pass_context= True)
@commands.has_permissions(administrator= True)
async def reg_no(ctx):
    await Bot.say("`Неуспешная регистрация!`")
    await Bot.delete_message(ctx.message)


@Bot.command(pass_context= True)
@commands.has_permissions(administrator= True)
async def reg(ctx):
    await Bot.say("`Успешная регистрация!`")
    await Bot.delete_message(ctx.message)

@Bot.command(pass_context= True)
@commands.has_permissions(administrator= True)
async def rainbow(ctx, role:discord.Role):
    global status
    status = True
    while status:
        await Bot.edit_role(ctx.message.server, role, colour= discord.Colour.red())
        await asyncio.sleep(0.01)
        await Bot.edit_role(ctx.message.server, role, colour= discord.Colour.orange())
        await asyncio.sleep(0.01)
        await Bot.edit_role(ctx.message.server, role, colour= discord.Colour.gold())
        await asyncio.sleep(0.01)
        await Bot.edit_role(ctx.message.server, role, colour= discord.Colour.green())
        await asyncio.sleep(0.01)
        await Bot.edit_role(ctx.message.server, role, colour= discord.Colour.blue())
        await asyncio.sleep(0.01)
        await Bot.edit_role(ctx.message.server, role, colour= discord.Colour.dark_blue())
        await asyncio.sleep(0.01)
        await Bot.edit_role(ctx.message.server, role, colour= discord.Colour.dark_purple())
        await asyncio.sleep(0.01)

@Bot.command(pass_context= True)
@commands.has_permissions(administrator= True)
async def stop(ctx):
    global status
    status = False

@Bot.command(pass_context= True)
async def version(ctx):
    await Bot.say("`V.0.0.1`")
    await Bot.delete_message(ctx.message)

token = os.environ.get('NTYwMTc0NDQ0MzYzMTIwNjgw.D31PMA.d-qC7wRX4DtMxgxo35djUIZ4lzA')

Bot.run('NTYwMTc0NDQ0MzYzMTIwNjgw.D31PMA.d-qC7wRX4DtMxgxo35djUIZ4lzA')
