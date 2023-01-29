from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.posteo import Posteo
from flask_app.models.usuario import Usuario
from flask_app.models.like import Like

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/nuevo/posteo')
def posteos():
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": session['user_id']
    }
    return render_template('posteos.html', user=Usuario.traer_id(data))


@app.route('/crear/posteo', methods=['POST'])
def crear_posteo():
    if 'user_id' not in session:
        return redirect('/inisesion')
    ##if not Posteo.validar_posteo(request.form):
      ##  return redirect('/pagina1')
    data = {
        "posteo": request.form["posteo"],
        "user_id": session["user_id"]
    }
    Posteo.save(data)
    return redirect('/pagina1')



@app.route('/posteo/<int:id>')
def mostrar_posteo(id):
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": id
    }
    user_data = {
        "id": session['user_id']
    }
    return render_template("mostrar.html", posteo=Posteo.todo(data), user=Usuario.traer_id(user_data))


@app.route('/posteo/eliminar/<int:id>')
def eliminar(id):
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": id
    }
    Posteo.eliminar(data)
    return redirect('/pagina1')


