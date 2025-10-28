from flask import render_template, redirect, url_for, request, flash
from my_app.models import db, Juego, Usuario, Reseña
from my_app.forms import JuegoForm, RegistroForm, LoginForm, EditarPerfilForm, ReseñaForm
from flask_login import login_user, logout_user, login_required, current_user
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

        # --- Lógica para asociar reseñas a juegos ---
        reseñas_dict = {}
        for juego in juegos:
            reseña = Reseña.query.filter_by(juego_id=juego.id).order_by(Reseña.id.desc()).first()
            reseñas_dict[juego.id] = reseña
        # --------------------------------------------

        form = JuegoForm()
        editar_perfil_form = EditarPerfilForm(obj=current_user)

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

        return render_template(
            'index.html',
            juegos=juegos,
            q=q,
            form=form,
            editar_perfil_form=editar_perfil_form,
            reseñas_dict=reseñas_dict  # <--- Añade esto
        )

    @app.route('/editar/<int:id>', methods=['POST'])
    def editar_juego(id):
        juego = Juego.query.get_or_404(id)   # obtenemos el juego de la DB
        form = JuegoForm()

        if form.validate_on_submit():
            # actualizamos en vez de crear uno nuevo
            juego.nombre = form.nombre.data
            juego.genero = form.genero.data
            juego.plataforma = form.plataforma.data
            juego.descripcion = form.descripcion.data

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

    @app.route('/editar_perfil', methods=['POST'])
    @login_required
    def editar_perfil():
        form = EditarPerfilForm()
        if form.validate_on_submit():
            current_user.nombre_completo = form.nombre_completo.data
            current_user.edad = form.edad.data
            db.session.commit()
            flash('Perfil actualizado con éxito', 'success')
        else:
            flash('Error al actualizar el perfil', 'danger')
        return redirect(url_for('index'))

    @app.route('/añadir_reseña/<int:juego_id>', methods=['POST'])
    def añadir_reseña(juego_id):
        form = ReseñaForm()
        if form.validate_on_submit():
            reseña = Reseña(
                calificacion=form.calificacion.data,
                texto_reseña=form.texto_reseña.data,
                juego_id=juego_id
            )
            db.session.add(reseña)
            db.session.commit()
            flash('Reseña añadida con éxito', 'success')
        else:
            flash('Error al añadir la reseña', 'danger')
        return redirect(url_for('index'))
