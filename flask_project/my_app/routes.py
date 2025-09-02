from flask import render_template, redirect, url_for, request, flash
from my_app.models import db, Juego, Usuario
from my_app.forms import JuegoForm, RegistroForm, LoginForm
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

def register_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        q = request.args.get('q', '').strip()

        if q:
            juegos = Juego.query.filter(
                (Juego.nombre.ilike(f'%{q}%')) |
                (Juego.genero.ilike(f'%{q}%')) |
                (Juego.plataforma.ilike(f'%{q}%'))
            ).all()
        else:
            juegos = Juego.query.all()

        form = JuegoForm()

        # Handle new game submission from modal
        if form.validate_on_submit():
            juego = Juego(
                nombre=form.nombre.data,
                genero=form.genero.data,
                plataforma=form.plataforma.data,
                descripcion=form.descripcion.data
            )
            db.session.add(juego)
            db.session.commit()
            flash('Juego agregado con éxito', 'success')
            return redirect(url_for('index'))

        return render_template('index.html', juegos=juegos, q=q, form=form)

    @app.route('/editar/<int:id>', methods=['POST'])
    def editar_juego(id):
        juego = Juego.query.get_or_404(id)
        juego.nombre = request.form['nombre']
        juego.genero = request.form['genero']
        juego.plataforma = request.form['plataforma']
        juego.descripcion = request.form['descripcion']
        db.session.commit()
        flash('Juego actualizado con éxito', 'success')
        return redirect(url_for('index'))


    @app.route('/eliminar/<int:id>', methods=['POST'])
    def eliminar_juego(id):
        juego = Juego.query.get_or_404(id)
        db.session.delete(juego)
        db.session.commit()
        flash('Juego eliminado', 'success')
        return redirect(url_for('index'))


    @app.route('/registro', methods=['GET', 'POST'])
    def registro():
        form = RegistroForm()
        if form.validate_on_submit():
            hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
            nuevo_usuario = Usuario(username=form.username.data, password=hashed_password)
            db.session.add(nuevo_usuario)
            db.session.commit()
            flash('Usuario registrado con éxito', 'success')
            return redirect(url_for('login'))
        return render_template('registro.html', form=form)


    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            usuario = Usuario.query.filter_by(username=form.username.data).first()
            if usuario and check_password_hash(usuario.password, form.password.data):
                login_user(usuario)
                return redirect(url_for('index'))
            flash('Usuario o contraseña incorrectos', 'danger')
        return render_template('login.html', form=form)


    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('login'))


    @app.route('/perfil')
    @login_required
    def perfil():
        return render_template('perfil.html')
