"""assign users to villas

Revision ID: 7bcb020b1aa1
Revises: 7201a6de3029
Create Date: 2022-06-11 12:58:28.430924

"""
from alembic import op, context
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '7bcb020b1aa1'
down_revision = '7201a6de3029'
branch_labels = None
depends_on = None


def upgrade():
    if context.get_x_argument(as_dictionary=True).get('prod', True):
        data_upgrade()


def downgrade():
    if not context.get_x_argument(as_dictionary=True).get('prod', False):
        data_downgrade()


def data_upgrade():
    op.execute("""insert into uservillas(userid, villaid)
values ((select id userid from users where name='__Xiao'),
        (select id villaid from villas where name='Santiago'))""")


def data_downgrade():
    op.execute("""delete from uservillas where userid = (select id userid from users where name='__Xiao') and
                             villaid =   (select id villaid from villas where name='Santiago');
""")
