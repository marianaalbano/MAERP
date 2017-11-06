from flask import Blueprint, render_template, request, redirect, url_for, Response
from Model.Model import db, Vendas, Clientes
from ClienteClass import ClientesClass
from ProdutosClass import ProdutosClass


class VendasClass:

    def listar_vendas(self):
        return Vendas.query.order_by("data")


    def filtrar_venda(self, id):
        return Vendas.query.get(id)


    def adicionar_venda(self, info):
        print 'aqui'
        cliente = ClientesClass()
        cliente = cliente.filtrar_cliente(info.get('cliente_id'))
        produto = ProdutosClass()
        produto = produto.filtrar_produto(info.get('produto_id'))
        venda = Vendas()
        venda.total = 1000#info.get('total')
        venda.descricao = 'teste'
        cliente.vendas.append(venda)
        venda.produtos.append(produto)
        db.session.add(venda)
        db.session.commit()



if __name__ == '__main__':
    v = VendasClass()
    v.adicionar_venda(data='15/03/1995', cliente='1', produto_id='1')
