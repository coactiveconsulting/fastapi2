"""add content column to posts table

Revision ID: c110ead23535
Revises: 67005c6225d9
Create Date: 2021-11-17 16:21:47.489486

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c110ead23535"
down_revision = "67005c6225d9"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
