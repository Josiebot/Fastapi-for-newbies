"""add last few columns to posts table

Revision ID: e55a9350f64e
Revises: 90d054ea9df4
Create Date: 2026-07-04 12:27:28.781035

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e55a9350f64e'
down_revision: Union[str, Sequence[str], None] = '90d054ea9df4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),
                  )
    
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=True, server_default=sa.text('NOW()')),
                  )


    
    pass


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_column('posts', 'publish')
    op.drop_column('posts', 'created_at')
    pass
