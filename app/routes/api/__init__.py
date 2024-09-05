from flask import Blueprint
from flask_restx import Api

bp = Blueprint('api', __name__)
api = Api(bp,
          version='1.0',
          title='API Dellavia',
          description='Disponibilizar informações para aplicação externas')

import app.routes.api.cliente
import app.routes.api.orcamento
import app.routes.api.pesquisa