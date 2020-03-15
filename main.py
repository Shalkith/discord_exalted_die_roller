import random
import discord

#paste in discord token
#invite the bot
#type the below command in discord to roll 10 dice (d10s only for exalted)
#!roll 10


TOKEN = 'paste discord token here'
def roll(die):
    try:
        die = int(die.split('!roll')[1].replace(' ','',99))

    except:
        return 'Command not formatted correctly\n Try: !roll 5 \n Where 5 is the die count you want to roll'

    if die >100:
        return 'You cant roll more than 100 dice.'
    count = int(die)
    results = []
    success = 0
    damagesuccesses = 0
    msg = ''
    for x in range(1,count+1):
        result = random.randrange(1,11)
        if result == 7 or result == 8 or result == 9:
            success = success +1
            damagesuccesses = damagesuccesses + 1

        if result == 10:
            success = success +2
            damagesuccesses = damagesuccesses + 1
        results.append(result)

    results.sort(reverse=True)
    msg = msg + 'You rolled: '+str(results)+'\n'
    msg = msg + 'Successes: '+str(success)+'\n'
    msg = msg + 'Damage Successes: '+str(damagesuccess)+'\n'
    if 1 in results and success == 0:
        msg = msg + 'BOTCH!!!'
    return msg

client = discord.Client()

@client.event
async def on_message(message):
    formatting = '**'
    f = formatting

    user = message.author
    if message.author.nick == None:
        user = message.author.name
    else:
        user = message.author.nick

    if message.author == client.user:
        return
    elif message.content.lower().startswith('!roll'):
        msg = roll(message.content.lower())
        await message.channel.send(f+' '+user+f+'\n'+msg)

client.run(TOKEN)
