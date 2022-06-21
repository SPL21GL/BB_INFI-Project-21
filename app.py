from flask import Flask

from controllers.auto import autos_blueprint
from controllers.kategorie import kategorie_blueprint
from controllers.stellplatz import stellplatz_blueprint
from model.models import db
from controllers.index import index_blueprint

from flask_wtf.csrf import CSRFProtect

import sqlalchemy
app = Flask(__name__)
app.secret_key = "VerySecretSecretKey"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/INFI_Project_21"

csrf = CSRFProtect(app)

db.init_app(app)

#hier blueprint registrieren
app.register_blueprint(index_blueprint)
app.register_blueprint(autos_blueprint)
app.register_blueprint(kategorie_blueprint)
app.register_blueprint(stellplatz_blueprint)

app.run(debug=True)
