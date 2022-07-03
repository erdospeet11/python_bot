import discord
from discord.ext import commands

class kep(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Game("Nagy kutyak vagytok amugy"))
        print("Im online")

    @commands.command()
    async def fiatalember(self,ctx):
        await ctx.send('https://imgur.com/YeB2jfk')
    
    @commands.command()
    async def kabbe(self,ctx):
        await ctx.send('https://imgur.com/jOUjDTc')

    @commands.command()
    async def azkom(self,ctx):
        await ctx.send('https://imgur.com/up72Y0c')

    @commands.command()
    async def nyulpeter(self,ctx):
        await ctx.send('https://imgur.com/stfxTR1')

    @commands.command()
    async def zsolt(self,ctx):
        await ctx.send('https://imgur.com/rAST9pE')

    @commands.command()
    async def nemtom(self,ctx):
        await ctx.send('https://imgur.com/5CVY8vh')

    @commands.command()
    async def stilo(self,ctx):
        await ctx.send('https://imgur.com/bB8DyJL')

    @commands.command()
    async def fityma(self,ctx):
        await ctx.send('https://imgur.com/pi9sHoU')

    @commands.command()
    async def gibbon(self,ctx):
        await ctx.send('https://imgur.com/XHUIHRG')

    @commands.command()
    async def cigany(self,ctx):
        await ctx.send('https://imgur.com/CCYErG8')

    @commands.command()
    async def flashbang(self,ctx):
        await ctx.send('https://imgur.com/8ZCE0w0')

    @commands.command()
    async def hir(self,ctx):
        await ctx.send('https://imgur.com/4w3l701')

    @commands.command()
    async def gyere(self,ctx):
        await ctx.send('https://imgur.com/CB1y3fB')

    @commands.command()
    async def jánvári(self,ctx):
        await ctx.send('https://imgur.com/hiLBsNL')

    @commands.command()
    async def romania(self,ctx):
        await ctx.send('https://imgur.com/kaAZ02c')

    @commands.command()
    async def szerencse(self,ctx):
        await ctx.send('https://imgur.com/zUO4jno')

    @commands.command()
    async def lehetetlen(self,ctx):
        await ctx.send('https://imgur.com/gBlBRA7')

    @commands.command()
    async def haltam(self,ctx):
        await ctx.send('https://imgur.com/YTkfU1T')

    @commands.command()
    async def szopógép(self,ctx):
        await ctx.send('https://imgur.com/GzwLeTj')

    @commands.command()
    async def ecipeci(self,ctx):
        await ctx.send('https://imgur.com/HE7Cv8A')

    @commands.command()
    async def szex(self,ctx):
        await ctx.send('https://imgur.com/UxYBcHQ')

    @commands.command()
    async def keresett(self,ctx):
        await ctx.send('https://imgur.com/J6Doiey')

    @commands.command()
    async def villamos(self,ctx):
        await ctx.send('https://imgur.com/DizAfsW')

    @commands.command()
    async def rendorseg(self,ctx):
        await ctx.send('https://imgur.com/X24MLNb')

    @commands.command()
    async def zse(self,ctx):
        await ctx.send('@Puzsér Róbert [BITTO DUO]')

    @commands.command()
    async def öcskös(self,ctx):
        await ctx.send('https://imgur.com/YMFZDbb')

    @commands.command()
    async def file(self,ctx):
        await ctx.send('https://imgur.com/2IgLf5g')

    @commands.command()
    async def buzi(self,ctx):
        await ctx.send('https://imgur.com/ac4j35H')

    @commands.command()
    async def buzivagyok(self,ctx):
        await ctx.send('https://www.twitch.tv/xani_lol/clip/IncredulousAbrasiveTriangleWTRuck')