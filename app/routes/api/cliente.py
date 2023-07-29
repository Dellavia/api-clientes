from flask_restx import Resource
from app.routes.api import api
from app.extensions.apitoken import token_required, auth
from app.models import Cliente


ns = api.namespace('cliente', description='Informações de clientes', authorizations=auth)


@ns.route('/<string:cnpj_cpf>')
@ns.param('cnpj_cpf', 'CNPJ ou CPF do cliente solicitado')
class ClienteRes(Resource):
    @ns.doc(security='apikey')
    @token_required
    def get(self, cnpj_cpf):
        '''Busca informações de cliente pela sua chave'''
        cliente = Cliente.query.get(cnpj_cpf)
        code = 200

        if cliente:
            cliente = cliente.to_dict()
        else:
            cliente = {}
            code = 404

        return cliente, code

