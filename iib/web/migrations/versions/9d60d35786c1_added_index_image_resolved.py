"""Added index_image_resolved.

Revision ID: 9d60d35786c1
Revises: 7573241a5156
Create Date: 2021-02-11 15:48:27.192389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d60d35786c1'
down_revision = '7573241a5156'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('request_add', schema=None) as batch_op:
        batch_op.add_column(sa.Column('index_resolved_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            "index_resolved_id_fkey", 'image', ['index_resolved_id'], ['id']
        )

    with op.batch_alter_table('request_rm', schema=None) as batch_op:
        batch_op.add_column(sa.Column('index_resolved_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            "index_resolved_id_fkey", 'image', ['index_resolved_id'], ['id']
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('request_rm', schema=None) as batch_op:
        batch_op.drop_constraint("index_resolved_id_fkey", type_='foreignkey')
        batch_op.drop_column('index_resolved_id')

    with op.batch_alter_table('request_add', schema=None) as batch_op:
        batch_op.drop_constraint("index_resolved_id_fkey", type_='foreignkey')
        batch_op.drop_column('index_resolved_id')

    # ### end Alembic commands ###