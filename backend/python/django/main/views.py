'''
#django
from django.shortcuts import render
from django.template.response import TemplateResponse
from .forms import *


# Create your views here.
#necess
from threading import Thread
import time
from dotenv import load_dotenv
import os
import asyncio
import json,io

### excisting directories
#load page
from bettermenews.main.views.load_page_engine import load_page, load_topic,take_ndb, topic_count, find_pos ,position_show,view_process
#scrap
from .easy_json.easy_json import opendb, writedb
#database
from .database.mongodb.discord_user_database import discord_user,take_discord_user_by_id
from .database.mongodb.rac_database import creRAC, takeRAC, take_rate_number_by_pos, check_can_comment
#scraping and database
from .bettermenews_database.add_new_data import test_create_data, create_data
#from bettermenews_database.news_database import ndb,take_ndb
from bettermenews.main.views.auto_scrap import scrap_by_page_number, title_process, auto_scrap_process

############# login and oauth

########## 1.oauth discord

from zenora import APIClient

load_dotenv()
TOKEN = os.getenv("TOKEN")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URL = os.getenv("REDIRECT_URL")
OAUTH_URL = os.getenv("OAUTH_URL")
print(OAUTH_URL)

client = APIClient(TOKEN, client_secret=CLIENT_SECRET)

def get_discord_user(access_token):

  if access_token == None:
    current_user = None

  else:
    try:
      bearer_client = APIClient(access_token, bearer=True)
      current_user = bearer_client.users.get_current_user()
    except Exception as e:
      print(e)
      current_user = None

  return current_user

def is_admin(access_token) -> bool:
  current_user = get_discord_user(access_token)
  if current_user:
    if current_user.id in admin_id:
      return True
    else:
      return False
  else:
    return False

@app.get("/discord_oauth")
async def discord_oauth(
  request:Request,
  response: Response,
  code:str
  ):

    print(code)

    URIFragments = client.oauth.get_access_token(code, REDIRECT_URL)
    URIFragments.expires_in = None
    discord_access_token = URIFragments.access_token

    current_user = get_discord_user(discord_access_token)
    if current_user:

      discord_user(current_user)

      pre_page = request.cookies.get("pre_page")
      print(pre_page)
      resp = RedirectResponse(url=f"/{pre_page}")
      resp.set_cookie(
        key="discord_access_token",
        value=discord_access_token,
        httponly=True,
        secure= True
        )

      return resp

    else:
      return "Something wrong with your login"

@app.get("/logout")
async def logout(request:Request,response: Response):

  access_token = request.cookies.get("discord_access_token")
  if access_token != None:
    response.delete_cookie("discord_access_token")

  return "u r logout"


    #return templates.TemplateResponse("discord_oauth.html",{"request":request,"current_user":current_user, "db":db[str(current_user.id)]})
  #except:
    #return "invalid token"


### oauth
  #
  # oauth discord
  #
  # oauth google

### cookie
  #
  # hash token(rsa)
  #   
  #
  # remember







###############index

topic = ["khoa-hoc","lich-su","dia-ly","sinh-hoc",
         "10-van-cau-hoi-vi-sao","su-that-thu-vi","1001-bi-an","danh-nhan-the-gioi","the-gioi-dong-vat",
         "y-hoc-suc-khoe","kien-truc-doc-dao"]
admin_id = [880359404036317215,278423331026501633]

tam1, tam2, tam3 = load_page(1)
post_list = tam1
hot_list = tam2
hot_first = hot_list[0]
del hot_list[0]
most_view_list = tam3

stable_pos = topic_count("count")["value"]

#page
@app.get("/page-{page_number}")
async def page(
  request:Request,
  response: Response,
  page_number:str):

  response.set_cookie(
    key="pre_page",
    value=f"page-{page_number}",
    )

  try:
    page_number = int(page_number)
  except Exception as e:
    page_number = 0
    print(e)

  if page_number != 0:
    tam1, tam2, tam3 = load_page(page_number)

    post_list = tam1
    hot_list = tam2
    hot_first = hot_list[0]
    del hot_list[0]
    most_view_list = tam3

    if len(post_list) >= 17:
      return templates.TemplateResponse("news.html",{"request":request,
        "post_list":post_list,
        "hot_first":hot_first,
        "hot_list":hot_list,
        "most_view_list":most_view_list,
        "page":page_number,
        "next_page":True,
        })
    elif len(post_list) >= 1:
      return templates.TemplateResponse("news.html",{"request":request,
        "post_list":post_list,
        "hot_first":hot_first,
        "hot_list":hot_list,
        "most_view_list":most_view_list,
        "page":page_number,
        })
    else:
      return templates.TemplateResponse("404_error.html",{"request":request})
  else:
    return templates.TemplateResponse("404_error.html",{"request":request})


@app.get("/{name}/page-{page_number}")
async def topic_page(request:Request,name:str,page_number:str):
  print(name)
  print(page_number)

  try:
    page_number = int(page_number)
  except Exception as e:
    page_number = 0
    print(e)

  if page_number != 0:
    post_list,most_view_list = load_topic(name,page_number)

    if len(post_list) >= 17:
      return templates.TemplateResponse("topic.html",{"request":request,
        "topic_name": name,
        "post_list":post_list,
        "most_view_list":most_view_list,
        "page":page_number,
        "next_page":True,
        })
    elif len(post_list) >= 1:
      return templates.TemplateResponse("topic.html",{"request":request,
        "topic_name": name,
        "post_list":post_list,
        "most_view_list":most_view_list,
        "page":page_number,
        })

    else:
      return templates.TemplateResponse("404_error.html",{"request":request})
  else:
    return templates.TemplateResponse("404_error.html",{"request":request})
'''
###################################################################################### scraping 
'''
@app.get("/scraping-khtv")
async def _scraping_khtv(request:Request):
  global topic

  return templates.TemplateResponse("scraping.html",{
    "request":request,
    "topics": topic
    })

@app.post("/scraping")
async def _scraping(
  request: Request,

  url: str = Form(...),
  name: str = Form(...),
  html_type: str = Form(...),

  pic_link: str = Form(...),

  description: str = Form(...),

  tags: list = Form(...)

  ):

  if pic_link == "None":
    return "Nhập sai dữ liệu"
  elif html_type not in ["normal","horror"]:
    return "Nhập sai dữ liệu"

  if "650" in str(pic_link) and "200" not in str(pic_link):
    thumbnail_link = ""
    slide_show_link = pic_link
  elif "200" in str(pic_link) and "650" not in str(pic_link):
    thumbnail_link = pic_link
    slide_show_link = ""    
  else:
    return "can detect pic link"



  if description == "None":
    description = ""

  data = await test_create_data(url,name,html_type,thumbnail_link,slide_show_link,description,tags)
  description = data["description"]
  keywords = data["keywords"]
  html_type = data["html_type"]
  content = data["content"]
  print(f"Add {name} to waiting_dict")

  #add data to wating dict 
  waiting_dict = opendb()
  i = 0
  while str(i) in waiting_dict:
    i += 1
  waiting_dict[str(i)]= {
  "url": url,
  "name": name,
  "html_type": html_type,
  "thumbnail_link": thumbnail_link,
  "slide_show_link": slide_show_link,
  "description": description,
  "tags": tags
  }
  writedb(waiting_dict)
  
  return templates.TemplateResponse("demo_news_post.html",
    {"request":request,
    "description": description,
    "keywords": keywords,
    "html_type": html_type,
    "content": content
    })

########## duyệt bài
@app.get("/check-list")
async def _check_list(
  request: Request,
  ):

  return templates.TemplateResponse("check-list.html",
    {"request":request,
    "waiting_dict": opendb()
    })

@app.get("/demo{num}")
async def _check(
  request: Request,
  num: int
  ):
  value = opendb()[str(num)]

  url = value["url"]
  name = value["name"] 
  html_type = value["html_type"] 
  thumbnail_link = value["thumbnail_link"] 
  slide_show_link = value["slide_show_link"] 
  description = value["description"] 
  tags = value["tags"] 

  data = await test_create_data(url,name,html_type,thumbnail_link,slide_show_link,description,tags)

  description = data["description"]
  keywords = data["keywords"]
  html_type = data["html_type"]
  content = data["content"]
  
  return templates.TemplateResponse("demo_news_post.html",
    {"request":request,
    "description": description,
    "keywords": keywords,
    "html_type": html_type,
    "content": content
    })

def new_data(check_list,waiting_dict):
  for key in check_list:
    value = waiting_dict[key]
    url = value["url"]
    name = value["name"]
    html_type = value["html_type"] 
    thumbnail_link = value["thumbnail_link"] 
    slide_show_link = value["slide_show_link"] 
    description = value["description"] 
    tags = value["tags"] 

    real_element = create_data(url,name,html_type,thumbnail_link,slide_show_link,description,tags)
    ndb(real_element)

@app.post("/confirm")
async def _confirm(
  request: Request,
  check_list: list = Form(...)
  ):
  print(check_list)

  waiting_dict = opendb()

  for key in check_list:
    value = waiting_dict[key]
    url = value["url"]
    name = value["name"]
    html_type = value["html_type"] 
    thumbnail_link = value["thumbnail_link"] 
    slide_show_link = value["slide_show_link"] 
    description = value["description"] 
    tags = value["tags"] 

    real_element = await create_data(url,name,html_type,thumbnail_link,slide_show_link,description,tags)
    ndb(real_element)

  #delete
  for key in check_list:
    if key in waiting_dict:
      del waiting_dict[key]

  writedb(waiting_dict)

  return f"Đã thêm {check_list} vào data"
'''
'''
######################################################topic + post
@app.get("/{name}")
async def _topic_post(
  request: Request,
  response: Response,
  name:str,
  ):

  if name in topic:
    page_number = 1
    post_list,most_view_list = load_topic(name,1)


    if len(post_list) >= 17:
      return templates.TemplateResponse("topic.html",{"request":request,
        "topic_name": name,
        "post_list":post_list,
        "most_view_list":most_view_list,
        "page":page_number,
        "next_page":True,
        })
    elif len(post_list) >= 1:
      return templates.TemplateResponse("topic.html",{"request":request,
        "topic_name": name,
        "post_list":post_list,
        "most_view_list":most_view_list,
        "page":page_number,
        })


  else:
    #take page content
    key = take_ndb("name",name)

    if key != False:
        description = key['description']
        keywords = key['keywords']
        title = key["title"]
        content = key["content"]
        html_type = key["html_type"]

        position = key['position']

        if "og_image" in key:
          og_image = key["og_image"]
        else:
          og_image = None

        view_process(key)

        #take current user
        discord_access_token = request.cookies.get("discord_access_token")
        current_user = get_discord_user(discord_access_token)

        #take rate and comment
        rac = await takeRAC('position',position)

        if current_user:
          can_cmt = check_can_comment(current_user.id,position)
        else:
          can_cmt = True

        resp = templates.TemplateResponse("news_post.html".format(html_type),
          {"request":request,

          #page content
          "description":description,
          "keywords":keywords,
          "og_image":og_image,
          "content":content,
          "title":title,
          'html_type':html_type,

          'name': name,

          #current user
          'current_user':current_user,
          'OAUTH_URL':OAUTH_URL,

          #rate and comment
          'position': position,
          'rac': rac,
          'can_cmt': can_cmt
          })

        resp.set_cookie(key="pre_page",value=f"{name}")

        return resp

    else:
      return templates.TemplateResponse("404_error.html",{"request":request})

#comment

@app.post("/comment")
async def _comment(
  request: Request,
  position: int = Form(...),
  rate: int = Form(...),
  comment: str = Form(...),
  ):

  discord_access_token = request.cookies.get("discord_access_token")
  current_user = get_discord_user(discord_access_token)
  if current_user:
    discord_user(current_user)
    comment_number = await take_rate_number_by_pos(position)
    await creRAC(current_user.id,position,rate,comment,comment_number)
    print(f"pos: {position} | rating: {rate} | comment: {comment}")

    return "success"
  else:
    return "Login to rate and comment"

@app.get("/nicepage")
async def test(request:Request):
  return templates.TemplateResponse("nicepage.html",{"request":request})

#auto scraping

@app.get('/auto-scrap/{page_number}')
async def auto_scrap(
  request: Request,
  page_number: int
  ):

  ad_check = is_admin(request.cookies.get("discord_access_token"))
  if ad_check == True:

      #return scrap_by_page_number(page_number)
      return templates.TemplateResponse("auto-scrap.html",{
        "request":request,
        "scraping": scrap_by_page_number(page_number),
        "topics": topic
        })

  else:
    content =  f"""
    <html>
      <a href={OAUTH_URL}>dang nhap</a>
    </html>
    """

    response = HTMLResponse(content=content,status_code=200)
    response.set_cookie(key="pre_page",value=f"auto-scrap/{page_number}")

    return response

  
@app.get('/auto-scrap/check-content/{name}')
async def scrap_check(
  request: Request,
  name: str,

  #html_type: str = Form(...),
  #tags: list = Form(...)

  ):

  with open('check_data.json', encoding='utf-8') as f1:
    all_post = json.load(f1)

  name = "/"+name
  url = "https://khoahoc.tv" + name
  thumbnail_link = all_post[name]['thumb_src']
  name = title_process(name)
  

  data = await test_create_data(url,name,"normal",thumbnail_link,"","",['khoa-hoc'])
  print(data)

  description = data["description"]
  keywords = data["keywords"]
  html_type = data["html_type"]
  content = data["content"]

  
  return templates.TemplateResponse("demo_news_post.html",
    {"request":request,
    "description": description,
    "keywords": keywords,
    "html_type": html_type,
    "content": content
    })

@app.post('/auto-scrap/confirm')
async def scrap_check(
  request: Request,

  check_list: list = Form(...),

  html_type: list = Form(...),
  tags: list = Form(...)

  ):

  #print(check_list)
  #print(html_type)
  #print(tags)

  await auto_scrap_process(check_list,html_type,tags)

  return "done"



import uvicorn
uvicorn.run(app,port=8082)
'''
