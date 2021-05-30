"""empty message

Revision ID: 728db68f9467
Revises: 98b2a504d40b
Create Date: 2021-05-30 14:56:26.695952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '728db68f9467'
down_revision = '98b2a504d40b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer_heading', sa.Column('customer_desc', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('customer_heading', 'customer_desc')
    # ### end Alembic commands ###
