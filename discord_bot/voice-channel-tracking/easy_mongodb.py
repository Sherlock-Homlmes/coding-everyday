from threading import Thread
import os
import time
######database
#
from pymongo import MongoClient

from threading import Thread
from waiting import wait

from dotenv import load_dotenv

## thuộc tính: account, password, key1, key2
load_dotenv()
database_url = os.getenv('database_url', "value does not exist")
cluster = MongoClient(database_url)
dtbs = cluster["discord_betterme"]
dtb = dtbs["betterme_study_time"]
data_key = "learn_time_count"
#start
#########################################advance#####################################
#cre_data
def cre_data(name,value):
	default_data ={
	"name":name,
	"value":value
	}
	dtb.insert_one(default_data)
#take_data
def take_data(name):
    tests = dtb.find( { "name":name } )
    for test in tests:
        return test["value"]

db = take_data(data_key)
stable_db = take_data(data_key)    
########def
def open_again(name):
  global db,stable_db
  dtb.update_one({ "name": name },  {'$set': {'value':db}} )
  stable_db = take_data(data_key)

def run1():
  global db,stable_db
  print("call mongo database")
  while True:
    #print("repeat\n")
    wait(lambda: db != stable_db, timeout_seconds=None)
    #print("change\n")
    #start
    #start_time = time.time()
    open_again(data_key)
    #end_time = time.time()
    #print('Total all time elapsed: %.6f seconds' % (end_time - start_time))
    

    
#t1 = Thread(target=run1)
#t1.start()


hdtb = dtbs["transfer_history"]

def transfer_history(user_id):
  user_id = str(user_id)
  history = hdtb.find({"id":user_id})

  transfer = None
  for his in history:
    transfer = his

  if transfer:
    value = 0
    for val in transfer["history"]:
      value += transfer["history"][val]

    return {"value" : value, "history": transfer["history"] }  
  else:
    return {"value" : 0, "history":{} }