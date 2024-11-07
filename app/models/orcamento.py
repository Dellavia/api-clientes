from app.extensions import db
from app.models.base_model import BaseModel


class Orcamento(BaseModel):
    id = db.Column(db.String(6), primary_key=True)
    emissao = db.Column(db.String(8))
    operador = db.Column(db.String(6))
    loja = db.Column(db.String(2))
    dtemisnf = db.Column(db.String(8))
    vlrbruto = db.Column(db.Float)

    def __repr__(self):
        return f'<Orcamento "{self.id}">'
