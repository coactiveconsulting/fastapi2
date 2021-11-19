"""add last few columns to posts table

Revision ID: 839f2ef9fc7f
Revises: aadb5d0761c6
Create Date: 2021-11-17 16:26:59.864644

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "839f2ef9fc7f"
down_revision = "aadb5d0761c6"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )
    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
