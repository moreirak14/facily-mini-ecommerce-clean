from src.domain.payment_method.model import PaymentMethod
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork


def create_payment_method(name: str, enabled: bool, uow: SqlAlchemyUnitOfWork):
    with uow:
        uow.category_repository.add(PaymentMethod(name=name, enabled=enabled))
        uow.commit()
