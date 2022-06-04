"""create table users

Revision ID: 31ca6d216cdc
Revises: 
Create Date: 2022-05-30 09:39:47.560082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31ca6d216cdc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.Text, primary_key=True),
    )


def downgrade():
    op.drop_table('users')
