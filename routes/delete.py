from flask import Flask, render_template, request, url_for, redirect
from __main__ import app, db
from models.pessoa import Pessoa

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
  pessoa = Pessoa.query.filter_by(id_pessoa=id).first()
  if request.method == 'POST':   
    current_db_sessions = db.session.object_session(pessoa)  
    current_db_sessions.delete(pessoa)
    current_db_sessions.commit()
  return redirect(url_for('index'))