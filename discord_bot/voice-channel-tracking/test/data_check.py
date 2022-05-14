#from replit import db
import time
import io,json
import os
######database
#
from pymongo import MongoClient

## thuộc tính: account, password, key1, key2
mongo_key=[os.environ['mongo_key0'],os.environ['mongo_key1'],os.environ['mongo_key2'],os.environ['mongo_key3']]
cluster = MongoClient("mongodb+srv://"+mongo_key[0]+":"+mongo_key[1]+"@cluster0.gd2ti.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
dtbs = cluster[mongo_key[2]]
dtb = dtbs[mongo_key[3]]

#start
#########################################advance#####################################
#take_data
def take_data(name):
    tests = dtb.find( { "name":name } )
    for test in tests:
        return test["value"]




d_value = {
  "name":"",
  "y" : 0,
  "mon" : 0,
  "d":0,
  "h":0,
  "min":0,
  "h_all_time":0,
  "m_all_time":0,
  "h_all_time_transfer":0,
  "time_per_day":{
    "h_1":0,"m_1":0,
    "h_2":0,"m_2":0,
    "h_3":0,"m_3":0,
    "h_4":0,"m_4":0,
    "h_5":0,"m_5":0,
    "h_6":0,"m_6":0,
    "h_7":0,"m_7":0,
    "h_8":0,"m_8":0,
    "h_9":0,"m_9":0,
    "h_10":0,"m_10":0,  
    "h_11":0,"m_11":0,
    "h_12":0,"m_12":0,
    "h_13":0,"m_13":0,
    "h_14":0,"m_14":0,
    "h_15":0,"m_15":0,
    "h_16":0,"m_16":0,
    "h_17":0,"m_17":0,
    "h_18":0,"m_18":0,
    "h_19":0,"m_19":0,
    "h_20":0,"m_20":0,
    "h_21":0,"m_21":0,
    "h_22":0,"m_22":0,
    "h_23":0,"m_23":0,
    "h_24":0,"m_24":0,
    "h_25":0,"m_25":0,  
    "h_26":0,"m_26":0,
    "h_27":0,"m_27":0,
    "h_28":0,"m_28":0,
    "h_29":0,"m_29":0,
    "h_30":0,"m_30":0
  }
}

pass_key=["server_study_time"]

def time_data():
  db = take_data("learn_time_count")
  x = len(db.keys()) - 3
  y = 0
  z = 0
  start_time = time.time()
  for key in db.keys():
    if key not in pass_key:
      #print(db[key])
      if db[key]["h_all_time"] > 23:
        y = y+1
      if db[key]["h_all_time"] > 0:
        z = z+1

  end_time = time.time()
  print('Total time elapsed: %.2f seconds' % (end_time - start_time))
  print("Tổng số người học:"+str(x))
  print("Học trên 1 ngày:"+str(y))
  print("Học trên 1 giờ:"+str(z))
  return [str(x),str(y),str(z)]

####convert database
def convert_database():
  global db
  i = 0
  f = open("data.txt", "w")
  length = len(db.keys())

  db["server_study_time"] ={}
  db["server_study_time"]["h_all_time"] = db["d_all"]*24 + db["h_all"]
  db["server_study_time"]["m_all_time"] = db["m_all"]
  
  del db["d_all"]
  del db["h_all"]
  del db["m_all"]

  for key in db.keys():
    if key in pass_key:
      pass
    else:
      i += 1
      print(i)
      if i != length:
        f.write('"'+key+'":'+str(db[key])+",\n")
      else:
        f.write('"'+key+'":'+str(db[key]))
  print("done")

  f = open("data.txt", "r")
  x = f.read()
  x = x.replace("ObservedDict(value=", "")
  x = x.replace(")", "")
  x = x.replace("'", '"')
  x = "{\n"+x+"\n}"

  f = open("new_data.txt", "w")
  f.write(x)


def plus_time(h1,m1,h2,m2):
  m = m1+m2
  if m>=60:
    m = m - 60
    h = 1
  else:
    h = 0
  h += h1+h2
  return [h,m]
def minus_time(h1,m1,h2,m2):
  m = m1-m2
  if m<0:
    m = m + 60
    h = -1
  else:
    h = 0
  h += h1-h2
  return [h,m]

def fix_data():
  global d_value

  with open('easy_json.json', encoding='utf-8') as f1:     
    dtb  = json.load(f1)
  with open('clone.json', encoding='utf-8') as f2:     
    db  = json.load(f2)

  x = d_value["time_per_day"]
  for key in dtb.keys():
    dtb[key]["time_per_day"] = x
  for key in db.keys():
    db[key]["time_per_day"] = x 
    
  for key in db.keys():
    if key in dtb.keys():
      dtb[key]["h_all_time"] = minus_time(dtb[key]["h_all_time"],dtb[key]["m_all_time"],db[key]["h_all_time"],db[key]["m_all_time"])[0]
      dtb[key]["m_all_time"] = minus_time(dtb[key]["h_all_time"],dtb[key]["m_all_time"],db[key]["h_all_time"],db[key]["m_all_time"])[1]      
    else:
      dtb[key] = db[key]  

  print(dtb["881167503370362890"])
  #with io.open('easy_json.json', 'w', encoding='utf-8') as f:
    #json.dump(dtb, f, ensure_ascii=False, indent=4)     

def fix_data2():
  global d_value

  with open('easy_json.json', encoding='utf-8') as f1:     
    db  = json.load(f1)

  for key in db.keys():
    print(key)
    del db[key]["time_per_day"]

  with io.open('easy_json.json', 'w', encoding='utf-8') as f:
    json.dump(db, f, ensure_ascii=False, indent=4)       

def start():
  start_time = time.time()
  #convert_database()
  #fix_data()
  #fix_data2()
  #time_data()
  end_time = time.time()
  print('Total time elapsed: %.2f seconds' % (end_time - start_time))

#start()
