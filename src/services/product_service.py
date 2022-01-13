from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork
from src.services.exceptions import (
    CategoryNotFound,
    SupplierNotFound,
    PaymentMethodNotFound,
    ProductNotFound,
)
from src.domain.product.model import Product
from src.domain.product_discount.model import ProductDiscount


def create_product(
    description: str,
    price: float,
    technical_details: str,
    image: str,
    visible: bool,
    category_id: int,
    supplier_id: int,
    uow: SqlAlchemyUnitOfWork,
):
    with uow:
        category = uow.category_repository.get(id=category_id)
        if not category:
            raise CategoryNotFound("Categoria não encontrada")

        supplier = uow.supplier_repository.get(id=supplier_id)
        if not supplier:
            raise SupplierNotFound("Fornecedor não encontrado")

        product = Product(
            description=description,
            price=price,
            technical_details=technical_details,
            image=image,
            visible=visible,
            category=category,
            supplier=category,
        )

        uow.product_repository.add(product)
        uow.commit()


def create_discount(
    mode: str,
    value: float,
    payment_method_id: int,
    product_id: int,
    uow: SqlAlchemyUnitOfWork,
):
    with uow:
        payment_method = uow.payment_method_repository.get(id=payment_method_id)
        if not payment_method:
            raise PaymentMethodNotFound("Metodo de pagamento não encontrado")

        product = uow.product_repository.get(id=product_id)
        if not product:
            raise ProductNotFound("Produto não encontrado")

        discount = ProductDiscount(
            mode=mode, value=value, payment_method=payment_method
        )
        product.add_discount(discount)

        uow.commit()
