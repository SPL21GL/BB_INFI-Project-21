from flask_wtf import FlaskForm
from wtforms.fields import IntegerField


class DeleteAuto(FlaskForm):
    AutoId = IntegerField("AutoId")
