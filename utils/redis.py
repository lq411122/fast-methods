"""
REDIS数据库
"""
import redis
from .redis_pool import POOL

conn = redis.Redis(connection_pool=POOL)

