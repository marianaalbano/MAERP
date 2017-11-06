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
        try:
            del(info['produtos'][-1])
            venda = Vendas()
            clientes = Clientes()
            cliente = ClientesClass()
            produto = ProdutosClass()
            cliente = cliente.filtrar_cliente(info.get('cliente_id'))
            print cliente.nome
            print info['produtos']
            total = 0
            for prod in info['produtos']:
                total += int(prod.get('total'))
                p = produto.filtrar_produto(prod.get('ID'))
                print p.nome
                venda.produtos.append(p)
            venda.total = total
            venda.descricao = 'teste'
            venda.data = info.get('data')
            clientes.vendas.append(venda)
            db.session.add(venda)
            db.session.commit()
        except Exception as e:
            print 'erro: %s' %e



if __name__ == '__main__':
    v = VendasClass()
    v.adicionar_venda(data='15/03/1995', cliente='1', produto_id='1')
