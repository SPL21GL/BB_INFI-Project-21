from flask_wtf import FlaskForm
from wtforms.fields import IntegerField


class DeleteKategorie(FlaskForm):
    KategorieId = IntegerField("KategorieId")
