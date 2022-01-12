"""Added the table payment discount

Revision ID: 3b97974f7db6
Revises: 
Create Date: 2022-01-11 22:22:42.258392

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3b97974f7db6"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "category",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=45), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "coupon",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("code", sa.String(length=10), nullable=True),
        sa.Column("expire_at", sa.DateTime(), nullable=True),
        sa.Column("limit", sa.Integer(), nullable=True),
        sa.Column("type", sa.String(length=15), nullable=True),
        sa.Column("value", sa.Float(precision=10, asdecimal=2), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("code"),
    )
    op.create_table(
        "payment_method",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=45), nullable=True),
        sa.Column("enabled", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "supplier",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=45), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "product",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("description", sa.String(length=100), nullable=True),
        sa.Column("technical_details", sa.String(length=255), nullable=True),
        sa.Column("price", sa.Float(precision=10, asdecimal=2), nullable=True),
        sa.Column("visible", sa.Boolean(), nullable=True),
        sa.Column("category_id", sa.Integer(), nullable=True),
        sa.Column("supplier_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["category_id"],
            ["category.id"],
        ),
        sa.ForeignKeyConstraint(
            ["supplier_id"],
            ["supplier.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "payment_discount",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("mode", sa.String(length=45), nullable=True),
        sa.Column("value", sa.Float(precision=10, asdecimal=2), nullable=True),
        sa.Column("product_id", sa.Integer(), nullable=True),
        sa.Column("payment_method_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["payment_method_id"],
            ["payment_method.id"],
        ),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["product.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("payment_discount")
    op.drop_table("product")
    op.drop_table("supplier")
    op.drop_table("payment_method")
    op.drop_table("coupon")
    op.drop_table("category")
    # ### end Alembic commands ###
