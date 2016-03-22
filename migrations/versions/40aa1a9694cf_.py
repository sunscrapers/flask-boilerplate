"""

Revision ID: 40aa1a9694cf
Revises: None
Create Date: 2016-03-22 00:08:31.860252

"""

# revision identifiers, used by Alembic.
revision = '40aa1a9694cf'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    op.create_table('document',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('data', postgresql.JSONB(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('document')
