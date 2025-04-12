"""

initial

Revision ID: 82538ab72d38
Revises:
Create Date: 2025-04-11 11:51:58.425895

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "82538ab72d38"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "table",
        sa.Column(
            "name",
            sa.String(length=55),
            nullable=False,
        ),
        sa.Column(
            "seats",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "location",
            sa.String(length=140),
            nullable=False,
        ),
        sa.Column(
            "id",
            sa.Integer(),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint(
            "id",
            name=op.f("pk_table"),
        ),
        sa.UniqueConstraint(
            "name",
            name=op.f("uq_table_name"),
        ),
    )
    op.create_index(
        op.f("ix_table_id"),
        "table",
        ["id"],
        unique=False,
    )
    op.create_table(
        "reservation",
        sa.Column(
            "customer_name",
            sa.String(length=55),
            nullable=False,
        ),
        sa.Column(
            "reservation_time",
            sa.DateTime(),
            nullable=False,
        ),
        sa.Column(
            "duration_minutes",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "table_id",
            sa.Integer(),
            nullable=True,
        ),
        sa.Column(
            "id",
            sa.Integer(),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["table_id"],
            ["table.id"],
            name=op.f("fk_reservation_table_id_table"),
        ),
        sa.PrimaryKeyConstraint(
            "id",
            name=op.f("pk_reservation"),
        ),
    )
    op.create_index(
        op.f("ix_reservation_id"),
        "reservation",
        ["id"],
        unique=False,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(
        op.f("ix_reservation_id"),
        table_name="reservation",
    )
    op.drop_table(
        "reservation",
    )
    op.drop_index(
        op.f("ix_table_id"),
        table_name="table",
    )
    op.drop_table(
        "table",
    )
