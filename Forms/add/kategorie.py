from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms import IntegerField, DateField


class AddKategorie(FlaskForm):
    Kategoriename = StringField("Kategoriename")
    Preis = IntegerField("Preis")
    Videoueberwachung = IntegerField("Videoueberwachung")
    Versicherung = StringField("Versicherung")
    Farbe = StringField("Versicherung")
