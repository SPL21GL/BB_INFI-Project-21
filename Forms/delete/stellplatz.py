from flask_wtf import FlaskForm
from wtforms.fields import IntegerField


class DeleteStellplatz(FlaskForm):
    StellplatzId = IntegerField("StellplatzId")
