from src.adapter.repositories.product_repository import ProductRepository
from src.domain.product.model import Product
from src.domain.category.model import Category
from src.domain.supplier.model import Supplier
from src.adapter.database import Session
from src.adapter.orm import start_mapper


start_mapper()

db = Session()

repository = ProductRepository(db)

supplier = Supplier(name="LG")
category = Category(name="Eletronico")

product = Product(
    description="TV",
    price=980,
    technical_details="fonte desligando sozinha",
    image="",
    visible=True,
    category=category,
    supplier=supplier,
)

repository.add(product)

print(product.id)
print(product.description)
