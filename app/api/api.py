from fastapi import APIRouter
from .endpoints.market import router as market_router
from .endpoints.methods import router as methods_router


router = APIRouter()
router.include_router(market_router, prefix="/market")
router.include_router(methods_router, prefix="/methods")

