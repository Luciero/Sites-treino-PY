from comunidadeimpressionadora.criarbanco import db
from datetime import datetime

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    foto_de_perfil = db.Column(db.String, default='default.jpg')
    cursos = db.Column(db.String, nullable=False, default='Não informado!')

    def __repr__(self):
        return f'<{self.username}>'



class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.Text, nullable=False)
    corpo = db.Column(db.Text, nullable=False)
    data_criacao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    def __repr__(self):
        return f'<{self.titulo}>'