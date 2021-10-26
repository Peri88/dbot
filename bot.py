import discord, asyncio
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():

  await client.change_presence(status=discord.Status.online) #온라인
  #await client.change_presence(status=discord.Status.idle) #자리비움
  #await client.change_presence(status=discord.Status.dnd) #다른용무
  #await client.change_presence(status=discord.Status.offline) #오프라인

  await client.change_presence(activity=discord.Game(name="게임"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
  print("봇 이름:",client.user.name,"봇 아이디:",client.user.id,"봇 버전:",discord.__version__)

@client.event
async def on_member_join(member):
    fmt = '{1.name} 에 오신것을 환영합니다., {0.mention} 님'
    channel = member.server.get_channel("902039163698819093")
    await client.send_message(channel, fmt.format(member, member.server))
 
@client.event
async def on_member_remove(member):
    channel = member.server.get_channel("902039163698819093")
    fmt = '{0.mention} 님이 서버에서 나가셨습니다.'
    await client.send_message(channel, fmt.format(member, member.server))

client.run(os.environ['OTAyMDQwODIwNDYxNDY5NzE4.YXYo-g.UBZgZ6ZOeIBYtoy5vPNj2auqXnk'])