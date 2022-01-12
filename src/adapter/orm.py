from sqlalchemy import Table
from sqlalchemy.orm import mapper, relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Float, Integer, String
from src.adapter.database import Base
from src.domain.product.model import Product
from src.domain.category.model import Category
from src.domain.supplier.model import Supplier
from src.domain.coupon.model import Coupon
from src.domain.payment_method.model import PaymentMethod
from src.domain.payment_discount.model import PaymentDiscount


metadata = Base.metadata


table_category = Table(
    "category",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(45)),
)

table_supplier = Table(
    "supplier",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(45)),
)

table_product = Table(
    "product",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("description", String(100)),
    Column("technical_details", String(255)),
    Column("price", Float(10, 2)),
    Column("visible", Boolean),
    Column("category_id", ForeignKey("category.id")),
    Column("supplier_id", ForeignKey("supplier.id")),
)


table_coupon = Table(
    "coupon",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("code", String(10), unique=True),
    Column("expire_at", DateTime),
    Column("limit", Integer),
    Column("type", String(15)),
    Column("value", Float(10, 2)),
)

table_payment_method = Table(
    "payment_method",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(45)),
    Column("enabled", Boolean, default=True),
)


table_payment_discount = Table(
    "payment_discount",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("mode", String(45)),
    Column("value", Float(10, 2)),
    Column("product_id", ForeignKey("product.id")),
    Column("payment_method_id", ForeignKey("payment_method.id")),
)


def start_mapper():
    category_mapper = mapper(Category, table_category)
    supplier_mapper = mapper(Supplier, table_supplier)

    mapper(
        Product,
        table_product,
        properties={
            "category": relationship(category_mapper),
            "supplier": relationship(supplier_mapper),
        },
    )

    payment_method_mapper = mapper(PaymentMethod, table_payment_method)

    mapper(
        PaymentDiscount,
        table_payment_discount,
        properties={
            "product": relationship(Product),
            "payment_method": relationship(payment_method_mapper),
        },
    )

    mapper(Coupon, table_coupon)
