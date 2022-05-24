from threading import Thread
import os
import time
import asyncio
######database
#
from pymongo import MongoClient

from .discord_user_database import take_discord_user_by_id_list
import numpy as np

from dotenv import load_dotenv
import json,io

## thuộc tính: account, password, key1, key2
load_dotenv()
database_url = os.getenv('database_url', 'value does not exist')
cluster = MongoClient(database_url)
dtbs = cluster['better_news']

rac_db = dtbs['rating_and_comment']

#start
#########################################database#####################################
#cre_data
async def creRAC(user_id:int,position:int,rate:int,comment:str,comment_number:int):

  if check_can_comment(user_id,position) == False:
    return False
  else:
    rac = {
    "user_id": user_id,

    "position":position,

    "rate":rate,
    "comment":comment,
    "comment_number":comment_number
    }
    rac_db.insert_one(rac)

    return True

#take_data
async def takeRAC(key,value) -> list:
  element = rac_db.find( { f'{key}': value } )
  value = []

  #take all element
  for ele in element:
    value.append(ele)

  #take all user
  user_list = []
  for val in value:
    user_list.append(val['user_id'])

  user_dict = await take_discord_user_by_id_list(user_list)

  #sort element and process infomation
  for i in range(len(value)):
    value[i]['avatar_url'] = user_dict[ str(value[i]['user_id']) ] ['avatar_url']
    value[i]['username'] =   user_dict[ str(value[i]['user_id']) ] ['username']

  return value

async def take_rate_number_by_pos(position):
  value = rac_db.find( { 'position': position } ).sort('comment_number',-1).limit(1)

  for v in value:
    return v['comment_number']

#check if can comment
def check_can_comment(user_id:int,position:int):
  can_cmt = rac_db.count_documents(
    {
    "position":position,
    "user_id":user_id
    }
  )
  if can_cmt >= 1:
    return False
  else:
   return True