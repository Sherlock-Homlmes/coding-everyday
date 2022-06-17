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

dtb = dtbs['news_data']
tdtb = dtbs["topic_position"]
ldtb = dtbs["load_news_data"]

#start
#########################################database#####################################
#cre_data
def ndb(value):
  tests = dtb.find({ 'name':value['name'] })
  i = 0
  for test in tests:
    i += 1

  if i == 0:

    tag_count = topic_count("count")
    tag_count["value"] += 1
    pos = tag_count["value"]
    value['position'] = pos
    update_topic_count("count",tag_count)
    
    for key in value["tags"]:
      topic = topic_count(key)
      topic["value"] += 1
      topic["position"].insert(0,pos)
      update_topic_count(key,topic)

    dtb.insert_one(value)
    minimum_data(value)

  else:
    print('already have '+ value['name'])

def minimum_data(element:dict):
  ele = {}
  ele["position"] = element["position"]
  ele["name"] = element["name"]
  ele["title"] = element["title"]
  ele["description"] = element["description"]
  ele["slide_show_link"] = element["slide_show_link"]
  ele["thumbnail_link"] = element["thumbnail_link"]

  ldtb.insert_one(ele)
  print(" ")
  print("insert minimum element done")
  print(ele)
  print(" ")


#take_data
def take_ndb(key,value):
  tests = dtb.find( { '{}'.format(key): value } )
  i = 0
  for test in tests:
    i += 1
    return test

  if i == 0: return False

#update_data
def update_ndb(pos,value):
  global dtb
  dtb.update_one({ 'position': pos },  {'$set':value} )

#count

def topic_count(key:str):
  tests = tdtb.find( { 'name': key } )
  for test in tests:
    return test

def update_topic_count(key,value):
  tdtb.update_one({"name":key},{'$set':value})

#update element
def update_element(pos:int,key:str,value):
  dtb.update_one({"position":pos},{'$set':{'{}'.format(key) : value }})

################################################### page process
#tag find
def position_show(pos_start:int,pos_end:int):
  element = dtb.find({ 'position': {'$gt':pos_start-1,'$lt':pos_end+1} }).sort('position',-1)

  value = []
  for ele in element:
    value.append(ele)

  return value

#find element in post list
def find_pos(pos_list:list):
  ###element = dtb.find({"position": { '$in': pos_list }  }).sort('position',-1)
  element = ldtb.find({"position": { '$in': pos_list }  }).sort('position',-1)

  value = []
  for ele in element:
    value.append(ele)

  return value


