from flask import Blueprint, render_template, request, redirect, url_for, Response
from Model.Model import db, Vendas, Clientes, VendaProdutos
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
            vp = VendaProdutos()
            v = Vendas()
            c = ClientesClass()
            cliente = Clientes()
            produto = ProdutosClass()
            cliente = c.filtrar_cliente(info.get('cliente_id'))
            total = 0
            for prod in info['produtos']:
                total += int(prod.get('total'))
                p = produto.filtrar_produto(prod.get('ID'))
                vp.produtos.append(p)
            v.total = total
            v.descricao = 'teste'
            v.data = info.get('data')
            vp = info.get('quantidade')
            cliente.vendas.append(vp)
            vp.vendas.append(v)
            db.session.add(v)
            db.session.commit()
        except Exception as e:
            print 'erro: %s' %e



if __name__ == '__main__':
    v = VendasClass()
    v.adicionar_venda(data='15/03/1995', cliente='1', produto_id='1')
