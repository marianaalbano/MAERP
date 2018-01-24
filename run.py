from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import LoginManager, login_required, login_user, logout_user
from Model.Model import Clientes, Vendas, Produtos, db, app
from Blueprints.Vendas import vendas
from Blueprints.Clientes import clientes
from Blueprints.Produtos import produtos
from Classes.Usuario import Usuario
from Classes.VendasClass import VendasClass
from Classes.ProdutosClass import ProdutosClass
from Classes.ClienteClass import ClientesClass
from datetime import timedelta

#app = Flask(__name__)
app.secret_key = "mariana"
login_manager = LoginManager()


app.register_blueprint(vendas)
app.register_blueprint(clientes)
app.register_blueprint(produtos)


app.permanent_session_lifetime = timedelta(seconds=3600)

login_manager = LoginManager(app)
login_manager.init_app(app)


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("login"))

@login_manager.user_loader
def load_user(id):
    usuario = Usuario()
    return usuario.find_by_id(id)


@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login/', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('password')
        usuario = Usuario()
        usuario = usuario.login(email, senha)
        if usuario:
            login_user(usuario, remember=False)
            return redirect(url_for('index'))
        else:
            return 'xxx'
    else:

        return render_template('login.html')



@login_manager.unauthorized_handler
def unauthorized():
    return redirect('/login/')



@app.route("/logout/")
def logout():
    logout_user()
    return redirect('/login/')



@app.route("/index")
@login_required
def index():
    session.permanent = True
    vendas = VendasClass()
    qtd_vendas = vendas.listar_vendas()

    clientes = ClientesClass()
    qtd_clientes = clientes.listar_clientes()

    produtos = ProdutosClass()
    qtd_produtos = produtos.listar_produtos()
    total = Vendas.query.all()
    return render_template('index.html', 
                            clientes=qtd_clientes, 
                            vendas=qtd_vendas, 
                            produtos=qtd_produtos, 
                            total=1)


if __name__ == '__main__':
    import sys  

    reload(sys)  
    sys.setdefaultencoding('utf8')

    app.run(debug=True, host='0.0.0.0',port=8081)