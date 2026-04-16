from app.extensions import db


class Service(db.Model):
    __tablename__ = 'service'

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(255), nullable = False)
    descricao = db.Column(db.String(256), nullable = False)
    preco_base = db.Column(db.Integer, nullable = False)

class ServiceOrder(db.Model):
    __tablename__ = 'service_order'

    id = db.Column(db.Integer, primary_key = True)
    descricao = db.Column(db.String(256), nullable = False)
    status = db.Column(db.Boolean, nullable = False)
    service_id = db.Column(db.ForeignKey('service.id'), nullable = False)
