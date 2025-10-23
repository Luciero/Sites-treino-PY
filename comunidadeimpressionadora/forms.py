from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()], )
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha =  PasswordField('Senha', validators=[DataRequired(), Length(8, 20)])
    confirmacao_senha = PasswordField('Confirmar senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')



class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(8, 20)])
    botao_submit_login = SubmitField('Fazer Login')
    lembrar_dados = BooleanField("Lembrar Dados da Conta")
