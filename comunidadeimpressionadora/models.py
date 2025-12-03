from comunidadeimpressionadora import login_manager, db
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_usuario(id_usuario):
     return Usuario.query.get(int(id_usuario))


class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    senha = db.Column(db.String(30), nullable=False)
    foto_perfil = db.Column(db.String, default='default.jpg')
    cursos = db.Column(db.String, nullable=False, default='Não informado!')
    posts = db.relationship('Post', backref='autor', lazy=True)




class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.Text, nullable=False)
    corpo = db.Column(db.Text, nullable=False)
    data_criacao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

