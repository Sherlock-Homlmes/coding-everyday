from pymongo import MongoClient
from dotenv import load_dotenv
import os
import time

## thuộc tính: account, password, key1, key2
load_dotenv()
database_url = os.getenv('database_url', "value does not exist")
cluster = MongoClient(database_url)
dtbs = cluster["discord_betterme"]
dtb = dtbs["betterme_study_time"]
data_key = "learn_time_count"
def take_data(name):
    tests = dtb.find( { "name":name } )
    for test in tests:
        return test["value"]

db = take_data(data_key)

def convert():
	global db
	db["server_study_time"]["date"] = [2022,2,14,17]
	for key in db.keys():
		#Step 1: date
		if key != "server_study_time":
			db[key]["date"] = [db[key]["y"],db[key]["mon"],db[key]["d"],db[key]["h"],db[key]["min"]]

			del db[key]["y"]
			del db[key]["mon"]
			del db[key]["d"]
			del db[key]["h"]
			del db[key]["min"]

		#Step 2: time per day
		#db[key]["time_per_day"] = [ db[key]["time_per_day"]["m_1"],db[key]["time_per_day"]["m_2"],db[key]["time_per_day"]["m_3"],db[key]["time_per_day"]["m_4"],db[key]["time_per_day"]["m_5"],db[key]["time_per_day"]["m_6"],db[key]["time_per_day"]["m_7"],db[key]["time_per_day"]["m_8"],db[key]["time_per_day"]["m_9"],db[key]["time_per_day"]["m_10"],db[key]["time_per_day"]["m_11"],db[key]["time_per_day"]["m_12"],db[key]["time_per_day"]["m_13"],db[key]["time_per_day"]["m_14"],db[key]["time_per_day"]["m_15"],db[key]["time_per_day"]["m_16"],db[key]["time_per_day"]["m_17"],db[key]["time_per_day"]["m_18"],db[key]["time_per_day"]["m_19"],db[key]["time_per_day"]["m_20"],db[key]["time_per_day"]["m_21"],db[key]["time_per_day"]["m_22"],db[key]["time_per_day"]["m_23"],db[key]["time_per_day"]["m_24"],db[key]["time_per_day"]["m_25"],db[key]["time_per_day"]["m_26"],db[key]["time_per_day"]["m_27"],db[key]["time_per_day"]["m_28"],db[key]["time_per_day"]["m_29"],db[key]["time_per_day"]["m_30"] ]
		db[key]["time_per_day"] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

		#Step 3:m_all_time
		if key != "server_study_time":
			db[key]["m_all_time"] += db[key]["h_all_time"]*60

			try:
				del db[key]["h_all_time"]
				del db[key]["h_all_time_transfer"]
			except:
				print(key)
		else:
			db[key]["m_all_time"] += db[key]["h_all_time"]*60
			del db[key]["h_all_time"]


print("start")
start_time = time.time()
convert()
dtb.update_one({ "name": data_key },  {'$set': {'value':db}} )
end_time = time.time()
print('Total all time elapsed: %.6f seconds' % (end_time - start_time))
print("\nconvert done")