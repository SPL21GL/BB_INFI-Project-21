from flask import Flask, redirect, request, flash, session
from flask.templating import render_template
from model.models import db
from controllers.index import index_blueprint

from flask_wtf.csrf import CSRFProtect

import sqlalchemy
app = Flask(__name__)
app.secret_key = "VerySecretSecretKey"

#Datenbankzugriff konfigurieren
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/INFI_Project_21"

csrf = CSRFProtect(app)

db.init_app(app)

app.register_blueprint(index_blueprint)

app.run(debug=True)
