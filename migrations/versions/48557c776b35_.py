"""empty message

Revision ID: 48557c776b35
Revises: 52c402feead9
Create Date: 2021-01-23 11:26:17.244440

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48557c776b35'
down_revision = '52c402feead9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('scale',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('scale')
    # ### end Alembic commands ###
