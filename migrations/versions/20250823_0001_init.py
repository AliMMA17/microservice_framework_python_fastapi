"""init: create test_items

Revision ID: 20250823_0001
Revises:
Create Date: 2025-08-23 00:00:00

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "20250823_0001"
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        "test_items",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(length=120), nullable=False),
        sa.Column("note", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("NOW()"), nullable=False),
    )
    op.create_index("ix_test_items_name", "test_items", ["name"])

def downgrade():
    op.drop_index("ix_test_items_name", table_name="test_items")
    op.drop_table("test_items")
