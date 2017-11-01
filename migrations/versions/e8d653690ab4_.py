"""Tables Species, Proteins and Interactions

Revision ID: e8d653690ab4
Revises: 
Create Date: 2017-11-01 11:26:40.276016

"""

# revision identifiers, used by Alembic.
revision = 'e8d653690ab4'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('species',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('short_label', mysql.TEXT(), nullable=True),
    sa.Column('tax_id', sa.Integer(), nullable=True),
    sa.Column('full_name', mysql.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('species_pk'))
    )
    op.create_table('proteins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sequence', mysql.TEXT(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('specie_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['specie_id'], ['species.id'], name=op.f('proteins_specie_id_foreign')),
    sa.PrimaryKeyConstraint('id', name=op.f('proteins_pk'))
    )
    op.create_table('interactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('protein_id_1', sa.Integer(), nullable=False),
    sa.Column('protein_id_2', sa.Integer(), nullable=False),
    sa.Column('extra_data', mysql.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['protein_id_1'], ['proteins.id'], name=op.f('interactions_protein_id_1_foreign')),
    sa.ForeignKeyConstraint(['protein_id_2'], ['proteins.id'], name=op.f('interactions_protein_id_2_foreign')),
    sa.PrimaryKeyConstraint('id', name=op.f('interactions_pk'))
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('interactions')
    op.drop_table('proteins')
    op.drop_table('species')
    ### end Alembic commands ###
