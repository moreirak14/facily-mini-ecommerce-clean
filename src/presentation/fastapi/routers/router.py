from fastapi import APIRouter
from src.presentation.fastapi.routers.product_router import router as product_router
from src.presentation.fastapi.routers.category_router import router as category_router


router = APIRouter()
router.include_router(product_router, prefix="/products", tags=["product"])
router.include_router(category_router, prefix="/categories", tags=["category"])
