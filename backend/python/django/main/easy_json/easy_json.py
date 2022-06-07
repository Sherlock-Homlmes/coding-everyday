#
import json

#
import asyncio
import io, json

from waiting import wait
import time

#
import threading
from threading import Thread

waiting_dict = None

#function
def opendb():
     with open('easy_json/easy_json.json', encoding='utf-8') as f1:
          waiting_dict = json.load(f1)
     return waiting_dict

def writedb(waiting_dict: dict):
     with io.open('easy_json/easy_json.json', 'w', encoding='utf-8') as f:
          json.dump(waiting_dict, f, ensure_ascii=False, indent=4) 


def open_database():
     global waiting_dict, stable_db
     try:
          with open('easy_json/easy_json.json', encoding='utf-8') as f1:
               stable_db = json.load(f1)
          with open('easy_json/easy_json.json', encoding='utf-8') as f2:     
               waiting_dict  = json.load(f2)          
          print("load database 1")
          with io.open('easy_json/prevent_easy_json.json', 'w', encoding='utf-8') as f:
               json.dump(waiting_dict, f, ensure_ascii=False, indent=4)
          print("rewrite database 2")
     except Exception as e:
          print(e)
          with open('easy_json/prevent_easy_json.json', encoding='utf-8') as f1:
               stable_db = json.load(f1)
          with open('easy_json/prevent_easy_json.json', encoding='utf-8') as f2:     
               waiting_dict  = json.load(f2)        
          print("load database 2")
          with io.open('easy_json/easy_json.json', 'w', encoding='utf-8') as f:
               json.dump(waiting_dict, f, ensure_ascii=False, indent=4)
          print("rewrite database 1")

def open_again():
     global waiting_dict,stable_db
     with io.open('easy_json/easy_json.json', 'w', encoding='utf-8') as f:
          json.dump(waiting_dict, f, ensure_ascii=False, indent=4) 
     with io.open('easy_json/prevent_easy_json.json', 'w', encoding='utf-8') as f:
          json.dump(waiting_dict, f, ensure_ascii=False, indent=4)
     with open('easy_json/easy_json.json', encoding='utf-8') as f1:
          stable_db = json.load(f1)

     print("database reload")

def run():
     global waiting_dict,stable_db
     open_database()
     while True:
          #print("repeat")
          wait(lambda: waiting_dict != stable_db, timeout_seconds=None)
          #start_time = time.time()
          #print("change")
          open_again()
          #end_time = time.time()
          #print('Total time elapsed: %.2f seconds' % (end_time - start_time))

def start_db():
     t1 = Thread(target=run)
     t1.start()