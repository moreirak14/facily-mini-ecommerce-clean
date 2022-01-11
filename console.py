from sqlalchemy.orm.base import NON_PERSISTENT_OK
from src.adapter.repositories.product_repository import ProductRepository
from src.adapter.repositories.coupon_repository import CouponRepository
from src.domain.product.model import Product
from src.domain.category.model import Category
from src.domain.supplier.model import Supplier
from src.domain.coupon.model import Coupon
from src.adapter.database import Session
from src.adapter.orm import start_mapper


start_mapper()

db = Session()

repository = CouponRepository(db)

# product = Product(description='descricao 1', price=10, technical_details='detalhes tecnicos', image='', visible=True)
# category = Category(name='Eletronico')
# supplier = Supplier(name='LG')

coupon = Coupon(code='A1B2C3D4E5', expire_at=None, limit=10, type='percentage', value=10)

repository.add(coupon)
repository.get()

print(coupon.id)
print(coupon.code)
