# Importamos la instancia de nuestra DB 
from app.extensions import db

class Calificacion(db.Model):
    __tablename__ = 'calificacion'
    id_calificacion = db.Column(db.Integer, primary_key=True)
    puntuacion = db.Column(db.Numeric(3,1), nullable=False)  
    fecha_calificacion = db.Column(db.TIMESTAMP, nullable=False, default=db.func.now())
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    id_puesto = db.Column(db.Integer, db.ForeignKey('puesto_de_comida.id'), nullable=False)

    def __repr__(self):
        return f'<Calificacion {self.puntuacion}>'
