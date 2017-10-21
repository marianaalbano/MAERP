from Model.Model import db, Produtos


class ProdutosClass:

    def listar_produtos(self):
        return Produtos.query.all()


    def filtrar_produto(self,id):
        return Produtos.query.get(id)

    def inserir_produto(self, info):
            produto = Produtos()
            produto.nome = info.get('nome')
            produto.valor = info.get('valor')
            db.session.add(produto)
            db.session.commit()

    def editar_produto(self, id, info):
        try:
            produto = Produtos.query.get(id)
            produto.nome = info.get('nome')
            produto.valor = info.get('valor')

            db.session.add(produto)
            db.session.commit()
        except Exception as e:
            return "Erro: %s" %e


    def desativar_produto(self, id):
        try:
            produto = Produtos.query.get(id)
            produto.ativo = False
            db.session.commit()
        except Exception as e:
            return "Erro: %s" % e

    def ativar_produto(self, id):
        try:
            produto = Produtos.query.get(id)
            produto.ativo = True
            db.session.commit()
        except Exception as e:
            return "Erro: %s" % e