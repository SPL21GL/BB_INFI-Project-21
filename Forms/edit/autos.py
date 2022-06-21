from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, HiddenField
from wtforms.fields import IntegerField
from wtforms import DateField


class EditAuto(FlaskForm):
    AutoId = HiddenField("AutoId")
    Kategorie = StringField("Kategorie")
    Kennzeichen = StringField("Kennzeichen")
    Laenge = IntegerField("Laenge")
    Breite = IntegerField("Breite")
    Hoehe = IntegerField("Hoehe")
