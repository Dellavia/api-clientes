from flask_restx import Resource, fields
from app.routes.api import api
from app.extensions import db
from app.models import Pesquisa

ns = api.namespace('pesquisa', description='Recebe resultado da pesquisa de satisfacao')
pesq_model = api.model('Pesquisa', { \
    'loja': fields.String(required=True, description='Loja onde ocorreu o atendimento'),
    'cpf': fields.String(required=True, description='CPF do cliente'),
    'tel': fields.String(required=True, description='Telefone celular do cliente'),
    'aval': fields.Integer(required=True, description='Avaliacao do atendimento'),
    'referencia': fields.String(required=True, description='Onde ou como conheceu a Dellavia')
})


@ns.route('/', methods=['POST'])
class PesquisaRes(Resource):
    @ns.expect(pesq_model)
    def post(self):
        '''Grava resultado da pesquisa de satisfacao'''

        code = 201
        result = api.payload

        pesquisa = Pesquisa(loja=result["loja"], \
                            cpf=result["cpf"], \
                            telefone=result["tel"], \
                            aval=result["aval"], \
                            referencia=result["referencia"])

        db.session.add(pesquisa)
        db.session.commit()

        return code

