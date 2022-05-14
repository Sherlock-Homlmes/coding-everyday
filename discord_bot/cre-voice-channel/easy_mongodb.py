from threading import Thread
import os
from dotenv import load_dotenv
import time
######database
#
from pymongo import MongoClient

from threading import Thread
from waiting import wait

from functools import reduce

## thuộc tính: database_url
load_dotenv()
database_url = os.getenv('database_url', "value does not exist")
cluster = MongoClient(database_url)
dtbs = cluster["discord_betterme"]
#dtb = dtbs["create_vc"]
dtb = dtbs["test_data"]
#start
#########################################advance#####################################
data_key = "cre_vc"
#cre_data
def cre_data(name,value):
	default_data ={
	"name":name,
	"value":value
	}
	dtb.insert_one(default_data)

#cre_data("cre_vc",{})

#take_data
def take_data(name):
    tests = dtb.find( { "name":name } )
    for test in tests:
        return test["value"]

def stable_val(val):
	return val

db = take_data(data_key)
stable_db = take_data(data_key)    
########def
def open_again(name):
    global db,stable_db
    dtb.update_one({ "name": name },  {'$set': {'value':db}} )
    stable_db = take_data(data_key)

def run1():
	global db,stable_db
	while True:
		#print("repeat\n")
		wait(lambda: db != stable_db, timeout_seconds=None)
		#print("change\n")
		#start
		#start_time = time.time()
		open_again(data_key)
		#end_time = time.time()
		#print('Total all time elapsed: %.6f seconds' % (end_time - start_time))
    

def run2():
	while True:
		tong = 0
		for i in range(10000000):
			tong += i
		print(tong)
		time.sleep(600)

t1 = Thread(target=run1)
t1.start()
t2 = Thread(target=run2)
t2.start()

print("start")
time.sleep(15)
print(db["20"])



