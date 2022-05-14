from replit import db


def clear():
  for key in db.keys():
    del db[key]

def cre():
  db["name"]={"0":0,}
  db["old_time"] = 45

def check():
  global i
  i = 0
  for key in db.keys():
    #if "host_id" in db[key]:
    i = i +1
    print(key)
    print(db[key])


#check()
#clear()
#cre()
check()
print(i)

#db["old_time"] = 50