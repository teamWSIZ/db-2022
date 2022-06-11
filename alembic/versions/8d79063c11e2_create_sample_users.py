"""create sample users

Revision ID: 8d79063c11e2
Revises: a45292a5f34c
Create Date: 2022-06-11 12:42:30.417677

"""
from alembic import op, context
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d79063c11e2'
down_revision = 'a45292a5f34c'
branch_labels = None
depends_on = None


def upgrade():
    if not context.get_x_argument(as_dictionary=True).get('prod', False):
        data_upgrade()


def downgrade():
    if not context.get_x_argument(as_dictionary=True).get('prod', False):
        data_downgrade()


def data_upgrade():
    user_names = ['Xiao', 'Li', 'Zhang']
    for u in user_names:
        op.execute(f"INSERT INTO users(name) values ('__{u}')")


def data_downgrade():
    user_names = ['Xiao', 'Li', 'Zhang']
    print('removing users')
    for n in user_names:
        op.execute(f"DELETE FROM users WHERE name = '__{n}'")
