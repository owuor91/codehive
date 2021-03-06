"""add student model

Revision ID: 537fbc202b20
Revises: 
Create Date: 2021-07-08 14:08:52.139293

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
from sqlalchemy.dialects.postgresql import ENUM

revision = "537fbc202b20"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "student",
        sa.Column("date_created", sa.DateTime(timezone=True), nullable=False),
        sa.Column("date_updated", sa.DateTime(timezone=True), nullable=False),
        sa.Column("created_by", sa.String(length=100), nullable=False),
        sa.Column("updated_by", sa.String(length=100), nullable=False),
        sa.Column("active", sa.Boolean(), nullable=False),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("meta", sa.JSON(), server_default="{}", nullable=True),
        sa.Column("student_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("email", sa.String(length=100), nullable=False),
        sa.Column("phone_number", sa.String(length=50), nullable=False),
        sa.Column("date_of_birth", sa.Date(), nullable=False),
        sa.Column(
            "nationality",
            ENUM(
                "KENYAN",
                "RWANDAN",
                "UGANDAN",
                "SOUTH_SUDANESE",
                "SUDANESE",
                name="nationality",
                create_type=False,
            ),
            nullable=False,
        ),
        sa.Column("password", sa.String(length=256), nullable=False),
        sa.PrimaryKeyConstraint("student_id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("phone_number"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("student")
    # ### end Alembic commands ###
