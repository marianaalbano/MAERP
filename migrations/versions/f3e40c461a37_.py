"""empty message

Revision ID: f3e40c461a37
Revises: 
Create Date: 2017-10-20 00:36:36.680253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3e40c461a37'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clientes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('telefone', sa.String(), nullable=False),
    sa.Column('endereco', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('ativo', sa.String(), default=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('produtos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('valor', sa.Integer(), nullable=False),
    sa.Column('ativo', sa.String(), default=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('senha', sa.String(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('sobrenome', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vendas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.DateTime(), nullable=True),
    sa.Column('descricao', sa.String(), nullable=False),
    sa.Column('total', sa.Integer(), nullable=False),
    sa.Column('clientes_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['clientes_id'], ['clientes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vendas_produtos',
    sa.Column('venda_id', sa.Integer(), nullable=True),
    sa.Column('produto_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['produto_id'], ['produtos.id'], ),
    sa.ForeignKeyConstraint(['venda_id'], ['vendas.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vendas_produtos')
    op.drop_table('vendas')
    op.drop_table('usuarios')
    op.drop_table('produtos')
    op.drop_table('clientes')
    # ### end Alembic commands ###
