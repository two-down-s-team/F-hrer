import discord
import asyncio
import requests

import info as i

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name=i.prefix + "help"))
    print('Logged in')
    print('Username: ' + str(client.user.name))
    print('Client ID: ' + str(client.user.id))
    print('Invite URL: ' + 'https://discordapp.com/oauth2/authorize?&client_id=' + client.user.id + '&scope=bot&permissions=0')

@client.event
async def on_message(message):
    if message.content.startswith(i.prefix):

        message.content = message.content[1:].lower()
        # Комманда для выключения бота
        if message.content.startswith('oof') and message.author.id == i.owner_id:
            await client.send_message(message.channel, 'Выключение...')
            await client.logout()
            await client.close()
        # Команда help
        if message.content.startswith('help'):
            await client.send_message(message.channel, i.helpMsg)
        if message.content.startswith('user'):
            await client.send_message(message.channel, 'Твой id: ' + message.author.id + '\nТвоя ава: ' + message.author.avatar_url)
            emb = discord.Embed(title= "Информация о {}".format(message.author.name), colour = 0x00ff00)

# Запуск бота
client.run(i.token)
