"""change user model

Revision ID: 79f700208d0e
Revises: 127d63aacf72
Create Date: 2024-11-14 08:06:45.123642

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '79f700208d0e'
down_revision: Union[str, None] = '127d63aacf72'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('create schema test')
    op.create_table('user_account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('fullname', sa.String(), nullable=True),
    sa.Column('surname', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__user_account')),
    schema='test'
    )
    op.drop_table('user_account')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_account',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=30), autoincrement=False, nullable=False),
    sa.Column('fullname', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('surname', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk__user_account')
    )
    op.drop_table('user_account', schema='test')
    op.execute('drop schema test')
    # ### end Alembic commands ###
