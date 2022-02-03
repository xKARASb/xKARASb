import discord
from disco.api.client import APIClient

client = APIClient('OTM4MTAwMTI3MjI1MjI5MzQz.YflX0w.pUAaJm0uzfQ8OBRPpahEvNyRbiE')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    global bot_channel
    bot_channel = client.get_channel(934400691512934441)
react = {}
print(react)
@client.event
async def on_message(message):
    id = 910141858347384848
    print(message.channel.id)
    if message.author.bot == False :
        if message.channel.id == id:
            await message.add_reaction('✅')
            await message.add_reaction('❌')
            react.update({message.id:{}})
            print(react)
        else:
            return
    else:
        message.channel.send('Ti bot')

    print(f'{message.content}')

@client.event
async def on_reaction_add(reaction, user):
  if reaction.emoji == '✅' :
    global white_mark
    white_mark = reaction.count
    react[reaction.message.id].update({'✅': white_mark})
  elif reaction.emoji == '❌' :
      global red_mark
      red_mark = reaction.count
      react[reaction.message.id].update({'❌': red_mark})
  else:
    return
  if white_mark + red_mark >= 5:
    if white_mark > red_mark :
        if (red_mark/white_mark) * 100 >= 30 :
            global msg
            msg = reaction.message
            await bot_channel.send(f'Автор: {msg.author}\n Идея:\n `{msg.content}`')
        else:
            return
    else:
        return
  else:
      return

@client.event
async def on_reaction_remove(reaction, user):
  if reaction.emoji == '✅' :
    global white_mark
    white_mark = reaction.count
    react[reaction.message.id].update({'✅': white_mark})
  elif reaction.emoji == '❌' :
      global red_mark
      red_mark = reaction.count
      react[reaction.message.id].update({'❌': red_mark})
  else:
    return
  if white_mark + red_mark >= 5:
    if white_mark > red_mark :
        if (red_mark/white_mark) * 100 >= 30 :
            global msg
            msg = reaction.message
            await bot_channel.send(f'Автор: {msg.author}\n Идея:\n `{msg.content}`')
        else:
            return
    else:
        return
  else:
      return
