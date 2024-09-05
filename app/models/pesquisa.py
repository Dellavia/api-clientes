from app.extensions import db
from app.models.base_model import BaseModel


class Pesquisa(BaseModel):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    loja = db.Column(db.String(2)) 
    cpf = db.Column(db.String(14))
    telefone = db.Column(db.String(25))
    aval = db.Column(db.Integer)
    referencia = db.Column(db.String(25))
    date_time = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<Pesquisa "{self.id}">'
