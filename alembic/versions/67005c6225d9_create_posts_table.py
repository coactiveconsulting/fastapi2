"""create posts table

Revision ID: 67005c6225d9
Revises: 
Create Date: 2021-11-17 16:16:43.947285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "67005c6225d9"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


def downgrade():
    op.drop_table("posts")
    pass
