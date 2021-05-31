"""empty message

Revision ID: 60c728001757
Revises: eb460c82c57e
Create Date: 2021-05-31 16:30:20.537062

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60c728001757'
down_revision = 'eb460c82c57e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('about_heading',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('about_subheading', sa.String(length=255), nullable=True),
    sa.Column('about_heading', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('about_heading')
    # ### end Alembic commands ###
