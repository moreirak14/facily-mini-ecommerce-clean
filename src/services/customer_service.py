from datetime import date
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork
from src.domain.customer.model import Customer
from src.domain.address.model import Address
from src.services.exceptions import CustomerNotFound


def create_customer(
    first_name: str,
    last_name: str,
    phone_number: str,
    genre: str,
    document_id: str,
    birth_date: date,
    uow: SqlAlchemyUnitOfWork,
):
    with uow:
        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            genre=genre,
            document_id=document_id,
            birth_date=birth_date,
        )
        uow.category_repository.add(customer)
        uow.commit()


def create_address(
    address: str,
    city: str,
    state: str,
    number: str,
    zipcode: str,
    neighbourhood: str,
    primary: bool,
    customer_id: int,
    uow: SqlAlchemyUnitOfWork,
):
    with uow:
        customer = uow.customer_repository.get(id=customer_id)
        if not customer:
            raise CustomerNotFound("Produto não encontrado")

        addresses = Address(
            address=address,
            city=city,
            state=state,
            number=number,
            zipcode=zipcode,
            neighbourhood=neighbourhood,
            primary=primary,
        )
        customer.add_address(addresses)
        uow.commit()
