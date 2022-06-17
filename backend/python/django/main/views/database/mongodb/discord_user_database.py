from threading import Thread
import os
import time
import asyncio
######database
#
from pymongo import MongoClient
import numpy as np

from dotenv import load_dotenv
import json,io

## thuộc tính: account, password, key1, key2
load_dotenv()
database_url = os.getenv('database_url', 'value does not exist')
cluster = MongoClient(database_url)
dtbs = cluster['better_news']

user_db = dtbs['user_info']

#start
#########################################database#####################################
#cre_data
def discord_user(current_user):

  if take_discord_user_by_id(current_user.id):
    print("update user")
    update_discord_user_by_id(current_user)

  else:
    print("new user")

    user_info = {
    "user_id": current_user.id,
    "email": current_user.email,

    "is_verified": current_user.is_verified,

    "username": current_user.username,
    "discriminator": current_user.discriminator,
    "avatar_url": current_user.avatar_url

    }

    user_db.insert_one(user_info)

#take_data
def take_discord_user_by_id(value) -> list:
  element = user_db.find( { 'user_id': value } ).limit(1)
  value = []
  for ele in element:
    value.append(ele)
    
  if value  == []:
    return None
  else:
    return value[0]

async def take_discord_user_by_id_list(list_value) -> dict:
  element = user_db.find( { 'user_id': {'$in':list_value} } )
  value = {}
  for ele in element:
    value[str(ele['user_id'])] = ele
  
  #print(f'List value:{list_value}')
  #print(f'Value:{value}')
  return value

#update
def update_discord_user_by_id(current_user):
    user_info = {
    "$set":
      {
      "user_id": current_user.id,
      "email": current_user.email,

      "is_verified": current_user.is_verified,

      "username": current_user.username,
      "discriminator": current_user.discriminator,
      "avatar_url": current_user.avatar_url

      }
    }

    user_db.update_one( { 'id': current_user.id }, user_info )
