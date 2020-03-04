"""
MONGODB数据库
"""
from pymongo import MongoClient
from config.testing import MONGODB_URL

db_client = MongoClient(MONGODB_URL)
db = db_client["test"]
collection = db["shop_list"]