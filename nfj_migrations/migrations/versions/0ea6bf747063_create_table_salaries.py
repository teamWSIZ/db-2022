"""create table salaries

Revision ID: 0ea6bf747063
Revises: 6e1b64d8d912
Create Date: 2022-07-02 13:03:58.756547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ea6bf747063'
down_revision = '6e1b64d8d912'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
    create table salaries
(
    salary_id    serial primary key,
    pay_type_id  int references pay_types (pay_type_id),
    low          int not null check ( low > 0 ),
    high         int not null check ( high > low ),
    paid_holiday boolean
);
    """)


def downgrade():
    op.execute("""
    drop table salaries;

    """)
