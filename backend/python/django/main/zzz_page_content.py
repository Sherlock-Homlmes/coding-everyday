#django
from urllib import response
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
from .load_page_engine import load_page, load_topic,take_ndb, topic_count, find_pos ,position_show,view_process
#scrap
from .easy_json.easy_json import opendb, writedb
#database
from .database.mongodb.discord_user_database import discord_user,take_discord_user_by_id
from .database.mongodb.rac_database import creRAC, takeRAC, take_rate_number_by_pos, check_can_comment
#scraping and database
from .bettermenews_database.add_new_data import test_create_data, create_data
#from bettermenews_database.news_database import ndb,take_ndb
from .auto_scrap import scrap_by_page_number, title_process, auto_scrap_process

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


async def home(request):
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

    print(hot_first)

    response = TemplateResponse(request,"news.html",{
      "post_list":post_list,
      "hot_first":hot_first,
      "hot_list":hot_list,
      "most_view_list":most_view_list,
      "page":page_number,
      "next_page":True,
      })
    response.set_cookie("pre_page","")
    return response

  elif len(post_list) >= 1:
    response =  TemplateResponse(request,"news.html",{
      "post_list":post_list,
      "hot_first":hot_first,
      "hot_list":hot_list,
      "most_view_list":most_view_list,
      "page":page_number,
      })
    response.set_cookie("pre_page","")
    return response

  else:
    return TemplateResponse(request,"404_error.html",{})


async def topic_post(request,name:str):

  if name in topic:
    page_number = 1
    post_list,most_view_list = load_topic(name,1)


    if len(post_list) >= 17:
      return TemplateResponse(request,"topic.html",{
        "topic_name": name,
        "post_list":post_list,
        "most_view_list":most_view_list,
        "page":page_number,
        "next_page":True,
        })
    elif len(post_list) >= 1:
      return TemplateResponse(request,"topic.html",{
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
        discord_access_token = request.COOKIES.get("discord_access_token")
        current_user = get_discord_user(discord_access_token)

        #take rate and comment
        rac = await takeRAC('position',position)

        if current_user:
          can_cmt = check_can_comment(current_user.id,position)
        else:
          can_cmt = True

        resp = TemplateResponse(request, "news_post.html",
          {
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
      return TemplateResponse("404_error.html",{"request":request})