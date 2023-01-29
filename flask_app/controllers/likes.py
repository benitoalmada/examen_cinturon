from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.posteo import Posteo
from flask_app.models.usuario import Usuario
from flask_app.models.like import Like


@app.route('/nuevo/like')
def like():
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": session['user_id']
    }
    return render_template('posteos.html', user=Usuario.traer_id(data), lik=Like.save(data))


@app.route('/crear/like', methods=['POST'])
def crear_like():
    if 'user_id' not in session:
        return redirect('/inisesion')
   # if not Posteo.validar_posteo(request.form):
   # return redirect('/pagina1')
    data = {
        "id": request.form["id"],
        "user_id": session["user_id"]

    }
    Like.save(data)
    return redirect('/pagina1')



@app.route('/like/eliminar/<int:id>')
def eliminar(id):
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": id
    }
    Like.eliminar(data)
    return redirect('/pagina1')

