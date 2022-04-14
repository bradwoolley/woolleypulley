"""add content column to posts table

Revision ID: 0ba25d2820e7
Revises: 3f7262e0b7fe
Create Date: 2022-04-14 11:40:57.534178

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ba25d2820e7'
down_revision = '3f7262e0b7fe'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column('posts', 'content')
    pass
