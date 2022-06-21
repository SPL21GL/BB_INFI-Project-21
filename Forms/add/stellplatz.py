from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms import IntegerField, DateField


class AddStellplatz(FlaskForm):
    KategorieId = IntegerField("KategorieId")
    Qualitaet = StringField("Qualitaet")
    Laenge = StringField("Laenge")
    Breite = StringField("Breite")
    Hoehe = StringField("Hoehe")