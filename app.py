from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://walyssonpaiva:<password>@<hostname>:3306/walyssonpaiva"
db = SQLAlchemy(app)
db.create_all()

import routes.index
import routes.create
import routes.delete


if __name__ == '__main__':
  app.run(debug=True)
