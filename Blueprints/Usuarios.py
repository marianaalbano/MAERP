from flask import Blueprint

usuarios = Blueprint('usuarios',__name__)

@usuarios.route("/usuario/")
def usuario():
    pass