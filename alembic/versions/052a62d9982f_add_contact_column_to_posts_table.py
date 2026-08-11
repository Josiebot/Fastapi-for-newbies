"""add contact column to posts table

Revision ID: 052a62d9982f
Revises: 12c5eed76d9e
Create Date: 2026-07-06 11:13:31.890857

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '052a62d9982f'
down_revision: Union[str, Sequence[str], None] = '12c5eed76d9e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key = True),  sa.Column('title', sa.Integer(), nullable=False, primary_key = True))
    pass



def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
