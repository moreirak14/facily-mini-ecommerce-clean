"""Added the tables address and customer

Revision ID: 624b8a73f166
Revises: de029f3465a8
Create Date: 2022-01-12 11:52:07.837150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "624b8a73f166"
down_revision = "de029f3465a8"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "customers",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("first_name", sa.String(length=45), nullable=True),
        sa.Column("last_name", sa.String(length=45), nullable=True),
        sa.Column("phone_number", sa.String(length=15), nullable=True),
        sa.Column("genre", sa.String(length=45), nullable=True),
        sa.Column("document_id", sa.String(length=45), nullable=True),
        sa.Column("birth_date", sa.Date(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("document_id"),
    )
    op.create_table(
        "addresses",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("address", sa.String(length=255), nullable=True),
        sa.Column("city", sa.String(length=45), nullable=True),
        sa.Column("state", sa.String(length=2), nullable=True),
        sa.Column("number", sa.String(length=10), nullable=True),
        sa.Column("zipcode", sa.String(length=6), nullable=True),
        sa.Column("neighbourhood", sa.String(length=45), nullable=True),
        sa.Column("primary", sa.Boolean(), nullable=True),
        sa.Column("customer_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["customer_id"],
            ["customers.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("addresses")
    op.drop_table("customers")
    # ### end Alembic commands ###
