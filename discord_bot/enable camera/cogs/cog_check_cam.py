import os
import discord
from discord.utils import get
import asyncio
from discord.ext import commands


class Example(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  full_cam_id =[
  #915923719216574485,
  #915238716803514389,
  #922906319642583050

  923680071280103424
  ]
  cam_stream_id = [
  923680395491434516
  ]

  @commands.Cog.listener()
  async def on_ready(self):
    print("check cam is ready")

  @commands.event
  async def on_voice_state_update(self,member, member_before, member_after):

    #guild = bot.get_guild(880360143768924210)



  ###############only cam
    if member_after.channel != None:
  ####check cam on
      if member_after.channel.id in full_cam_id:
          await asyncio.sleep(5)
          mem_voice_state = member.voice
          if mem_voice_state.self_video == False:
            print("kick cam start")
            await asyncio.sleep(10)

            #nhắc nhở
            mem_voice_state = member.voice
            if mem_voice_state != None:
              if mem_voice_state.self_video == False and mem_voice_state.channel.id in full_cam_id:

                embed= discord.Embed(
                title = "**Nhắc nhở**",
                description = member.name+", bạn đang ở trong phòng FULL CAM. Hãy bật camera, nếu không bạn sẽ bị kick sau 1 phút",
                colour = discord.Colour.red()
                )
                pfp = member.avatar_url
                embed.set_thumbnail(url=pfp)
                embed.set_footer(text='''BetterMe-Better everyday''')

                msg = await member.send(content=member.mention,embed=embed)

                #kick
                await asyncio.sleep(45)
                mem_voice_state = member.voice
                if mem_voice_state != None:
                  if mem_voice_state.self_video == False and mem_voice_state.channel.id in full_cam_id:
                    await member.move_to(None)

                    embed= discord.Embed(
                    title = "**Nhắc nhở**",
                    description = member.name+", bạn đã bị kick ra khỏi phòng vì không bật cam",
                    colour = discord.Colour.red()
                    )
                    pfp = member.avatar_url
                    embed.set_thumbnail(url=pfp)
                    embed.set_footer(text='''BetterMe-Better everyday''')
                    await msg.edit(embed=embed)
                  else:

                    embed= discord.Embed(
                    title = "**Cảm ơn**",
                    description = member.name+", cảm ơn bạn đã bật cam",
                    colour = discord.Colour.green()
                    )
                    pfp = member.avatar_url
                    embed.set_thumbnail(url=pfp)
                    embed.set_footer(text='''BetterMe-Better everyday''')

                    await msg.edit(embed=embed)

                else:
                  embed= discord.Embed(
                      title = "**Cảm ơn**",
                      description = member.name+", cảm ơn bạn đã rời phòng",
                      colour = discord.Colour.green()
                      )
                  pfp = member.avatar_url
                  embed.set_thumbnail(url=pfp)
                  embed.set_footer(text='''BetterMe-Better everyday''')

                  await msg.edit(embed=embed)                  
            print("kick cam end")



  ###############cam | stream
    if member_after.channel != None:
  ####check cam on
      if member_after.channel.id in cam_stream_id:
          await asyncio.sleep(5)
          mem_voice_state = member.voice
          if mem_voice_state.self_video == False and mem_voice_state.self_stream == False:
            print("kick stream start")
            await asyncio.sleep(10)

            #nhắc nhở
            mem_voice_state = member.voice
            if mem_voice_state != None:
              if mem_voice_state.self_video == False and mem_voice_state.self_stream == False and mem_voice_state.channel.id in cam_stream_id:

                embed= discord.Embed(
                title = "**Nhắc nhở**",
                description = member.name+", bạn đang ở trong phòng CAM/STREAM. Hãy bật camera hoặc stream, nếu không bạn sẽ bị kick sau 1 phút",
                colour = discord.Colour.red()
                )
                pfp = member.avatar_url
                embed.set_thumbnail(url=pfp)
                embed.set_footer(text='''BetterMe-Better everyday''')

                msg = await member.send(content=member.mention,embed=embed)

                #kick
                await asyncio.sleep(45)
                mem_voice_state = member.voice
                if mem_voice_state != None:
                  if mem_voice_state.self_video == False and mem_voice_state.self_stream == False and mem_voice_state.channel.id in cam_stream_id:
                    await member.move_to(None)

                    embed= discord.Embed(
                    title = "**Nhắc nhở**",
                    description = member.name+", bạn đã bị kick ra khỏi phòng vì không bật cam hoặc stream",
                    colour = discord.Colour.red()
                    )
                    pfp = member.avatar_url
                    embed.set_thumbnail(url=pfp)
                    embed.set_footer(text='''BetterMe-Better everyday''')

                    await msg.edit(embed=embed)
                  else:

                    embed= discord.Embed(
                    title = "**Cảm ơn**",
                    description = member.name+", cảm ơn bạn đã bật cam/stream",
                    colour = discord.Colour.green()
                    )
                    pfp = member.avatar_url
                    embed.set_thumbnail(url=pfp)
                    embed.set_footer(text='''BetterMe-Better everyday''')

                    await msg.edit(embed=embed)

                else:
                  embed= discord.Embed(
                      title = "**Cảm ơn**",
                      description = member.name+", cảm ơn bạn đã rời phòng",
                      colour = discord.Colour.green()
                      )
                  pfp = member.avatar_url
                  embed.set_thumbnail(url=pfp)
                  embed.set_footer(text='''BetterMe-Better everyday''')

                  await msg.edit(embed=embed)                  
            print("kick stream end")


def setup(bot):
  bot.add_cog(Example(client))