"""users.id should be a SERIAL

Revision ID: 025ad5d0b733
Revises: 60145067f31c
Create Date: 2022-05-30 12:10:06.460711

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '025ad5d0b733'
down_revision = '60145067f31c'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('CREATE SEQUENCE users_id RESTART WITH 100')
    op.execute("ALTER TABLE users ALTER COLUMN id SET DEFAULT nextval('users_id')")


def downgrade():
    op.execute('ALTER TABLE users ALTER COLUMN id DROP DEFAULT')
    op.execute('DROP SEQUENCE users_id')
