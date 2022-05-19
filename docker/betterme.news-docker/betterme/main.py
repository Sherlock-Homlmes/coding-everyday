#necess
from threading import Thread
import time
from dotenv import load_dotenv
import os
import asyncio

#fastapi
from fastapi import (
  FastAPI, Body, Request, 
  File, UploadFile, Form, 
  Depends,  
  Response, Cookie, Header,
  Query, 
  WebSocket, 
  status
  )
#template
from fastapi.templating import Jinja2Templates
#model
from betterme.model import RACModel

from fastapi.responses import HTMLResponse
#from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from typing import Optional
from pydantic import BaseModel
from typing import Union

#load page
from betterme.load_page_engine import load_page, load_topic,take_ndb, topic_count, find_pos ,position_show,view_process

#scrap
from betterme.easy_json.easy_json import opendb, writedb


app = FastAPI(docs_url="/all-api", redoc_url=None)
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="betterme/static"), name="static")

############# login and oauth

########## 1.oauth discord

from zenora import APIClient
from betterme.database.mongodb.discord_user_database import discord_user,take_discord_user_by_id

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


@app.get("/discord_oauth")
async def discord_oauth(request:Request,response: Response,code:str):

    print(code)

    URIFragments = client.oauth.get_access_token(code, REDIRECT_URL)
    URIFragments.expires_in = None
    discord_access_token = URIFragments.access_token

    current_user = get_discord_user(discord_access_token)
    if current_user:
      response.set_cookie(
        key="discord_access_token",
        value=discord_access_token,
        httponly=True
        )

      discord_user(current_user)

      return "got ur token"

    else:
      return "Something wrong with your login"


@app.get("/test_discord")
async def read_cookie(
  request: Request
  ):


  client_host = request.client.host
  print(client_host)
  discord_access_token = request.cookies.get("discord_access_token")
  print(discord_access_token)

  try:
    current_user = get_discord_user(discord_access_token)
    print(current_user)

  except Exception as e:
    print(e)
    return "something wrong"

  return templates.TemplateResponse("discord_oauth.html",
    {"request":request,
    "current_user":current_user
    })

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

### jwt
  #
  # hash token
  #   # save to database: {hashvalue:token}
  #
  # remember







###############index

topic = ["khoa-hoc","lich-su","dia-ly","sinh-hoc",
         "10-van-cau-hoi-vi-sao","su-that-thu-vi","1001-bi-an","danh-nhan-the-gioi","the-gioi-dong-vat",
         "y-hoc-suc-khoe","kien-truc-doc-dao"]

tam1, tam2, tam3 = load_page(1)
post_list = tam1
hot_list = tam2
hot_first = hot_list[0]
del hot_list[0]
most_view_list = tam3

stable_pos = topic_count("count")["value"]


@app.get("/")
async def home(request:Request):
  global post_list, hot_list, hot_first, most_view_list,stable_pos

  start_time = time.time()
  page_number = 1

  now_pos = topic_count("count")["value"]
  if now_pos != stable_pos:

    tam1, tam2, tam3 = load_page(1)
    post_list = tam1
    hot_list = tam2
    hot_first = hot_list[0]
    del hot_list[0]
    most_view_list = tam3

    print("load new page")
  else:
    print("load stable page")
  end_time = time.time()
  print('Total all time elapsed: %.6f seconds' % (end_time - start_time))

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

#page
@app.get("/page-{page_number}")
async def page(request:Request,page_number:str):

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

###################################################################################### scraping 
from betterme.bettermenews_database.add_new_data import test_create_data, create_data, ndb

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

######################################################topic + post
@app.get("/{name}")
async def topic_post(request:Request,name:str):
  print(name)

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

        return templates.TemplateResponse("news_post.html".format(html_type),
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
    else:
      return templates.TemplateResponse("404_error.html",{"request":request})

#comment
from betterme.database.mongodb.rac_database import creRAC, takeRAC, take_rate_number_by_pos, check_can_comment

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

'''
###########index
@app.get('/')
async def index(request:Request):
  return templates.TemplateResponse("index.html",{"request":request,"oauth_url":OAUTH_URL})

#########check-data
@app.get("/check_data")
async def check_data(request:Request):
  return templates.TemplateResponse("check_data.html",{"request":request})
  
#result of check_data
@app.post("/result")
async def result(request:Request,name:str = Form(...)):
  global db
  
  if name in db.keys():
    hour = db[name]["m_all_time"] / 60
    minute = db[name]["m_all_time"] % 60
    return templates.TemplateResponse("check_data.html", {"request":request,"name" : db[name]["name"], "hour" : hour, "minute" : minute}) 
  else:
    return "Nhập sai ID hoặc chưa từng học ở BetterMe"


@app.get("/")
async def test(request:Request):
  #global db
  return templates.TemplateResponse("test.html",{"request":request})

async def get_cookie_or_token(
    websocket: WebSocket,
    session: Optional[str] = Cookie(None),
    token: Optional[str] = Query(None),
):
    if session is None and token is None:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
    return session or token

@app.websocket("/items/{item_id}/ws")
async def websocket_endpoint(
    websocket: WebSocket,
    item_id: str,
    q: Optional[int] = None,
    cookie_or_token: str = Depends(get_cookie_or_token),
):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        print(data)
        await websocket.send_text(
            f"Session cookie or query token value is: {cookie_or_token}"
        )
        if q is not None:
            await websocket.send_text(f"Query parameter q is: {q}")
        await websocket.send_text(f"Message text was: {data}, for item ID: {item_id}")

@app.get("/nicepage")
async def test(request:Request):
  return templates.TemplateResponse("nicepage.html",{"request":request})

@app.get("/news")
async def news(request:Request):

  page_number = 1
  number_of_news = count()["count"]

  pos_start = number_of_news - 17 * (page_number)
  if pos_start < 1:
    pos_start = 1

  pos_end = number_of_news - 17 * (page_number - 1)


  #print(pos_start,pos_end)
  post_list = position_show(pos_start,pos_end)
  #print(post_list)

  return templates.TemplateResponse("news.html",{"request":request,"post_list":post_list,"page":page_number})



'''




###### run
#import uvicorn
#uvicorn.run(app,port=8082)