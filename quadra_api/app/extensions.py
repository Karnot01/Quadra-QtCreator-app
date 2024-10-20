from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# Creamos una instancia llamada "db" la cual nos ayudará a establecer conexión con la base de datos
db = SQLAlchemy()

# Creamos una instancia de JWT
jwt = JWTManager()