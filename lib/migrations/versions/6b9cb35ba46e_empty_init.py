"""Empty Init

Revision ID: 6b9cb35ba46e
Revises: 
Create Date: 2022-08-04 13:21:26.936909

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b9cb35ba46e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'birthday', new_column_name=sa.Column('birth_day', sa.String))


def downgrade() -> None:
    op.alter_column('students', 'birth_day', new_column_name=sa.Column('birthday', sa.String)) 
