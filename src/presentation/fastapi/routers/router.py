from fastapi import APIRouter
from src.presentation.fastapi.routers.product_router import router as product_router
from src.presentation.fastapi.routers.category_router import router as category_router
from src.presentation.fastapi.routers.supplier_router import router as supplier_router
from src.presentation.fastapi.routers.payment_method_router import (
    router as payment_method_router,
)
from src.presentation.fastapi.routers.customer_router import router as customer_router


router = APIRouter()
router.include_router(product_router, prefix="/products", tags=["product"])
router.include_router(category_router, prefix="/categories", tags=["category"])
router.include_router(supplier_router, prefix="/suppliers", tags=["supplier"])
router.include_router(
    payment_method_router, prefix="/payment_methods", tags=["payment_method"]
)
router.include_router(customer_router, prefix="/customers", tags=["customer"])
