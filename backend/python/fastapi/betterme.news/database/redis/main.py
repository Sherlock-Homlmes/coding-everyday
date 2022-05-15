import redis
import asyncio

### command for linux :
# sudo service redis-server {start|stop|restart|force-reload|status}

r = redis.Redis(
	host='localhost', 
	port=6379, 
	db=0)

def redis_add(key,value):
	value = r.hmset(key,value)

def redis_find(key):
	value = r.hgetall(key)
	print(value)

	if value == None:
		#do something
		pass

	return value

### build project
	# check position of news_post
				#
				# excist: take from redis
				#
				# not excist: take from database

### improve
	# build dict in redis function