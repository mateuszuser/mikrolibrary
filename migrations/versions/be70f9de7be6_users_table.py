"""users table

Revision ID: be70f9de7be6
Revises: 5dc5602dfec2
Create Date: 2022-07-22 08:14:11.675491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be70f9de7be6'
down_revision = '5dc5602dfec2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('avaible_notation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('borrow_date', sa.DateTime(), nullable=True),
    sa.Column('give_back_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_avaible_notation_borrow_date'), 'avaible_notation', ['borrow_date'], unique=False)
    op.create_index(op.f('ix_avaible_notation_give_back_date'), 'avaible_notation', ['give_back_date'], unique=False)
    op.drop_index('ix_post_created', table_name='post')
    op.drop_table('post')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('body', sa.TEXT(), nullable=True),
    sa.Column('created', sa.DATETIME(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_post_created', 'post', ['created'], unique=False)
    op.drop_index(op.f('ix_avaible_notation_give_back_date'), table_name='avaible_notation')
    op.drop_index(op.f('ix_avaible_notation_borrow_date'), table_name='avaible_notation')
    op.drop_table('avaible_notation')
    op.drop_table('author')
    op.drop_table('book')
    # ### end Alembic commands ###