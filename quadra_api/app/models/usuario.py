from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)  # Hacemos que el email sea único
    password = db.Column(db.String(255), nullable=False)  # Ajustamos el tamaño de la columna
    fecha_registro = db.Column(db.TIMESTAMP, nullable=False)

    def __repr__(self):
        return f'<Usuario {self.username}>'  # Ajuste en la representación

    def set_password(self, password):
        # Genera y almacena el hash de la contraseña
        self.password = generate_password_hash(password)

    def check_password(self, password):
        # Compara la contraseña proporcionada con el hash almacenado
        return check_password_hash(self.password, password)

    @classmethod
    def get_user_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()  # Volvemos atrás si hay algún error
            raise e

    def delete(self):
        try:
            db.session.delete(self)  # Eliminamos el usuario en lugar de agregarlo
            db.session.commit()
        except Exception as e:
            db.session.rollback()  # Volvemos atrás si hay algún error
            raise e
