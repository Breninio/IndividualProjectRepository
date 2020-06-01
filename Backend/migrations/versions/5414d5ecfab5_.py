"""empty message

Revision ID: 5414d5ecfab5
Revises: 76bd7642fbc3
Create Date: 2020-05-03 01:16:22.275112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5414d5ecfab5'
down_revision = '76bd7642fbc3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('activitytable',
    sa.Column('activity_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=60), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('start_date', sa.Date(), nullable=True),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.Column('reason', sa.String(length=200), nullable=True),
    sa.Column('learning', sa.String(length=200), nullable=True),
    sa.Column('application', sa.String(length=200), nullable=True),
    sa.Column('support', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('activity_id')
    )
    op.create_index(op.f('ix_activitytable_application'), 'activitytable', ['application'], unique=False)
    op.create_index(op.f('ix_activitytable_description'), 'activitytable', ['description'], unique=False)
    op.create_index(op.f('ix_activitytable_end_date'), 'activitytable', ['end_date'], unique=False)
    op.create_index(op.f('ix_activitytable_learning'), 'activitytable', ['learning'], unique=False)
    op.create_index(op.f('ix_activitytable_reason'), 'activitytable', ['reason'], unique=False)
    op.create_index(op.f('ix_activitytable_start_date'), 'activitytable', ['start_date'], unique=False)
    op.create_index(op.f('ix_activitytable_support'), 'activitytable', ['support'], unique=False)
    op.create_index(op.f('ix_activitytable_title'), 'activitytable', ['title'], unique=False)
    op.create_table('user_activities',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('activity_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['activity_id'], ['activitytable.activity_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['usertable.user_id'], )
    )
    op.add_column('usertable', sa.Column('is_cpdChamp', sa.Boolean(), nullable=True))
    op.add_column('usertable', sa.Column('user_id', sa.Integer(), nullable=False))
    op.drop_column('usertable', 'is_admin')
    op.drop_column('usertable', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usertable', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.add_column('usertable', sa.Column('is_admin', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('usertable', 'user_id')
    op.drop_column('usertable', 'is_cpdChamp')
    op.drop_table('user_activities')
    op.drop_index(op.f('ix_activitytable_title'), table_name='activitytable')
    op.drop_index(op.f('ix_activitytable_support'), table_name='activitytable')
    op.drop_index(op.f('ix_activitytable_start_date'), table_name='activitytable')
    op.drop_index(op.f('ix_activitytable_reason'), table_name='activitytable')
    op.drop_index(op.f('ix_activitytable_learning'), table_name='activitytable')
    op.drop_index(op.f('ix_activitytable_end_date'), table_name='activitytable')
    op.drop_index(op.f('ix_activitytable_description'), table_name='activitytable')
    op.drop_index(op.f('ix_activitytable_application'), table_name='activitytable')
    op.drop_table('activitytable')
    # ### end Alembic commands ###
