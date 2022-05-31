from flask import Blueprint
import sqlalchemy

from forms.ProductDeleteForm import ProductDeleteForm
from forms.ProductForm import ProductForm
from model.models import Auto

products_blurprint = Blueprint('products_blueprint', __name__)
