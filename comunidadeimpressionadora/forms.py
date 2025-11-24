from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from comunidadeimpressionadora.models import Usuario
from flask_login import current_user



class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()], )
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha =  PasswordField('Senha', validators=[DataRequired(), Length(8, 20)])
    confirmacao_senha = PasswordField('Confirmar senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

    def validate_email(self,email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail ja cadastrado, Cadastre-se novamente com outro email')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(8, 20)])
    botao_submit_login = SubmitField('Fazer Login')
    lembrar_dados = BooleanField("Lembrar Dados da Conta")


class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()], )
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['jpg','png'])])
    botao_submit_editar_perfil = SubmitField('Confirmar Edição')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                return ValidationError('Ja existe um usuário com esse E-mail. Cadastre com outro E-mail')