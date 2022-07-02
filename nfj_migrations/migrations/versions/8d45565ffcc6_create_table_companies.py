"""create table companies

Revision ID: 8d45565ffcc6
Revises: 
Create Date: 2022-07-02 12:59:31.145225

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d45565ffcc6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
    create table companies
(
    company_id SERIAL primary key,
    name       text not null,
    url        text not null,
    UNIQUE (name, url)
);
    """)


def downgrade():
    op.execute("""
    drop table companies;
    """)