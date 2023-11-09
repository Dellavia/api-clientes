from app.extensions import db
from app.models.base_model import BaseModel


class Cliente(BaseModel):
    id = db.Column(db.String(14), primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    ddd = db.Column(db.String(3))
    telefone = db.Column(db.String(25))
    endereco = db.Column(db.String(100))
    bairro = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    estado = db.Column(db.String(2))
    cep = db.Column(db.String(9))
    sexo = db.Column(db.String(1))
    ult_compra = db.Column(db.String(8))
    dt_nascimento = db.Column(db.String(8))


    def __repr__(self):
        return f'<User "{self.id}">'
