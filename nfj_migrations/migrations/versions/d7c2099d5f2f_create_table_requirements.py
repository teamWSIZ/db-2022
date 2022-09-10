"""create table requirements

Revision ID: d7c2099d5f2f
Revises: 1cd0b417608c
Create Date: 2022-07-02 13:24:58.294333

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'd7c2099d5f2f'
down_revision = '1cd0b417608c'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""create table requirements
(
    posting_id    int references postings (posting_id),
    technology_id int references technologies (technology_id),
    must          boolean not null,
    unique (posting_id, technology_id)
)""")


def downgrade():
    op.execute("""drop table requirements
    """)
