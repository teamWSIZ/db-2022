"""create table levels

Revision ID: 665541869e31
Revises: 6c9c7ba7ea54
Create Date: 2022-07-02 13:23:03.638504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '665541869e31'
down_revision = '6c9c7ba7ea54'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """create table levels
    (
    level_id serial primary key,
    name     text not null
    );"""
    )


def downgrade():
    op.execute("""drop table levels;""")
