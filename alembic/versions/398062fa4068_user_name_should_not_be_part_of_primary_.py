"""user.name should not be part of primary key

Revision ID: 398062fa4068
Revises: e3338ee5caa5
Create Date: 2022-05-30 11:38:48.104195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '398062fa4068'
down_revision = 'e3338ee5caa5'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('users', 'name', primary_key=False)


def downgrade():
    op.alter_column('users', 'name', primary_key=True)
