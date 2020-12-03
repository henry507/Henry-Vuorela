# Import helper libs
from Modules import Clients, Reservations, Workspaces
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import date
import pandas as pd
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///TUAS.sqlite3'


@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def hello():
    # clients_list = Clients('ahmed', '12547')
    # Workspace_list = Workspaces('work1')
    # Reservations_list = Reservations(1, 1)
    # db.session.add( Reservations_list)
    # db.session.commit()
    cc = Reservations.query.all()
    print(cc[0].Workspace_id)
    return 'welcome to reservation'


if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True)
