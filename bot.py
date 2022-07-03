import discord
from discord.ext.commands import bot
import asyncio
import datetime as DT
import random
from discord.ext import commands, tasks
import os
from random import Random, choice
from kep import kep

bot = commands.Bot(command_prefix='!', help_command=None)
client = discord.Client()
currentDT = DT.datetime.now()

bot.add_cog(kep(bot))

monke = ["https://tenor.com/bDYus.gif", "https://tenor.com/bix4J.gif", "https://tenor.com/bf9IM.gif",
         "https://tenor.com/bfbhy.gif", "https://tenor.com/bGTPu.gif"]


@bot.command()
async def monke(ctx):
    await ctx.send(random.choice(monke))

bot.ennyivel = 2

@bot.command()
async def jossz(ctx):
    await ctx.send('Zse ennyivel jon nekem: ' + str(bot.ennyivel))


@bot.command()
async def pingvin(ctx):
    await ctx.send(random.choice(pingvinek))


pingvinek = ["https://imgur.com/rAST9pE", "https://imgur.com/5CVY8vh", "https://imgur.com/pi9sHoU",
             "https://imgur.com/XHUIHRG", "https://imgur.com/CCYErG8", "https://imgur.com/8ZCE0w0",
             "https://imgur.com/4w3l701", "https://imgur.com/CB1y3fB", "https://imgur.com/kaAZ02c",
             "https://imgur.com/HE7Cv8A", "https://imgur.com/UxYBcHQ", "https://imgur.com/J6Doiey",
             "https://imgur.com/DizAfsW", "https://imgur.com/YMFZDbb", "https://imgur.com/2IgLf5g",
             "https://imgur.com/ac4j35H", "https://imgur.com/YeB2jfk"]


@bot.command()
async def ajandek(ctx):
    await ctx.send(random.choice(igen))


igen = ["teljesül", "most sajnos nem teljesül"]

@bot.command()
async def idő(ctx):
    currentDT = DT.datetime.now()
    await ctx.send(currentDT)


bot.var = 0
bot.zse = 357542157298565120


@bot.command()
async def nemjott(ctx):
    bot.var += 1
    await ctx.send("Zse ennyiszer nem jott: " + str(bot.var))


@bot.command()
async def elment(ctx):
    bot.var += 1
    await ctx.send("Zse mar megint cserben hagyta a baratait! :/")


@bot.command()
async def bejott(ctx):
    embed = discord.Embed(title="Zse bejott", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", color=0xff0000)
    embed.add_field(name="Zse bejott", value="Zse bejott", inline=True)
    embed.add_field(name="Zse bejott", value="Zse bejott", inline=True)
    embed.set_footer(text="hopp hopp hopp")
    await ctx.send(embed=embed)


@bot.command()
async def teszt(ctx):
    await ctx.send('https://imgur.com/UJCvVwl')


@bot.command()
async def hello(ctx):
    await ctx.send()


@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

@bot.command()
async def summon(ctx, arg1):
    if(arg1 == "zse"):
        await ctx.send("https://imgur.com/9D8XQdq")
    else:
        await ctx.send("azkom")

###############################################################################################################
bot.penz = 100


@bot.command()
async def inditas(ctx):
    embed = discord.Embed(title="Tippelős játék",
                          description="a !tipp <tét> paranccsal tudod elindítani a játékot. Ekkor a bot generál neked 0-100-ig egy számot, neked meg kell tippelned, hogy nagyobb-e a szám vagy sem. Ha eltalálod megkapod a téted kétszeresét. Sok sikert!",
                          color=discord.Color.blue())
    await ctx.send(embed=embed)


@bot.command()
async def egyenleg(ctx):
    await ctx.send("Ennyi az egyenleged: ||{}||".format(str(bot.penz)))


@bot.command()
async def feltoltes(ctx, mennyit):
    mennyit = int(mennyit)
    if mennyit > 100:
        await ctx.send("Ennyit nem tudsz feltölteni")
    else:
        bot.penz += mennyit
    await ctx.send("Ennyi az egyenleged: ||{}||".format(str(bot.penz)))


@bot.command()
async def jatek(ctx, tet):
    tet = int(tet)

    bot.adott = random.randint(0, 100)
    bot.gondolt = random.randint(0, 100)
    await ctx.send("Ez a szám kisebb vagy nagyobb-e mint a gondolt számom? " + str(bot.adott))

    try:
        msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)

    except asyncio.TimeoutError:
        await ctx.send("Gyorsabban pötyögj kérlek!")

    else:
        if msg.content == "nagyobb":
            if bot.adott > bot.gondolt:
                await ctx.send("**Eltaláltad!**")
                bot.penz += tet
            else:
                await ctx.send("**Nem találtad el!**")
                bot.penz -= tet
            await ctx.send("Ennyi az egyenleged: ||{}||".format(str(bot.penz)))
        elif msg.content == "kisebb":
            if bot.adott < bot.gondolt:
                await ctx.send("**Eltaláltad!**")
                bot.penz += tet
            else:
                await ctx.send("**Nem találtad el!**")
                bot.penz -= tet
            await ctx.send("Ennyi az egyenleged: ||{}||".format(str(bot.penz)))
        else:
            await ctx.send("Huh?")
    await ctx.send("Ez volt a gondolt szám: {}".format(str(bot.gondolt)))

#################################################HANGMAN GAME#########################################################################
hangman_phase = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

betuk = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
szavak = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
print(szavak)

beirt = 'Eddigi tippjeid: ' + ','.join(str(x) for x in list(betuk))

@bot.command()
async def jatek2(ctx):
    i = 0
    eletek = 6
    megfejtes = random.choice(szavak)
    huzott = []
    for c in megfejtes:
        huzott.append('-')
    s = ' '.join(str(x) for x in list(huzott))
    embed=discord.Embed(title="Akasztófa játék", color=0x0040ff)
    embed.add_field(name="Tippjeid:", value=s, inline=False)
    embed.add_field(name="Rajz:", value=hangman_phase[i], inline=False)
    embed.add_field(name="Megfejtes:", value=megfejtes, inline=False)
    await ctx.send(embed=embed)

    while(eletek != 0 or s == megfejtes):
        try:
            msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)
            eletek -= 1
        except asyncio.TimeoutError:
            await ctx.send("Gyorsabban pötyögj kérlek!")
        else:
            if str(msg.content) in betuk:
                index = megfejtes.index(msg.content)
                for i in range(len(megfejtes)):
                    if megfejtes[i] == msg.content:
                        huzott[index] = megfejtes[index]
                s = ' '.join(str(x) for x in list(huzott))
                await ctx.send("**Benne van**")
                embed=discord.Embed(title="Akasztófa játék", color=0x0040ff)
                embed.add_field(name="Tippjeid:", value=s, inline=False)
                embed.add_field(name="Rajz:", value=hangman_phase[i], inline=False)
                embed.add_field(name="Megfejtes:", value=megfejtes, inline=False)
                await ctx.send(embed=embed)
            else:
                await ctx.send("Nincsen benne")
    await ctx.send("Ez volt a gondolt szám: {}".format(str(megfejtes)))     



print("Minden rendben várom a következő utasításokat!")
bot.run('Nzg2MTg5MzYwNjkzMTE2OTU4.X9Cx5g.d4UNiJSNoAxqNXuw4ijfM9VOQ3s')