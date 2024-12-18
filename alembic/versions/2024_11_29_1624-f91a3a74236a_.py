"""empty message

Revision ID: f91a3a74236a
Revises: b11b99b0f9ef
Create Date: 2024-11-29 16:24:16.197360

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f91a3a74236a'
down_revision: Union[str, None] = 'b11b99b0f9ef'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('parts', schema='test')
    op.create_table('parts',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('article', sa.String(), nullable=True),
    sa.Column('article_unit', sa.String(), nullable=True),
    sa.Column('serial_number_machine', sa.String(), nullable=True),
    sa.Column('alternative_article', sa.String(), nullable=True),
    sa.Column('name_eng', sa.String(), nullable=True),
    sa.Column('name_ru', sa.String(), nullable=True),
    sa.Column('material', sa.String(), nullable=True),
    sa.Column('weight_kg', sa.Float(), nullable=True),
    sa.Column('size', sa.Float(), nullable=True),
    sa.Column('part_type', sa.String(), nullable=True),
    sa.Column('description_custom', sa.String(), nullable=True),
    sa.Column('manufacturer', sa.String(), nullable=True),
    sa.Column('trade_mark', sa.String(), nullable=True),
    sa.Column('qty_in_unit', sa.Integer(), nullable=True),
    sa.Column('country_eng', sa.String(), nullable=True),
    sa.Column('s_code', sa.String(), nullable=True),
    sa.Column('path_catalog', sa.String(), nullable=True),
    sa.Column('path_documentation', sa.String(), nullable=True),
    sa.Column('path_photo', sa.String(), nullable=True),
    sa.Column('path_avatar', sa.String(), nullable=True),
    sa.Column('hashtags', sa.String(), nullable=True),
    sa.Column('createAt', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('comment', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__parts')),
    schema='test'
    )
    op.create_table('user_account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('fullname', sa.String(), nullable=True),
    sa.Column('surname', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__user_account')),
    schema='test',
    if_not_exists=True
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_account', schema='test')
    op.drop_table('parts', schema='test')
    op.create_table('parts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('article', sa.String(), nullable=True),
    sa.Column('article_unit', sa.String(), nullable=True),
    sa.Column('serial_number_machine', sa.String(), nullable=True),
    sa.Column('alternative_article', sa.String(), nullable=True),
    sa.Column('name_eng', sa.String(), nullable=True),
    sa.Column('name_ru', sa.String(), nullable=True),
    sa.Column('material', sa.String(), nullable=True),
    sa.Column('weight_kg', sa.Float(), nullable=True),
    sa.Column('size', sa.Float(), nullable=True),
    sa.Column('part_type', sa.String(), nullable=True),
    sa.Column('description_custom', sa.String(), nullable=True),
    sa.Column('manufacturer', sa.String(), nullable=True),
    sa.Column('trade_mark', sa.String(), nullable=True),
    sa.Column('qty_in_unit', sa.Integer(), nullable=True),
    sa.Column('country_eng', sa.String(), nullable=True),
    sa.Column('s_code', sa.String(), nullable=True),
    sa.Column('path_catalog', sa.String(), nullable=True),
    sa.Column('path_documentation', sa.String(), nullable=True),
    sa.Column('path_photo', sa.String(), nullable=True),
    sa.Column('path_avatar', sa.String(), nullable=True),
    sa.Column('hashtags', sa.String(), nullable=True),
    sa.Column('createAt', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('comment', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__parts')),
    schema='test'
    )
    # ### end Alembic commands ###
