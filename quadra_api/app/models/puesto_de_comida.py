# Importamos la instancia de nuestra DB 
from app.extensions import db
from geoalchemy2.types import Geometry

class PuestoDeComida(db.Model):
    __tablename__ = 'puesto_de_comida'
    id_puesto = db.Column(db.Integer, primary_key=True)
    nombre_puesto = db.Column(db.String(100), nullable=False)
    ubicacion = db.Column(Geometry(geometry_type='POINT', srid=4326))
    comentario = db.Column(db.Text, nullable=False)
    foto = db.Column(db.String(255), nullable=False)
    fecha_creacion = db.Column(db.TIMESTAMP, nullable=False, default=db.func.now())
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)

    def __repr__(self):
        return f'<Puesto_de_comida {self.nombre_puesto}>'