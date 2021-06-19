from flask import render_template
from __main__ import app
from models.pessoa import Pessoa

@app.route('/')
@app.route('/index')
def index(): 
  pessoas = Pessoa.query.all()
  return render_template('index.html', pessoas = pessoas)