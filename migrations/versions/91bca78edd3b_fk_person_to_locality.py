"""fk_person_to_locality

Revision ID: 91bca78edd3b
Revises: 72c6b6d928e3
Create Date: 2023-06-13 20:19:59.155262

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91bca78edd3b'
down_revision = '72c6b6d928e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.add_column(sa.Column('locality', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'locality', ['locality'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('locality')

    # ### end Alembic commands ###
