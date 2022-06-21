from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms import IntegerField, DateField


class AddAuto(FlaskForm):
    Kategorie = StringField("Kategorie")
    Kennzeichen = StringField("Kennzeichen")
    Laenge = IntegerField("Laenge")
    Breite = IntegerField("Breite")
    Hoehe = IntegerField("Hoehe")