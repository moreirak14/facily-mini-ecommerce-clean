from src.adapter.repositories.payment_method_repository import PaymentMethodRepository
from src.adapter.repositories.product_repository import ProductRepository
from src.adapter.repositories.coupon_repository import CouponRepository
from src.domain.product.model import Product
from src.domain.category.model import Category
from src.domain.supplier.model import Supplier
from src.domain.coupon.model import Coupon
from src.domain.payment_method.model import PaymentMethod
from src.adapter.database import Session
from src.adapter.orm import start_mapper


start_mapper()

db = Session()

repository = PaymentMethodRepository(db)

# product = Product(description='descricao 1', price=10, technical_details='detalhes tecnicos', image='', visible=True)
# category = Category(name='Eletronico')
# supplier = Supplier(name='LG')
# coupon = Coupon(code='A1B2C3D4E5', expire_at=None, limit=10, type='percentage', value=10)

payment_method = PaymentMethod(name='credit card', enabled=True)

repository.add(payment_method)
repository.get()

print(payment_method.id)
print(payment_method.name)
