#!/usr/bin/python
#-*- coding: utf8 -*-
from flask import Blueprint, render_template, request, redirect, url_for, Response, flash
from flask_login import login_required
from Classes.VendasClass import VendasClass
from Model.Model import Vendas
from pdfkit import from_string, configuration


vendas = Blueprint('vendas', __name__)



@vendas.route("/vendas/")
@login_required
def listar_vendas():
    vendas = VendasClass()
    info = vendas.listar_vendas()
    return render_template('vendas.html', vendas=info)


@vendas.route("/pdf/", methods=['GET', 'POST'])
@login_required
def cria_pdf():
    if request.method == 'POST':
        vendas = VendasClass()
        try:
            id = request.form.get('id')
            info = vendas.filtrar_venda(id)
            html = render_template('nota.html', vendas=info)
            pdf = from_string(html, False)
            header = {"Content-disposition": "attachment; filename=nota.pdf"}
            a = Response(pdf, mimetype="application/pdf", headers=header)
            return a
        except Exception as e:
            flash('Falha ao gerar PDF: %s' % e, 'danger')
            return redirect(url_for('.listar_vendas'))
    else:
        return redirect(url_for('.listar_vendas'))


@vendas.route("/info/", methods=['GET', 'POST'])
@login_required
def info():
    vendas = VendasClass()
    if request.method == 'POST':
        try:
            id = request.form.get('id')
            vendas = vendas.buscar_info(id)
            total = 0
            for venda in vendas:
                total += venda.quantidade * venda.produto.valor
            return render_template('info.html', vendas=vendas, total=total)
        except Exception as e:
            flash('Falha ao gerar informações: %s' % e, 'danger')
            return redirect(url_for('.listar_vendas'))


@vendas.route("/nova_venda/", methods=['GET', 'POST'])
@login_required
def nova_venda():
    if request.method == 'POST':
        try:
            dados = request.get_json()
            venda = VendasClass()
            venda.adicionar_venda(dados)
            flash('Venda adicionada com sucesso!', 'success')
            return redirect(url_for('.nova_venda'))
        except Exception as e:
            flash('Falha ao inserir: %s' %e, 'danger')
            return redirect(url_for('.nova_venda'))
    else:
        return render_template('nova_venda.html')