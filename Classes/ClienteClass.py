from Model.Model import db, Clientes


class ClientesClass:

    def listar_clientes(self):
        return Clientes.query.all()


    def filtrar_cliente(self,id):
        return Clientes.query.get(id)

    def inserir_cliente(self, info):
            cliente = Clientes()
            cliente.nome = info.get('nome')
            cliente.endereco = info.get('endereco')
            cliente.telefone = str(info.get('telefone'))
            cliente.email = info.get('email')
            db.session.add(cliente)
            db.session.commit()

    def editar_cliente(self, id, info):
        try:
            cliente = Clientes.query.get(id)
            cliente.nome = info.get('nome')
            cliente.endereco = info.get('endereco')
            cliente.telefone = str(info.get('telefone'))
            cliente.email = info.get('email')
            db.session.add(cliente)
            db.session.commit()
        except Exception as e:
            return "Erro: %s" %e


    def desativar_cliente(self, id):
        try:
            cliente = Clientes.query.get(id)
            cliente.ativo = False
            db.session.commit()
        except Exception as e:
            return "Erro: %s" % e

    def ativar_cliente(self, id):
        try:
            cliente = Clientes.query.get(id)
            cliente.ativo = True
            db.session.commit()
        except Exception as e:
            return "Erro: %s" % e