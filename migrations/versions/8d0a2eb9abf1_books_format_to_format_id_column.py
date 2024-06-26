"""Books -> format to format_id column

Revision ID: 8d0a2eb9abf1
Revises: 83ccd899489d
Create Date: 2024-03-27 21:08:03.823857

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d0a2eb9abf1'
down_revision = '83ccd899489d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.add_column(sa.Column('format_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('books_format_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'books_format', ['format_id'], ['id'], ondelete='CASCADE')
        batch_op.drop_column('format')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.add_column(sa.Column('format', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('books_format_fkey', 'books_format', ['format'], ['id'], ondelete='CASCADE')
        batch_op.drop_column('format_id')

    # ### end Alembic commands ###
