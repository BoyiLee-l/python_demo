"""create an address table

Revision ID: 2afa38a961ec
Revises: 
Create Date: 2024-02-27 17:35:09.640143

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2afa38a961ec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("address",
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("address", sa.String(50), nullable=False),
    sa.Column("city", sa.String(50), nullable=False),
    sa.Column("state", sa.String(50), nullable=False))


def downgrade():
    op.drop_table("address")
