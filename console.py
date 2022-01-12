from src.domain.address.model import Address
from src.domain.customer.model import Customer
from src.adapter.repositories.customer_repository import CustomerRepository
from src.adapter.repositories.address_repository import AddressRepository
from src.adapter.database import Session
from src.adapter.orm import start_mapper


start_mapper()

db = Session()

customer_repository = CustomerRepository(db)
address_repository = AddressRepository(db)

customer = Customer(
    first_name="kaique",
    last_name="moreira",
    phone_number="11912345678",
    genre="M",
    document_id="45579312345",
    birth_date=None,
)
customer.add_address(Address(
    address="Rua tal",
    city="Aruja",
    state="SP",
    number="139",
    zipcode="074000",
    neighbourhood="137",
    primary=True,
))
customer.add_address(Address(
    address="Rua sei la",
    city="Aruja",
    state="SP",
    number="139",
    zipcode="074000",
    neighbourhood="137",
    primary=True,
))
for i in customer.address:
    print(i.address)
    print(i.primary)
customer_repository.add(customer)

# address_repository = AddressRepository(db)
# address = Address(
    # address="Rua tal 1",
    # city="Aruja 1",
    # state="SP 1",
    # number="140",
    # zipcode="074000",
    # neighbourhood="137",
    # primary=False,

# address_repository.add(address)

# repository = ProductRepository(db)

# supplier = Supplier(name="LG")
# category = Category(name="Eletronico")

# product = Product(
#     description="TV",
#     price=980,
#     technical_details="fonte desligando sozinha",
#     image="",
#     visible=True,
#     category=category,
#     supplier=supplier,
# )

# payment_method = PaymentMethod(name="debito", enabled=True)

# payment_discount = PaymentDiscount(
#     mode="dinheiro",
#     value=25,
#     product=product,
#     payment_method=payment_method,
# )

# repository.add(payment_discount)

# print(payment_discount.id)
# print(payment_discount.mode)
