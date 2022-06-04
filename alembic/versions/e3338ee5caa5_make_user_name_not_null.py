"""make user.name not null

Revision ID: e3338ee5caa5
Revises: 31ca6d216cdc
Create Date: 2022-05-30 11:34:47.489261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3338ee5caa5'
down_revision = '31ca6d216cdc'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('users', 'name', nullable=False)


def downgrade():
    op.alter_column('users', 'name', nullable=True)
