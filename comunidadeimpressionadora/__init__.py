import bcrypt
from flask import Flask
from comunidadeimpressionadora.criarbanco import db
from comunidadeimpressionadora.models import Usuario, Post
from flask_bcrypt import Bcrypt

lista_usuarios = ['Pedro','João','Maria','Mauro']

app = Flask(__name__)
app.config['SECRET_KEY'] = 'adca60707f946de523ded83a1cf470a5'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'

db.init_app(app)
bcrypt = Bcrypt(app)


