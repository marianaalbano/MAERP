#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from datetime import datetime
import os

POSTGRES_USER = os.environ["POSTGRES_USER"]
POSTGRES_PW = os.environ["POSTGRES_PW"]
POSTGRES_URL = os.environ["POSTGRES_URL"]
POSTGRES_DB = os.environ["POSTGRES_DB"]

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)


app = Flask(__name__,static_folder='../static', template_folder='../templates')
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app, session_options={"autoflush": False})


migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Usuarios(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    senha = db.Column(db.String, nullable=False)
    nome = db.Column(db.String, nullable=False)
    sobrenome = db.Column(db.String, nullable=False)

    def is_active(self):
        # return True if self.active is True else False
        return self.is_active()

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False


class Clientes(db.Model):
    __tablename__ = 'clientes'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    telefone = db.Column(db.String, nullable=False)
    endereco = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    ativo = db.Column(db.String, default=True)
    vendas = db.relationship("Vendas", backref='clientes')


class Produtos(db.Model):
    __tablename__ = 'produtos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String,  nullable=False)
    valor = db.Column(db.Integer, nullable=False)
    ativo = db.Column(db.String, default=True)
    vendas = db.relationship("Vendas", backref='produtos')



class Vendas(db.Model):
    __tablename__ = 'vendas'

    id = db.Column(db.Integer, primary_key=True)
    id_venda = db.Column(db.Integer, nullable=False)
    data = db.Column(db.DateTime, default=datetime.now())
    quantidade = db.Column(db.Integer)
    clientes_id = db.Column(db.Integer, db.ForeignKey("clientes.id"))
    produtos_id = db.Column(db.Integer, db.ForeignKey("produtos.id"))
    cliente = db.relationship("Clientes")
    produto = db.relationship("Produtos")


if __name__ == '__main__':
    manager.run()