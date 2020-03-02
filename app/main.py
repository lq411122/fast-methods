from fastapi import FastAPI
from config.testing import API_V1_STR
from .api.api import router as api_router


def create_app():
    app = FastAPI()
    app.include_router(api_router, prefix=API_V1_STR)

    return app





