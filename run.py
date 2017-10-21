from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import LoginManager, login_required, login_user, logout_user
from Model.Model import Clientes, Vendas, Produtos, db, app
from Blueprints.Vendas import vendas
from Blueprints.Clientes import clientes
from Blueprints.Produtos import produtos
from Classes.Usuario import Usuario
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
    clientes = db.session.query(Clientes).count()
    vendas = db.session.query(Vendas).count()
    produtos = db.session.query(Produtos).count()
    total = Vendas.query.all()
    return render_template('index.html', clientes=clientes, vendas=vendas, produtos=produtos, total=total)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8081)