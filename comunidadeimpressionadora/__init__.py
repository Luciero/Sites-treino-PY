from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

lista_usuarios = ['Pedro','João','Maria','Mauro']

app = Flask(__name__)
app.config['SECRET_KEY'] = 'adca60707f946de523ded83a1cf470a5'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'

db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'                # redireciona para o login se nao tiver logado
login_manager.login_message_category = 'alert-info'

