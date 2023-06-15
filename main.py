# encoding:utf-8
# Imports

import os
import qrcode
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

try:
  import imdb
except ImportError:
  os.system("pip install imdbpy")
  import imdb
  
try:
  import openai
except ImportError:
  os.system("pip install openai")
  import openai
  
try:
  import wikipedia
except ImportError:
  os.system("pip install wikipedia")
  import wikipedia

try:
  from PIL import Image
except ImportError:
  os.system('pip install pillow')
  from PIL import Image

try:
  from yt_dlp import YoutubeDL
except ImportError:
  os.system("python3 -m pip install --force-reinstall https://github.com/yt-dlp/yt-dlp/archive/master.tar.gz")
  from yt_dlp import YoutubeDL

from time import sleep
import gtts
import keep_alive
from discord.ext import commands, tasks
import discord
from discord import app_commands
import requests
from discord.utils import get
import random
from discord import FFmpegOpusAudio

import urllib.parse, urllib.request, re
import instaloader
from roblox import Client
from roblox.thumbnails import AvatarThumbnailType
import json
import io, asyncio
import contextlib
import typing
from datetime import datetime
from datetime import timedelta
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
    with open("jsons/song_queue.json") as f:
      icerik = f.read()
    icerik_dict = json.loads(icerik)

    for guild in client.guilds:
      icerik_dict[str(guild.id)] = []
    with open("jsons/song_queue.json", "w") as f:
      f.write(json.dumps(icerik_dict))
        
    print('Bota bağlanıldı: {}'.format(client.user.name))

    print('Bot ID: {}'.format(client.user.id))

    activity = discord.Game(name="/play | /standoff", type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print("Durum ayarlandı!")
    spotimer.start()
    if not self.synced:
      await tree.sync()
      self.synced = True

client = aclient()
tree = app_commands.CommandTree(client)
imdb_access = imdb.IMDb()

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
            f"**<@{member.id}> joined the server.** :tada:")
        await member.create_dm()
        await member.dm_channel.send(
            f"**HAII! WELCOME TO OUR SERVER!!! <@{member.id}>**")
    else:
        return


@client.event
async def on_member_remove(member):
    if member.guild.id == 1015344885433372732:
        channel = client.get_channel(1015526727767838811)
        await channel.send(f"**{member.name} left the server.** :sob:")
    else:
        return

@client.event
async def on_member_ban(guild, member):
  if guild.id == grupgrubu:
    entries = [entry async for entry in guild.audit_logs(action=discord.AuditLogAction.ban, limit=1)]
    embed = discord.Embed(title=f"A member has been banned!", description=f"*Banned Member*: **{member.name}**\n*Moderator who banned*:**{entries[0].user.name}**\n*Reason*:**{entries[0].reason}**", color=discord.Colour.red())
    
    await client.get_channel(1041395609652969552).send(embed=embed)
  else:
    pass

@client.event
async def on_member_kick(guild, member):
  if guild.id == grupgrubu:
    entries = [entry async for entry in guild.audit_logs(action=discord.AuditLogAction.kick, limit=1)]
    embed = discord.Embed(title=f"A member has been kicked!", description=f"*Kicked Member*: **{member.name}**\n*Moderator who kicked*:**{entries[0].user.name}\n*Reason*:**{entries[0].reason}", color=discord.Colour.red())
    await client.get_channel(1041395609652969552).send(embed=embed)
  else:
    pass

@client.event
async def on_bulk_message_delete(messages):
  if messages[0].guild.id == grupgrubu:
    embed = discord.Embed(title=f"Bulk delete detected!", description=f"*Number of deleted messages*:**{len(messages)}**\n*Channel*:{messages[0].channel.mention}", color=discord.Colour.light_gray())
    await client.get_channel(1041395609652969552).send(embed=embed)

@client.event
async def on_guild_role_create(role):
  if role.guild.id == grupgrubu:
    embed = discord.Embed(title=f"A role created!", description=f"*Role*:**{role.mention}**", color=discord.Colour.green())
    await client.get_channel(1041395609652969552).send(embed=embed)

@client.event
async def on_guild_role_delete(after,role):
  if role.guild.id == grupgrubu:
    embed = discord.Embed(title=f"A role deleted!", description=f"*Role*:**{role.name}**", color=discord.Colour.red())
    await client.get_channel(1041395609652969552).send(embed=embed)

@client.event
async def on_guild_role_update(after, role):
  if role.guild.id == grupgrubu:
    entries = [entry async for entry in after.guild.audit_logs(action=discord.AuditLogAction.role_update, limit=1)]
    embed = discord.Embed(title=f"A role updated!", description=f"*Role*:**{role.mention}**\n*Moderator who updated*:**{entries[0].user.name}", color=discord.Colour.blue())
    embed.add_field(name="Changes",value=entries[0].changes.after)
    await client.get_channel(1041395609652969552).send(embed=embed)    

@client.event
async def on_thread_create(thread):
  if thread.guild.id == grupgrubu:
    entries = [entry async for entry in thread.guild.audit_logs(action=discord.AuditLogAction.thread_create, limit=1)]
    embed = discord.Embed(title=f"A thread has been created!", description=f"*Thread*:**{thread.mention}**\n*Moderator who created*:**{entries[0].user.name}**", color=discord.Colour.green())
    await client.get_channel(1041395609652969552).send(embed=embed)

@client.event
async def on_thread_update(fart,thread):
  if thread.guild.id == grupgrubu:   
    entries = [entry async for entry in thread.guild.audit_logs(action=discord.AuditLogAction.thread_update, limit=1)]
    embed = discord.Embed(title=f"A thread has been updated!", description=f"*Thread*:**{thread.mention}**\n*Moderator who updated*:**{entries[0].user.name}**", color=discord.Colour.blue())
    embed.add_field(name="Changes",value=entries[0].changes.after)
    await client.get_channel(1041395609652969552).send(embed=embed)

@client.event
async def on_thread_remove(thread):
  if thread.guild.id == grupgrubu:
    entries = [entry async for entry in thread.guild.audit_logs(action=discord.AuditLogAction.thread_remove, limit=1)]
    embed = discord.Embed(title=f"A thread has been deleted!", description=f"*Thread*:**{thread.name}**\n*Moderator who deleted*:**{entries[0].user.name}**", color=discord.Colour.red())
    await client.get_channel(1041395609652969552).send(embed=embed)

@client.event
async def on_guild_channel_create(channel):
  if channel.guild.id == grupgrubu:
    entries = [entry async for entry in channel.guild.audit_logs(action=discord.AuditLogAction.channel_create, limit=1)]
    embed = discord.Embed(title=f"A channel has been created!", description=f"*Channel*:**{channel.mention}**\n*Moderator who created*:**{entries[0].user.name}**", color=discord.Colour.green())
    await client.get_channel(1041395609652969552).send(embed=embed)

@client.event
async def on_guild_channel_update(before,after):
  if after.guild.id == grupgrubu:   
    entries = [entry async for entry in after.guild.audit_logs(action=discord.AuditLogAction.channel_update, limit=1)]
    embed = discord.Embed(title=f"A channel has been updated!", description=f"*Channel*:**{after.mention}**\n*Moderator who updated*:**{entries[0].user.name}**", color=discord.Colour.blue())
    embed.add_field(name="Changes",value=entries[0].changes.after)
    await client.get_channel(1041395609652969552).send(embed=embed)

@client.event
async def on_guild_channel_delete(channel):
  if channel.guild.id == grupgrubu:
    entries = [entry async for entry in channel.guild.audit_logs(action=discord.AuditLogAction.channel_delete, limit=1)]
    embed = discord.Embed(title=f"A channel has been deleted!", description=f"*Channel*:**{channel.name}**\n*Moderator who deleted*:**{entries[0].user.name}**", color=discord.Colour.red())
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
    embed = discord.Embed(title=f"A message has been deleted!", description=f"*Sender*: **{message.author.name}**\n*Message Content*:  **{message.content}**", color=discord.Colour.red())
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
        await message.reply(
            'Shut up and stop pinging me.')

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
  await interaction.response.defer(ephemeral=True, thinking=True)
  respon = openai.Image.create(prompt=f"{prompt}", n=1, size="512x512")
  icerik = requests.get(respon["data"][0]["url"]).content
  with open('image.png','wb') as f:
    f.write(icerik)
  await interaction.followup.send(f'Here is your picture, {interaction.user.mention}!\nPrompt:{prompt}', file = discord.File("image.png"))
  os.remove('image.png')

@tree.command(name="history", description="Creator's song history.")
async def history(ctx:discord.Interaction):
  await ctx.response.send_message(file=discord.File('txts/history.txt'))

@tree.command(name="imdb",description="Get some information about a movie.")
async def find_movie(ctx: discord.Interaction, title: str):
    await ctx.response.defer(thinking=True)
    movies = imdb_access.search_movie(title)

    if not movies:
        await ctx.followup.send(f"No information found about `{title}`!")
        return

    movie = imdb_access.get_movie(movies[0].getID())
    print(movie)
    response = (
        f"**{movie['title']}** ({movie['year']})\n"
        f"**Genre:** {', '.join(str(genre) for genre in movie['genres'])}\n"
        f"**Runtime:** {movie['runtime'][0]} dk\n"
        f"**Rating:** {movie['rating']:.1f} / 10\n"
        f"**Description:** {movie.get('plot outline', 'Açıklama bulunamadı')}"
    )

    await ctx.followup.send(response)

@tree.context_menu(name="Get Avatar")
async def react(interaction: discord.Interaction, message: discord.Message):
    await interaction.response.send_message(message.author.avatar.url, ephemeral=False)

@tree.command(name="automod_create", description="Create a automod rule.")  # AutoMod komutunu oluşturup ona bir isim ve bir açıklama veriyorum.
@app_commands.describe(name="The name of the automod rule.", event_type="The type of event that the automod rule will trigger on.",trigger="The triggers that will trigger the automod rule.",actions= "The actions that will be taken when the automod rule is triggered.", enabled="Whether the automod rule is enabled. Discord will default to False.",reason="The reason for creating this automod rule. Shows up on the audit log.",channel_id="The ID of the channel or thread to send the alert message to, if any. Passing this sets type to send_alert_message.",custom_message="A custom message which will be shown to a user when their message is blocked. Passing this sets type to block_message.",duration="Needed if timeout is selected. Default is 1 minute.")  # Optionsların açıklamalarını burada belirtiyorum.
@app_commands.checks.has_permissions(manage_guild=True) # Sadece sunucuyu yönet yetkisine sahip kişiler kullanın diye yaptım.
async def automodpro(ctx:discord.Interaction, name: str, event_type: typing.Literal["message_send"], trigger:str, actions: typing.Literal["block_message","send_alert_message","timeout","block_message&send_alert_message","all_of_them"], enabled: typing.Literal["True","False"] = None, reason: str = None, channel_id:str = None, custom_message: str = None,duration: int = 1): 
  if enabled == None: # enabled optionunun defaultunu direk False yapmama discord izin vermediği için bu şekilde False yaptım.
    enabled = False

  
  if actions == "block_message":  # Block Message kısmı
    action = discord.AutoModRuleAction(channel_id=int(channel_id), duration=None, custom_message=custom_message)
    action.type = discord.AutoModRuleActionType.block_message
    await ctx.guild.create_automod_rule(name=name, event_type=discord.AutoModRuleEventType.message_send, trigger=discord.AutoModTrigger( keyword_filter=[i for i in trigger.split(",")]), actions=[action], enabled=enabled, reason=reason)

  if actions == "send_alert_message": # Send Alert Message kısmı
    action = discord.AutoModRuleAction(channel_id=int(channel_id), duration=None, custom_message=custom_message)
    action.type = discord.AutoModRuleActionType.send_alert_message
    await ctx.guild.create_automod_rule(name=name, event_type=discord.AutoModRuleEventType.message_send, trigger=discord.AutoModTrigger( keyword_filter=[i for i in trigger.split(",")]), actions=[action], enabled=enabled, reason=reason)


  if actions == "timeout": # timeout cart curt
    action = discord.AutoModRuleAction(channel_id=int(channel_id), duration=timedelta(minutes = int(duration)), custom_message=custom_message)
    action.type = discord.AutoModRuleActionType.timeout
    await ctx.guild.create_automod_rule(name=name, event_type=discord.AutoModRuleEventType.message_send, trigger=discord.AutoModTrigger( keyword_filter=[i for i in trigger.split(",")]), actions=[action], enabled=enabled, reason=reason)

  if actions == "block_message&send_alert_message": # ikisi birden
    action = [discord.AutoModRuleAction(channel_id=int(channel_id), duration=None, custom_message=custom_message), discord.AutoModRuleAction(channel_id=int(channel_id), duration=None, custom_message=custom_message)]
    action[0].type = discord.AutoModRuleActionType.block_message
    action[1].type = discord.AutoModRuleActionType.send_alert_message
    await ctx.guild.create_automod_rule(name=name, event_type=discord.AutoModRuleEventType.message_send, trigger=discord.AutoModTrigger( keyword_filter=[i for i in trigger.split(",")]), actions=action, enabled=enabled, reason=reason)

  if actions == "all_of_them": # hepsi
    
    action = [
      discord.AutoModRuleAction(channel_id=int(channel_id), duration=None, custom_message=custom_message),
      discord.AutoModRuleAction(channel_id=int(channel_id), duration=None, custom_message=custom_message),
      discord.AutoModRuleAction(duration=timedelta(minutes = int(duration)))
    ]
    
    action[0].type = discord.AutoModRuleActionType.block_message
    action[1].type = discord.AutoModRuleActionType.send_alert_message
    action[2].type = discord.AutoModRuleActionType.timeout
    await ctx.guild.create_automod_rule(name=name, event_type=discord.AutoModRuleEventType.message_send, trigger=discord.AutoModTrigger( keyword_filter=[i for i in trigger.split(",")]), actions=action, enabled=enabled, reason=reason)
  
  
  triggers = "".join(f"{i} " for i in trigger.split(",")) # Bilgi mesajı atarken triggersları bir arada belirtmek için böyle yaptım.
  
  if reason: # reason default falan
    pass
  else:
    reason = "No reason given."
      
  if custom_message: # custom message default falan
    pass
  else:
    custom_message = "No custom message given."
      
  await ctx.response.send_message(f"# AutoMod Rule\n\n{ctx.user.mention} created a AutoMod rule. Here is the details:\n\n> - Rule Name: {name}\n> - Event Type: {event_type}\n> - Triggers: {triggers}\n> - Actions: {actions}\n> - Enabled: {enabled}\n> - Reason: {reason}\n> - Custom Message: {custom_message}")
  

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

@tree.command(name='wikipedia', description='Search a topic on Wikipedia.')
@app_commands.describe(language="Default is English.")
async def unrealwikipedia(ctx, topic: str, language: typing.Literal['Turkish','English'] = 'English'):
  await ctx.response.defer()
  try:
    if language == 'Turkish':
      wikipedia.set_lang("tr")
    elif language == 'English':
      wikipedia.set_lang("en")
    sum = wikipedia.summary(topic, sentences=5)
    await ctx.followup.send(sum)
  except wikipedia.exceptions.DisambiguationError as e:
    await ctx.followup.send(f"Disambiguation Error: {e}")
  except wikipedia.exceptions.PageError as e:
    await ctx.followup.send(f"Page Error: {e}")
  

@tree.command(name="fact",description="Shows a random useless fact")
async def fact(ctx):
    await ctx.response.defer(thinking=False)
    response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
    if response.status_code == 200:
        fact = response.json()['text']
        await ctx.followup.send(f'**Useless Fact:** {fact}')
    else:
        await ctx.followup.send('Unable to fetch facts :(')

@tree.command(name='chat-gpt',description='Chat with ChatGPT 3.5 Turbo',guilds=client.guilds)
async def pro(interaction: discord.Interaction, message: str):
  await interaction.response.defer(ephemeral = False, thinking=True)
  karakter_sayisi = 0
  response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "You are a helpful assistant which Solø created. Users' names will be specified before their messages but you don't have to do that."},{"role": "user", "content": f"{interaction.user.name}: {message}"}], temperature=1.0, max_tokens=3700)
  for karakter in str(response["choices"][0]["message"]["content"]).strip():
    if karakter.isalpha():
      karakter_sayisi += 1
  if karakter_sayisi > 1700:
    with open("response.txt","w+") as f:
      f.write(str(response["choices"][0]["message"]["content"]).strip())
    print(str(response["choices"][0]["message"]["content"]).strip())
    await interaction.followup.send(content="", attachments=[discord.File("response.txt")])
  else:
    print(str(response["choices"][0]["message"]["content"]).strip())
    await interaction.followup.send(content=str(response["choices"][0]["message"]["content"]).strip())
def checkle(react,user):
  return react.emoji == "🔫"
@tree.command(name="standoff",description="Who is the best cowboy?")
async def standoff(ctx, player2: discord.User):
    # Bot tarafından bir mesaj gönderin
    await ctx.response.send_message('Started.',ephemeral=True)
    mesaj = await ctx.channel.send(f'Welcome to the cowboy game {ctx.user.mention} {player2.mention}! Suddenly a emoji is going to appear. The player who clicks the emoji first wins!')
    idler = [ctx.user.id,player2.id]
    # Kullanıcıların tabanca emojisi ile tepki vermesini bekleyin
    try:
        sleep(random.randint(2,5))
        await mesaj.add_reaction("🔫")
        reaction = await client.wait_for('reaction_add', timeout=3.0, check=checkle)
    except asyncio.TimeoutError:
        await ctx.channel.send('Time is up! Use the "/standoff" command to restart the game.')
    else:
        # Eğer bir kullanıcı tepki vermişse oyunu bitirin
        
          print(reaction)
          print(reaction[1].id)
          if reaction[1].id in idler:
            await ctx.channel.send(f'{reaction[1].mention} won! Congratulations! Use the "/standoff" command to restart the game.')
            
          else:
            pass
"""
@tree.command(name="fight", description="A basic fight game that you can play with your friends!")
async def fight_game(ctx, user2: discord.User):
    #View = Dovus()
    if user2.id == client.user.id:
      await ctx.response.send_message('CHOOSE A REAL PERSON TO PLAY')
      return
    turn = 1
    user1 = ctx.user
    user1_health = 200
    user2_health = 200
    user1_blocked = False
    user2_blocked = False
    user1_ofke = 0
    user2_ofke = 0
    embed = discord.Embed(title="Choose your attack!",description="[1] - Punch\n[2] - Kick\n[3] - Block\n[4] - Ulti\n{}".format(user1.mention))
    embed.set_footer(text=f"{user2.name}! Your health is now at {user2_health}.")
    await ctx.response.send_message("Kavga başlatıldı agaaa",ephemeral=True)
    
    while user1_health > 0 and user2_health > 0:
        embed = discord.Embed(title="Choose your attack!",description="[1] - **Punch**\n[2] - **Kick**\n[3] - **Block**\n[4] - **Rage**\n{}".format(user1.mention))
        embed.set_footer(text=f"{user2.name}! Your health is now at {user2_health}.")
        await ctx.channel.send(embed=embed)
        punch_button = discord.ui.Button(label="Punch", style=discord.ButtonStyle.red)
      
        kick_button = discord.ui.Button(label="Kick", style=discord.ButtonStyle.green)
      
        block_button = discord.ui.Button(label="Block", style=discord.ButtonStyle.blurple)
      
        rage_button = discord.ui.Button(label="Rage")

        async def punch(interaction: discord.Interaction):
          if turn == 1 and ctx.user.id == interaction.user.id:
            if user2_blocked == False:
              hasar = random.randint(5,19)
            else:
              hasar = random.randint(1,7)
              user2_blocked = False
            user2_health -= hasar
            user2_ofke += 10
            embed = discord.Embed(title="PUNCH",description=f"**{user1.mention} used a punch attack and dealt {hasar} damage!**")
            embed.set_footer(text=f"{user2.name}! Your health is now at {user2_health}.")
            await ctx.edit_original_response(embed=embed)
            turn = 2
          elif turn == 2 and user2.id == interaction.user.id:
            if user1_blocked == False:
              hasar = random.randint(5,19)
            else:
              hasar = random.randint(1,7)
              user1_blocked = False
            user1_health -= hasar
            user1_ofke += 10
            embed = discord.Embed(title="PUNCH",description=f"**{user2.mention} used a punch attack and dealt {hasar} damage!**")
            embed.set_footer(text=f"{user1.name}! Your health is now at {user1_health}.")
            await ctx.edit_original_response(embed=embed)
            turn = 1
          else:
            await interaction.response.send_message("It's not your turn.", ephemeral=True)
        async def kick(interaction: discord.Interaction):
          if turn == 1 and ctx.user.id == interaction.user.id:
            if user2_blocked == False:
              real = random.randint(15,25)
            else:
              real = random.randint(1,7)
              user2_blocked = False
            user2_ofke += 20
            user2_health -= real
            embed = discord.Embed(title="KICK",description=f"**{user1.mention} used a kick attack and dealt {real} damage!**")
            embed.set_footer(text=f"{user2.name}! Your health is now at {user2_health}.")
            await ctx.edit_original_response(embed=embed)
            turn = 2
          elif turn == 2 and user2.id == interaction.user.id:
            if user1_blocked == False:
              real = random.randint(15,25)
            else:
              real = random.randint(1,7)
              user1_blocked = False
            user1_ofke += 20
            user1_health -= real
            embed = discord.Embed(title="KICK",description=f"**{user2.mention} used a kick attack and dealt {real} damage!**")
            embed.set_footer(text=f"{user1.name}! Your health is now at {user1_health}.")
            await ctx.edit_original_response(embed=embed)
            turn = 1
          
          else:
            await interaction.response.send_message("It's not your turn.", ephemeral=True)

        async def block(ctx: discord.Interaction):
          
        attack = await client.wait_for("message", check=lambda message: message.author.id == user1.id)

        elif attack.content == "3":
            embed = discord.Embed(title="BLOCKED",description=f"**{user1.mention} blocked the attack! {user1.mention} will get less damage just for one time.**")
            embed.set_footer(text=f"{user2.name}! Your health is now at {user2_health}.")
            await ctx.channel.send(embed=embed)
            user1_blocked = True
        elif attack.content == "4":
          if user1_ofke <= 50:
            embed = discord.Embed(title="RAGE",description="**You tried to use your rage but you are not ready for this.**")
            embed.set_footer(text=f"{user2.name}! Your health is now at {user2_health}.")
            await ctx.channel.send(embed=embed)
          else:
            user2_health -= 75
            embed = discord.Embed(title="RAGE",description="You used your rage and gave him 75 DAMAGE!")
            embed.set_footer(text=f"{user2.name}! Your health is now at {user2_health}.")
            await ctx.channel.send(embed=embed)
            
        else:
            await ctx.channel.send("Invalid attack choice. Please try again.")
        
        if user2_health <= 0:
            await ctx.channel.send(f"**{user1.mention} won the game!**")
            return
        embed = discord.Embed(title="Choose your attack!",description="[1] - **Punch**\n[2] - **Kick**\n[3] - **Block**\n[4] - **Ulti**\n{}".format(user2.mention))
        embed.set_footer(text=f"{user1.name}! Your health is now at {user1_health}.")

        elif attack.content == "3":
            embed = discord.Embed(title="BLOCKED",description=f"**{user1.mention} blocked the attack! {user1.mention} will get less damage just for one time.**")
            embed.set_footer(text=f"{user1.name}! Your health is now at {user1_health}.")
            await ctx.channel.send(embed=embed)
            user2_blocked = True
        elif attack.content == "4":
          if user2_ofke <= 50:
            embed = discord.Embed(title="RAGE",description="**You tried to use your rage but you are not ready for this.**")
            embed.set_footer(text=f"{user1.name}! Your health is now at {user1_health}.")
            await ctx.channel.send(embed=embed)
          else:
            user1_health -= 75
            embed = discord.Embed(title="RAGE",description="**You used your rage and gave him 75 DAMAGE!**")
            embed.set_footer(text=f"{user1.name}! Your health is now at {user1_health}.")
            await ctx.channel.send(embed=embed)            
        else:
            await ctx.channel.send("Invalid attack choice. Please try again.")
        if user1_health <= 0:
            await ctx.channel.send(f"**{user2.mention} won the game!**")
            return
"""

@tree.command(name="botinfo",description="Information about bot.")
async def botinfo(ctx: discord.Interaction):
  kisiler = 0
  for k in client.guilds:
    kisiler = kisiler + len(k.members)
  solo= ctx.guild.me

  embed = discord.Embed(title="Information about SoloBot", description=f"**Bot: \tSoloBot\n\nHow many servers is it serving:\t{len(client.guilds)}\n\nHow many members is it serving:\t{kisiler}\n\nCreated at:\t<t:{client.user.created_at}>\n\nJoined at:\t<t:{solo.joined_at.timestamp()}>**",colour= discord.Colour.blurple())
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
    embed = discord.Embed(title="Information about {}".format(kisi.name), description=f"**Nickname: {kisi.name}\n\nIs Bot?:\t{kisi.bot}\n\nStatus:\t{fart}\n\nCreated at:\t<t:{kisi.created_at.timestamp()}>\n\nJoined at:\t<t:{lol.joined_at.timestamp()}>**",colour= discord.Colour.blurple())
    embed.set_thumbnail(url=kisi.avatar.url)
    await ctx.response.send_message(embed=embed)
  except Exception as e:
    print(e)

@tree.command(name="qr",description="Create a qr code.")
@app_commands.describe(text="What should bot write in qr code?")
async def qr(ctx, text: str):
  qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 100,
    border = 4
  )
  qr.add_data(f'{text}')
  qr.make(fit=True)

  kod = qr.make_image(fill_color=(0,0,0),back_color='white')
  kod.save('qrcode.png')
  await ctx.response.send_message(file=discord.File('qrcode.png'))
  sleep(1)
  os.remove('qrcode.png')

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
  embed = discord.Embed(title="Last deleted message", description=f"{mesaj}\n{a[-2]}",colour= discord.Colour.blurple())
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
  embed.add_field(name=f'Last edited message', value=f'~~{messaj}~~\n\n{a[-2]}', inline=False)
  embed.set_author(name=uye.name+"#"+str(uye.discriminator),icon_url=uye.avatar.url)
  await ctx.response.send_message(embed=embed)  

@tree.command(name="id",description="Learn a emoji's id")
async def id(ctx: discord.Interaction,emoji: str):
  for emo in ctx.guild.emojis:
    if emo.name == emoji:
      await ctx.response.send_message(emo.id)
    else:
      pass

@tree.command(name="fakemessage",description="Write a fake message like someone else.")
@app_commands.describe(kişi="Specify a member.", mesaj="The message content.")
async def mesajyaz(ctx:discord.Interaction, kişi: discord.Member, mesaj: str):
    try:
        await ctx.response.send_message("Done.",ephemeral=True)

        webhook = await ctx.channel.create_webhook(name=kişi.name)
        await webhook.send(content=mesaj,
                           username=kişi.nick,
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
@app_commands.describe(kisi="The player's nickname.")
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
            f'\nUsername: **{user.name}**\n\nNickname: **{user.display_name}**\n\nDescription: **{user.description}**\n\nIs Banned?: **{user.is_banned}**\n\nCreated at: **<t:{user.created.timestamp()}>**'
        )
        await ctx.response.send_message(embed=embed)
    except Exception as e:
        await ctx.response.send_message(e)


@tree.command(name="rfoto",description="Sends a random picture.")
async def rfoto(ctx: discord.Interaction):
    a = random.randint(1, 1000)
    r = requests.get(f"https://api.unsplash.com/photos/random?client_id={os.environ['pic']}")
    data = r.json()
    photo_url = data['urls']['regular']
    embed = discord.Embed(title='Random Picture!',
                          colour=discord.Colour.random())
    embed.set_image(url=photo_url)
    embed.set_footer(text=f'This command is used by {ctx.user.name}')
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
            'B-Bro... I think you need a real person to play with... ')
        return
    elif oyuncu2.id == ctx.user.id:
        await ctx.response.send_message(
            'Okay bro you played with yourself and u won. Now wanna play with a real person?'
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
        f'Hey <@{oyuncu2.id}>! {ctx.user.name} invited you to a tic-tac-toe game! Do you want to join?'
    )
    try:
        red_kabul = await client.wait_for(
            'message',
            check=lambda message: message.author.id == oyuncu2.id,
            timeout=30)

        if red_kabul.content.lower() == 'yes':
            xox = await ctx.channel.send('{}\n{}\n{}'.format(taht + taht2 + taht3,
                                                     taht4 + taht5 + taht6,
                                                     taht7 + taht8 + taht9))
            await ctx.channel.send(
                f'<@{ctx.user.id}> your turn! Say a number between 1-9!'
            )
            sonihtimal = 0
            while True:
                if taht == ':x:' and taht2 == ':x:' and taht3 == ':x:' or taht == ':x:' and taht4 == ':x:' and taht7 == ':x:' or taht == ':x:' and taht5 == ':x:' and taht9 == ':x:' or taht4 == ':x:' and taht5 == ':x:' and taht6 == ':x:' or taht7 == ':x:' and taht8 == ':x:' and taht9 == ':x:' or taht2 == ':x:' and taht5 == ':x:' and taht8 == ':x:' or taht3 == ':x:' and taht6 == ':x:' and taht9 == ':x:' or taht3 == ':x:' and taht5 == ':x:' and taht7 == ':x:':
                    await ctx.channel.send(f'<@{oyuncu2.id}> WON!')
                    return
                elif taht == ':o:' and taht2 == ':o:' and taht3 == ':o:' or taht == ':o:' and taht4 == ':o:' and taht7 == ':o:' or taht == ':o:' and taht5 == ':o:' and taht9 == ':o:' or taht4 == ':o:' and taht5 == ':o:' and taht6 == ':o:' or taht7 == ':o:' and taht8 == ':o:' and taht9 == ':o:' or taht2 == ':o:' and taht5 == ':o:' and taht8 == ':o:' or taht3 == ':o:' and taht6 == ':o:' and taht9 == ':o:' or taht3 == ':o:' and taht5 == ':o:' and taht7 == ':o:':
                    await ctx.channel.send(f'<@{ctx.user.id}> WON!')
                    return
                if sonihtimal == 9:
                    await ctx.channel.send('Tie.'
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
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o1.content) == 2:
                    if taht2 != ':x:' or taht2 != ':o:':
                        taht2 = ':o:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o1.content) == 3:
                    if taht3 != ':x:' or taht3 != ':o:':
                        taht3 = ':o:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o1.content) == 4:
                    if taht4 != ':x:' or taht4 != ':o:':
                        taht4 = ':o:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o1.content) == 5:
                    if taht5 != ':x:' or taht5 != ':o:':
                        taht5 = ':o:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o1.content) == 6:
                    if taht6 != ':x:' or taht6 != ':o:':
                        taht6 = ':o:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o1.content) == 7:
                    if taht7 != ':x:' or taht7 != ':o:':
                        taht7 = ':o:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o1.content) == 8:
                    if taht8 != ':x:' or taht8 != ':o:':
                        taht8 = ':o:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o1.content) == 9:
                    if taht9 != ':x:' or taht9 != ':o:':
                        taht9 = ':o:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                else:
                  await ctx.channel.send('Unexpected answer!')
                  return
                if taht == ':x:' and taht2 == ':x:' and taht3 == ':x:' or taht == ':x:' and taht4 == ':x:' and taht7 == ':x:' or taht == ':x:' and taht5 == ':x:' and taht9 == ':x:' or taht4 == ':x:' and taht5 == ':x:' and taht6 == ':x:' or taht7 == ':x:' and taht8 == ':x:' and taht9 == ':x:' or taht2 == ':x:' and taht5 == ':x:' and taht8 == ':x:' or taht3 == ':x:' and taht6 == ':x:' and taht9 == ':x:' or taht3 == ':x:' and taht5 == ':x:' and taht7 == ':x:':
                    await ctx.channel.send(f'<@{oyuncu2.id}> WON!')
                    return
                elif taht == ':o:' and taht2 == ':o:' and taht3 == ':o:' or taht == ':o:' and taht4 == ':o:' and taht7 == ':o:' or taht == ':o:' and taht5 == ':o:' and taht9 == ':o:' or taht4 == ':o:' and taht5 == ':o:' and taht6 == ':o:' or taht7 == ':o:' and taht8 == ':o:' and taht9 == ':o:' or taht2 == ':o:' and taht5 == ':o:' and taht8 == ':o:' or taht3 == ':o:' and taht6 == ':o:' and taht9 == ':o:' or taht3 == ':o:' and taht5 == ':o:' and taht7 == ':o:':
                    await ctx.channel.send(f'<@{ctx.user.id}> WON!')
                    return
                if sonihtimal == 9:
                    await ctx.channel.send('Tie.'
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
                    if taht2 != ':x:' or taht2 != ':o:':
                        taht2 = ':x:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o2.content) == 3:
                    if taht3 != ':x:' or taht3 != ':o:':
                        taht3 = ':x:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o2.content) == 4:
                    if taht4 != ':x:' or taht4 != ':o:':
                        taht4 = ':x:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o2.content) == 5:
                    if taht5 != ':x:' or taht5 != ':o:':
                        taht5 = ':x:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o2.content) == 6:
                    if taht6 != ':x:' or taht6 != ':o:':
                        taht6 = ':x:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o2.content) == 7:
                    if taht7 != ':x:' or taht7 != ':o:':
                        taht7 = ':x:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o2.content) == 8:
                    if taht8 != ':x:' or taht8 != ':o:':
                        taht8 = ':x:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                elif int(o2.content) == 9:
                    if taht9 != ':x:' or taht9 != ':o:':
                        taht9 = ':x:'
                        await xox.edit(content='{}\n{}\n{}'.format(
                            taht + taht2 + taht3, taht4 + taht5 +
                            taht6, taht7 + taht8 + taht9))
                else:
                  await ctx.channel.send('Unexpected answer!')
                  return
        elif red_kabul.content.lower() == 'no':
            await ctx.channel.send(
                'The person you invited didn\'t accept your invite.'
            )
            return

        else:
            await ctx.channel.send('Unexpected answer!')
            pass
    except asyncio.TimeoutError:
        await ctx.channel.send("It took too long to respond!")
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
    embed = discord.Embed(title='Server Info', colour=discord.Colour.random())
    embed.add_field(
        name=f'Information about {ctx.guild.name}',
        value=
        f':white_small_square: Owner: {s} :white_small_square: \n \n :white_small_square: Number of the members: {ü} :white_small_square: \n \n :white_small_square: Number of channels: {k} :white_small_square: \n \n :white_small_square: Number of text channels: {yk} :white_small_square: \n \n :white_small_square: Number of voice channels: {sk} :white_small_square: \n \n :white_small_square: Verification: {vr} :white_small_square:'
    )
    embed.set_footer(text=f'This command is used by {ctx.user.name}')
    await ctx.response.send_message(embed=embed)


@tree.command(name="minecraft",description="Minecraft achievement.")
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
        await ctx.response.send_message(f'**Error: {e}**')


@tree.command(name="guessthenumber",description="Guess the number game.")
@commands.cooldown(1, 45, commands.BucketType.user)
async def sayıtahmin(ctx: discord.Interaction):
    x = random.randint(1, 100)
    y = 6
    await ctx.response.send_message(
        'I have chosen a number between 1 and 100. Can you guess it? You have 6 tries to guess!'
    )
    while True:
        try:
            msg = await client.wait_for(
                'message',
                check=lambda message: message.author.id == ctx.user.id,
                timeout=90)
            if y == 1 and int(msg.content) == x:
                await msg.channel.send('Congratulations! You found the number!')
            elif y == 1:
                await msg.channel.send(
                    f'Unfortunately, your tries have run out... **The number I chose was: {x}**')
                break

            elif int(msg.content) > x:
                y = y - 1
                await msg.channel.send(
                    f'The number I chose is a **smaller** number! ** You have {y} tries remaining!**'
                )

            elif int(msg.content) < x:
                y = y - 1
                await msg.channel.send(
                    f'The number I chose is a **bigger** number! ** You have {y} tries remaining!**'
                )

            else:
                await msg.channel.send('Congratulations! You found the number!')
                break
        except ValueError:
            pass
        except Exception as e:
            print(e)
            await ctx.response.send_message(
                'You took too long to respond!')
            return


@tree.command(name="hack",description="Learn how to hack bots")
async def yolla(ctx: discord.Interaction):
  await ctx.response.send_message('<a:rickroll:1016265373919760406>')



@tree.command(name="ban",description="Ban a member.")
@app_commands.describe(üye="Specify a member to ban", neden="Reason of ban.")
@app_commands.rename(üye="member",neden="reason",mesajsil="deletemessages")
@discord.app_commands.checks.has_permissions(ban_members=True)
async def ban(ctx: discord.Interaction, üye: discord.Member, neden: str, mesajsil: int = 0):
    if üye.id == client.user.id:
        await ctx.response.send_message(
            'Okay bro I banned myself. Wanna ban someone else now?'
        )
    elif üye.id == ctx.user.id:
        await ctx.response.send_message(
            'Look... Bro... You are gonna ban yourself permanently.. Are you sure? (yes/no)')
        zort = await client.wait_for(
            'message',
            check=lambda msg: ctx.user.id == msg.author.id,
            timeout=50)
        if zort.content.lower() == 'yes':
            await üye.ban(reason='suicide... member self-banned..',delete_message_days=0)
            await ctx.response.send_message('rip ' + ctx.user.name)
        else:
            return
    else:
        await üye.ban(reason=neden,delete_message_days=mesajsil)
        await ctx.response.send_message(
            f'**{ctx.user.name} banned a member named {üye.name}. Reason:{neden}**'
        )


@tree.command(name="unban", description="Unban a member.")
@app_commands.describe(üye="Member's nick and tag without any space.")
@app_commands.rename(üye="member")
@discord.app_commands.checks.has_permissions(ban_members=True)
async def unban(ctx: discord.Interaction, üye: str):
    banlılar = [banli async for banli in ctx.guild.bans()]
    üye_nick, üye_tag = üye.split('#')

    for i in banlılar:
        bismillah = i.user

        if (bismillah.name, bismillah.discriminator) == (üye_nick, üye_tag):
            await ctx.guild.unban(bismillah)
            await ctx.response.send_message(f'{bismillah} kullanıcısının banı kaldırıldı!')


@tree.command(name="kick",description="Kick a member.")
@app_commands.describe(üye="Specify a member.",neden="Reason of kick.")
@app_commands.rename(üye="member", neden="reason")
@discord.app_commands.checks.has_permissions(kick_members=True)
async def kick(ctx: discord.Interaction, üye: discord.Member, neden: str):
    if üye.id == client.user.id:
        await ctx.response.send_message(
            'OK. I banned myself now. Do you wanna ban others?')
    elif üye.id == ctx.user.id:
        await ctx.response.send_message(
            'Look... Bro... You will ban urself permanently...')
        zort = await client.wait_for(
            'message',
            check=lambda msg: ctx.user.id == msg.author.id,
            timeout=50)
        if zort.content.lower() == 'evet':
            await üye.kick(reason='suicide... member self-banned..')
            await ctx.response.send_message('https://youtu.be/2agdQzh_zSk?t=72')
        else:
            return
    else:
        await üye.kick(reason=neden)
        await ctx.response.send_message(
            f'**{üye.name} is banned by {ctx.user.name}\nReason: {neden}**'
        )


@tree.command(name="pfp",description="Sends a member's pfp")
@app_commands.rename(arg="member")
async def pfp(ctx: discord.Interaction, arg: discord.Member = None):
    if not arg == None:
        pfp = arg.avatar.url
        embed = discord.Embed(title="Profile Picture",
                              description='{}'.format(arg.mention),
                              color=0xecce8b)
        embed.set_image(url=(pfp))
        await ctx.response.send_message(embed=embed)
    else:
        arg = ctx.user
        pfp = arg.avatar.url
        embed = discord.Embed(title="Profile Picture",
                              description='{}'.format(arg.mention),
                              color=0xecce8b)
        embed.set_image(url=(pfp))
        await ctx.response.send_message(embed=embed)


@tree.command(name="tts",description="Text to speech.")
@app_commands.describe(text="Write a text.",language="Use 'en' for english, 'es' for spanish, 'ru' for russian, 'ja' for japanese etc. Default is English.")
async def tts(ctx: discord.Interaction,text: str, language: str = "en"):
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
        voice.play(FFmpegOpusAudio(f'adana{x}.mp3'))
        voice.is_playing()
        sleep(1)
        os.remove(f'adana{x}.mp3')




@tree.command(name="skip",description="Skip the song.")
async def s(ctx: discord.Interaction):
    
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {
        'before_options':
        '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn'
    }
    await ctx.response.send_message("Song skipped!",ephemeral=True)
    voice = get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    with YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(song_queue[str(ctx.guild.id)][1], download=False)
    URL = info['url']
    voice.play(FFmpegOpusAudio(URL, **FFMPEG_OPTIONS))
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
    await a.send('**Channel recreated successfully!**')
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
        await ctx.response.send_message('**Loop started.**')
    else:
        loopunbabası.stop()
        await ctx.response.send_message('**Loop stopped.**')


@tree.command(name="play",description="Plays music.")
async def play(ctx: discord.Interaction, search: str):
  try:
      try:
          if ctx.user.voice.channel:
              pass
      except:
          await ctx.response.send_message("You are not connected to any voice channel.", ephemeral=True)
          return
  
      await ctx.response.send_message('**Searching the video...**')
      query_string = urllib.parse.urlencode({'search_query': search})
      htm_content = urllib.request.urlopen('http://www.youtube.com/results?' + query_string)
      search_results = re.findall(r'/watch\?v=(.{11})', htm_content.read().decode())
  
      YDL_OPTIONS = {
          'format': 'bestaudio',
          'noplaylist': True,
          'nocheckcertificate': True,
          'ignoreerrors': False,
          'logtostderr': False,
          'quiet': True,
          'no_warnings': True,
          'source_address': '0.0.0.0'
      }
      FFMPEG_OPTIONS = {
          'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
          'options': '-vn'
      }
  
      voice = get(client.voice_clients, guild=ctx.guild)
      channel = ctx.user.voice.channel
  
      if voice and voice.is_connected():
          await voice.move_to(channel)
      else:
          voice = await channel.connect()
  
      if not voice.is_playing():
          if len(song_queue[str(ctx.guild.id)]) == 0:
              song_queue[str(ctx.guild.id)] = [f'{search_results[0]}']
          else:
              del song_queue[str(ctx.guild.id)][0]
  
          await ctx.edit_original_response(content='**Fetching video information...**')
          print(song_queue[str(ctx.guild.id)])
  
          with YoutubeDL(YDL_OPTIONS) as ydl:
              info = ydl.extract_info(song_queue[str(ctx.guild.id)][0], download=False)
          URL = info['url']
          TITLE = info['title']
          thumb = info['thumbnails'][0]
          videofoto = thumb['url']
          sure = info['duration']
          kanal = info["uploader"]
          videoizlen = info['view_count']
          suremin = sure // 60
          suresec = sure % 60
  
          if suresec < 10:
              suresec = f'0{suresec}'
          if suremin < 10:
              suremin = f'0{suremin}'
  
          voice.play(FFmpegOpusAudio(URL, **FFMPEG_OPTIONS))
          voice.is_playing()
  
          embed = discord.Embed(title='Now playing...', description='', colour=discord.Colour.default())
          embed.set_footer(text=f'Views: {videoizlen}')
          embed.set_thumbnail(url=videofoto)
          embed.add_field(name=kanal, value=f'```{TITLE}\n\n00:00 ------------------------- {suremin}:{suresec}```', inline=False)
          
          if len(song_queue[str(ctx.guild.id)]) > 0:
              del song_queue[str(ctx.guild.id)][0]
  
          await ctx.edit_original_response(content=None, embed=embed)
      else:
          if len(song_queue[str(ctx.guild.id)]) == 0:
              song_queue[str(ctx.guild.id)] = [f'{search_results[0]}']
          else:
              song_queue[str(ctx.guild.id)].append(f'{search_results[0]}')
  
          with YoutubeDL(YDL_OPTIONS) as ydl:
              info = ydl.extract_info(song_queue[str(ctx.guild.id)][-1], download=False)
          TITLE = info['title']
          thumb = info['thumbnails'][0]
          videofoto = thumb['url']
          embed = discord.Embed(title='Song added to the queue.', description='', colour=discord.Colour.default())
          embed.set_footer(text='SoloBot by Solø#1000')  # İstediğiniz bir şey varsa yazabilirsiniz
          embed.set_thumbnail(url=videofoto)  # İstediğiniz bir şey varsa URL'yi buraya yazabilirsiniz
          embed.add_field(name='**Added the queue**', value=f'```Song: {TITLE}```', inline=False)
          await ctx.edit_original_response(content=None, embed=embed)
  
          try:
              sıra.start(ctx, search)
          except:
              pass
  except Exception as e:
      print(e)



# durdurulmuş şarkıyı devam ettirme
@tree.command()
async def resume(ctx: discord.Interaction):
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        voice.resume()
        await ctx.response.send_message('**Song continues from where it left off...**')


# duraklatır bir süreliğine
@tree.command()
async def pause(ctx: discord.Interaction):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
        await ctx.response.send_message('**Song paused...**')


# durdurur
@tree.command(description="Disconnects the bot from the voice channel")
async def disconnect(ctx: discord.Interaction):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
      try:
        song_queue[str(ctx.guild.id)][0] = []
      except:
        pass
      finally:
        voice.stop()
        voice = await client.voice_clients[0].disconnect()        
        await ctx.response.send_message('**Leaving the voice chat...**')
    else:
        voice = await client.voice_client[0].disconnect()



# mesaj silmece
@tree.command(name="purge",description="Purge the messages.")
@app_commands.checks.cooldown(1, 30)
@app_commands.describe(amount="Number of messages to be deleted")
@discord.app_commands.checks.has_permissions(manage_messages=True)
async def sil(ctx: discord.Interaction, amount: int = 15, reason: str = "No reason given."):
    await ctx.response.defer()
    ney = await ctx.followup.send("**Deleting {} messages...**".format(amount),ephemeral=False)
    # mesaj silmece check
    def silcheck(mesaj):
      return mesaj != ney
    await ctx.channel.purge(limit=amount+1,reason=reason, check=silcheck)
    await ney.delete(delay=3)

@sil.error
async def sil_error(ctx: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.CommandOnCooldown):
        saniye = float(str(error).split("Try again in ")[1].split("s")[0])
        await ctx.response.send_message(str(error), ephemeral=False, delete_after=saniye)
    


@tree.command(name="yt",description="Search a video on Youtube")
@app_commands.rename(search="search_query")
async def yt(ctx: discord.Interaction, search: str):

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

@tree.command(name="queue",description="Get the song queue.")
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
        await ctx.response.send_message('There are no songs in the queue.')


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
                voice.play(FFmpegOpusAudio(URL, **FFMPEG_OPTIONS))
                voice.is_playing()
                embed = discord.Embed(title='Şuanda oynatılan...',
                                      description='',
                                      colour=discord.Colour.default())
                embed.set_footer(
                    text=
                    f'Views: {videoizlen}'
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
                voice.play(FFmpegOpusAudio(URL, **FFMPEG_OPTIONS))
                voice.is_playing()
                embed = discord.Embed(title='Now playing...',
                                      description='',
                                      colour=discord.Colour.default())
                embed.set_footer(
                    text=f'Views: {videoizlen}'
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
                    voice.play(FFmpegOpusAudio(URL, **FFMPEG_OPTIONS))
                    voice.is_playing()
                    embed = discord.Embed(title='Now playing...',
                                          description='',
                                          colour=discord.Colour.default())
                    embed.set_footer(
                        text=
                        f'Views: {videoizlen}'
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
# Spotify dinlediğin için teşekkürler. Ciddiyim.
with open('jsons/calan.json') as f:
  calan_json = f.read()
calan = json.loads(calan_json)
starting = None
ending = None
sure=None
@tasks.loop(seconds=1)
async def spotimer():
  ctx = client.get_guild(1015344885433372732)
  yunus = ctx.get_member(921084920116437002)
  global calan 
  global starting 
  global ending
  global sure
  spotify_dinledigin_icin_tesekkurler_ciddiyim_radyo_dinliyor_olabilirdin_kaset_caliyor_olabilirdin_plak_caliyor_olabilirdin_veya_sekiz_parcalik_teyp_de_dinliyor_olabilirdin_ama_spotify_dinliyorsun_tekrar_tesekkurler_ve_hala_tadini_cikarabilecegin_onlarca_farklı_calma_listesi_var = yunus.activities
  if spotify_dinledigin_icin_tesekkurler_ciddiyim_radyo_dinliyor_olabilirdin_kaset_caliyor_olabilirdin_plak_caliyor_olabilirdin_veya_sekiz_parcalik_teyp_de_dinliyor_olabilirdin_ama_spotify_dinliyorsun_tekrar_tesekkurler_ve_hala_tadini_cikarabilecegin_onlarca_farklı_calma_listesi_var == None:
    pass
  else:
    buldum = None
    for i in spotify_dinledigin_icin_tesekkurler_ciddiyim_radyo_dinliyor_olabilirdin_kaset_caliyor_olabilirdin_plak_caliyor_olabilirdin_veya_sekiz_parcalik_teyp_de_dinliyor_olabilirdin_ama_spotify_dinliyorsun_tekrar_tesekkurler_ve_hala_tadini_cikarabilecegin_onlarca_farklı_calma_listesi_var:
      if i.name == 'Spotify':
        buldum=i
       
      else:
        pass
      try:
        if buldum != None:
          if calan['title'] != buldum.title:
            ending = (datetime.now().minute*60) + datetime.now().second
            try:
              try:
                print('l1')
                sure = int(ending)-int(starting)
                print(sure)
              except Exception as e:
                print(e)
                pass
              print('l3')
              
              with open('txts/history.txt','r') as f:
                eski = f.read()
              split2 = eski
              with open('txts/history.txt','w+') as f:
                f.write('{}\n\n{} ----> {}\n- [{}]'.format(split2,calan['title'],str(sure),calan['url']))
                print('l4')
            
            except Exception as e:
              print(e)
              pass
            calan['title'] = buldum.title
            calan['url'] = buldum.track_url
            starting = (datetime.now().minute*60) + datetime.now().second
            print(calan['title'] + ' ' + calan['url'])
      except:
        calan['title'] = buldum.title
        calan['url'] = buldum.track_url
        pass
    else:
      pass

keep_alive.keep_alive()
client.run(TOKEN)

