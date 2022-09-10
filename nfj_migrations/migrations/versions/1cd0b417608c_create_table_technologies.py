"""create table technologies

Revision ID: 1cd0b417608c
Revises: 665541869e31
Create Date: 2022-07-02 13:24:17.497368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1cd0b417608c'
down_revision = '665541869e31'
branch_labels = None
depends_on = None

def upgrade():
        op.execute("""create table technologies
(
    technology_id serial primary key,
    name          text not null,
    unique (name)
)""")

def downgrade():
        op.execute("""drop table technologies
    """)