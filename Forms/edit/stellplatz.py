from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, HiddenField
from wtforms.fields import IntegerField
from wtforms import DateField


class EditStellplatz(FlaskForm):
    StellplatzId = HiddenField("StellplatzId")
    KategorieId = IntegerField("KategorieId")
    Kategorie = StringField("Kategorie")
    Qualitaet = IntegerField("Videoueberwachung")
    Laenge = StringField("Versicherung")
    Breite = StringField("Breite")
    Hoehe = StringField("Hoehe")
