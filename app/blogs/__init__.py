from flask import Blueprint

blog = Blueprint('blogs', __name__, url_prefix='/blog')

from . import views
