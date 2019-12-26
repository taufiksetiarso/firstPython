import redis

r = redis.Redis(
    host="localhost",
    port=6379  , 
    password="")


value = r.get('foo')
r.delete('foo')
print(value)

