from flask import render_template, redirect, url_for, flash, request
from comunidadeimpressionadora.forms import FormLogin, FormCriarConta, FormEditarPerfil
from comunidadeimpressionadora import app, lista_usuarios, bcrypt, db
from comunidadeimpressionadora.models import Usuario, Post
from flask_login import login_user, logout_user, current_user, login_required


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/usuarios')
@login_required
def usuarios():
    return render_template('usuarios.html',lista_usuarios=lista_usuarios)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')
            par_next = request.args.get('next')
            if par_next:                               # parametro para retornar a pagina que clicou antes de fazer login
                return redirect(par_next)
            else:
                return redirect(url_for('home'))
        else:
            flash(f'Login não foi feito, preencha com um email valido', 'alert-danger')

    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        senha_crypt = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha_crypt)
        db.session.add(usuario)
        db.session.commit()
        flash(f'Conta criada com sucesso no e-mail: {form_criarconta.email.data}', 'alert-success' )
        return redirect(url_for('home'))
    return render_template('login.html', form_login = form_login, form_criarconta = form_criarconta)


@app.route('/sair')
@login_required
def sair():
    logout_user()
    flash('Logout feito com Sucesso!', 'alert-success')
    return redirect(url_for('home'))


@app.route('/perfil')
@login_required
def perfil():
    foto_perfil = url_for('static', filename='fotos_perfil/{}'.format(current_user.foto_perfil))
    return render_template('perfil.html', foto_perfil=foto_perfil)


@app.route('/post/criar')
@login_required
def criar_post():
    return render_template('criarpost.html')


@app.route('/perfil/editar', methods=['GET', 'POST'])
@login_required
def editar_perfil():
    form = FormEditarPerfil()
    if form.validate_on_submit():
        current_user.email = form.email.data
        current_user.username = form.username.data
        db.session.commit()
        flash('Perfil atualizacado com Sucesso!', 'alert-success')
        return redirect(url_for('perfil'))
    elif request.method == 'GET':
        form.email.data = current_user.email
        form.username.data = current_user.username
    foto_perfil = url_for('static', filename='fotos_perfil/{}'.format(current_user.foto_perfil))
    return render_template('editarperfil.html', foto_perfil=foto_perfil, form=form)



