"""feat: add some data

Revision ID: a45292a5f34c
Revises: d9f2a2d84b28
Create Date: 2022-05-30 12:44:03.741170

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
from sqlalchemy import MetaData, Table

revision = 'a45292a5f34c'
down_revision = 'd9f2a2d84b28'
branch_labels = None
depends_on = None


def upgrade():
    villa_names = ['Montevideo', 'Santiago', 'Buenos Aires']
    for v in villa_names:
        op.execute(f"INSERT INTO villas(name) values ('{v}')")


def downgrade():
    villa_names = ['Montevideo', 'Santiago', 'Buenos Aires']
    for n in villa_names:
        op.execute(f"DELETE FROM villas WHERE name = '{n}'")
