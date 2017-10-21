from flask import Blueprint, render_template, request, redirect, url_for, Response, flash
from flask_login import login_required
from Model.Model import Produtos, db
from Classes.ProdutosClass import ProdutosClass

produtos = Blueprint('produtos', __name__)



@produtos.route("/produtos/")
@login_required
def lista_produtos():
        produtos = ProdutosClass()
        lista = produtos.listar_produtos()
        return render_template('produtos.html', produtos=lista)

@produtos.route("/novo_produto/", methods=['GET', 'POST'])
@login_required
def novo_produto():
    if request.method == 'POST':
        try:
            produto = ProdutosClass()
            produto.inserir_produto(request.form)
            flash('Produto adicionado com sucesso!', 'success')
            return redirect(url_for('.lista_produtos'))
        except Exception as e:

            flash('Falha ao inserir: %s' %e, 'danger')
            return redirect(url_for('.lista_produtos'))
    else:
        return render_template('novo_produto.html')


@produtos.route("/editar_produto/<id>/", methods=['GET', 'POST'])
@login_required
def editar_produto(id):
    produto = ProdutosClass()

    if request.method == 'POST':
        try:
            produto.editar_produto(id, request.form)
            flash('produto alterado com sucesso!', 'success')
            return redirect(url_for('.lista_produtos'))
        except Exception as e:
            flash('Falha ao alterar: %s' %e, 'danger')
            return redirect(url_for('.lista_produtos'))
    else:
        info = produto.filtrar_produto(id)
        return render_template('editar_produto.html', produto=info)


@produtos.route("/desativar_produto/<id>/", methods=['POST'])
@login_required
def desativar_produto(id):
    produto = ProdutosClass()
    if request.method == 'POST':
        try:
            produto.desativar_produto(id)
            flash('produto desativado com sucesso!', 'success')
            return redirect(url_for('.lista_produtos'))
        except Exception as e:
            flash('Falha ao remover: %s' %e, 'danger')
            return redirect(url_for('.lista_produtos'))
    else:
        produto = produto.filtrar_produto(id)
        return render_template('editar_produto.html', produto=produto)


@produtos.route("/ativar_produto/<id>/", methods=['POST'])
@login_required
def ativar_produto(id):
    produto = ProdutosClass()
    if request.method == 'POST':
        try:
            produto.ativar_produto(id)
            flash('produto ativado com sucesso!', 'success')
            return redirect(url_for('.lista_produtos'))
        except Exception as e:
            flash('Falha ao remover: %s' %e, 'danger')
            return redirect(url_for('.lista_produtos'))
    else:
        produto = produto.filtrar_produto(id)
        return render_template('editar_produto.html', produto=produto)