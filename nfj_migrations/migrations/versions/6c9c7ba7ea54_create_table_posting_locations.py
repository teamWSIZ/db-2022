"""create table posting_locations

Revision ID: 6c9c7ba7ea54
Revises: 55ded161cc58
Create Date: 2022-07-02 13:22:13.621616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c9c7ba7ea54'
down_revision = '55ded161cc58'
branch_labels = None
depends_on = None

def upgrade():
    op.execute(
        """create table posting_locations
    (
    posting_id  int not null references postings (posting_id),
    location_id int not null references location_types (location_id),
    unique (posting_id, location_id)
    );"""
    )


def downgrade():
    op.execute("""drop table post-ing_locations;""")