from app.extensions import db


class Cliente(db.Model):
    id = db.Column(db.String(14), primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    telefone = db.Column(db.String(25))
    endereco = db.Column(db.String(100))
    bairro = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    estado = db.Column(db.String(2))
    cep = db.Column(db.String(9))
    sexo = db.Column(db.String(1))
    ult_compra = db.Column(db.String(8))


    def __repr__(self):
        return f'<User "{self.id}">'

    def to_dict(self):
        dict = {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone,
            "endereco": self.endereco,
            "bairro": self.bairro,
            "cidade": self.cidade,
            "estado": self.estado,
            "cep": self.cep,
            "sexo": self.sexo,
            "ult_compra": self.ult_compra
            }
        return dict
