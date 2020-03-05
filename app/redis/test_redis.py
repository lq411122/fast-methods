from utils.redis import redis

redis.set("name", "i")

data = redis.get("name")
print(data)