from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork
from src.services.exceptions import (
    CategoryNotFound,
    SupplierNotFound,
    PaymentMethodNotFound,
    ProductNotFound,
)
from src.domain.product.model import Product
from src.domain.product_discount.model import ProductDiscount
from src.services.product.product_dto import ProductDTO


def create_product(product_dto: ProductDTO, uow: SqlAlchemyUnitOfWork):
    with uow:
        category = uow.category_repository.get(id=product_dto.category_id)
        if not category:
            raise CategoryNotFound("Categoria não encontrada")

        supplier = uow.supplier_repository.get(id=product_dto.supplier_id)
        if not supplier:
            raise SupplierNotFound("Fornecedor não encontrado")

        product = Product(
            description=product_dto.description,
            price=product_dto.price,
            technical_details=product_dto.technical_details,
            image=product_dto.image,
            visible=product_dto.visible,
            category=category,
            supplier=supplier,
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
