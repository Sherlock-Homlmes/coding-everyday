from threading import Thread
import os
import time
######database
#
from pymongo import MongoClient

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
def creRAC(user_id:int,position:int,rate:int,comment:str,comment_number:int):
  can_cmt = rac_db.find(
    {
    "position":position,
    "user_id":user_id
    }
  )
  print(can_cmt)
  #return False

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
def takeRAC(key,value):
  element = rac_db.find( { f'{key}': value } )
  value = []
  for ele in element:
    value.append(ele)

  return value


