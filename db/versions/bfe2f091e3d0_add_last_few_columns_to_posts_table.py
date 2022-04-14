"""add last few columns to posts table

Revision ID: bfe2f091e3d0
Revises: 44b4fbc9bd73
Create Date: 2022-04-14 12:31:24.369527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfe2f091e3d0'
down_revision = '44b4fbc9bd73'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass