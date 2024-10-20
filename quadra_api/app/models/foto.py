# Importamos la instancia de nuestra DB 
from app.extensions import db

class Foto(db.Model):
    __tablename__ = 'foto'
    id_foto = db.Column(db.Integer, primary_key=True)
    foto = db.Column(db.String(255), nullable=False)
    id_puesto = db.Column(db.Integer, db.ForeignKey('puesto_de_comida.id'), nullable=False)  # Clave foránea corregida

    def __repr__(self):
        return f'<Foto {self.url_foto}>'  # Corregido
