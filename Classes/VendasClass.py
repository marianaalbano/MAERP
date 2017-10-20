from flask import Blueprint, render_template, request, redirect, url_for, Response
from Model.Model import db, Vendas


class VendasClass:

    def listar_vendas(self):
        return Vendas.query.order_by("data")


    def filtrar_venda(self, id):
        return Vendas.query.get(id)