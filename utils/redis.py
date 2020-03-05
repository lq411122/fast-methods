import redis


REDIS_CACHE = {
    "host": '192.168.196.129',
    "port": '6379',
    "db": 0,
    "password": ''
}


class RedisClient(redis.StrictRedis):
    """
    Singleton pattern
    """
    _instance = {}

    def __init__(self, server):
        redis.StrictRedis.__init__(self, **server)

    def __new__(cls, *args):
        if str(args) not in cls._instance:
            cls._instance[str(args)] = super(RedisClient, cls).__new__(cls)
        return cls._instance[str(args)]


redis = RedisClient(REDIS_CACHE)


