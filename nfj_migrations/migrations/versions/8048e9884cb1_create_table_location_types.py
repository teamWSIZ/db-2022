"""create table location_types

Revision ID: 8048e9884cb1
Revises: 0ea6bf747063
Create Date: 2022-07-02 13:18:22.634956

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '8048e9884cb1'
down_revision = '0ea6bf747063'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
    create table location_types
    (
    location_id  serial primary key,
    city         text    not null,
    remote       boolean not null,
    remote_level int
    );
    """
    )


def downgrade():
    op.execute("""drop table location_types;""")
