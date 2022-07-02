"""create table paytypes

Revision ID: 6e1b64d8d912
Revises: 8d45565ffcc6
Create Date: 2022-07-02 13:03:07.269173

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '6e1b64d8d912'
down_revision = '8d45565ffcc6'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
    create table pay_types
(
    pay_type_id serial primary key,
    name        text not null
);
    """)


def downgrade():
    op.execute("""
    drop table pay_types;
    """)
