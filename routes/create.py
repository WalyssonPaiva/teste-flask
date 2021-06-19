from flask import request, url_for, redirect
from __main__ import app, db
from models.pessoa import Pessoa

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
  if request.method == 'POST':
    nome = (request.form.get('nome'))
    rg = (request.form.get('rg'))
    cpf = (request.form.get('cpf'))
    data_nascimento = (request.form.get('data_nascimento'))
    data_admissao = (request.form.get('data_admissao'))
    funcao = (request.form.get('funcao'))

    p = Pessoa(nome,rg,cpf,data_nascimento,data_admissao,funcao)
    db.session.add(p)
    db.session.commit()
    
    return redirect(url_for('index'))