from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import StringField, TextAreaField
from wtforms.fields
from wtforms import validators

class ProductDeleteForm(FlaskForm):
    productCode = StringField("productCode",  [validators.InputRequired()])