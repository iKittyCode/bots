import discord
import random
client = discord.Client()
emojilist =  '👩‍💻','👩🏻‍💻','👩🏽‍💻','👩🏼‍💻','👩🏾‍💻','👩🏿‍💻','👨‍💻','👨🏻‍💻','👨🏼‍💻','👨🏽‍💻','👨🏾‍💻','👨🏿‍💻'
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/hello'):
        await message.channel.send('hello!')
    elif message.content.startswith('/randomNumber'):
        await message.channel.send(random.randint(0, 1000000000)) 
    elif message.content.startswith('!deleteme'):
            msg = await message.channel.send('I will delete myself now...')
            await msg.delete()
            await message.channel.send("A message was deleted")
    elif message.content.startswith("!emoji"):
         await message.channel.send(emojilist[random.randint(0, 15)])    
                

   
client.run('OTQ4Njc3MzYwODkzNDQ0MTg3.Yh_SpA.tjrUzOwIQl8RicIt3b1uCUopweo')
