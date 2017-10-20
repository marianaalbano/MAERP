"""empty message

Revision ID: 231f361a9c4f
Revises: f3e40c461a37
Create Date: 2017-10-20 00:36:51.098298

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date
from alembic import op


# revision identifiers, used by Alembic.
revision = '231f361a9c4f'
down_revision = 'f3e40c461a37'
branch_labels = None
depends_on = None


def upgrade():

    # Create an ad-hoc table to use for the insert statement.
    usuarios = table('usuarios',
                           column('id', Integer),
                           column('email', String),
                           column('senha', String),
                           column('nome', String),
                           column('sobrenome', String)
                           )

    op.bulk_insert(usuarios,
                   [
                       {'id': 1,
                        'email': 'admin@erp.com.br',
                        'senha':'Mudar@123',
                        'nome':'Administrador',
                        'sobrenome':'Sistema'}
                   ]
                   )


def downgrade():
    pass
    # usuarios = table('usuarios',
    #                  column('id', Integer),
    #                  column('email', String),
    #                  column('senha', String),
    #                  column('nome', String),
    #                  column('sobrenome', String)
    #
    # op.bulk_delete(usuarios,
    #                [
    #                    {'id': 1,
    #                     'email': 'admin@erp.com.br',
    #                     'senha': 'Mudar@123',
    #                     'nome': 'Administrador',
    #                     'sobrenome': 'Sistema'}
    #                ]
    #                )
