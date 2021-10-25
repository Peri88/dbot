import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():

  await client.change_presence(status=discord.Status.online) #온라인
  #await client.change_presence(status=discord.Status.idle) #자리비움
  #await client.change_presence(status=discord.Status.dnd) #다른용무
  #await client.change_presence(status=discord.Status.offline) #오프라인

  await client.change_presence(activity=discord.Game(name="게임 하는중"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
  print("봇 이름:",client.user.name,"봇 아이디:",client.user.id,"봇 버전:",discord.__version__)

async def on_member_join(member):
    channel = client.get_channel('718410583396843614')
    await member.send('방가방가\n $ 명령어를 통해 다양한 서비스를 제공받을 수 있으니 해보라구 !') #privit 한 메세지를 보내줌 await channel.send('안뇽')
    await channel.send('안뇽')

client.run(os.environ['token'])