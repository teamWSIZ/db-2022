"""users p-key should use id only

Revision ID: 60145067f31c
Revises: 398062fa4068
Create Date: 2022-05-30 12:03:48.701565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60145067f31c'
down_revision = '398062fa4068'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('ALTER TABLE users DROP CONSTRAINT users_pkey')
    op.create_primary_key('users_pkey', 'users', ['id'])


def downgrade():
    op.execute('ALTER TABLE users DROP CONSTRAINT users_pkey')
    op.create_primary_key('users_pkey', 'users', ['id', 'name'])
