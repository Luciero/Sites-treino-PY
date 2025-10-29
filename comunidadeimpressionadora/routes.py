from flask import render_template, redirect, url_for, flash, request
from comunidadeimpressionadora.forms import FormLogin, FormCriarConta
from comunidadeimpressionadora import app, lista_usuarios, Usuario, bcrypt
from comunidadeimpressionadora.criarbanco import db


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html',lista_usuarios=lista_usuarios)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()

    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')
        return redirect(url_for('home'))

    elif form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:

        senha_crypt = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha_crypt)
        db.session.add(usuario)
        db.session.commit()

        flash(f'Conta criada com sucesso no e-mail: {form_criarconta.email.data}', 'alert-success' )
        return redirect(url_for('home'))
    return render_template('login.html', form_login = form_login, form_criarconta = form_criarconta)