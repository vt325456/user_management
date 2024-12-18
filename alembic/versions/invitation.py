from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from alembic import op
def upgrade():
    op.create_table(
        'invitations',
        Column('id', Integer, primary_key=True, index=True),
        Column('inviter_id', Integer, ForeignKey('users.id'), nullable=False),
        Column('invitee_email', String, nullable=False),
        Column('qr_code_url', String, nullable=True),
        Column('status', String, default="sent")
    )
def downgrade():
    op.drop_table('invitations')