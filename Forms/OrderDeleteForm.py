from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import StringField
from wtforms.fields
from wtforms import validators

class OrderDeleteForm(FlaskForm):
    orderNumber = StringField("orderNumber")
