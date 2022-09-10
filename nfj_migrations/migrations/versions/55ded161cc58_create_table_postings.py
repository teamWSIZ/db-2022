"""create table postings

Revision ID: 55ded161cc58
Revises: 8048e9884cb1
Create Date: 2022-07-02 13:20:51.536374

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '55ded161cc58'
down_revision = '8048e9884cb1'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""create table postings
(
    posting_id serial primary key,
    title      text not null,
    company_id int references companies (company_id),
    salary_id  int references salaries (salary_id)
)""")


def downgrade():
    op.execute("""drop table postings
""")
