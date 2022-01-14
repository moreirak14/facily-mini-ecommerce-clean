from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork
from src.adapter.database import Session
from src.adapter.orm import start_mapper
from src.services.category.category_service import create_category
from src.services.supplier_service import create_supplier

start_mapper()

db = Session()
uow = SqlAlchemyUnitOfWork(db)

# category = create_category(name="Eletronicos", uow=uow)
# supplier = create_supplier(name="LG", uow=uow)

# product = create_product(
#     description="TV",
#     price=10,
#     technical_details="fonte desligando",
#     image="",
#     visible=True,
#     category_id=1,
#     supplier_id=1,
#     uow=uow)

# payment_method = create_payment_method(name="Visa Card", enabled=True, uow=uow)

# product_discount = create_discount(
#     mode="percentage",
#     value=25,
#     payment_method_id=1,
#     product_id=1,
#     uow=uow)

# customer = create_customer(
#     first_name="kaique",
#     last_name="moreira",
#     phone_number="11912345678",
#     genre="M",
#     document_id="45579312345",
#     birth_date=None,
#     uow=uow,
# )

# address = create_address(
#     address="Rua sei lá",
#     city="Aruja",
#     state="SP",
#     number="140",
#     zipcode="074000",
#     neighbourhood="139",
#     primary=True,
#     customer_id=1,
#     uow=uow
# )


## SEM UNIT OF WORK
# customer_repository = CustomerRepository(db)

# customer = Customer(
#     first_name="kaique",
#     last_name="moreira",
#     phone_number="11912345678",
#     genre="M",
#     document_id="45579312345",
#     birth_date=None,
# )
# customer.add_address(
#     Address(
#         address="Rua tal",
#         city="Aruja",
#         state="SP",
#         number="139",
#         zipcode="074000",
#         neighbourhood="137",
#         primary=True,
#     )
# )
# customer.add_address(
#     Address(
#         address="Rua sei la",
#         city="Aruja",
#         state="SP",
#         number="139",
#         zipcode="074000",
#         neighbourhood="137",
#         primary=True,
#     )
# )
# for i in customer.address:
#     print(i.address)
#     print(i.primary)
# customer_repository.add(customer)
