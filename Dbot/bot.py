import discord
import asyncio
import requests



client = discord.Client()
user = discord.User

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    await client.change_presence(game=discord.Game(name="Making a bot"))

    if message.content.startswith('+hi'):
        print('[command]: hi ')
        await client.send_message(message.channel, 'Привет, ' + message.author.mention + '!')

    if message.content.startswith('+user'):
        print('[command]: user')
        await client.send_message(message.channel, 'User name: ' + message.author.id + '\nUser avatar: ' +  message.author.avatar_url + '\nUser bot: ' + str(message.author.bot))

    if message.content.startswith('+abc123'):
        await client.send_message(message.channel, message.content[::-1])

    if message.content.startswith('+bot'):
        await client.send_message(message.channel, '+user')

    if message.content.startswith('info ' + str(user.name)):
        await client.send_message(message.channel, user.id)

client.run('NTYwMTc0NDQ0MzYzMTIwNjgw.D3zLpQ.xigPonBZdwSRWCyhYWiaxy5n9i0')
