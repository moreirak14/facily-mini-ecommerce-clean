from fastapi import APIRouter
from src.presentation.fastapi.routers.product_router import router as product_router

router = APIRouter()

router.include_router(product_router, prefix="/products", tags=["product"])