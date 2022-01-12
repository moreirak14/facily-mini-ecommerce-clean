"""Added table payment method

Revision ID: 228840dc557d
Revises: 8dbe5d32e361
Create Date: 2022-01-11 13:52:56.456678

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "228840dc557d"
down_revision = "8dbe5d32e361"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "payment_method",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=45), nullable=True),
        sa.Column("enabled", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("payment_method")
    # ### end Alembic commands ###
