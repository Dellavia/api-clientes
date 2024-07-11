from flask_restx import Resource
from app.routes.api import api
from app.extensions import token_required, auth
from app.models import Orcamento


ns = api.namespace('orcamento', description='Valida existencia de orçamento no Call Center', authorizations=auth)


@ns.route('/<string:emissao>/<string:num_orc>')
@ns.param('emissao', 'Data da emissão do orçamento')
@ns.param('num_orc', 'Numero do orçamento')
class OrcamentoRes(Resource):
    @ns.doc(security='apikey')
    @token_required
    def get(self, emissao, num_orc):
        '''Busca orçamento pela data e numero'''
        orcamento = Orcamento.query.filter_by(id=num_orc).filter(Orcamento.emissao >= emissao).first()
        code = 200

        if orcamento:
            orcamento = orcamento.to_dict()
        else:
            orcamento = {}
            code = 404

        return orcamento, code

