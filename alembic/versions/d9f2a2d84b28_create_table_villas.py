"""create table villas

Revision ID: d9f2a2d84b28
Revises: 025ad5d0b733
Create Date: 2022-05-30 12:30:55.076638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9f2a2d84b28'
down_revision = '025ad5d0b733'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('CREATE TABLE villas(id SERIAL PRIMARY KEY, name TEXT)')


def downgrade():
    op.execute('DROP TABLE villas')
