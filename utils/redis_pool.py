"""
REDIS连接池
"""
from redis import ConnectionPool

POOL = ConnectionPool(
    host="127.0.0.1",
    port = 6379,
    max_connections=100
)