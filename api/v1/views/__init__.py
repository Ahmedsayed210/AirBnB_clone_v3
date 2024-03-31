
from api.v1.views.index import *
from flask import Blueprints

app_views = Blueprints('app_views', __name__, url_prefix='/api/v1')
