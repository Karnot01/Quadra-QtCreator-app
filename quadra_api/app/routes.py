# En el archivo routes vamos a tener las rutas (paths) que el servidor va a poder manejar

from flask import request # Libería que nos permite interceptar la info del usuario
from flask_restful import Resource
from .methods import * # Importamos los métodos de nuestra API
from flask_jwt_extended import jwt_required, get_jwt_identity

# Creamos un recurso que nuestra aplicación puede cargar (METODO)
class HolaMundo(Resource):
    # Este método se ejecuta cuando el usuario lo llama con un GET
    @jwt_required()
    def get(self):
        identidad = get_jwt_identity()
        return { 'message': f'Hola {identidad} bienvenido', 'status':200 }

class User_register(Resource):
    # Como el usuario envia información utlizamos un POST
    def post(self):
        # Informacion que el usuario envia a través del post
        data = request.form
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        respuesta, status = user_register(username, email, password)

        return respuesta, status
    
class User_login(Resource):
    def post(self):
        data = request.form
        email = data.get('email')
        password = data.get('password')

        respuesta, status = inicio_sesion(email, password)

        return respuesta, status
    
class PuestoDeComida(Resource):
    def post(self):
        # Usar request.json para recibir datos en formato JSON
        data = request.get_json(silent=True)
        print(f"Datos recibidos: {data}")  # Agregar impresión para depurar

        if data is None:
            return {'Error': 'La solicitud debe ser en formato JSON'}, 400

        # Extraer los datos correctamente desde el JSON
        nombre_puesto = data.get('nombre_puesto')
        ubicacion = data.get('ubicacion')
        comentario = data.get('comentario')
        foto = data.get('foto')
        id_usuario = data.get('id_usuario')

        print(f"Nombre puesto: {nombre_puesto}, Ubicacion: {ubicacion}, Usuario ID: {id_usuario}")  # Depurar campos recibidos

        # Validación de campos obligatorios
        if not nombre_puesto or not ubicacion or not id_usuario:
            return {'Error': 'Faltan campos obligatorios'}, 400
        
        # Llamamos a la función que registra el puesto de comida
        response, status = registrar_puesto_de_comida(nombre_puesto, ubicacion, comentario, foto, id_usuario)
        return response, status

# Clase que se va a encargar de agregar rutas a los recursos
class APIRoutes:
    def init_api(self, api):
        api.add_resource(HolaMundo, '/')  # Ruta raíz
        api.add_resource(User_register, '/usuarios/registro')
        api.add_resource(User_login, '/usuarios/login')
        api.add_resource(PuestoDeComida, '/puesto')
        