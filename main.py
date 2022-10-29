# encoding:utf-8
# Imports
import os
import qrcode
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
os.system("pip install openai")
import openai
from time import sleep
import gtts
import keep_alive
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
from roblox import Client
from roblox.thumbnails import AvatarThumbnailType
import json
import io
import contextlib

# Intents
intents = discord.Intents.all()
intents.members = True
intents.message_content = True
intents.presences = True

client = commands.Bot(command_prefix='+', intents=intents, help_command=None)

# Variables
with open('jsons/song_queue.json') as f:
  loading_json = f.read()
song_queue = json.loads(loading_json)
players = {}
evet = 'Evet'
hayır = 'Hayır'
eymen = discord.File('attachments/eymenifsa.jpg')
eymen2 = discord.File('attachments/eymenifsa1.jpg')
eymen3 = discord.File("attachments/eymenpipi.png")

# Lists
eymenifsa = [eymen, eymen2, eymen3]
karar = [evet, hayır]

# Fonksiyonlar

# Credentials
TOKEN = os.environ["token"]
spotoken = os.environ['spotoken']
openai.api_key = os.getenv("OPENAI_API_KEY")
robux = Client()



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
    if member.guild.id == 1015344885433372732:
        channel = client.get_channel(1015526727767838811)
        await channel.send(
            f"**<@{member.id}> adlı kullanıcı sunucuya katıldı** :tada:")
        await member.create_dm()
        await member.dm_channel.send(
            f"**Merhaba! Sunucumuza hoşgeldin! <@{member.id}>**")
    else:
        return


@client.event
async def on_member_remove(member):
    if member.guild.id == 1015344885433372732:
        channel = client.get_channel(1015526727767838811)
        await channel.send(
            f"**{member.name} adlı kullanıcı sunucudan ayrıldı** :sob:")
    else:
        return


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.BotMissingPermissions):
        a = await ctx.send('Hata: Botun bunu yapmaya yetkisi yok')
        sleep(3)
        await a.delete()
    elif isinstance(error, commands.CheckFailure):
        a = await ctx.send(f'Üzgünüm dostum... Bu komutu kullanamazsın...')
        sleep(3)
        await a.delete()
      
    elif isinstance(error, commands.MissingPermissions):
        a = await ctx.send(
            f'Hata: Üzgünüm <@{ctx.author.id}>, bunu yapmaya yetkin yok')
        sleep(3)
        await a.delete()

    elif isinstance(error, commands.CommandNotFound):
        a = await ctx.reply(f'Hata: Böyle bir komut yok!')
        sleep(3)
        await a.delete()

    elif isinstance(error, commands.CommandOnCooldown):
        a = await ctx.send(f'Hata: {error}')
        sleep(3)
        await a.delete()
    elif isinstance(error, commands.UserNotFound):
        a = await ctx.send(f'Hata: Kullanıcı bulunamadı!')
        sleep(3)
        await a.delete()
    elif isinstance(error, commands.errors.MissingRequiredArgument):
        a = await ctx.send(
            f'Hata: Yanlış kullanım! Gerekli argümanları giriniz!')
        sleep(3)
        await a.delete()
    
@client.event
async def on_message_delete(message):
  if message.guild.id == 1015344885433372732 and message.author.id != client.user.id:
    with open('txts/silinenmesajlar.txt','w+') as f:
      try:
        f.write(f'{message.content}\n{message.created_at}\n{message.author.id}')
      except Exception as e:
        print(e)
      print('Ok!')

@client.event
async def on_message_edit(before,after):
  if after.guild.id == 1015344885433372732 and after.author.id != client.user.id:
    with open('txts/editlenenmesajlar.txt','w+') as f:
      f.write(f'{before.content}\n{after.content}\n{after.author.id}')
    print('Ok!')
    
@client.event
async def on_message(message):
    if message.content.lower() == 'sa':
        await message.channel.send('Aleyküm Selam')

    if message.content.lower() == 'anamın ruhunu ortaya koyuyorum':
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/816599222417621005/904057052610060368/yt5s.com-Anamn_ruhunu_ortaya_koyuyorum-240p.mp4'
        )

    if message.content.lower() == 'yunus ifşa':
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/818555613108764723/913426756730511361/sketch-1637599477924.png'
        )

    if message.content == '<@901414164289961986>':
        await message.channel.send(
            'Hey dostum! Prefixim \' + \'. Belki ihtiyacın olur diye yani...')

    if message.content.lower() == 'Merhaba':
        await message.reply('Merhaba!')

    if message.content.lower() == 'maraşlı ifşa':
        await message.reply(file=discord.File("attachments/marasliifsa.jpg"))

    if message.content.lower() == 'yusuf ifşa':
        await message.channel.send(
            'https://media.discordapp.net/attachments/843145381118345247/872096405076983848/Screenshot_2021-08-03-15-38-15_1.jpg'
        )

    if message.content.lower() == 'eymen ifşa':
        await message.channel.send(file=random.choice(eymenifsa))
    await client.process_commands(message)


# commands
@client.command()
async def yardım(ctx,help = None):
  if help == None:
    embed = discord.Embed(
        title=' ',
        description=
        ' ',
        colour=discord.Colour.blue())
    embed.add_field(name='Yardım Komutları', value='**<a:mod:1028649041619320932>     Moderatör Komutları: +yardım mod\n\n<a:music:1028648378638290994>     Müzik Komutları: +yardım muzik\n\n<a:eglence:1028649336873160824>     Eğlence Komutları: +yardım eglence**')
    embed.set_footer(
        text='Bu komut {} tarafından kullanıldı!'.format(ctx.author.name))
    await ctx.send(embed=embed)
  elif help.lower() == "mod":
    embed = discord.Embed(title=' ',
                          description='',
                          colour=discord.Colour.blue())
    embed.set_footer(text='Umarım yardımcı olmuştur.')
    embed.add_field(
        name='Komutlar:',
        value=
        '```+sil: Belirttiğiniz kadar mesaj siler.\n\n+kick: Etiketlenen kişiyi atar.\n\n+ban: Etiketlenen kişiyi banlar.\n\n+unban: İsmi ve etiketi yazılan kişinin banını kaldırır.\n\n+nick: Etiketlediğiniz kişinin nickini değiştirir.```',
        inline=False)
    await ctx.send(embed=embed)
  elif help.lower() == "muzik":
    embed = discord.Embed(title=' ',
                          description='',
                          colour=discord.Colour.blue())
    embed.set_footer(text='Umarım yardımcı olmuştur.')
    embed.add_field(
        name='Komutlar:',
        value=
        '```+oynat: Yazdığınız şarkıyı oynatır.\n\n+dur: Şarkıyı duraklatır.\n\n+devam: Şarkıyı devam ettirir.\n\n+kapat: Şarkıyı temelli kapatır.\n\n+s: Çalınan şarkıyı atlar.\n\n+sr: Yazdığınız sırada hangi şarkının olduğunu söyler.\n\n+loop: Çalınan şarkıyı loopa sokar.\n\n+tts: Bot bulunduğunuz ses kanalına gelip yazdığınız şeyi okur.\n\n+yt: Yazdığınız şeyi youtube\'de aratır ve çıkan sonucu size söyler.```',
        inline=False)
    await ctx.send(embed=embed)
  elif help.lower() == "eglence":
    embed = discord.Embed(title=' ',
                          description='',
                          colour=discord.Colour.blue())
    embed.set_footer(text='Umarım yardımcı olmuştur.')
    embed.add_field(
        name='Komutlar:',
        value=
        '```+trs: Başka bir dili türkçeye çevirir.\n\n+trsr: Herhangi bir dili seçtiğiniz dile çevirir.\n\n+rfoto: Rastgele bir fotoğraf atar.\n\n+xox: Etiketlediğiniz kişi ile xox oynarsınız.\n\n+instapp: Yazdığınız instagram hesabının profil fotoğrafını atar.\n\n+mcbaşarım: Yazdığınız şeyi minecraft başırımı gibi editler.\n\n+pfp: Etiketlenen kişinin profil fotosunu atar.Kimseyi etiketlemezseniz sizinkini atar.\n\n+mesajyaz: Etiketlediğiniz kişinin yerine mesaj yazarsınız.\n\n+sayıtahmin: Sayı tahmin oyunu oynarsınız.\n\n+tts: Bot bulunduğunuz ses kanalına gelip yazdığınız metni okur```',
        inline=False)
    await ctx.send(embed=embed)

@client.command(aliases=["commands"])
async def help(ctx, yardim = None):
  if yardim == None:
    embed = discord.Embed(
        title=' ',
        description=
        ' ',
        colour=discord.Colour.blue())
    embed.add_field(name='Help Commands', value='**<a:mod:1028649041619320932>     Mod Commands: +help mod\n\n<a:music:1028648378638290994>     Music Commands: +help music\n\n<a:eglence:1028649336873160824>     Fun Commands: +help fun**')
    embed.set_footer(
        text='This command used by {}!'.format(ctx.author.name))
    await ctx.send(embed=embed)
  elif yardim.lower() == "mod":
    embed = discord.Embed(title=' ',
                          description='',
                          colour=discord.Colour.blue())
    embed.set_footer(text='Hope this helps.')
    embed.add_field(
        name='Commands:',
        value=
        '```+purge: Deletes the messages.\n\n+kick: Kicks a user.\n\n+ban: Bans a member.\n\n+unban: Unbans a user.\n\n+nick: Changes nickname of a member.```',
        inline=False)
    await ctx.send(embed=embed)
  elif yardim.lower() == "music":
    embed = discord.Embed(title=' ',
                          description='',
                          colour=discord.Colour.blue())
    embed.set_footer(text='Hope this helps.')
    embed.add_field(
        name='Komutlar:',
        value=
        '```+play: Plays a song.\n\n+pause: Pauses the song.\n\n+continue: Continues the song.\n\n+stop: Stops the song and disconnects from voice channel.\n\n+skip: Skips the song.\n\n+queue: Shows the queue.\n\n+loop: Loops the song.\n\n+tts: Bot joins the voice channel and tells that what you wrote.\n\n+yt: Searches a song on youtube.```',
        inline=False)
    await ctx.send(embed=embed)
  elif yardim.lower() == "fun":
    embed = discord.Embed(title=' ',
                          description='',
                          colour=discord.Colour.blue())
    embed.set_footer(text='Hope this helps.')
    embed.add_field(
        name='Komutlar:',
        value=
        '```+rfoto: Sends a random photo.\n\n+xox: Starts a xox game with you and the person who you pinged.\n\n+instapp: Sends the profile picture of a instagram account.\n\n+achievement: M-Minecraft achievements???\n\n+pfp: Sends the profile picture of person who you pinged.\n\n+fakemessage: Writes a fake message.\n\n+guess: Guess the number game.\n\n+botinfo: Info about SoloBot.\n\n+userinfo: Info about a member.```',
        inline=False)
    await ctx.send(embed=embed)


@client.command()
async def botinfo(ctx):
  kisiler = 0
  for k in client.guilds:
    kisiler = kisiler + len(k.members)
  solo= ctx.guild.me

  embed = discord.Embed(title="SoloBot hakkında bazı bilgiler.", description=f"**Bot: \tSoloBot\n\nKaç adet sunucuya hizmet veriyor:\t{len(client.guilds)}\n\nKaç adet üyeye hizmet veriyor:\t{kisiler}\n\nOluşturulma tarihi:\t{client.user.created_at}\n\nSunucuya katılma tarihi:\t{solo.joined_at}**",colour= discord.Colour.blurple())
  await ctx.reply(embed=embed)

@client.command()
async def userinfo(ctx, kisi: discord.User = None):
  try:
    if kisi == None:
      kisi = ctx.author
    lol = ctx.guild.get_member(kisi.id)
    embed = discord.Embed(title="{} hakkında bazı bilgiler.".format(kisi.name), description=f"**Nickname: {kisi.name}\n\nBot mu?:\t{kisi.bot}\n\nDurumu:\t{lol.status}\n\nHesabın oluşturulma tarihi:\t{kisi.created_at}\n\nSunucuya katılma tarihi:\t{lol.joined_at}**",colour= discord.Colour.blurple())
    embed.set_thumbnail(url=kisi.avatar.url)
    await ctx.reply(embed=embed)
  except Exception as e:
    print(e)

@client.command()
async def qr(ctx,*,arg):
  qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 100,
    border = 4
  )
  qr.add_data(f'{arg}')
  qr.make(fit=True)

  kod = qr.make_image(fill_color=(0,0,0),back_color='white')
  kod.save('qrcode.png')
  await ctx.send(file=discord.File('qrcode.png'))
  sleep(1)
  os.remove('qrcode.png')

@client.command()
async def sb(ctx,*,metin):
  try:
    with open('txts/history.txt') as f:
      gecmislist = f.read()
    gecmis = gecmislist
    response = openai.Completion.create(model=f"text-davinci-002", prompt=f"{gecmis}{ctx.author.name}"+" "+metin+"\nSoloBot:", temperature=1.0, max_tokens=150)
    if "my" in metin.lower():
      with open('txts/history.txt','w+') as f:
        if "my" in metin.lower():
          f.write(f"{gecmis}{ctx.author.name}: {metin}\nSoloBot:{response.choices[0].text}\n\n")
    else:
      pass
    print(response.choices[0].text)
    await ctx.reply(response.choices[0].text.capitalize())
  except Exception as e:
    print(e)

@client.command()
async def snipe(ctx):
  mesaj = ""
  with open('txts/silinenmesajlar.txt') as f:
    a = f.readlines()
  for i in a:
    if i == a[-1] or i == a[-2]:
      pass
    else:
      mesaj = mesaj+i
  uye = ctx.guild.get_member(int(a[-1]))
  embed = discord.Embed(title="Son silinen mesaj", description=f"{mesaj}\n{a[-2]}",colour= discord.Colour.blurple())
  embed.set_author(name=uye.name+"#"+str(uye.discriminator),icon_url=uye.avatar.url)
  await ctx.send(embed=embed)

@client.command()
async def sniper(ctx):
  mesaj = ""
  with open('txts/editlenenmesajlar.txt') as f:
    a = f.readlines()
  for i in a:
    if i == a[-1] or i == a[-2]:
      pass
    else:
      mesaj = mesaj+i
    messaj = mesaj.split('\n')[0]
  uye = ctx.guild.get_member(int(a[-1]))
  embed = discord.Embed(title=" ", description=f" ",colour= discord.Colour.blurple())
  embed.add_field(name=f'Son editlenen mesaj', value=f'~~{messaj}~~\n\n{a[-2]}', inline=False)
  embed.set_author(name=uye.name+"#"+str(uye.discriminator),icon_url=uye.avatar.url)
  await ctx.send(embed=embed)  

@client.command()
async def id(ctx,emoji):
  for emo in ctx.guild.emojis:
    if emo.name == emoji:
      await ctx.reply(emo.id)
    else:
      pass

@client.command(aliases=["fakemessage"])
async def mesajyaz(ctx, kişi: discord.User, *, mesaj):
    try:
        await ctx.message.delete()
        webhook = await ctx.channel.create_webhook(name=kişi.name)
        await webhook.send(content=mesaj,
                           username=kişi.name,
                           avatar_url=kişi.avatar.url,
                           wait=True)
        await webhook.delete()
    except Exception as e:
        print(e)


async def is_owner(ctx):
    return ctx.author.id == 921084920116437002 or ctx.author.id == 733002439279640577


@client.command()
@commands.check(is_owner)
async def eval(ctx, *, code):
  stdout = io.StringIO()

  try:
    with contextlib.redirect_stdout(stdout):
      exec(code)
      result = stdout.getvalue()
      if len(result) != 0:
        embed = discord.Embed(title="Kodunuzun çıktısı:",description=f"```py\n{result}```",colour= discord.Colour.dark_blue())
      else:
        embed = discord.Embed(title="Kodunuzun çıktısı:",description=f"```Kodunuzun herhangi bir çıktısı olmadı.```",colour= discord.Colour.dark_blue())
      await ctx.reply(embed=embed)
  except Exception as e:
    print(e)
    embed = discord.Embed(title="Kodunuzun çıktısı:",description=f"```py\n{e}```",colour= discord.Colour.dark_theme())
    await ctx.reply(embed=embed)
    pass


@client.command()
async def rb(ctx, kisi):
    try:
        user = await robux.get_user_by_username(username=kisi)
        user_thumbnails = await robux.thumbnails.get_user_avatar_thumbnails(
            users=[user], type=AvatarThumbnailType.full_body, size=(720, 720))
        embed = discord.Embed(title='Roblox Information',
                              description='',
                              colour=discord.Colour.red())
        embed.set_thumbnail(
            url=str(user_thumbnails[0]).split("image_url='")[1].split("'")[0])
        embed.add_field(
            name='Information about {}'.format(kisi),
            value=
            f'\nKullanıcı Adı: **{user.name}**\n\nGörüntülenen Ad: **{user.display_name}**\n\nHesabın açıklaması: **{user.description}**\n\nHesap banlı mı?: **{user.is_banned}**\n\nHesabın oluşturulma zamanı: **{user.created}**'
        )
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(e)


@client.command()
async def rfoto(ctx):
    a = random.randint(1, 1000)
    embed = discord.Embed(title='Rastgele Foto!',
                          colour=discord.Colour.random())
    embed.set_image(url=f'https://source.unsplash.com/random?={a}')
    embed.set_footer(text=f'Bu komut {ctx.author.name} tarafından kullanıldı!')
    await ctx.send(embed=embed)


@client.command()
@commands.check(is_owner)
async def ayrıl(ctx, guild_id):
    await client.get_guild(int(guild_id)).leave()
    await ctx.send(f"Ayrıldım: {guild_id}")


@client.command()
async def xox(ctx, oyuncu2: discord.Member = None):
    if oyuncu2.id == client.user.id:
        await ctx.send(
            'D-Dostum sanırım oynamak için gerçek birini etiketlemen lazım...')
        return
    elif oyuncu2.id == ctx.author.id:
        await ctx.send(
            'Tamam kanka kendi kendine oynadın şuan... Başkasıyla beraber oynamaya ne dersin? '
        )
        return
    taht = ':white_large_square:'
    taht2 = ':white_large_square:'
    taht3 = ':white_large_square:'
    taht4 = ':white_large_square:'
    taht5 = ':white_large_square:'
    taht6 = ':white_large_square:'
    taht7 = ':white_large_square:'
    taht8 = ':white_large_square:'
    taht9 = ':white_large_square:'
    await ctx.send(
        f'Hey <@{oyuncu2.id}>! {ctx.author.name} seni bir xox oyununa davet etti, katılmak ister misin?'
    )
    try:
        red_kabul = await client.wait_for(
            'message',
            check=lambda message: message.author.id == oyuncu2.id,
            timeout=30)

        if red_kabul.content.lower() == 'evet':
            xox = await ctx.send('{}\n{}\n{}'.format(taht + taht2 + taht3,
                                                     taht4 + taht5 + taht6,
                                                     taht7 + taht8 + taht9))
            await ctx.send(
                f'<@{ctx.author.id}> senin sıran! Oynamak için 1-9 arasında bir sayı söyle!'
            )
            sonihtimal = 0
            while True:
                if taht == ':x:' and taht2 == ':x:' and taht3 == ':x:' or taht == ':x:' and taht4 == ':x:' and taht7 == ':x:' or taht == ':x:' and taht5 == ':x:' and taht9 == ':x:' or taht4 == ':x:' and taht5 == ':x:' and taht6 == ':x:' or taht7 == ':x:' and taht8 == ':x:' and taht9 == ':x:' or taht2 == ':x:' and taht5 == ':x:' and taht8 == ':x:' or taht3 == ':x:' and taht6 == ':x:' and taht9 == ':x:' or taht3 == ':x:' and taht5 == ':x:' and taht7 == ':x:':
                    await ctx.send(f'<@{oyuncu2.id}> KAZANDI!')
                    return
                elif taht == ':o:' and taht2 == ':o:' and taht3 == ':o:' or taht == ':o:' and taht4 == ':o:' and taht7 == ':o:' or taht == ':o:' and taht5 == ':o:' and taht9 == ':o:' or taht4 == ':o:' and taht5 == ':o:' and taht6 == ':o:' or taht7 == ':o:' and taht8 == ':o:' and taht9 == ':o:' or taht2 == ':o:' and taht5 == ':o:' and taht8 == ':o:' or taht3 == ':o:' and taht6 == ':o:' and taht9 == ':o:' or taht3 == ':o:' and taht5 == ':o:' and taht7 == ':o:':
                    await ctx.send(f'<@{ctx.author.id}> KAZANDI!')
                    return
                if sonihtimal == 9:
                    await ctx.send('Hiç kimse kazanamadı! Oyun berabere bitti!'
                                   )
                    return
                o1 = await client.wait_for(
                    'message',
                    check=lambda msg: msg.author.id == ctx.author.id,
                    timeout=25)
                sonihtimal = sonihtimal + 1
                if int(o1.content) == 1:
                    if taht != ':x:' or taht != ':o:':
                        taht = ':o:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o1.content) == 2:
                    if taht != ':x:' or taht != ':o:':
                        taht2 = ':o:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o1.content) == 3:
                    if taht != ':x:' or taht != ':o:':
                        taht3 = ':o:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o1.content) == 4:
                    if taht != ':x:' or taht != ':o:':
                        taht4 = ':o:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o1.content) == 5:
                    if taht != ':x:' or taht != ':o:':
                        taht5 = ':o:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o1.content) == 6:
                    if taht != ':x:' or taht != ':o:':
                        taht6 = ':o:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o1.content) == 7:
                    if taht != ':x:' or taht != ':o:':
                        taht7 = ':o:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o1.content) == 8:
                    if taht != ':x:' or taht != ':o:':
                        taht8 = ':o:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o1.content) == 9:
                    if taht != ':x:' or taht != ':o:':
                        taht9 = ':o:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                if taht == ':x:' and taht2 == ':x:' and taht3 == ':x:' or taht == ':x:' and taht4 == ':x:' and taht7 == ':x:' or taht == ':x:' and taht5 == ':x:' and taht9 == ':x:' or taht4 == ':x:' and taht5 == ':x:' and taht6 == ':x:' or taht7 == ':x:' and taht8 == ':x:' and taht9 == ':x:' or taht2 == ':x:' and taht5 == ':x:' and taht8 == ':x:' or taht3 == ':x:' and taht6 == ':x:' and taht9 == ':x:' or taht3 == ':x:' and taht5 == ':x:' and taht7 == ':x:':
                    await ctx.send(f'<@{oyuncu2.id}> KAZANDI!')
                    return
                elif taht == ':o:' and taht2 == ':o:' and taht3 == ':o:' or taht == ':o:' and taht4 == ':o:' and taht7 == ':o:' or taht == ':o:' and taht5 == ':o:' and taht9 == ':o:' or taht4 == ':o:' and taht5 == ':o:' and taht6 == ':o:' or taht7 == ':o:' and taht8 == ':o:' and taht9 == ':o:' or taht2 == ':o:' and taht5 == ':o:' and taht8 == ':o:' or taht3 == ':o:' and taht6 == ':o:' and taht9 == ':o:' or taht3 == ':o:' and taht5 == ':o:' and taht7 == ':o:':
                    await ctx.send(f'<@{ctx.author.id}> KAZANDI!')
                    return
                if sonihtimal == 9:
                    await ctx.send('Hiç kimse kazanamadı! Oyun berabere bitti!'
                                   )
                    return
                o2 = await client.wait_for(
                    'message',
                    check=lambda msg: msg.author.id == oyuncu2.id,
                    timeout=25)
                sonihtimal = sonihtimal + 1
                if int(o2.content) == 1:
                    if taht != ':x:' or taht != ':o:':
                        taht1 = ':x:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht1 + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o2.content) == 2:
                    if taht != ':x:' or taht != ':o:':
                        taht2 = ':x:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o2.content) == 3:
                    if taht != ':x:' or taht != ':o:':
                        taht3 = ':x:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o2.content) == 4:
                    if taht != ':x:' or taht != ':o:':
                        taht4 = ':x:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o2.content) == 5:
                    if taht != ':x:' or taht != ':o:':
                        taht5 = ':x:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o2.content) == 6:
                    if taht != ':x:' or taht != ':o:':
                        taht6 = ':x:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o2.content) == 7:
                    if taht != ':x:' or taht != ':o:':
                        taht7 = ':x:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o2.content) == 8:
                    if taht != ':x:' or taht != ':o:':
                        taht8 = ':x:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o2.content) == 9:
                    if taht != ':x:' or taht != ':o:':
                        taht9 = ':x:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))

        elif red_kabul.content.lower() == 'hayır':
            await ctx.send(
                'Davet ettiğin kişi oyuna katılmayı kabul etmedi! Maç iptal edildi!'
            )
            return

        else:
            pass
    except ValueError:
        pass
    except Exception as e:
        print(e)
        pass


@client.command()
async def serverinfo(ctx):
    yk = len(ctx.guild.text_channels)
    sk = len(ctx.guild.voice_channels)
    k = len(ctx.guild.channels)
    ü = len(ctx.guild.members)
    s = ctx.guild.owner.name
    vr = ctx.guild.verification_level
    embed = discord.Embed(title='Sunucu Info', colour=discord.Colour.random())
    embed.add_field(
        name=f'{ctx.guild.name} sunucusu hakkında bilgiler',
        value=
        f':white_small_square: Sunucu sahibi: {s} :white_small_square: \n \n :white_small_square: Sunucudaki üye sayısı {ü} :white_small_square: \n \n :white_small_square: Toplam kanal sayısı: {k} :white_small_square: \n \n :white_small_square: Toplam metin kanalı sayısı: {yk} :white_small_square: \n \n :white_small_square: Toplam ses kanalı sayısı: {sk} :white_small_square: \n \n :white_small_square: Sunucu doğrulaması: {vr} :white_small_square:'
    )
    embed.set_footer(text=f'Bu komut {ctx.author.name} tarafından kullanıldı!')
    await ctx.send(embed=embed)


@client.command(aliases=["achievement"])
async def mcbaşarım(ctx, *, msg):
    embed = discord.Embed(title='Minecraft Başarım',
                          colour=discord.Colour.random())
    embed.set_image(
        url=
        'https://minecraftskinstealer.com/achievement/1/Basarim+Kazanildi%21/'
        + msg)
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


@client.command(aliases=["guess"])
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
async def yolla(ctx):
    if ctx.author.id == 921084920116437002:
        await ctx.send('<a:rickroll:1016265373919760406>')
    else:
        return


@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, üye: discord.Member, *, neden=None):
    if üye.id == client.user.id:
        await ctx.send(
            'Tamam kanka şuan kendimi banladım. Başkasını banlamaya ne dersin?'
        )
    elif üye.id == ctx.author.id:
        await ctx.reply(
            'Bak kardeşim... Son pişmanlık fayda etmez diyorum.. Emin misin?')
        zort = await client.wait_for(
            'message',
            check=lambda msg: ctx.author.id == msg.author.id,
            timeout=50)
        if zort.content.lower() == 'evet':
            await üye.ban(reason='intihar... kendini banlattı..')
            await ctx.send('https://youtu.be/2agdQzh_zSk?t=72')
        else:
            return
    else:
        await üye.ban(reason=neden)
        await ctx.send(
            f'**{üye.name} adlı kullanıcı {neden} nedeniyle {ctx.author.name} tarafından banlandı**'
        )


@client.command()
@has_permissions(ban_members=True)
async def unban(ctx, *, üye):
    banlılar = await ctx.guild.bans()
    üye_nick, üye_tag = üye.split('#')

    for i in banlılar:
        bismillah = i.user

        if (bismillah.name, bismillah.discriminator) == (üye_nick, üye_tag):
            await ctx.guild.unban(bismillah)
            await ctx.reply(f'{bismillah} kullanıcısının banı kaldırıldı!')


@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, üye: discord.Member, *, neden=None):
    if üye.id == client.user.id:
        await ctx.send(
            'Tamam kanka şuan kendimi attım. Başkasını atmaya ne dersin?')
    elif üye.id == ctx.author.id:
        await ctx.reply(
            'Bak kardeşim... Son pişmanlık fayda etmez diyorum.. Emin misin?')
        zort = await client.wait_for(
            'message',
            check=lambda msg: ctx.author.id == msg.author.id,
            timeout=50)
        if zort.content.lower() == 'evet':
            await üye.kick(reason='intihar... kendini banlattı..')
            await ctx.send('https://youtu.be/2agdQzh_zSk?t=72')
        else:
            return
    else:
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


@client.command(aliases=["avatar","pp"])
async def pfp(ctx, arg: discord.Member = None):
    if not arg == None:
        pfp = arg.avatar.url
        embed = discord.Embed(title="Profil Fotoğrafı",
                              description='{}'.format(arg.mention),
                              color=0xecce8b)
        embed.set_image(url=(pfp))
        await ctx.send(embed=embed)
    else:
        arg = ctx.author
        pfp = arg.avatar.url
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


@client.command(aliases=["skip"])
async def s(ctx):
    
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {
        'before_options':
        '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn'
    }
    voice = get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    with YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(song_queue[str(ctx.guild.id)][1], download=False)
    URL = info['url']
    TITLE = info['title']
    thumb = info['thumbnails'][0]
    videofoto = thumb['url']
    sure = info['duration']
    kanal = info['uploader']
    videoizlen = info['view_count']
    videolike = info['like_count']
    suremin = sure // 60
    suresec = sure % 60
    if suresec < 10:
        suresec = f'0{suresec}'
    if suremin < 10:
        suremin = f'0{suremin}'
    voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    voice.is_playing()
    embed = discord.Embed(title='Şuanda oynatılan...',
                          description='',
                          colour=discord.Colour.default())
    embed.set_footer(
        text=f'İzlenme sayısı:{videoizlen}\nLike sayısı:{videolike}')
    embed.set_thumbnail(url=videofoto)
    embed.add_field(
        name=kanal,
        value=
        f'```{TITLE}\n\n00:00 ------------------------- {suremin}:{suresec}```',
        inline=False)
    await ctx.send(embed=embed)
    voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    voice.is_playing()
    del song_queue[str(ctx.guild.id)][0]


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
async def durum(ctx, *, durum):
    if is_owner(ctx=ctx):

        activity = discord.Game(name=f"{durum}", type=3)
        await client.change_presence(status=discord.Status.idle,
                                     activity=activity)
    else:
        await ctx.send(
            'N-Ne yapmaya çalışıyorsun k-kanka... Böyle bir komut yok ki...')


@client.command()
async def loop(ctx):
    if not loopunbabası.is_running():
        loopunbabası.start(ctx)
        await ctx.send('**Loop başlatıldı!!**')
    else:
        loopunbabası.stop()
        await ctx.send('**Loop kapatıldı!!**')


@client.command(aliases=["play"])
async def oynat(ctx, *, search):
    try:
        mesaj = await ctx.send('**Video aranıyor...**')
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
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        if not voice.is_playing():
            try:
                del song_queue[str(ctx.guild.id)][0]
            except KeyError as e:
              print(e)
              song_queue[str(ctx.guild.id)] = []
            finally:
                song_queue[str(ctx.guild.id)] = song_queue[str(ctx.guild.id)] + [f'{search_results[0]}']
            await mesaj.edit(content='**Video bilgisi alınıyor...**')
            with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(song_queue[str(ctx.guild.id)][0], download=False)
            URL = info['url']
            TITLE = info['title']
            thumb = info['thumbnails'][0]
            videofoto = thumb['url']
            sure = info['duration']
            kanal = info['uploader']
            videoizlen = info['view_count']
            videolike = info['like_count']
            suremin = sure // 60
            suresec = sure % 60
            if suresec < 10:
                suresec = f'0{suresec}'
            if suremin < 10:
                suremin = f'0{suremin}'
            voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
            voice.is_playing()
            await mesaj.delete()
            embed = discord.Embed(title='Şuanda oynatılan...',
                                  description='',
                                  colour=discord.Colour.default())
            embed.set_footer(
                text=f'İzlenme sayısı:{videoizlen}\nLike sayısı:{videolike}')
            embed.set_thumbnail(url=videofoto)
            embed.add_field(
                name=kanal,
                value=
                f'```{TITLE}\n\n00:00 ------------------------- {suremin}:{suresec}```',
                inline=False)
            del song_queue[str(ctx.guild.id)][0]
            await ctx.send(embed=embed)
            # eğer zaten oynatılıyordu
        else:
                song_queue[str(ctx.guild.id)] = song_queue[str(ctx.guild.id)] + [f'{search_results[0]}']
                with YoutubeDL(YDL_OPTIONS) as ydl:
                    info = ydl.extract_info(song_queue[str(ctx.guild.id)][-1], download=False)
                TITLE = info['title']
                embed = discord.Embed(title='Şarkı Sıraya Eklendi!',
                                      description='',
                                      colour=discord.Colour.default())
                embed.set_footer(text='')  # istediğin bişey varsa yaz
                embed.set_thumbnail(url='')  # istediğin bişey varsa yaz
                embed.add_field(name='**Sıraya eklendi**',
                                value=f'```Eklenen şarkı:{TITLE}```',
                                inline=False)
                await ctx.send(embed=embed)
                try:
                    sıra.start(ctx, search)
                    return
                except:
                    pass
    except Exception as e:
        print(e)


# durdurulmuş şarkıyı devam ettirme
@client.command(aliases=["continue"])
async def devam(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        voice.resume()
        await ctx.send('**Şarkı kaldığı yerden devam ediyor...**')


# duraklatır bir süreliğine
@client.command(aliases=["stop"])
async def dur(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
        await ctx.send('**Şarkı durduruldu...**')


# durdurur
@client.command(aliases=["close","disconnect"])
async def kapat(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        song_queue[str(ctx.guild.id)][0] = []
        voice.stop()
        voice = await ctx.voice_client.disconnect()        
        await ctx.send('**Kapatılıyor...**')
    else:
        voice = await ctx.voice_client.disconnect()


# mesaj silmece
@client.command(aliases=["purge","delete"])
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
async def spotify(ctx, *, search):
  sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_secret='e42352bdc1994ee9b66f1fa392fe366f',client_id='19783e5c318e4bd2ad943db0f6acee4c'))
  tracks= sp.search(q=search, type='track')
  sonuç = tracks['tracks']['items'][0]['external_urls']['spotify']
  sonuçname = tracks['tracks']['items'][0]['name']
  thumbnail = tracks['tracks']['items'][0]['album']['images'][0]['url']
  artist = tracks['tracks']['items'][0]['artists'][0]['name']
  embed = discord.Embed(title='Spotify Search',description='',colour=discord.Colour.default())
  embed.add_field(name=artist,value=f'Here is the result for [{sonuçname}]({sonuç})',inline=False)
  embed.set_thumbnail(url=thumbnail)
  await ctx.reply(embed=embed)

@client.command(aliases=["queue","sıra"])
async def sr(ctx):
    queue = ''
    sira = 1
    if len(song_queue[str(ctx.guild.id)]) != 0:
        for i in song_queue[str(ctx.guild.id)]:
            if not i == song_queue[str(ctx.guild.id)][-1]:
                r = requests.get(f'https://youtube.com/watch?v={i}')
                j = r.content.decode()
                x = j.split(
                    '{\"prefetchPriority\":0,\"countdownUiRelativeSecondsPrefetchCondition\":-3}}}}]},\"hasDecorated\":true}},\"contents\":{\"twoColumnWatchNextResults\":{\"results\":{\"results\":{\"contents\":[{\"videoPrimaryInfoRenderer\":{\"title\":{\"runs\":[{\"text\":\"'
                )[1]
                y = x.split('\"')[0]
                queue = queue + f'{sira} - {y} \n- [https://youtube.com/watch?v={i}] \n \n'
                sira = sira + 1
            else:
                r = requests.get(f'https://youtube.com/watch?v={i}')
                j = r.content.decode()
                x = j.split(
                    '{\"prefetchPriority\":0,\"countdownUiRelativeSecondsPrefetchCondition\":-3}}}}]},\"hasDecorated\":true}},\"contents\":{\"twoColumnWatchNextResults\":{\"results\":{\"results\":{\"contents\":[{\"videoPrimaryInfoRenderer\":{\"title\":{\"runs\":[{\"text\":\"'
                )[1]
                y = x.split('\"')[0]
                queue = queue + f'{sira} - {y} \n- [https://youtube.com/watch?v={i}]'
                sira = sira + 1
        await ctx.send(f'''```diff
{queue}```''')
    else:
        await ctx.send('Sırada hiç şarkı yok.')


@tasks.loop(seconds=1)
async def loopunbabası(ctx):
    try:
        sıra.stop()
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
                with YoutubeDL(YDL_OPTIONS) as ydl:
                    info = ydl.extract_info(song_queue[str(ctx.guild.id)][0], download=False)
                URL = info['url']
                TITLE = info['title']
                thumb = info['thumbnails'][0]
                videofoto = thumb['url']
                sure = info['duration']
                kanal = info['uploader']
                videoizlen = info['view_count']
                videolike = info['like_count']
                suremin = sure // 60
                suresec = sure % 60
                if suresec < 10:
                    suresec = f'0{suresec}'
                if suremin < 10:
                    suremin = f'0{suremin}'
                voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
                voice.is_playing()
                embed = discord.Embed(title='Şuanda oynatılan...',
                                      description='',
                                      colour=discord.Colour.default())
                embed.set_footer(
                    text=
                    f'İzlenme sayısı:**{videoizlen}**\nLike sayısı:{videolike}'
                )
                embed.set_thumbnail(url=videofoto)

                embed.add_field(
                    name=kanal,
                    value=
                    f'```{TITLE}\n\n00:00 ------------------------- {suremin}:{suresec}```',
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
                with YoutubeDL(YDL_OPTIONS) as ydl:
                    info = ydl.extract_info(song_queue[str(ctx.guild.id)][0], download=False)
                URL = info['url']
                TITLE = info['title']
                thumb = info['thumbnails'][0]
                videofoto = thumb['url']
                sure = info['duration']
                kanal = info['uploader']
                videoizlen = info['view_count']
                videolike = info['like_count']
                suremin = sure // 60
                suresec = sure % 60
                if suresec < 10:
                    suresec = f'0{suresec}'
                if suremin < 10:
                    suremin = f'0{suremin}'
                voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
                voice.is_playing()
                embed = discord.Embed(title='Şuanda oynatılan...',
                                      description='',
                                      colour=discord.Colour.default())
                embed.set_footer(
                    text=f'İzlenme sayısı {videoizlen}\nLike sayısı:{videolike}'
                )
                embed.set_thumbnail(url=videofoto)

                embed.add_field(
                    name=kanal,
                    value=
                    f'```{TITLE}\n\n00:00 ------------------------- {suremin}:{suresec}```',
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
            if voice.is_connected() and len(song_queue[str(ctx.guild.id)]) >= 1:
                

                YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
                FFMPEG_OPTIONS = {
                    'before_options':
                    '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                    'options': '-vn'
                }
                voice = get(client.voice_clients, guild=ctx.guild)
                if not voice.is_playing():
                    with YoutubeDL(YDL_OPTIONS) as ydl:
                        info = ydl.extract_info(song_queue[str(ctx.guild.id)][0], download=False)
                    URL = info['url']
                    TITLE = info['title']
                    thumb = info['thumbnails'][0]
                    videofoto = thumb['url']
                    sure = info['duration']
                    kanal = info['uploader']
                    videoizlen = info['view_count']
                    videolike = info['like_count']
                    suremin = sure // 60
                    suresec = sure % 60
                    if suresec < 10:
                        suresec = f'0{suresec}'
                    if suremin < 10:
                        suremin = f'0{suremin}'
                    voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
                    voice.is_playing()
                    embed = discord.Embed(title='Şuanda oynatılan...',
                                          description='',
                                          colour=discord.Colour.default())
                    embed.set_footer(
                        text=
                        f'İzlenme sayısı {videoizlen}\nLike sayısı:{videolike}'
                    )
                    embed.set_thumbnail(url=videofoto)
                    embed.add_field(
                        name=kanal,
                        value=
                        f'```{TITLE}\n\n00:00 ------------------------- {suremin}:{suresec}```',
                        inline=False)
                    await ctx.send(embed=embed)
                    del song_queue[str(ctx.guild.id)][0]
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

