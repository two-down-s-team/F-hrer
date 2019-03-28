import discord
from discord.ext import commands
from discord.ext.commands import Bot

Bot = commands.Bot(command_prefix='+')

@Bot.event
async def on_ready():
    print('Бот в сети ')

@Bot.command(pass_context= True)
async def hello(ctx):
    await Bot.say('Привет, {}'.format(ctx.message.author.mention))

@Bot.command(pass_context= True)
async def info(ctx, user: discord.User):
    emb = discord.Embed(title= user.name, colour= 0x00FF00)
    emb.add_field(name= 'Создан', value= user.created_at)
    emb.add_field(name= 'Зашёл', value= user.joined_at)
    emb.set_thumbnail(url=user.avatar_url)
    await Bot.say(embed = emb)

Bot.run('NTYwMTc0NDQ0MzYzMTIwNjgw.D31PMA.d-qC7wRX4DtMxgxo35djUIZ4lzA')
