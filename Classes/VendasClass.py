from flask import Blueprint, render_template, request, redirect, url_for, Response
from Model.Model import db, Vendas, Clientes
from ClienteClass import ClientesClass
from ProdutosClass import ProdutosClass
from sqlalchemy import distinct



class VendasClass:

    def listar_vendas(self):
        query = db.session.query(Vendas.id_venda.distinct())
        vendas = []
        for venda in query:
            unica = Vendas.query.get(venda)
            vendas.append(unica)
        return vendas

    def filtrar_venda(self, id):
        return Vendas.query.get(id)

    def buscar_info(self,id):
        return Vendas.query.filter_by(id_venda=id).order_by(Vendas.id.desc()).all()

    def adicionar_venda(self, info):
        try:
            #busca o ultimo ID
            venda_id = Vendas.query.order_by(Vendas.id.desc()).first()
            if venda_id:
                venda_id = venda_id.id + 1
            else:
                venda_id = 1

            p = ProdutosClass()
            
            for prod in info['produtos']:
                del(info['produtos'][-1])
                v = Vendas()
                if info.get('data'):
                    v.data = info.get('data')

                #encontra o cliente
                c = ClientesClass()
                cliente = c.filtrar_cliente(info.get('cliente_id'))
                cliente.vendas.append(v)

                total = 0
                #encontra os produtos
                produto = p.filtrar_produto(prod.get('ID'))
                v.quantidade = prod.get('quantidade')
                total += int(prod.get('total'))
                produto.vendas.append(v)

                #adiciona
                v.total = total
                v.id_venda = venda_id
                db.session.add(v)
                db.session.commit()

        except Exception as e:
            return 'Erro: %s' %e