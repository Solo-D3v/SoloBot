# encoding:utf-8
# Imports
import keep_alive
import os
from discord.ext import commands, tasks
import discord
from replit import db
import json
import traceback
import requests
from requests import get
import random
from flask import request
import functools

orangeid = 677214856109359118
import youtube_dl
import time
from dotenv import load_dotenv
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL
import urllib.parse, urllib.request, re
from datetime import datetime
from discord.ext.commands import has_permissions, MissingPermissions, cooldown
from discord import Member
# Intents
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='+', intents=intents)
# Variables
an = datetime.now()
deneme = datetime(2021, 11, 21, 14, 30)
fark = an - deneme
players = {}
evet = 'Evet'
hayır = 'Hayır'
eymen = 'https://media.discordapp.net/attachments/896424613305798747/904366902841860096/Screenshot_2021-10-31-16-50-38_1.jpg'
eymen2 = 'https://cdn.discordapp.com/attachments/896423964593758278/903743912101937173/Screenshot_20211029-233517_Discord2.jpg'
eymen3 = 'https://media.discordapp.net/attachments/896423964593758278/905876541567811614/Screenshot_2021-11-04-18-02-39-1.png'
eymen4 = 'https://cdn.discordapp.com/attachments/811629842474860615/912432787011813396/20211122_230113.JPG'
# Lists
eymenifsa = [eymen, eymen2, eymen3, eymen4]
karar = [evet, hayır]
song_queue = []
# Credentials
TOKEN = os.environ["token"]


# Startup info
@client.event
async def on_ready():
    print('Bota bağlanıldı: {}'.format(client.user.name))

    print('Bot ID: {}'.format(client.user.id))

    activity = discord.Game(name="+yardım", type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print("Durum ayarlandı!")


# Events
@client.event
async def on_member_join(member):
    channel = client.get_channel(896423295501623326)
    await channel.send(f"<@{member.id}> adlı kullanıcı sunucuya katıldı :tada:"
                       )
    await member.create_dm()
    await member.dm_channel.send(
        f"Merhaba! Sunucumuza hoşgeldin! <@{member.id}>")


@client.event
async def on_member_remove(member):
    channel = client.get_channel(896423295501623326)
    await channel.send(
        f"<@{member.id}> adlı kullanıcı sunucuya dan ayrıldı :sob:")
    try:
        await member.create_dm()
        await member.dm_channel.send("Reyiz niye ayrıldın yaw :weary: :sob:")
    except:
        print(
            'Kullanıcı ile ortak hiçbir sunucuda bulunmadığımız veya kullanıcının dm si kapalı olduğu mesaj için gönderilemedi'
        )


@client.event
async def on_message(message):
    if message.content == 'Sa':
        await message.channel.send('Aleyküm Selam')

    if message.content.startswith('https://discord.gg'):
        await message.delete()
        await message.channel.send(
            f"**Link göndermek yasak! <@{message.author.id}> !")

    if message.content == 'anamın ruhunu ortaya koyuyorum':
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/816599222417621005/904057052610060368/yt5s.com-Anamn_ruhunu_ortaya_koyuyorum-240p.mp4'
        )

    if message.content.startswith('https://tenor.com/'):
        await message.delete()
        await message.channel.send(
            f"Üzgünüm <@{message.author.id}>, sunucumuzda gif göndermek yasak."
        )

    if message.content.startswith('http://discord.gg'):
        await message.delete()
        await message.channel.send(
            f"**Link göndermek yasak! <@{message.author.id}> !")

    if message.content.startswith('discord.gg/'):
        await message.delete()
        await message.channel.send(
            f"**Link göndermek yasak! <@{message.author.id}> !")

    if message.content.startswith('Discord.gg/'):
        await message.delete()
        await message.channel.send(
            f"**Link göndermek yasak! <@{message.author.id}> !")

    if message.content == 'Naber':
        await message.channel.send('İyiyim senden naber')

    if message.content == '<@!>':
        await message.channel.send(
            'Hey dostum! Prefixim +! Belki ihtiyacın olur diye yani...')

    if message.content == '+karar':
        await message.channel.send(random.choice(karar))

    if message.content == 'Merhaba':
        await message.reply('Merhaba!')
    await client.process_commands(message)


# commands
@client.command()
async def yardım(ctx):
    await ctx.channel.send(
        '***+yardım:Bu mesajı görüntüler.\n \n +yt: Bir şarkı ararsınız.\n \n +oynat: Gönderdiğiniz linki oynatır.\n \n +dur: Şarkıyı duraklatır.\n \n +devam: Şarkıyı devam ettirir.\n \n +kapat: Şarkıyı temelli kapatır.\n \n +sil: Belirttiğiniz kadar mesaj siler.\n \n +davet: Botun ve discord sunucumuzun linkini atar.***'
    )


@client.command()
async def davet(ctx):
    await ctx.reply(
        '**Bot davet linki: https://discord.com/api/oauth2/authorize?client_id=&permissions=8&scope=bot**'
    )


# bir linki oynatır
@client.command()
async def oynat(ctx, url):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {
        'before_options':
        '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn'
    }
    voice = get(client.voice_clients, guild=ctx.guild)
    channel = ctx.message.author.voice.channel

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['url']
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
        await ctx.send('**Oynatılıyor...**')
        # eğer zaten oynatılıyorsa
    else:
        await ctx.send("**Zaten bir şarkı oynatılıyor...**")
        return


@oynat.error
async def oynat_error(ctx, error):
    await ctx.channel.send('**Şarkıyı oynatırken bir sorunla karşılaşıldı...**'
                           )


# durdurulmuş şarkıyı devam ettirme
@client.command()
async def devam(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        voice.resume()
        await ctx.send('**Şarkı kaldığı yerden devam ediyor...**')


# duraklatır bir süreliğine
@client.command()
async def dur(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
        await ctx.send('**Şarkı durduruldu...**')


# durdurur
@client.command()
async def kapat(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.stop()
        voice = await ctx.voice_client.disconnect()
        await ctx.send('**Kapatılıyor...**')
    else:
        voice = await ctx.voice_client.disconnect()


# mesaj silmece
@client.command()
@has_permissions(manage_messages=True)
async def sil(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send("**Mesajlar silindi!**")


@sil.error
async def sil_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.channel.send(
            f"**Üzgünüm <@{ctx.author.id}>, bunu yapmaya yetkin yok.**")
    else:
        await ctx.channel.send(
            '**Mesaj silme yetkim olmadığı için mesajlar silinemedi.**')


@client.command()
async def haber(ctx):
    import feedparser
    NewsFeed = feedparser.parse("http://sondakika.haber7.com/sondakika.rss")
    entry = NewsFeed.entries[0]
    await ctx.channel.send(
        f"**{NewsFeed.entries[0].title}\n \n------Haberin Linki--------\n {entry.link}**"
    )


@client.command()
async def yt(ctx, *, search):

    query_string = urllib.parse.urlencode({'search_query': search})
    htm_content = urllib.request.urlopen('http://www.youtube.com/results?' +
                                         query_string)
    search_results = re.findall(r'/watch\?v=(.{11})',
                                htm_content.read().decode())
    await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])


keep_alive.keep_alive()
client.run(TOKEN)
