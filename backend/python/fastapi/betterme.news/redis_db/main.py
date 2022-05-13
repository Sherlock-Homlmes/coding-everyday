import redis

r = redis.Redis(
	host='192.168.1.2', 
	port=8080, 
	db=0)

r.set('foo', 'bar')
r.get('foo')