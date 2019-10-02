"""fixed timestamp

Revision ID: c02c73a3066b
Revises: 
Create Date: 2019-10-02 13:25:20.767910

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c02c73a3066b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('temperature',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(length=128), nullable=True),
    sa.Column('tmp', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('temperature')
    # ### end Alembic commands ###