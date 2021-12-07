import random as rand
import asyncio
import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")



client = commands.Bot(command_prefix='~')
@client.command()



@client.event


async def on_message(message):


    if message.content.startswith('~list'):
        channel = message.channel
        await channel.send("my other commands are:~punch, ~guess, ~customguess <number>, ~coolcheck <name>, ~annoy <name>")
        
        
    if message.content.startswith('~longhug'):
        channel = message.channel

        #starting variables
        funkyname = f""

        index = 0
        name = ""
        namesaid = False
        slot = 0
        namecheck = message.content

        #this grabs the name of the command if it's there


        if len(namecheck) > 8:
            index = 9
            funkyname = f"{message.content}"
            for i in range(len(funkyname) - 9):
                name = name + funkyname[index]
                index = index + 1

        #this grabs the user name without the number tag
        else:
            funkyname = f"{message.author}"
            while (funkyname[index] != "#"):
                name = name + funkyname[index]
                index = index + 1





        #defines a lot of lists that can be called for things that can be said
        def start1():
            global messages
            messages = [f"*grabs the {name}*", f"*grabs {name}*", "*grabs*"]

        def start2():
            global messages
            messages = [f"c'mere, {name}", f"The {name}", "you"]

        def start3():
            global messages
            messages = [f"*Holds the {name}*", f"*Picks up the {name}*", "*Picks up*"]

        def mid1():
            global messages
            messages = ["*squeeze*", "*huggggg*", "*holdddd*", "*squeeeeeze* >:3", "*tight snuggle* :3", "^w^"]

        def mid2():
            global messages
            messages = ["hug1.png", "hug2.png", "hug3.gif"]

        def mid3():
            global messages
            messages = ["*snuggles*", "*nuzzles*", "*gently hugs*", f"*nuzzles da {name}*", "*patpatpat*", "*scritchscratch*"]

        def end1():
            global messages
            messages = ["*lets go*", f"*drops the {name}*", f"*releases the {name}*"]

        def end2():
            global messages
            messages = ["*lets go*", f"*drops the {name}*", f"*releases the {name}*"]

        def end3():
            global messages
            messages = [f"*puts the {names}*", f"*sets the {name} down*", f"*places the {name} down*"]






        #the bot will start acting and talking

        #uses the starting definitions, prehug haha no going back
        await asyncio.sleep(1)
        if (0 == rand.randint(0,1)):
            namesaid = True
            await channel.send(f'{name} :3')



        start = [start1, start2, start3]
        slot = 2
        start[slot]()

        if (namesaid == True):
            await asyncio.sleep(2)
            await channel.send(f'{messages[2]}')
        else:
            await channel.send(f'{messages[rand.randint(0, 1)]}')
            await asyncio.sleep(2)
            await channel.send(":3")

        #uses middle definitions, grab da boi
        mid = [mid1, mid2, mid3]
        mid[slot]()

        await asyncio.sleep(1)
        if (slot == 1):
            await asyncio.sleep(rand.randint(1,3))
            await channel.send(file=discord.File(messages[rand.randint(0, 2)]))
        else:
            await asyncio.sleep(rand.randint(2,4))
            await channel.send(f'{messages[rand.randint(0,2)]}')

        mid3()
        for i in range(rand.randint(3, 5)):
            await asyncio.sleep(rand.randint(5,12))
            await channel.send(f'{messages[rand.randint(0,5)]}')
        mid1()
        await asyncio.sleep(4)
        await channel.send(f'{messages[rand.randint(3,5)]}')


        #uses end definitions, lets the boi go
        end = [end1, end2, end3]
        end[slot]()

        await asyncio.sleep(rand.randint(4,6))
        await channel.send(f'{messages[rand.randint(0,2)]}')
        
    if message.content.startswith('~hug'):
        channel = message.channel

        #starting variables
        funkyname = f""

        index = 0
        name = ""
        namesaid = False
        slot = 0
        namecheck = message.content

        #this grabs the name of the command if it's there


        if len(namecheck) > 4:
            index = 5
            funkyname = f"{message.content}"
            for i in range(len(funkyname) - 5):
                name = name + funkyname[index]
                index = index + 1

        #this grabs the user name without the number tag
        else:
            funkyname = f"{message.author}"
            while (funkyname[index] != "#"):
                name = name + funkyname[index]
                index = index + 1





        #defines a lot of lists that can be called for things that can be said
        def start1():
            global messages
            messages = [f"*grabs the {name}*", f"*grabs {name}*", "*grabs*"]

        def start2():
            global messages
            messages = [f"c'mere, {name}", f"The {name}", "you"]

        def start3():
            global messages
            messages = [f"*Holds the {name}*", f"*Picks up the {name}*", "*Picks up*"]

        def mid1():
            global messages
            messages = ["*squeeze* >:3", "*huggggg*", "*holdddd*"]

        def mid2():
            global messages
            messages = ["hug1.png", "hug2.png", "hug3.gif"]

        def mid3():
            global messages
            messages = ["*snuggles*", "*nuzzles*", "*gently hugs*"]

        def end1():
            global messages
            messages = ["*lets go*", f"*drops the {name}*", f"*releases the {name}*"]

        def end2():
            global messages
            messages = ["*lets go*", f"*drops the {name}*", f"*releases the {name}*"]

        def end3():
            global messages
            messages = ["*puts down*", f"*sets the {name} down*", f"*places the {name} down*"]






        #the bot will start acting and talking

        #uses the starting definitions, prehug haha no going back
        await asyncio.sleep(1)
        if (0 == rand.randint(0,1)):
            namesaid = True
            await channel.send(f'{name} :3')



        start = [start1, start2, start3]
        slot = rand.randint(0,2)
        start[slot]()

        if (namesaid == True):
            await asyncio.sleep(2)
            await channel.send(f'{messages[2]}')
        else:
            await channel.send(f'{messages[rand.randint(0, 1)]}')
            await asyncio.sleep(2)
            await channel.send(":3")

        #uses middle definitions, grab da boi
        mid = [mid1, mid2, mid3]
        mid[slot]()

        await asyncio.sleep(1)
        if (slot == 1):
            await asyncio.sleep(rand.randint(1,3))
            await channel.send(file=discord.File(messages[rand.randint(0, 2)]))
        else:
            await asyncio.sleep(rand.randint(2,4))
            await channel.send(f'{messages[rand.randint(0,2)]}')

        #uses end definitions, lets the boi go
        end = [end1, end2, end3]
        end[slot]()

        await asyncio.sleep(rand.randint(4,6))
        await channel.send(f'{messages[rand.randint(0,2)]}')

    if message.content.startswith('~punch'):
        channel = message.channel
        punchers = ["plane.mp4", "ten.mp4", "balls.mp4", "sod.mp4", "hello (2).mp4", "anger.mov"]
        await channel.send(file=discord.File(punchers[rand.randint(0, 5)]))

    if message.content.startswith('depression'):
        channel = message.channel
        await message.channel.send('No depression allowed! Take this!')
        await message.channel.send(file=discord.File('milk.png'))

    if message.content.startswith('~guess'):
        channel = message.channel

        await message.channel.send('Guess a number between 1 and 10. Now')
        await message.channel.send(file=discord.File('origun.png'))

        def is_correct(m):
            return m.author == message.author and m.content.isdigit()

        answer = rand.randint(1, 10)

        try:
            guess = await client.wait_for('message', check=is_correct, timeout=5.0)
        except asyncio.TimeoutError:
            await message.channel.send(f'Ha! You took to long! It was {answer}.')
            return await message.channel.send(file=discord.File('imded.mp4'))
        if int(guess.content) == answer:
            await message.channel.send('You are right! But only for now...')
        else:
            await message.channel.send(f'Wrong! It is actually {answer}, nerd.')

    if message.content.startswith('~customguess'):
        channel = message.channel
        numbercheck = message.content


        funkynumb = f""
        number = ""

        if len(numbercheck) > 12:
            index = 13
            funkynumb = f"{message.content}"
            for i in range(len(funkynumb) - 13):
                number = number + funkynumb[index]
                index = index + 1
            if number.isdigit():
                await message.channel.send(f'Guess a number between 1 and {number}. Now.')
                await message.channel.send(file=discord.File('origun.png'))

                def is_correct(m):
                    return m.author == message.author and m.content.isdigit()

                answer1 = rand.randint(1, int(number))

                try:
                    guess = await client.wait_for('message', check=is_correct, timeout=5.0)
                except asyncio.TimeoutError:
                    await message.channel.send(f'Ha! You took to long! It was {answer1}.')
                    return await message.channel.send(file=discord.File('imded.mp4'))
                if int(guess.content) == answer1:
                    await message.channel.send('You are right! But only for now...')
                else:
                    await message.channel.send(f'Wrong! It is actually {answer1}, nerd.')

        else:
            await message.channel.send("add a number after the command!")

    if message.content.startswith('~coolcheck'):
        channel = message.channel

        namecheck = message.content
        funkyname = f""
        name = ""

        if len(namecheck) > 10:
            index = 11
            funkyname = f"{message.content}"
            for i in range(len(funkyname) - 11):
                name = name + funkyname[index]
                index = index + 1

            await message.channel.send(f'Alright, checking {name} now...')
            await asyncio.sleep(3)
            await message.channel.send(file=discord.File('coolmario.png'))
            await message.channel.send(f'Yea! {name} is cool!')

        else:
            await message.channel.send("add a name with the command!")

    if message.content.startswith('~annoy'):
        channel = message.channel

        namecheck = message.content
        funkyname = f""
        name = ""

        if len(namecheck) > 6:
            index = 7
            funkyname = f"{message.content}"
            for i in range(len(funkyname) - 7):
                name = name + funkyname[index]
                index = index + 1

            await message.channel.send('*Inhails*')
            await asyncio.sleep(1)
            await message.channel.send('ANOYING TIMEEEEEEEEEEEEEEEEEEEE')
            for i in range(10):
                await asyncio.sleep(.5)
                await message.channel.send(f'{name}')
        else:
            await message.channel.send("add your @ after the command!")
            return

client.run(TOKEN)
