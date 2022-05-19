# encoding:utf-8
# Imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from googletrans import Translator
from time import sleep
import gtts
import keep_alive
import os
from discord.ext import commands, tasks
import discord
import requests
from discord.utils import get
import random
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
import urllib.parse, urllib.request, re
import instaloader
from discord.ext.commands import has_permissions, MissingPermissions
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select
from discord import Spotify
# Intents
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='+', intents=intents, help_command=None)
DiscordComponents(client)
# Variables
z = []
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
# Fonksiyonlar


# Credentials
TOKEN = os.environ["token"]
key = os.environ['key']


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
    if member.guild.id == 921845935930216479:
        return
    channel = client.get_channel(934065055346090014)
    await channel.send(
        f"**<@{member.id}> adlı kullanıcı sunucuya katıldı** :tada:")
    await member.create_dm()
    await member.dm_channel.send(
        f"**Merhaba! Sunucumuza hoşgeldin! <@{member.id}>**")


@client.event
async def on_member_remove(member):
    if member.guild.id == 921845935930216479:
        return
    channel = client.get_channel(934065055346090014)
    await channel.send(
        f"**{member.name} adlı kullanıcı sunucuya dan ayrıldı** :sob:")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send('Hata: Botun bunu yapmaya yetkisi yok')

    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            f'Hata: Üzgünüm <@{ctx.author.id}>, bunu yapmaya yetkin yok')

    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'Hata: {error}')

    if isinstance(error, commands.UserNotFound):
        await ctx.send(f'Hata: Kullanıcı bulunamadı!')


@client.event
async def on_message(message):
    if message.content == 'Sa':
        await message.channel.send('Aleyküm Selam')

    if message.content == 'anamın ruhunu ortaya koyuyorum':
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/816599222417621005/904057052610060368/yt5s.com-Anamn_ruhunu_ortaya_koyuyorum-240p.mp4'
        )

    if message.content == 'yunus ifşa':
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/818555613108764723/913426756730511361/sketch-1637599477924.png'
        )

    if message.content == '<@901414164289961986>':
        await message.channel.send(
            'Hey dostum! Prefixim +! Belki ihtiyacın olur diye yani...')

    if message.content == 'Merhaba':
        await message.reply('Merhaba!')

    if message.content == 'maraşlı ifşa':
        await message.reply(
            'https://cdn.discordapp.com/attachments/896423964593758278/904084898321670195/Screenshot_20210903-232928_WhatsApp2.jpg'
        )

    if message.content == 'yusuf ifşa':
        await message.channel.send(
            'https://media.discordapp.net/attachments/843145381118345247/872096405076983848/Screenshot_2021-08-03-15-38-15_1.jpg'
        )

    if message.content == 'eymen ifşa':
        await message.channel.send(random.choice(eymenifsa))
    await client.process_commands(message)


# commands
@client.command()
async def yardım(ctx):
    embed = discord.Embed(title='Yardım Komutları',
                          description='',
                          colour=discord.Colour.blue())
    embed.set_footer(text='Umarım yardımcı olmuştur.')
    embed.set_thumbnail(
        url=
        'https://cdn.discordapp.com/attachments/921343465537802281/922529554755620944/IMG-20211215-WA0016.jpg'
    )
    embed.set_author(
        name='SoloBot',
        icon_url=
        'https://cdn.discordapp.com/attachments/921343465537802281/922529554755620944/IMG-20211215-WA0016.jpg'
    )
    embed.add_field(
        name='Komutlar:',
        value=
        '```+yardım:Bu mesajı görüntüler.\n \n +yt: Youtube\'de bir video ararsınız.\n \n +oynat: Yazdığınız şarkıyı oynatır.\n \n +dur: Şarkıyı duraklatır.\n \n +devam: Şarkıyı devam ettirir.\n \n +kapat: Şarkıyı temelli kapatır.\n \n +sil: Belirttiğiniz kadar mesaj siler.\n \n +trs: Başka bir dili türkçeye çevirir.\n \n +trsr: Herhangi bir dili seçtiğiniz dile çevirir.\n \n +kısalt: Gönderdiğiniz linki kısaltır\n \n +tts: Bot bulunduğunuz ses kanalına gelip yazdığınız şeyi okur. ```',
        inline=False)
    await ctx.send(embed=embed)

@client.command()
async def rfoto(ctx):
  a = random.randint(1,1000)
  embed = discord.Embed(title='Rastgele Foto!', colour=discord.Colour.random())
  embed.set_image(url = f'https://source.unsplash.com/random?={a}')
  embed.set_footer(text=f'Bu komut {ctx.author.name} tarafından kullanıldı!')
  await ctx.send(embed=embed)

@client.command()
async def spotify(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
        pass
    if user.activities:
        for activity in user.activities:
            if isinstance(activity, Spotify):
                embed = discord.Embed(title = f"{user.name} kullanıcısının Spotify'ı",description = "{} dinliyor...".format(activity.title),colour = discord.Colour.random())
                embed.set_thumbnail(url=activity.album_cover_url)
                embed.add_field(name="Sanatçı", value=activity.artist)
                embed.add_field(name="Albüm", value=activity.album)
                embed.set_footer(text=" {}'dan beri dinliyor'".format(activity.created_at.strftime("%H:%M")))
                await ctx.send(embed=embed)

@client.command()
async def serverinfo(ctx):
  yk = len(ctx.guild.text_channels)
  sk = len(ctx.guild.voice_channels)
  k = len(ctx.guild.channels)
  ü = len(ctx.guild.members)
  s = ctx.guild.owner.name
  vr = ctx.guild.verification_level
  embed = discord.Embed(title='Server Info', colour=discord.Colour.random())
  embed.add_field(name = f'{ctx.guild.name} sunucusu hakkında bilgiler', value = f':white_small_square: Sunucu sahibi: {s} :white_small_square: \n \n :white_small_square: Sunucudaki üye sayısı {ü} :white_small_square: \n \n :white_small_square: Toplam kanal sayısı: {k} :white_small_square: \n \n :white_small_square: Toplam metin kanalı sayısı: {yk} :white_small_square: \n \n :white_small_square: Toplam ses kanalı sayısı: {sk} :white_small_square: \n \n :white_small_square: Sunucu doğrulaması: {vr} :white_small_square:')
  embed.set_footer(text=f'Bu komut {ctx.author.name} tarafından kullanıldı!')
  await ctx.send(embed=embed)

@client.command()
async def mcbaşarım(ctx,*,msg):
  embed = discord.Embed(title='Minecraft Başarım', colour=discord.Colour.random())
  embed.set_image(url = 'https://minecraftskinstealer.com/achievement/1/Basarim+Kazanildi%21/'+msg)
  embed.set_footer(text=f'Bu komut {ctx.author.name} tarafından kullanıldı!')
  await ctx.send(embed=embed)
    
@client.command()
async def instapp(ctx, *, kullaniciadi):
    try:
        ig = instaloader.Instaloader()
        profile = kullaniciadi
        ig.download_profile(profile, profile_pic_only=True)
        sss = os.scandir(kullaniciadi)
        for i in sss:
            if i.name.endswith('jpg'):
                await ctx.send(file=discord.File(i))
                os.remove(i)
                os.rmdir(kullaniciadi)
            else:
                os.remove(i)
    except Exception as e:
        await ctx.send(f'**Hata: {e}**')


@client.command()
async def kedi(ctx):
    r = requests.get('https://cataas.com/cat?json=true')
    a = r.json()
    link = 'https://cataas.com' + a['url']
    embed = discord.Embed(title='İşte sana bir kedicik! <a:kedy:966387117662036058>', colour=discord.Colour.random())
    embed.set_image(url = link)
    await ctx.send(embed=embed)
  

@client.command()
async def denemexd(ctx, *, arg):
    r = requests.get(arg)
    j = r.content.decode()
    x = j.split(
        '{\"prefetchPriority\":0,\"countdownUiRelativeSecondsPrefetchCondition\":-3}}}}]},\"hasDecorated\":true}},\"contents\":{\"twoColumnWatchNextResults\":{\"results\":{\"results\":{\"contents\":[{\"videoPrimaryInfoRenderer\":{\"title\":{\"runs\":[{\"text\":\"'
    )[1]
    y = x.split('\"')[0]
    await ctx.send(y)


@client.command()
@commands.cooldown(1, 45, commands.BucketType.user)
async def sayıtahmin(ctx):
    x = random.randint(1, 100)
    y = 6
    await ctx.reply(
        '1 ile 100 arasında bir sayı tuttum. Onu bulabilir misin? Tahmin etmek için 6 hakkın var!'
    )
    while True:
        try:
            msg = await client.wait_for(
                'message',
                check=lambda message: message.author.id == ctx.author.id,
                timeout=90)
            if y == 1 and int(msg.content) == x:
                await msg.channel.send('Tebrikler! Sayıyı buldun!')
            elif y == 1:
                await msg.channel.send(
                    f'Malesef hakkın bitti... **Tuttuğum sayı: {x}**')
                break

            elif int(msg.content) > x:
                y = y - 1
                await msg.channel.send(
                    f'Tuttuğum sayı daha **küçük** bir sayı! **{y} hakkın kaldı!**'
                )

            elif int(msg.content) < x:
                y = y - 1
                await msg.channel.send(
                    f'Tuttuğum sayı daha **büyük** bir sayı! **{y} hakkın kaldı!**'
                )

            else:
                await msg.channel.send('Tebrikler! Sayıyı buldun!')
                break
        except ValueError:
            pass
        except Exception as e:
            print(e)
            await ctx.send(
                'Çok uzun süredir yanıt vermediğiniz için oyun iptal edildi!')
            return


@client.command()
async def ban(ctx, üye: discord.Member, *, neden=None):
    await üye.ban(reason=neden)
    await ctx.send(
        f'**{üye.name} adlı kullanıcı {neden} nedeniyle {ctx.author.name} tarafından banlandı**'
    )


@client.command()
async def unban(ctx, *, üye):
    banlılar = await ctx.guild.bans()
    üye_nick, üye_tag = üye.split('#')

    for i in banlılar:
        bismillah = i.user

        if (bismillah.name, bismillah.discriminator) == (üye_nick, üye_tag):
            await ctx.guild.unban(bismillah)
            await ctx.reply(f'{bismillah} kullanıcısının banı kaldırıldı!')


@client.command()
async def kick(ctx, üye: discord.Member, *, neden=None):
    await üye.kick(reason=neden)
    await ctx.send(
        f'**{üye.name} adlı kullanıcı {neden} nedeniyle {ctx.author.name} tarafından atıldı**'
    )


@client.command()
@has_permissions(manage_nicknames=True)
async def nick(ctx, member: discord.Member = None, *, nick=None):
    await member.edit(nick=nick)
    await ctx.reply(
        f"{member.mention} kullanıcısının sunucudaki ismi değiştirildi!")


@client.command()
async def pfp(ctx, arg: discord.Member = None):
    if not arg == None:
        pfp = arg.avatar_url
        embed = discord.Embed(title="Profil Fotoğrafı",
                              description='{}'.format(arg.mention),
                              color=0xecce8b)
        embed.set_image(url=(pfp))
        await ctx.send(embed=embed)
    else:
        arg = ctx.author
        pfp = arg.avatar_url
        embed = discord.Embed(title="Profil Fotoğrafı",
                              description='{}'.format(arg.mention),
                              color=0xecce8b)
        embed.set_image(url=(pfp))
        await ctx.send(embed=embed)


@client.command()
async def tts(ctx, *, arg):
    voice = get(client.voice_clients, guild=ctx.guild)
    channel = ctx.message.author.voice.channel
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    if not voice.is_playing():
        x = random.randint(1, 100)
        tts = gtts.gTTS(f"{arg}", lang="tr")
        tts.save(f"adana{x}.mp3")
        voice.play(FFmpegPCMAudio(f'adana{x}.mp3'))
        voice.is_playing()
        sleep(1)
        os.remove(f'adana{x}.mp3')


# bir linki oynatır
async def dur(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
        await ctx.send('**Şarkı durduruldu...**')


async def devam(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        voice.resume()
        await ctx.send('**Şarkı kaldığı yerden devam ediyor...**')


async def kapat(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    voice = await ctx.voice_client.disconnect()
    await ctx.send('**Kapatılıyor...**')


@client.command()
async def s(ctx):
    global z
    x = 0
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {
        'before_options':
        '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn'
    }
    voice = get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    channel = ctx.message.author.voice.channel
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    z.remove(z[0])
    if not voice.is_playing():
        r = requests.get(f'https://youtube.com/watch?v={z[0]}')
        j = r.content.decode()
        x = j.split(
            '{\"prefetchPriority\":0,\"countdownUiRelativeSecondsPrefetchCondition\":-3}}}}]},\"hasDecorated\":true}},\"contents\":{\"twoColumnWatchNextResults\":{\"results\":{\"results\":{\"contents\":[{\"videoPrimaryInfoRenderer\":{\"title\":{\"runs\":[{\"text\":\"'
        )[1]
        y = x.split('\"')[0]
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(z[0], download=False)
        URL = info['url']
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
        embed = discord.Embed(title='Şuanda oynatılan...',
                              description='',
                              colour=discord.Colour.blue())
        embed.set_footer(text='Made by h4yır#0001')
        embed.set_thumbnail(url='')
        embed.set_author(name='SoloBot', icon_url='')
        embed.add_field(name='**Oynatılan şarkı:**',
                        value=f'```{y}```',
                        inline=False)
        await ctx.send(embed=embed,
                       components=[[
                           Button(label='Dur', style=3, custom_id='dur'),
                           Button(label='Devam', style=3, custom_id='devam'),
                           Button(label='Kapat', style=4, custom_id='kapat')
                       ]])
        x = 1
        while True:
            if x == 1:
                await client.wait_for('button_click',
                                      check=lambda i: i.custom_id == 'dur')
                await dur(ctx)

                await client.wait_for('button_click',
                                      check=lambda i: i.custom_id == 'devam')
                await devam(ctx)

                await client.wait_for('button_click',
                                      check=lambda i: i.custom_id == 'kapat')
                await kapat(ctx)
            else:
                break


@client.command()
@commands.has_permissions(manage_channels=True)
async def nuke(ctx):

    channel = ctx.channel
    channel_position = channel.position

    a = await channel.clone()
    await channel.delete()
    await a.edit(position=channel_position, sync_permissions=True)
    await a.send('**Kanal Başarıyla Tekrardan Oluşturuldu!**')
    return

@client.command()
async def durum(ctx,*,durum):
  activity = discord.Game(name=f"{durum}", type=3)
  await client.change_presence(status=discord.Status.idle, activity=activity)

@client.command()
async def loop(ctx):
  if not loopunbabası.is_running():
    loopunbabası.start(ctx)
    await ctx.send('**Loop başlatıldı!!**')
  else:
    loopunbabası.stop()
    await ctx.send('**Loop kapatıldı!!**')

@client.command()
async def oynat(ctx, *, search):
    try:
        global z
        ğ = 0

        query_string = urllib.parse.urlencode({'search_query': search})
        htm_content = urllib.request.urlopen(
            'http://www.youtube.com/results?' + query_string)
        search_results = re.findall(r'/watch\?v=(.{11})',
                                    htm_content.read().decode())
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True', 'default_search':'auto', 'writeinfojson':'True'}
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
        try:
            z.remove(z[0])
        except Exception as e:
            print(e)
            pass
        z.append(search_results[0])
        if not voice.is_playing():
            r = requests.get(f'https://youtube.com/watch?v={z[0]}')
            j = r.content.decode()
            x = j.split(
                '{\"prefetchPriority\":0,\"countdownUiRelativeSecondsPrefetchCondition\":-3}}}}]},\"hasDecorated\":true}},\"contents\":{\"twoColumnWatchNextResults\":{\"results\":{\"results\":{\"contents\":[{\"videoPrimaryInfoRenderer\":{\"title\":{\"runs\":[{\"text\":\"'
            )[1]
            y = x.split('\"')[0]
            with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(z[0], download=False)
            URL = info['url']
            voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
            voice.is_playing()
            embed = discord.Embed(title='Şuanda oynatılan...',
                                  description='',
                                  colour=discord.Colour.blue())
            embed.set_footer(text='')  # istediğin bişey varsa yaz
            embed.set_thumbnail(url='')
            embed.set_author(name='SoloBot', icon_url='')
            embed.add_field(name='**Oynatılan şarkı:**',
                            value=f'```{y}```',
                            inline=False)
            await ctx.send(embed=embed)
            # eğer zaten oynatılıyordu
        else:
            if len(z) >= 1:
                r = requests.get(f'https://youtube.com/watch?v={z[0]}')
                j = r.content.decode()
                x = j.split(
                    '{\"prefetchPriority\":0,\"countdownUiRelativeSecondsPrefetchCondition\":-3}}}}]},\"hasDecorated\":true}},\"contents\":{\"twoColumnWatchNextResults\":{\"results\":{\"results\":{\"contents\":[{\"videoPrimaryInfoRenderer\":{\"title\":{\"runs\":[{\"text\":\"'
                )[1]
                y = x.split('\"')[0]
                z.append(search_results[0])
                embed = discord.Embed(title='Şarkı Sıraya Eklendi!',
                                      description='',
                                      colour=discord.Colour.blue())
                embed.set_footer(text='')  # istediğin bişey varsa yaz
                embed.set_thumbnail(url='')  # istediğin bişey varsa yaz
                embed.set_author(name='SoloBot')
                embed.add_field(name='**Sıraya eklendi**',
                                value=f'```Eklenen şarkı:{y}```',
                                inline=False)
                await ctx.send(embed=embed)
                try:
                    sıra.start(ctx, search)
                    return
                except:
                    pass
            else:
                z.append(search_results[0])
    except Exception as e:
        print(e)


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


# çeviri şeysileri


@client.command()
async def trs(ctx, *, arg):
    translator = Translator()
    translation = translator.translate(arg, dest="tr")
    embed = discord.Embed(title='Çeviri',
                          description='',
                          colour=discord.Colour.blue())
    embed.set_footer(text='Made by h4yır#0001')
    embed.set_thumbnail(url='')
    embed.set_author(name='SoloBot', icon_url='')
    embed.add_field(
        name='**Sonuç:**',
        value=
        f'```{translation.text} \n \n (Orijinal cümle: {translation.origin} ) \n (Şu dilden çevirildi: {translation.src} )```',
        inline=False)
    await ctx.channel.send(embed=embed)


@client.command()
async def trsr(ctx, *, arg):
    translator = Translator()
    x = arg.split(';')[-1]
    translation = translator.translate(arg.replace(";" + arg.split(";")[-1],
                                                   ""),
                                       dest=f"{x}")
    embed = discord.Embed(title='Çeviri',
                          description='',
                          colour=discord.Colour.blue())
    embed.set_footer(text='Made by h4yır#0001')
    embed.set_thumbnail(url='')
    embed.set_author(name='SoloBot', icon_url='')
    embed.add_field(
        name='**Sonuç:**',
        value=
        f'```{translation.text} \n \n (Orijinal cümle: {translation.origin} ) \n (Şu dilden çevirildi: {translation.src} )```',
        inline=False)
    await ctx.channel.send(embed=embed)


# mesaj silmece
@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
@has_permissions(manage_messages=True)
async def sil(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send("**Mesajlar silindi!**")

@client.command()
async def yt(ctx, *, search):

    query_string = urllib.parse.urlencode({'search_query': search})
    htm_content = urllib.request.urlopen('http://www.youtube.com/results?' +
                                         query_string)
    search_results = re.findall(r'/watch\?v=(.{11})',
                                htm_content.read().decode())
    await ctx.send(f'http://www.youtube.com/watch?v={search_results[0]}')

@client.command()
async def sr(ctx, sıra):
    try:
        r = requests.get(f'https://youtube.com/watch?v={z[int(sıra)-1]}')
        j = r.content.decode()
        x = j.split(
            '{\"prefetchPriority\":0,\"countdownUiRelativeSecondsPrefetchCondition\":-3}}}}]},\"hasDecorated\":true}},\"contents\":{\"twoColumnWatchNextResults\":{\"results\":{\"results\":{\"contents\":[{\"videoPrimaryInfoRenderer\":{\"title\":{\"runs\":[{\"text\":\"'
        )[1]
        y = x.split('\"')[0]
        await ctx.send(f'''```css
  Belirttiğiniz sıradaki şarkı: {y} ```''')
    except:
        await ctx.send('Belirttiğiniz sırada herhangi bir şarkı yok')

@tasks.loop(seconds=1)
async def loopunbabası(ctx):
  try:
    sıra.stop()
    try:
        global z
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        FFMPEG_OPTIONS = {
            'before_options':
            '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn'
        }
        voice = get(client.voice_clients, guild=ctx.guild)
        channel = ctx.message.author.voice.channel
        try:
            await voice.move_to(channel)
        except:
            pass
        if not voice.is_playing():
            r = requests.get(f'https://youtube.com/watch?v={z[0]}')
            j = r.content.decode()
            x = j.split(
                '{\"prefetchPriority\":0,\"countdownUiRelativeSecondsPrefetchCondition\":-3}}}}]},\"hasDecorated\":true}},\"contents\":{\"twoColumnWatchNextResults\":{\"results\":{\"results\":{\"contents\":[{\"videoPrimaryInfoRenderer\":{\"title\":{\"runs\":[{\"text\":\"'
            )[1]
            y = x.split('\"')[0]
            with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(z[0], download=False)
            URL = info['url']
            voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
            voice.is_playing()
            embed = discord.Embed(title='Şuanda oynatılan...',
                                  description='',
                                  colour=discord.Colour.blue())
            embed.set_footer(text='')  # istediğin bişey varsa yaz
            embed.set_thumbnail(url='')
            embed.set_author(name='SoloBot', icon_url='')
            embed.add_field(name='**Oynatılan şarkı:**',
                            value=f'```{y}```',
                            inline=False)
            await ctx.send(embed=embed)
        
    except Exception as e:
        print(e)    
  except:
      try:
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        FFMPEG_OPTIONS = {
            'before_options':
            '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn'
        }
        voice = get(client.voice_clients, guild=ctx.guild)
        channel = ctx.message.author.voice.channel
        try:
            await voice.move_to(channel)
        except:
            pass
        if not voice.is_playing():
            r = requests.get(f'https://youtube.com/watch?v={z[0]}')
            j = r.content.decode()
            x = j.split(
                '{\"prefetchPriority\":0,\"countdownUiRelativeSecondsPrefetchCondition\":-3}}}}]},\"hasDecorated\":true}},\"contents\":{\"twoColumnWatchNextResults\":{\"results\":{\"results\":{\"contents\":[{\"videoPrimaryInfoRenderer\":{\"title\":{\"runs\":[{\"text\":\"'
            )[1]
            y = x.split('\"')[0]
            with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(z[0], download=False)
            URL = info['url']
            voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
            voice.is_playing()
            embed = discord.Embed(title='Şuanda oynatılan...',
                                  description='',
                                  colour=discord.Colour.blue())
            embed.set_footer(text='')  # istediğin bişey varsa yaz
            embed.set_thumbnail(url='')
            embed.set_author(name='SoloBot', icon_url='')
            embed.add_field(name='**Oynatılan şarkı:**',
                            value=f'```{y}```',
                            inline=False)
            await ctx.send(embed=embed)
        
      except Exception as e:
        print(e)
        pass
@tasks.loop(seconds=1)
async def sıra(ctx, search):
    try:
        voice = get(client.voice_clients, guild=ctx.guild)
        if not voice.is_playing():
            if voice.is_connected() and len(z) >= 1:
                z.remove(z[0])
                x = 0
                query_string = urllib.parse.urlencode({'search_query': search})
                htm_content = urllib.request.urlopen(
                    'http://www.youtube.com/results?' + query_string)
                search_results = re.findall(r'/watch\?v=(.{11})',
                                            htm_content.read().decode())
                YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
                FFMPEG_OPTIONS = {
                    'before_options':
                    '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                    'options': '-vn'
                }
                voice = get(client.voice_clients, guild=ctx.guild)
                channel = ctx.message.author.voice.channel
                if voice.is_connected():
                    await voice.move_to(channel)
                else:
                    voice = await channel.connect()
                z.append(search_results[0])
                if not voice.is_playing():
                    with YoutubeDL(YDL_OPTIONS) as ydl:
                        info = ydl.extract_info(z[0], download=False)
                    URL = info['url']
                    voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
                    voice.is_playing()
                    r = requests.get(
                        f'https://youtube.com/watch?v={z[int(sıra)-1]}')
                    j = r.content.decode()
                    x = j.split(
                        '{\"prefetchPriority\":0,\"countdownUiRelativeSecondsPrefetchCondition\":-3}}}}]},\"hasDecorated\":true}},\"contents\":{\"twoColumnWatchNextResults\":{\"results\":{\"results\":{\"contents\":[{\"videoPrimaryInfoRenderer\":{\"title\":{\"runs\":[{\"text\":\"'
                    )[1]
                    y = x.split('\"')[0]
                    embed = discord.Embed(title='Şuanda oynatılan...',
                                          description='',
                                          colour=discord.Colour.blue())
                    embed.set_footer(text='Made by h4yır#0001')
                    embed.set_thumbnail(url='')
                    embed.set_author(name='SoloBot', icon_url='')
                    embed.add_field(name='**Oynatılan şarkı:**',
                                    value=f'```{y}```',
                                    inline=False)
                    await ctx.send(embed=embed,
                                   components=[[
                                       Button(label='Dur',
                                              style=3,
                                              custom_id='dur'),
                                       Button(label='Devam',
                                              style=3,
                                              custom_id='devam'),
                                       Button(label='Kapat',
                                              style=4,
                                              custom_id='kapat')
                                   ]])
                    x = 1
                    while True:
                        if x == 1:
                            await client.wait_for(
                                'button_click',
                                check=lambda i: i.custom_id == 'dur')
                            await dur(ctx)

                            await client.wait_for(
                                'button_click',
                                check=lambda i: i.custom_id == 'devam')
                            await devam(ctx)

                            await client.wait_for(
                                'button_click',
                                check=lambda i: i.custom_id == 'kapat')
                            await kapat(ctx)
                        else:
                          break
                else:
                  sıra.stop()
            else:
                sıra.stop()
    except Exception as e:
      if not '\'is_connected\'' or '\'is_playing\'' in str(e):
        print(e)
        pass
      else:
        sıra.stop()


keep_alive.keep_alive()
client.run(TOKEN)
