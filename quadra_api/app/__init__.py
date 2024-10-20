# Se va a encargar de montar el servidor
# flask es una librería
# Flask con mayúscula es el módulo

from flask import Flask  # Nos permite crear el servidor
from flask_restful import Api # Crear la funcionalidad del API
from .routes import APIRoutes # Cuando queremos importar un archivo se usa punto
from .config import Config # Desde el archivo config importamos la clase "Config"
from .extensions import db, jwt # Desde el archivo extensions importamos la clase "db"

# Creamos una función que configure el servidor
def configurar_app():
    # Variable que va a almacenar el servidor
    app = Flask(__name__)
    # Le indico a mi app que como archivo de configuración utlice config
    app.config.from_object(Config)
    # Le decimos a mi base de datos que se va a inicializar en nuestra app
    db.init_app(app)
    # Conectamos la App con JWT
    jwt.init_app(app)
    # Manejador que se ejecuta mientras el servidor se esta montando
    with app.app_context():
        # Inicializa todas las tablas de nuestra base de datos
        db.create_all()
        # Variable que va almacenar la API
        # Le indicamos sobre que servidor va a interactuar
        api = Api(app)
        # Configuramos las rutas y los recursos
        routes = APIRoutes()
        routes.init_api(api)

    # Regresamos ese servidor montado
    return app