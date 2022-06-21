from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, HiddenField
from wtforms.fields import IntegerField
from wtforms import DateField


class EditKategorie(FlaskForm):
    KategorieId = HiddenField("KategorieId")
    Kategoriename = StringField("Kategoriename")
    Preis = IntegerField("Preis")
    Videoueberwachung = IntegerField("Videoueberwachung")
    Versicherung = StringField("Versicherung")
    Farbe = StringField("Farbe")
