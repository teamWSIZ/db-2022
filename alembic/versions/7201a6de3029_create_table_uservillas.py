"""create table uservillas

Revision ID: 7201a6de3029
Revises: 8d79063c11e2
Create Date: 2022-06-11 12:53:53.019702

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7201a6de3029'
down_revision = '8d79063c11e2'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""create table uservillas(userid int not null references users(id) on delete cascade, 
    villaid int not null references villas(id) on delete cascade)""")


def downgrade():
    op.execute('drop table uservillas')
