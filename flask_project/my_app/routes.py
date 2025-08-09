# my_app/routes.py
from flask import render_template, redirect, url_for, request
from my_app.models import db, Juego
from my_app.forms import JuegoForm

def register_routes(app):
    @app.route('/')
    def index():
        juegos = Juego.query.all()
        return render_template('index.html', juegos=juegos)

    @app.route('/nuevo', methods=['GET', 'POST'])
    def nuevo_juego():
        form = JuegoForm()
        if form.validate_on_submit():
            juego = Juego(
                nombre=form.nombre.data,
                genero=form.genero.data,
                plataforma=form.plataforma.data,
                descripcion=form.descripcion.data
            )
            db.session.add(juego)
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('nuevo_juego.html', form=form)

    @app.route('/editar/<int:id>', methods=['GET', 'POST'])
    def editar_juego(id):
        juego = Juego.query.get_or_404(id)
        form = JuegoForm(obj=juego)
        if form.validate_on_submit():
            juego.nombre = form.nombre.data
            juego.genero = form.genero.data
            juego.plataforma = form.plataforma.data
            juego.descripcion = form.descripcion.data
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('editar_juego.html', form=form)

    @app.route('/eliminar/<int:id>', methods=['POST'])
    def eliminar_juego(id):
        juego = Juego.query.get_or_404(id)
        db.session.delete(juego)
        db.session.commit()
        return redirect(url_for('index'))