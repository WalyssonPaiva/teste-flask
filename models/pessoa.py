from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pessoa(db.Model):
  __tablename__='pessoas'

  id_pessoa = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nome = db.Column(db.String(100), nullable=False)
  rg = db.Column(db.String(100), nullable=False)
  cpf = db.Column(db.String(100), nullable=False)
  data_nascimento = db.Column(db.DateTime(), nullable=False)
  data_admissao = db.Column(db.DateTime(), nullable=False)
  funcao = db.Column(db.String(100))

  def __init__(self, nome, rg, cpf, data_nascimento, data_admissao, funcao):
    self.nome = nome
    self.rg = rg
    self.cpf = cpf
    self.data_nascimento = data_nascimento
    self.data_admissao = data_admissao
    self.funcao = funcao