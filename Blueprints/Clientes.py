from flask import Blueprint, render_template, request, redirect, url_for, Response, flash
from flask_login import login_required
from Model.Model import Clientes, db
from Classes.ClienteClass import ClientesClass

clientes = Blueprint('clientes', __name__)



@clientes.route("/clientes/")
@login_required
def lista_clientes():
        clientes = ClientesClass()
        lista = clientes.listar_clientes()
        print lista[0].ativo
        return render_template('clientes.html', clientes=lista)

@clientes.route("/novo_cliente/", methods=['GET', 'POST'])
@login_required
def novo_cliente():
    if request.method == 'POST':
        try:
            cliente = ClientesClass()
            cliente.inserir_cliente(request.form)
            flash('Cliente adicionado com sucesso!', 'success')
            return redirect(url_for('.lista_clientes'))
        except Exception as e:

            flash('Falha ao inserir: %s' %e, 'danger')
            return redirect(url_for('.lista_clientes'))
    else:
        return render_template('novo_cliente.html')


@clientes.route("/editar_cliente/<id>/", methods=['GET', 'POST'])
@login_required
def editar_cliente(id):
    cliente = ClientesClass()

    if request.method == 'POST':
        try:
            cliente.editar_cliente(id, request.form)
            flash('Cliente alterado com sucesso!', 'success')
            return redirect(url_for('.lista_clientes'))
        except Exception as e:
            flash('Falha ao alterar: %s' %e, 'danger')
            return redirect(url_for('.lista_clientes'))
    else:
        info = cliente.filtrar_cliente(id)
        return render_template('editar_cliente.html', cliente=info)


@clientes.route("/remover_cliente/<id>/", methods=['POST'])
@login_required
def remover_cliente(id):
    cliente = ClientesClass()
    if request.method == 'POST':
        try:
            cliente.desativar_cliente(id)
            flash('Cliente removido com sucesso!', 'success')
            return redirect(url_for('.lista_clientes'))
        except Exception as e:
            flash('Falha ao remover: %s' %e, 'danger')
            return redirect(url_for('.lista_clientes'))
    else:
        cliente = cliente.filtrar_cliente(id)
        return render_template('editar_cliente.html', cliente=cliente)