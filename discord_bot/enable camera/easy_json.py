#
import io, json
from waiting import wait
from threading import Thread

db = None

def open_database():
     global db, stable_db
     try:
          with open('easy_json.json', encoding='utf-8') as f1:
               stable_db = json.load(f1)
          with open('easy_json.json', encoding='utf-8') as f2:     
               db  = json.load(f2)          
          print("load database 1")
          with io.open('prevent_easy_json.json', 'w', encoding='utf-8') as f:
               json.dump(db, f, ensure_ascii=False, indent=4)
          print("rewrite database 2")
     except:
          with open('prevent_easy_json.json', encoding='utf-8') as f1:
               stable_db = json.load(f1)
          with open('prevent_easy_json.json', encoding='utf-8') as f2:     
               db  = json.load(f2)        
          print("load database 2")
          with io.open('easy_json.json', 'w', encoding='utf-8') as f:
               json.dump(db, f, ensure_ascii=False, indent=4)
          print("rewrite database 1")

open_database()

def open_again():
     global db,stable_db
     with io.open('easy_json.json', 'w', encoding='utf-8') as f:
          json.dump(db, f, ensure_ascii=False, indent=4) 
     with io.open('prevent_easy_json.json', 'w', encoding='utf-8') as f:
          json.dump(db, f, ensure_ascii=False, indent=4)
     with open('easy_json.json', encoding='utf-8') as f1:
          stable_db = json.load(f1)

def run():
     global db,stable_db
     while True:
          wait(lambda: db != stable_db, timeout_seconds=None)
          open_again()

t1 = Thread(target=run)
t1.start()