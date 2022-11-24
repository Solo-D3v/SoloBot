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
from discord import app_commands
import requests
from discord.utils import get
import random
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
import urllib.parse, urllib.request, re
import instaloader
from roblox import Client
from roblox.thumbnails import AvatarThumbnailType
import json
import io
import contextlib
import typing
# Intents
intents = discord.Intents.all()
intents.members = True
intents.message_content = True
intents.presences = True
intents.guilds = True
class aclient(discord.Client):
  def __init__(self):
    super().__init__(intents=intents)
    self.synced = False

  async def on_ready(self):
    await self.wait_until_ready()
    print('Bota bağlanıldı: {}'.format(client.user.name))

    print('Bot ID: {}'.format(client.user.id))

    activity = discord.Game(name="/yardım | /help", type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print("Durum ayarlandı!")
    if not self.synced:
      await tree.sync()
      self.synced = True

client = aclient()
tree = app_commands.CommandTree(client)

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
grupgrubu = 1015344885433372732


# Startup info


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
        await channel.send(f"**{member.name} adlı kullanıcı sunucudan ayrıldı** :sob:")
    else:
        return

@client.event
async def on_member_ban(guild, member):
  if guild.id == grupgrubu:
    entries = [entry async for entry in guild.audit_logs(action=discord.AuditLogAction.ban, limit=1)]
    embed = discord.Embed(title=f"Bir üye banlandı!", description=f"*Banlanan*: **{member.name}**\n*Banlayan*:**{entries[0].user.name}**\n*Neden*:**{entries[0].reason}**", color=discord.Colour.red())
    
    await client.get_channel(1041395609652969552).send(embed=embed)
  else:
    pass

@client.event
async def on_member_kick(guild, member):
  if guild.id == grupgrubu:
    entries = [entry async for entry in guild.audit_logs(action=discord.AuditLogAction.kick, limit=1)]
    embed = discord.Embed(title=f"Bir üye atıldı!", description=f"Bir üye atıldı.!\n*Atılan*: **{member.name}**\n*Atan*:**{entries[0].user.name}\n*Neden*:**{entries[0].reason}", color=discord.Colour.red())
    await client.get_channel(1041395609652969552).send(embed=embed)
  else:
    pass

@client.event
async def on_bulk_message_delete(messages):
  if messages[0].guild.id == grupgrubu:
    embed = discord.Embed(title=f"Toplu mesaj silimi yapıldı!", description=f"*Silinen mesaj sayısı*:**{len(messages)}**\n*Kanal*:{messages[0].channel.mention}", color=discord.Colour.light_gray())
    await client.get_channel(1041395609652969552).send(embed=embed)

@client.event
async def on_guild_role_create(after,role):
  if role.guild.id == grupgrubu:
    embed = discord.Embed(title=f"Bir rol oluşturuldu!", description=f"*Rol*:**{role.mention}**", color=discord.Colour.green())
    await client.get_channel(1041395609652969552).send(embed=embed)

@client.event
async def on_guild_role_delete(after,role):
  if role.guild.id == grupgrubu:
    embed = discord.Embed(title=f"Bir rol silindi!", description=f"*Rol*:**{role.name}**", color=discord.Colour.red())
    await client.get_channel(1041395609652969552).send(embed=embed)

@client.event
async def on_guild_role_update(after, role):
  if role.guild.id == grupgrubu:
    entries = [entry async for entry in after.guild.audit_logs(action=discord.AuditLogAction.role_update, limit=1)]
    embed = discord.Embed(title=f"Bir rol güncellendi!", description=f"*Rol*:**{role.mention}**\n*Güncelleyen*:**{entries[0].user.name}", color=discord.Colour.blue())
    embed.add_field(name="Değişiklikler",value=entries[0].changes.after)
    await client.get_channel(1041395609652969552).send(embed=embed)    

@client.event
async def on_thread_create(thread):
  if thread.guild.id == grupgrubu:
    entries = [entry async for entry in thread.guild.audit_logs(action=discord.AuditLogAction.thread_create, limit=1)]
    embed = discord.Embed(title=f"Bir alt başlık oluşturuldu!", description=f"*Alt başlık*:**{thread.mention}**\n*Oluşturan*:**{entries[0].user.name}**", color=discord.Colour.green())
    await client.get_channel(1041395609652969552).send(embed=embed)

@client.event
async def on_thread_update(fart,thread):
  if thread.guild.id == grupgrubu:   
    entries = [entry async for entry in thread.guild.audit_logs(action=discord.AuditLogAction.thread_update, limit=1)]
    embed = discord.Embed(title=f"Bir alt başlık güncellendi!", description=f"*Alt başlık*:**{thread.mention}**\n*Güncelleyen*:**{entries[0].user.name}**", color=discord.Colour.blue())
    embed.add_field(name="Değişiklikler",value=entries[0].changes.after)
    await client.get_channel(1041395609652969552).send(embed=embed)

@client.event
async def on_thread_remove(thread):
  if thread.guild.id == grupgrubu:
    entries = [entry async for entry in thread.guild.audit_logs(action=discord.AuditLogAction.thread_remove, limit=1)]
    embed = discord.Embed(title=f"Bir alt başlık silindi!", description=f"*Alt başlık*:**{thread.name}**\n*Silen*:**{entries[0].user.name}**", color=discord.Colour.red())
    await client.get_channel(1041395609652969552).send(embed=embed)

@client.event
async def on_guild_channel_create(channel):
  if channel.guild.id == grupgrubu:
    entries = [entry async for entry in channel.guild.audit_logs(action=discord.AuditLogAction.channel_create, limit=1)]
    embed = discord.Embed(title=f"Bir kanal oluşturuldu!", description=f"*Kanal*:**{channel.mention}**\n*Oluşturan*:**{entries[0].user.name}**", color=discord.Colour.green())
    await client.get_channel(1041395609652969552).send(embed=embed)

@client.event
async def on_guild_channel_update(before,after):
  if after.guild.id == grupgrubu:   
    entries = [entry async for entry in after.guild.audit_logs(action=discord.AuditLogAction.channel_update, limit=1)]
    embed = discord.Embed(title=f"Bir kanal güncellendi!", description=f"*Kanal*:**{after.mention}**\n*Güncelleyen*:**{entries[0].user.name}**", color=discord.Colour.blue())
    embed.add_field(name="Değişiklikler",value=entries[0].changes.after)
    await client.get_channel(1041395609652969552).send(embed=embed)

@client.event
async def on_guild_channel_delete(channel):
  if channel.guild.id == grupgrubu:
    entries = [entry async for entry in channel.guild.audit_logs(action=discord.AuditLogAction.channel_delete, limit=1)]
    embed = discord.Embed(title=f"Bir kanal silindi!", description=f"*Kanal*:**{channel.name}**\n*Silen*:**{entries[0].user.name}**", color=discord.Colour.red())
    await client.get_channel(1041395609652969552).send(embed=embed)

@client.event
async def on_error(ctx: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.BotMissingPermissions):
        await ctx.response.send_message('Hata: Botun bunu yapmaya yetkisi yok', ephemeral=True)
        
    elif isinstance(error, app_commands.CheckFailure):
        await ctx.response.send_message(f'Üzgünüm dostum... Bu komutu kullanamazsın...', ephemeral=True)

      
    elif isinstance(error, app_commands.MissingPermissions):
        await ctx.response.send_message(
            f'Hata: Üzgünüm <@{ctx.user.id}>, bunu yapmaya yetkin yok', ephemeral=True)


    elif isinstance(error, app_commands.CommandNotFound):
        await ctx.response.send_message(f'Hata: Böyle bir komut yok!', ephemeral=True)

    elif isinstance(error, app_commands.CommandOnCooldown):
        await ctx.response.send_message(f'Hata: {error}', ephemeral=True)

    elif isinstance(error, app_commands.UserNotFound):
        await ctx.response.send_message(f'Hata: Kullanıcı bulunamadı!', ephemeral=True)

    
@client.event
async def on_message_delete(message):
  if message.guild.id == 1015344885433372732 and message.author.id != client.user.id:
    with open('txts/silinenmesajlar.txt','w+') as f:
      try:
        f.write(f'{message.content}\n{message.created_at}\n{message.author.id}')
      except Exception as e:
        print(e)
      print('Ok!')
    embed = discord.Embed(title=f"Bir mesaj silindi!", description=f"*Gönderen*: **{message.author.name}**\n*Mesaj içeriği*:  **{message.content}**", color=discord.Colour.red())
    await client.get_channel(1041395609652969552).send(embed=embed)

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

# commands
@tree.command(name='imagine',description='Draw a picture.',guilds=client.guilds)
@app_commands.describe(prompt="There are endless posibilities")
async def self(interaction: discord.Interaction, prompt: str):
  await interaction.response.send_message("Wait a second...", ephemeral=True)
  respon = openai.Image.create(prompt=f"{prompt}", n=1, size="512x512")
  icerik = requests.get(respon["data"][0]["url"]).content
  with open('image.png','wb') as f:
    f.write(icerik)
  await interaction.channel.send(f'Here is your picture, {interaction.user.mention}!\nPrompt:{prompt}', file = discord.File("image.png"))
  os.remove('image.png')
      
@tree.command(name="deneme",description="Just for fun")
async def deneme(ctx: discord.Interaction):
  select = discord.ui.Select(options = [
      discord.SelectOption(label="Halil",description="Klasik halil"),
      discord.SelectOption(label="halil",description="Klasik halil"),
      discord.SelectOption(label="hAlil",description="Klasik olmayan halil"),
    ],placeholder="sakın basma ples uwu",max_values=1,min_values=1)
  async def callback(ctx: discord.Interaction):
    if select.values[0] == "Halil":
      await ctx.response.send_message('fart',ephemeral=True)
    else:
      await ctx.response.send_message('Yuhhh yoksa {} mı seçtin???'.format(select.values[0]), ephemeral=True)
  select.callback = callback
  view = discord.ui.View()
  view.add_item(select)
  await ctx.response.send_message("Birini seç!",view=view)

@tree.command(name='yardım',description='Help Command.', guilds=client.guilds)
async def yardım(ctx:discord.Interaction,help: typing.Literal["mod","muzik","eglence"] = None):
  if help == None:
    embed = discord.Embed(
        title=' ',
        description=
        ' ',
        colour=discord.Colour.blue())
    embed.add_field(name='Yardım Komutları', value='**<a:mod:1028649041619320932>     Moderatör Komutları: +yardım mod\n\n<a:music:1028648378638290994>     Müzik Komutları: +yardım muzik\n\n<a:eglence:1028649336873160824>     Eğlence Komutları: +yardım eglence**')
    embed.set_footer(
        text='Bu komut {} tarafından kullanıldı!'.format(ctx.user.name))
    await ctx.response.send_message(embed=embed)
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
    await ctx.response.send_message(embed=embed)
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
    await ctx.response.send_message(embed=embed)
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
    await ctx.response.send_message(embed=embed)

@tree.command()
async def help(ctx:discord.Interaction,help: typing.Literal["mod","music","fun"] = None):
  if help == None:
    embed = discord.Embed(
        title=' ',
        description=
        ' ',
        colour=discord.Colour.blue())
    embed.add_field(name='Help Commands', value='**<a:mod:1028649041619320932>     Mod Commands: +help mod\n\n<a:music:1028648378638290994>     Music Commands: +help music\n\n<a:eglence:1028649336873160824>     Fun Commands: +help fun**')
    embed.set_footer(
        text='This command used by {}!'.format(ctx.user.name))
    await ctx.response.send_message(embed=embed)
  elif help.lower() == "mod":
    embed = discord.Embed(title=' ',
                          description='',
                          colour=discord.Colour.blue())
    embed.set_footer(text='Hope this helps.')
    embed.add_field(
        name='Commands:',
        value=
        '```+purge: Deletes the messages.\n\n+kick: Kicks a user.\n\n+ban: Bans a member.\n\n+unban: Unbans a user.\n\n+nick: Changes nickname of a member.```',
        inline=False)
    await ctx.response.send_message(embed=embed)
  elif help.lower() == "music":
    embed = discord.Embed(title=' ',
                          description='',
                          colour=discord.Colour.blue())
    embed.set_footer(text='Hope this helps.')
    embed.add_field(
        name='Komutlar:',
        value=
        '```+play: Plays a song.\n\n+pause: Pauses the song.\n\n+continue: Continues the song.\n\n+stop: Stops the song and disconnects from voice channel.\n\n+skip: Skips the song.\n\n+queue: Shows the queue.\n\n+loop: Loops the song.\n\n+tts: Bot joins the voice channel and tells that what you wrote.\n\n+yt: Searches a song on youtube.```',
        inline=False)
    await ctx.response.send_message(embed=embed)
  elif help.lower() == "fun":
    embed = discord.Embed(title=' ',
                          description='',
                          colour=discord.Colour.blue())
    embed.set_footer(text='Hope this helps.')
    embed.add_field(
        name='Komutlar:',
        value=
        '```+rfoto: Sends a random photo.\n\n+xox: Starts a xox game with you and the person who you pinged.\n\n+instapp: Sends the profile picture of a instagram account.\n\n+achievement: M-Minecraft achievements???\n\n+pfp: Sends the profile picture of person who you pinged.\n\n+fakemessage: Writes a fake message.\n\n+guess: Guess the number game.\n\n+botinfo: Info about SoloBot.\n\n+userinfo: Info about a member.```',
        inline=False)
    await ctx.response.send_message(embed=embed)


@tree.command(name="botinfo",description="Information about bot.")
async def botinfo(ctx: discord.Interaction):
  kisiler = 0
  for k in client.guilds:
    kisiler = kisiler + len(k.members)
  solo= ctx.guild.me

  embed = discord.Embed(title="SoloBot hakkında bazı bilgiler.", description=f"**Bot: \tSoloBot\n\nKaç adet sunucuya hizmet veriyor:\t{len(client.guilds)}\n\nKaç adet üyeye hizmet veriyor:\t{kisiler}\n\nOluşturulma tarihi:\t{client.user.created_at}\n\nSunucuya katılma tarihi:\t{solo.joined_at}**",colour= discord.Colour.blurple())
  await ctx.response.send_message(embed=embed)

@tree.command(name="userinfo",description="Information about a user.")
@app_commands.describe(kisi="Specify a member.")
async def userinfo(ctx: discord.Interaction, kisi: discord.User):
  try:
    lol = ctx.guild.get_member(kisi.id)
    fart = lol.activity
    if fart == None:
      fart = lol.status
    else:
      fart = lol.activity.name
    embed = discord.Embed(title="{} hakkında bazı bilgiler.".format(kisi.name), description=f"**Nickname: {kisi.name}\n\nBot mu?:\t{kisi.bot}\n\nDurumu:\t{fart}\n\nHesabın oluşturulma tarihi:\t{kisi.created_at}\n\nSunucuya katılma tarihi:\t{lol.joined_at}**",colour= discord.Colour.blurple())
    embed.set_thumbnail(url=kisi.avatar.url)
    await ctx.response.send_message(embed=embed)
  except Exception as e:
    print(e)

@tree.command(name="qr",description="Create a qr code.")
@app_commands.describe(arg="What should write in qr code?")
async def qr(ctx,arg: str):
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
  await ctx.response.send_message(file=discord.File('qrcode.png'))
  sleep(1)
  os.remove('qrcode.png')

@tree.command(name='sohbet',description="Ask/Say something to bot.")
@app_commands.describe(metin="What do you want to say/ask to bot?")
async def sb(ctx: discord.Interaction,metin: str):
  try:
    with open('txts/history.txt') as f:
      gecmislist = f.read()
    gecmis = gecmislist
    response = openai.Completion.create(model=f"text-davinci-002", prompt=f"{gecmis}{ctx.user.name}"+" "+metin+"\nSoloBot:", temperature=1.0, max_tokens=150)
    if "my" in metin.lower():
      with open('txts/history.txt','w+') as f:
        if "my" in metin.lower():
          f.write(f"{gecmis}{ctx.user.name}: {metin}\nSoloBot:{response.choices[0].text}\n\n")
    else:
      pass
    print(response.choices[0].text)
    await ctx.response.send_message(response.choices[0].text.capitalize())
  except Exception as e:
    print(e)

@tree.command(name="snipe",description="See the last deleted message.")
async def snipe(ctx:discord.Interaction):
  mesaj = ""
  with open('txts/silinenmesajlar.txt') as f:
    a = f.readlines()
  for i in a:
    if i == a[-1] or i == a[-2]:
      pass
    else:
      mesaj = mesaj+i
  uye = await ctx.guild.fetch_member(int(a[-1]))
  embed = discord.Embed(title="Son silinen mesaj", description=f"{mesaj}\n{a[-2]}",colour= discord.Colour.blurple())
  embed.set_author(name=uye.name+"#"+str(uye.discriminator),icon_url=uye.avatar.url)
  await ctx.response.send_message(embed=embed)

@tree.command(name="sniper",description="See the last edited message.")
async def sniper(ctx: discord.Interaction):
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
  await ctx.response.send_message(embed=embed)  

@tree.command(name="id",description="Learn a emoji's id")
async def id(ctx: discord.Interaction,emoji: str):
  for emo in ctx.guild.emojis:
    if emo.name == emoji:
      await ctx.response.send_message(emo.id)
    else:
      pass

@tree.command(name="mesajyaz",description="Write a fake message like someone else.")
@app_commands.describe(kişi="Specify a member.")
async def mesajyaz(ctx:discord.Interaction, kişi: discord.User, mesaj: str):
    try:
        await ctx.response.send_message("Done!",ephemeral=True)

        webhook = await ctx.channel.create_webhook(name=kişi.name)
        await webhook.send(content=mesaj,
                           username=kişi.name,
                           avatar_url=kişi.avatar.url,
                           wait=True)
        await webhook.delete()
    except Exception as e:
        print(e)

@tree.command(name="eval",description="Stay away from this command.")
async def eval(ctx:discord.Interaction, code: str):
  if not ctx.user.id == 921084920116437002 or ctx.user.id == 733002439279640577:
    await ctx.response.send_message("You can't use that.",ephemeral=True)
    return "Noob"
  stdout = io.StringIO()

  try:
    with contextlib.redirect_stdout(stdout):
      exec(code)
      result = stdout.getvalue()
      if len(result) != 0:
        embed = discord.Embed(title="Kodunuzun çıktısı:",description=f"```py\n{result}```",colour= discord.Colour.dark_blue())
      else:
        embed = discord.Embed(title="Kodunuzun çıktısı:",description=f"```Kodunuzun herhangi bir çıktısı olmadı.```",colour= discord.Colour.dark_blue())
      await ctx.response.send_message(embed=embed)
  except Exception as e:
    print(e)
    embed = discord.Embed(title="Kodunuzun çıktısı:",description=f"```py\n{e}```",colour= discord.Colour.dark_theme())
    await ctx.response.send_message(embed=embed)
    pass


@tree.command(name="roblox",description="Search some information about a roblox player")
async def rb(ctx: discord.Interaction, kisi: str):
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
        await ctx.response.send_message(embed=embed)
    except Exception as e:
        await ctx.response.send_message(e)


@tree.command(name="rfoto",description="Sends a random picture.")
async def rfoto(ctx: discord.Interaction):
    a = random.randint(1, 1000)
    embed = discord.Embed(title='Rastgele Foto!',
                          colour=discord.Colour.random())
    embed.set_image(url=f'https://source.unsplash.com/random?={a}')
    embed.set_footer(text=f'Bu komut {ctx.user.name} tarafından kullanıldı!')
    await ctx.response.send_message(embed=embed)


@tree.command(name="ayrıl",description="It's none of your business.")
async def ayrıl(ctx: discord.Interaction, guild_id: int):
    if not ctx.user.id == 921084920116437002 or ctx.user.id == 733002439279640577:
      return
    await client.get_guild(int(guild_id)).leave()
    await ctx.response.send_message(f"Ayrıldım: {guild_id}")



@tree.command(name="xox",description="Play xox with someone!")
async def xox(ctx:discord.Interaction, oyuncu2: discord.Member):
    if oyuncu2.id == client.user.id:
        await ctx.response.send_message(
            'D-Dostum sanırım oynamak için gerçek birini etiketlemen lazım...')
        return
    elif oyuncu2.id == ctx.user.id:
        await ctx.response.send_message(
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
    await ctx.response.send_message(
        f'Hey <@{oyuncu2.id}>! {ctx.user.name} seni bir xox oyununa davet etti, katılmak ister misin?'
    )
    try:
        red_kabul = await client.wait_for(
            'message',
            check=lambda message: message.author.id == oyuncu2.id,
            timeout=30)

        if red_kabul.content.lower() == 'evet':
            xox = await ctx.response.send_message('{}\n{}\n{}'.format(taht + taht2 + taht3,
                                                     taht4 + taht5 + taht6,
                                                     taht7 + taht8 + taht9))
            await ctx.channel.send(
                f'<@{ctx.user.id}> senin sıran! Oynamak için 1-9 arasında bir sayı söyle!'
            )
            sonihtimal = 0
            while True:
                if taht == ':x:' and taht2 == ':x:' and taht3 == ':x:' or taht == ':x:' and taht4 == ':x:' and taht7 == ':x:' or taht == ':x:' and taht5 == ':x:' and taht9 == ':x:' or taht4 == ':x:' and taht5 == ':x:' and taht6 == ':x:' or taht7 == ':x:' and taht8 == ':x:' and taht9 == ':x:' or taht2 == ':x:' and taht5 == ':x:' and taht8 == ':x:' or taht3 == ':x:' and taht6 == ':x:' and taht9 == ':x:' or taht3 == ':x:' and taht5 == ':x:' and taht7 == ':x:':
                    await ctx.response.send_message(f'<@{oyuncu2.id}> KAZANDI!')
                    return
                elif taht == ':o:' and taht2 == ':o:' and taht3 == ':o:' or taht == ':o:' and taht4 == ':o:' and taht7 == ':o:' or taht == ':o:' and taht5 == ':o:' and taht9 == ':o:' or taht4 == ':o:' and taht5 == ':o:' and taht6 == ':o:' or taht7 == ':o:' and taht8 == ':o:' and taht9 == ':o:' or taht2 == ':o:' and taht5 == ':o:' and taht8 == ':o:' or taht3 == ':o:' and taht6 == ':o:' and taht9 == ':o:' or taht3 == ':o:' and taht5 == ':o:' and taht7 == ':o:':
                    await ctx.response.send_message(f'<@{ctx.user.id}> KAZANDI!')
                    return
                if sonihtimal == 9:
                    await ctx.response.send_message('Hiç kimse kazanamadı! Oyun berabere bitti!'
                                   )
                    return
                o1 = await client.wait_for(
                    'message',
                    check=lambda msg: msg.author.id == ctx.user.id,
                    timeout=25)
                sonihtimal = sonihtimal + 1
                if int(o1.content) == 1:
                    if taht != ':x:' or taht != ':o:':
                        taht = ':o:'
                        await xox.edit_original_response(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o1.content) == 2:
                    if taht != ':x:' or taht != ':o:':
                        taht2 = ':o:'
                        await xox.edit_original_response(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o1.content) == 3:
                    if taht != ':x:' or taht != ':o:':
                        taht3 = ':o:'
                        await xox.edit_original_response(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o1.content) == 4:
                    if taht != ':x:' or taht != ':o:':
                        taht4 = ':o:'
                        await xox.edit_original_response(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o1.content) == 5:
                    if taht != ':x:' or taht != ':o:':
                        taht5 = ':o:'
                        await xox.edit_original_response(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o1.content) == 6:
                    if taht != ':x:' or taht != ':o:':
                        taht6 = ':o:'
                        await xox.edit_original_response(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o1.content) == 7:
                    if taht != ':x:' or taht != ':o:':
                        taht7 = ':o:'
                        await xox.edit_original_response(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o1.content) == 8:
                    if taht != ':x:' or taht != ':o:':
                        taht8 = ':o:'
                        await xox.edit_original_response(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o1.content) == 9:
                    if taht != ':x:' or taht != ':o:':
                        taht9 = ':o:'
                        await xox.edit_original_response(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                if taht == ':x:' and taht2 == ':x:' and taht3 == ':x:' or taht == ':x:' and taht4 == ':x:' and taht7 == ':x:' or taht == ':x:' and taht5 == ':x:' and taht9 == ':x:' or taht4 == ':x:' and taht5 == ':x:' and taht6 == ':x:' or taht7 == ':x:' and taht8 == ':x:' and taht9 == ':x:' or taht2 == ':x:' and taht5 == ':x:' and taht8 == ':x:' or taht3 == ':x:' and taht6 == ':x:' and taht9 == ':x:' or taht3 == ':x:' and taht5 == ':x:' and taht7 == ':x:':
                    await ctx.response.send_message(f'<@{oyuncu2.id}> KAZANDI!')
                    return
                elif taht == ':o:' and taht2 == ':o:' and taht3 == ':o:' or taht == ':o:' and taht4 == ':o:' and taht7 == ':o:' or taht == ':o:' and taht5 == ':o:' and taht9 == ':o:' or taht4 == ':o:' and taht5 == ':o:' and taht6 == ':o:' or taht7 == ':o:' and taht8 == ':o:' and taht9 == ':o:' or taht2 == ':o:' and taht5 == ':o:' and taht8 == ':o:' or taht3 == ':o:' and taht6 == ':o:' and taht9 == ':o:' or taht3 == ':o:' and taht5 == ':o:' and taht7 == ':o:':
                    await ctx.response.send_message(f'<@{ctx.user.id}> KAZANDI!')
                    return
                if sonihtimal == 9:
                    await ctx.response.send_message('Hiç kimse kazanamadı! Oyun berabere bitti!'
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
                        await xox.edit_original_response(content='{}\n{}\n{}'.format(
                            taht1 + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o2.content) == 2:
                    if taht != ':x:' or taht != ':o:':
                        taht2 = ':x:'
                        await xox.edit_original_response(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o2.content) == 3:
                    if taht != ':x:' or taht != ':o:':
                        taht3 = ':x:'
                        await xox.edit_original_response(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o2.content) == 4:
                    if taht != ':x:' or taht != ':o:':
                        taht4 = ':x:'
                        await xox.edit_original_response(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o2.content) == 5:
                    if taht != ':x:' or taht != ':o:':
                        taht5 = ':x:'
                        await xox.edit_original_response(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o2.content) == 6:
                    if taht != ':x:' or taht != ':o:':
                        taht6 = ':x:'
                        await xox.edit_original_response(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o2.content) == 7:
                    if taht != ':x:' or taht != ':o:':
                        taht7 = ':x:'
                        await xox.edit_original_response(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o2.content) == 8:
                    if taht != ':x:' or taht != ':o:':
                        taht8 = ':x:'
                        await xox.edit_original_response(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o2.content) == 9:
                    if taht != ':x:' or taht != ':o:':
                        taht9 = ':x:'
                        await xox.edit_original_response(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))

        elif red_kabul.content.lower() == 'hayır':
            await ctx.response.send_message(
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


@tree.command(name="serverinfo",description="Some information about a server.")
async def serverinfo(ctx: discord.Interaction):
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
    embed.set_footer(text=f'Bu komut {ctx.user.name} tarafından kullanıldı!')
    await ctx.response.send_message(embed=embed)


@tree.command(name="mcbasarim",description="Minecraft achievement.")
async def mcbaşarım(ctx: discord.Interaction, msg: str):
    re=requests.get("https://minecraftskinstealer.com/achievement/1/Achievement+Get%21/"+msg)
    embed = discord.Embed(title='Minecraft Achievement',
                          colour=discord.Colour.random())
    embed.set_image(
        url=re.url)
    embed.set_footer(text=f'That command is used by {ctx.user.name}')
    await ctx.response.send_message(embed=embed)


@tree.command(name="instapp",description="Sends a instagram account's pfp.")
async def instapp(ctx:discord.Interaction, kullaniciadi: str):
    try:
        ig = instaloader.Instaloader()
        profile = kullaniciadi
        ig.download_profile(profile, profile_pic_only=True)
        sss = os.scandir(kullaniciadi)
        for i in sss:
            if i.name.endswith('jpg') or i.name.endswith('png'):
                await ctx.response.send_message(file=discord.File(i))
                os.remove(i)
                os.rmdir(kullaniciadi)
            else:
                os.remove(i)
    except Exception as e:
        await ctx.response.send_message(f'**Hata: {e}**')


@tree.command(name="sayıtahmin",description="Guess the number game.")
@commands.cooldown(1, 45, commands.BucketType.user)
async def sayıtahmin(ctx: discord.Interaction):
    x = random.randint(1, 100)
    y = 6
    await ctx.response.send_message(
        '1 ile 100 arasında bir sayı tuttum. Onu bulabilir misin? Tahmin etmek için 6 hakkın var!'
    )
    while True:
        try:
            msg = await client.wait_for(
                'message',
                check=lambda message: message.author.id == ctx.user.id,
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
            await ctx.response.send_message(
                'Çok uzun süredir yanıt vermediğiniz için oyun iptal edildi!')
            return


@tree.command(name="hack",description="Learn how to hack bots")
async def yolla(ctx: discord.Interaction):
  await ctx.response.send_message('<a:rickroll:1016265373919760406>')



@tree.command(name="ban",description="Ban a member.")
@app_commands.describe(üye="Specify a member to ban", neden="Reason of ban.")
@discord.app_commands.checks.has_permissions(ban_members=True)
async def ban(ctx: discord.Interaction, üye: discord.Member, neden: str):
    if üye.id == client.user.id:
        await ctx.response.send_message(
            'Tamam kanka şuan kendimi banladım. Başkasını banlamaya ne dersin?'
        )
    elif üye.id == ctx.user.id:
        await ctx.response.send_message(
            'Bak kardeşim... Son pişmanlık fayda etmez diyorum.. Emin misin?')
        zort = await client.wait_for(
            'message',
            check=lambda msg: ctx.user.id == msg.author.id,
            timeout=50)
        if zort.content.lower() == 'evet':
            await üye.ban(reason='intihar... kendini banlattı..')
            await ctx.response.send_message('https://youtu.be/2agdQzh_zSk?t=72')
        else:
            return
    else:
        await üye.ban(reason=neden)
        await ctx.response.send_message(
            f'**{üye.name} adlı kullanıcı {neden} nedeniyle {ctx.user.name} tarafından banlandı**'
        )


@tree.command(name="unban", description="Unban a member.")
@app_commands.describe(üye="Member's nick and tag without any space.")
@discord.app_commands.checks.has_permissions(ban_members=True)
async def unban(ctx: discord.Interaction, üye: str):
    banlılar = await ctx.guild.bans()
    üye_nick, üye_tag = üye.split('#')

    for i in banlılar:
        bismillah = i.user

        if (bismillah.name, bismillah.discriminator) == (üye_nick, üye_tag):
            await ctx.guild.unban(bismillah)
            await ctx.response.send_message(f'{bismillah} kullanıcısının banı kaldırıldı!')


@tree.command(name="kick",description="Kick a member.")
@app_commands.describe(üye="Specify a member.",neden="Reason of kick.")
@discord.app_commands.checks.has_permissions(kick_members=True)
async def kick(ctx: discord.Interaction, üye: discord.Member, neden: str):
    if üye.id == client.user.id:
        await ctx.response.send_message(
            'Tamam kanka şuan kendimi attım. Başkasını atmaya ne dersin?')
    elif üye.id == ctx.user.id:
        await ctx.response.send_message(
            'Bak kardeşim... Son pişmanlık fayda etmez diyorum.. Emin misin?')
        zort = await client.wait_for(
            'message',
            check=lambda msg: ctx.user.id == msg.author.id,
            timeout=50)
        if zort.content.lower() == 'evet':
            await üye.kick(reason='intihar... kendini banlattı..')
            await ctx.response.send_message('https://youtu.be/2agdQzh_zSk?t=72')
        else:
            return
    else:
        await üye.kick(reason=neden)
        await ctx.response.send_message(
            f'**{üye.name} adlı kullanıcı {neden} nedeniyle {ctx.user.name} tarafından atıldı**'
        )


@tree.command()
@discord.app_commands.checks.has_permissions(manage_nicknames=True)
async def nick(ctx: discord.Interaction, member: discord.Member, nick: str):
    await member.edit(nick=nick)
    await ctx.response.send_message(
        f"{member.mention} kullanıcısının sunucudaki ismi değiştirildi!")


@tree.command(name="pfp",description="Sends a member's pfp")
async def pfp(ctx: discord.Interaction, arg: discord.Member = None):
    if not arg == None:
        pfp = arg.avatar.url
        embed = discord.Embed(title="Profil Fotoğrafı",
                              description='{}'.format(arg.mention),
                              color=0xecce8b)
        embed.set_image(url=(pfp))
        await ctx.response.send_message(embed=embed)
    else:
        arg = ctx.user
        pfp = arg.avatar.url
        embed = discord.Embed(title="Profil Fotoğrafı",
                              description='{}'.format(arg.mention),
                              color=0xecce8b)
        embed.set_image(url=(pfp))
        await ctx.response.send_message(embed=embed)


@tree.command(name="tts",description="Text to speech.")
@app_commands.describe(text="Write a text.",language="Use 'en' for english, 'es' for spanish, 'ru' for russian, 'ja' for japanese etc. Don't use anything for Turkish.")
async def tts(ctx: discord.Interaction,text: str, language: str = "tr"):
    voice = get(client.voice_clients, guild=ctx.guild)
    try:
      if ctx.user.voice.channel:
        pass
    except:
      await ctx.response.send_message("You are not connected to any voice channel.",ephemeral=True)
      return
    channel = ctx.user.voice.channel
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    if not voice.is_playing():
        await ctx.response.send_message("Done!",ephemeral=True)
        x = random.randint(1, 100)
        tts = gtts.gTTS(f"{text}", lang=language)
        tts.save(f"adana{x}.mp3")
        voice.play(FFmpegPCMAudio(f'adana{x}.mp3'))
        voice.is_playing()
        sleep(1)
        os.remove(f'adana{x}.mp3')

# bir linki oynatır
async def dur(ctx: discord.Interaction):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
        await ctx.response.send_message('**Şarkı durduruldu...**')


async def devam(ctx: discord.Interaction):
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        voice.resume()
        await ctx.response.send_message('**Şarkı kaldığı yerden devam ediyor...**')


async def kapat(ctx: discord.Interaction):
    voice = get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    voice = await ctx.voice_client.disconnect()
    await ctx.response.send_message('**Kapatılıyor...**')


@tree.command(name="skip",description="Skip the song.")
async def s(ctx: discord.Interaction):
    
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {
        'before_options':
        '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn'
    }
    await ctx.response.send_message("Skipped!",ephemeral=True)
    voice = get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    with YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(song_queue[str(ctx.guild.id)][1], download=False)
    URL = info['url']
    voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    voice.is_playing()
    voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    voice.is_playing()
    del song_queue[str(ctx.guild.id)][0]


@tree.command()
@discord.app_commands.checks.has_permissions(manage_channels=True)
async def nuke(ctx: discord.Interaction):

    channel = ctx.channel
    channel_position = channel.position

    a = await channel.clone()
    await channel.delete()
    await a.edit(position=channel_position, sync_permissions=True)
    await a.send('**Kanal Başarıyla Tekrardan Oluşturuldu!**')
    return


@tree.command()
async def durum(ctx: discord.Interaction, durum: str):
    if not ctx.user.id == 921084920116437002 or ctx.user.id == 733002439279640577:
      return
    activity = discord.Game(name=f"{durum}", type=3)
    await client.change_presence(status=discord.Status.idle,
                                     activity=activity)
    


@tree.command()
async def loop(ctx: discord.Interaction):
    if not loopunbabası.is_running():
        loopunbabası.start(ctx)
        await ctx.response.send_message('**Loop başlatıldı!!**')
    else:
        loopunbabası.stop()
        await ctx.response.send_message('**Loop kapatıldı!!**')


@tree.command(name="oynat",description="Plays music.")
async def oynat(ctx: discord.Interaction, search: str):
    try:
        try:
          if ctx.user.voice.channel:
            pass
        except:
          await ctx.response.send_message("You are not connected to any voice channel.",ephemeral=True)
          return
        await ctx.response.send_message('**Video aranıyor...**')
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
        channel = ctx.user.voice.channel
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
            except IndexError as e:
              print(e)
              pass
            finally:
                song_queue[str(ctx.guild.id)] = song_queue[str(ctx.guild.id)] + [f'{search_results[0]}']
            await ctx.edit_original_response(content='**Video bilgisi alınıyor...**')
            with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(song_queue[str(ctx.guild.id)][0], download=False)
            URL = info['url']
            TITLE = info['title']
            thumb = info['thumbnails'][0]
            videofoto = thumb['url']
            sure = info['duration']
            kanal = info['uploader']
            videoizlen = info['view_count']
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
                text=f'İzlenme sayısı:{videoizlen}')
            embed.set_thumbnail(url=videofoto)
            embed.add_field(
                name=kanal,
                value=
                f'```{TITLE}\n\n00:00 ------------------------- {suremin}:{suresec}```',
                inline=False)
            del song_queue[str(ctx.guild.id)][0]
            await ctx.edit_original_response(content=None,embed=embed)
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
                await ctx.edit_original_response(content=None,embed=embed)
                try:
                    sıra.start(ctx, search)
                    return
                except:
                    pass
    except Exception as e:
        print(e)


# durdurulmuş şarkıyı devam ettirme
@tree.command()
async def devam(ctx: discord.Interaction):
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        voice.resume()
        await ctx.response.send_message('**Şarkı kaldığı yerden devam ediyor...**')


# duraklatır bir süreliğine
@tree.command()
async def dur(ctx: discord.Interaction):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
        await ctx.response.send_message('**Şarkı durduruldu...**')


# durdurur
@tree.command()
async def kapat(ctx: discord.Interaction):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        song_queue[str(ctx.guild.id)][0] = []
        voice.stop()
        voice = await client.voice_client.disconnect()        
        await ctx.response.send_message('**Kapatılıyor...**')
    else:
        voice = await client.voice_client.disconnect()


# mesaj silmece
@tree.command(name="sil",description="Purge the messages.")
@commands.cooldown(1, 30, commands.BucketType.user)
@discord.app_commands.checks.has_permissions(manage_messages=True)
async def sil(ctx: discord.Interaction, amount: int = 15):
    await ctx.channel.purge(limit=amount)
    await ctx.response.send_message("**Mesajlar silindi!**",ephemeral=True)


@tree.command(name="yt",description="Search a video on Youtube")
async def yt(ctx: discord.Interaction,search: str):

    query_string = urllib.parse.urlencode({'search_query': search})
    htm_content = urllib.request.urlopen('http://www.youtube.com/results?' +
                                         query_string)
    search_results = re.findall(r'/watch\?v=(.{11})',
                                htm_content.read().decode())
    await ctx.response.send_message(f'http://www.youtube.com/watch?v={search_results[0]}')


@tree.command(name="spotify",description="Search a song on Spotify.")
async def spotify(ctx: discord.Interaction, search: str):
  sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_secret='e42352bdc1994ee9b66f1fa392fe366f',client_id='19783e5c318e4bd2ad943db0f6acee4c'))
  tracks= sp.search(q=search, type='track')
  sonuç = tracks['tracks']['items'][0]['external_urls']['spotify']
  sonuçname = tracks['tracks']['items'][0]['name']
  thumbnail = tracks['tracks']['items'][0]['album']['images'][0]['url']
  artist = tracks['tracks']['items'][0]['artists'][0]['name']
  embed = discord.Embed(title='Spotify Search',description='',colour=discord.Colour.default())
  embed.add_field(name=artist,value=f'Here is the result for [{sonuçname}]({sonuç})',inline=False)
  embed.set_thumbnail(url=thumbnail)
  await ctx.response.send_message(embed=embed)

@tree.command(name="queue",description="Learn the song queue.")
async def sr(ctx: discord.Interaction):
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
        await ctx.response.send_message(f'''```diff
{queue}```''')
    else:
        await ctx.response.send_message('Sırada hiç şarkı yok.')


@tasks.loop(seconds=1)
async def loopunbabası(ctx: discord.Interaction):
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
            channel = ctx.user.voice.channel
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
                await ctx.response.send_message(embed=embed)

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
            channel = ctx.user.voice.channel
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
                await ctx.response.send_message(embed=embed)

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
                    await ctx.channel.send(embed=embed)
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

