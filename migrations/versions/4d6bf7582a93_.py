"""empty message

Revision ID: 4d6bf7582a93
Revises: a505f4be6ef6
Create Date: 2020-12-25 03:14:15.916644

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d6bf7582a93'
down_revision = 'a505f4be6ef6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuario', sa.Column('hora_registro', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuario', 'hora_registro')
    # ### end Alembic commands ###