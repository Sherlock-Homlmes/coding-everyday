#### main
import discord
import time
from datetime import datetime,time,date
from discord.utils import get
import asyncio
from discord.ext import commands
from discord_slash import SlashCommand,SlashContext
from discord_slash.utils.manage_commands import create_option

#database
#from easy_mongodb import db,transfer_history

#xu ly thoi gian
#from timedef import minute, total_time, show_time, time_data, leader_board, time_per_day, time_in_day

from dotenv import load_dotenv



# start

#start
intents = discord.Intents().all()
bot = commands.Bot(command_prefix=["b,"], intents = intents)

@bot.event
async def on_ready():
  print("ready")

'''
from PIL import Image,ImageChops,ImageDraw,ImageFont
from io import BytesIO

def add_corners(im, rad):
  circle = Image.new('L', (rad * 2, rad * 2), 0)
  draw = ImageDraw.Draw(circle)
  draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
  alpha = Image.new('L', im.size, 255)
  w, h = im.size
  alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
  alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
  alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
  alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
  im.putalpha(alpha)
  return im


@bot.command(name="profile")
async def _profiles(ctx):
  async with ctx.typing():
    member = ctx.author

    name, nick, status = str(member), member.display_name, str(member.status).upper()
    joined_at = member.joined_at
    joined_at = str(joined_at.day)+"/"+str(joined_at.month)+"/"+str(joined_at.year)

    if str(member.id) not in db.keys():
      db[str(member.id)] = d_value

    show = show_time(db[str(member.id)]["m_all_time"])
    study_time = show[0]+" giờ "+show[1]+" phút"

    coin = str(int(show[0]) - transfer_history(str(member.id))["value"])

    profile = Image.open("pictures/user_info.png").convert("RGBA")
    role_hstc = get(ctx.guild.roles, name="HỌC SINH TÍCH CỰC")
    role_homie = get(ctx.guild.roles, name="HOMIE")
    if role_hstc in member.roles:
      hstc = Image.open("pictures/hstc.png").convert("RGBA")
    else:
      hstc = Image.open("pictures/hstc_nocolor.png").convert("RGBA")
    if role_homie in member.roles:
      homie = Image.open("pictures/homie.png").convert("RGBA")
    else:
      homie = Image.open("pictures/homie_nocolor.png").convert("RGBA")
    hstc = hstc.resize((200,200))
    homie = homie.resize((200,200))


    pfp = member.avatar_url_as(size=256)
    data = BytesIO(await pfp.read())
    pfp = Image.open(data)
    print(pfp.is_animated)
    print(pfp.n_frames)
    for frame in range(0,1):
      pfp.seek(frame)

    pfp = add_corners(pfp, 50)
    #pfp.save("pictures/{}.png".format(str(member.id)))
    #pfp = Image.open("pictures/{}.png".format(str(member.id)))


    draw = ImageDraw.Draw(profile)
    name_font = ImageFont.truetype("fonts/Mali-Italic.ttf",38)
    subfont = ImageFont.truetype("fonts/Mali-Regular.ttf",25)

    #center text
    max_width = 600
    w, h = draw.textsize(name, font=name_font)


    draw.text(((max_width-w)/2,30),name,font = name_font)
    draw.text((307,395),study_time,font = subfont)
    draw.text((190,425),coin,font = subfont)
    draw.text((325,460),joined_at,font = subfont)
    profile.paste(pfp,(172,110),pfp)
    profile.paste(hstc,(50,550),hstc)
    profile.paste(homie,(310,550),homie)    
    #profile.show()

    with BytesIO() as a:
      profile.save(a,"PNG")
      a.seek(0)
      await ctx.send(file = discord.File(a,"{}.png".format(str(member.id))))
'''


'''
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

'''



@bot.command(name="app")
async def app(ctx):
  from app.app import app
  await ctx.send("import done")







