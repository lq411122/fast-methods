import os

from databases import DatabaseURL
from dotenv import load_dotenv
from pymongo import MongoClient

API_V1_STR = "/api/docs"
per_page = 10  # 分页/每页数据条数


load_dotenv(".env")
MONGODB_URL = os.getenv("MONGODB_URL", "")  # deploying without docker-compose

if not MONGODB_URL:
    MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
    MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
    MONGO_USER = os.getenv("MONGO_USER", "admin")
    MONGO_PASS = os.getenv("MONGO_PASSWORD", "root")
    MONGO_DB = os.getenv("MONGO_DB", "test")

    MONGODB_URL = DatabaseURL(
        # f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"
        f"mongodb://{MONGO_HOST}:{MONGO_PORT}"
    )
else:
    MONGODB_URL = DatabaseURL(MONGODB_URL)

MONGODB_URL = "mongodb://localhost/27017"
db_client = MongoClient(MONGODB_URL)