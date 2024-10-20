# Importamos la instancia de nuestra DB 
from app.extensions import db

class Comentario(db.Model):
    __tablename__ = 'comentario'
    id_comentario = db.Column(db.Integer, primary_key=True)
    comentario = db.Column(db.String(500), nullable=False)
    fecha_comentario = db.Column(db.TIMESTAMP, nullable=False, default=db.func.now())
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    id_puesto = db.Column(db.Integer, db.ForeignKey('puesto_de_comida.id'), nullable=False)

    def __repr__(self):
        return f'<Comentario {self.texto}>'
