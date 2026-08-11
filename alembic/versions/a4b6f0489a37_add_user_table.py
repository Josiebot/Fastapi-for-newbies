"""add user table

Revision ID: a4b6f0489a37
Revises: 84637b80d4b2
Create Date: 2026-07-04 11:20:18.279857

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a4b6f0489a37'
down_revision: Union[str, Sequence[str], None] = '84637b80d4b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('user',
                   sa.Column('id', sa.Integer(), nullable = False),
                   sa.Column('email', sa.String(), nullable = False),
                    sa.Column('password', sa.String(), nullable = False),
                     sa.Column('created_at', sa.TIMESTAMP(timezone = True), server_default=sa.text('now()'), nullable = False),
                     sa.PrimaryKeyConstraint('id'),
                     sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('user')
    pass
