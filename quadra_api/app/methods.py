from flask import jsonify
from app.extensions import db
from .models.puesto_de_comida import PuestoDeComida
from .models.usuario import User
from flask_jwt_extended import create_access_token
from datetime import timedelta
from geoalchemy2.elements import WKBElement

def inicio_sesion(email, password):
    # Nos asegura que el usuario efectivamente esté registrado en la DB
    user = User.get_user_by_email(email=email)
    # Tiempo en el que el token expira
    caducidad = timedelta(minutes=120)
    # Si user es None y la contraseña hasheada coincide con la DB
    if user and (user.check_password(password=password)):
        # Creamos un token de acceso
        token_acceso = create_access_token(identity = user.nombre_usuario, expires_delta = caducidad)
        return { 'Mensaje': 'Sesión iniciada', 'Token': token_acceso }, 200
    
    return { 'Error': 'Correo o contraseña incorrectos' }, 401

def user_register(nombre_usuario, email, password):
    user = User.get_user_by_email(email=email)
    # Si el usuario ya esta registrado, regresamos un error
    if user is not None:
        return { 'Error': 'Este correo  ya esta registrado' }, 403
    
    # Se crea un objeto de tipo "User" con el username y el correo
    nuevo_usuario = User(nombre_usuario=nombre_usuario, email=email)
    # A ese objeto se le asigna una contraseña
    nuevo_usuario.set_password(password=password) # Contraseña cifrada
    # Guardamos el user en la DB
    nuevo_usuario.save()

    return { 'Nuevo usuario': {
        'email': email,
        'nombre_usuario': nombre_usuario
      }
    }, 200 # Le damos una respuesta satisfactoria al usuario

def convertir_a_wkt(ubicacion):
    # Asegurarse de que ubicacion es un WKBElement antes de convertir
    if isinstance(ubicacion, WKBElement):
        try:
            return ubicacion.wkt  # Convertir a Well-Known Text (WKT)
        except AttributeError as e:
            print(f"Error al acceder a WKT: {str(e)}")
            return {'Error': 'La ubicación no se pudo convertir a WKT'}
    else:
        print(f"Ubicación no es WKBElement, es {type(ubicacion)}")
        return {'Error': 'Tipo de ubicación no compatible'}

# Esta función busca un puesto de comida en la DB por nombre y por el navegador de botones "anterior y siguiente"
def buscar_puesto_de_comida(id_puesto=None, nombre_puesto=None):  
    # Verificar si el usuario mandó como Query el ID
    if id_puesto is not None:
        # Obtenemos el producto desde nuestra DB a través del ID 
        puesto_obtenido = PuestoDeComida.query.get_or_404(id_puesto)

        # Convertir ubicación a WKT
        ubicacion_wkt = convertir_a_wkt(puesto_obtenido.ubicacion)

        # Creamos un JSON donde mostramos los datos del elemento
        return {
            'ID': puesto_obtenido.id_puesto,
            'Nombre': puesto_obtenido.nombre_puesto,
            'Ubicacion': puesto_obtenido.ubicacion,
            'Reseña': puesto_obtenido.comentario,
            'Foto': puesto_obtenido.foto,
            'Fecha': puesto_obtenido.fecha_creacion,
            'Usuario': puesto_obtenido.id_usuario
        }
        return jsonify(respuesta)  # Usar jsonify para evitar problemas de serialización automática
    
    # Verificar si el usuario mandó como Query el nombre
    elif nombre_puesto is not None:
        # Buscamos un producto por su nombre y mostramos
        puesto_obtenido = PuestoDeComida.query.filter_by(nombre=nombre_puesto).first()
        if puesto_obtenido:
            ubicacion_wkt = convertir_a_wkt(puesto_obtenido.ubicacion)

            return {
                'ID': puesto_obtenido.id_puesto,
                'Nombre': puesto_obtenido.nombre_puesto,
                'Ubicacion': puesto_obtenido.ubicacion,
                'Reseña': puesto_obtenido.comentario,
                'Foto': puesto_obtenido.foto,
                'Fecha': puesto_obtenido.fecha_creacion,
                'Usuario': puesto_obtenido.id_usuario
            }
            return jsonify(respuesta)  # Usar jsonify para serializar la respuesta
            
        else:
            return jsonify({'Error': 'Producto no encontrado'}), 404
    
    return jsonify({'Error': 'No pusiste ninguna Query'}), 400
    
def registrar_puesto_de_comida(nombre_puesto, ubicacion, comentario, foto, usuario_id):
    # Depuración de los valores recibidos
    print(f"Nombre puesto: {nombre_puesto}")
    print(f"Ubicacion: {ubicacion}")
    print(f"Usuario ID: {usuario_id}")
    
    # Validaciones básicas de los campos
    if not nombre_puesto or not ubicacion or not usuario_id:
        return {'Error': 'Faltan campos obligatorios'}, 400
    
    # Verificamos que el usuario exista
    usuario = User.query.get(usuario_id)
    if not usuario:
        return {'Error': 'Usuario no encontrado'}, 404
    
    # Convertir la ubicación de WKT (cadena) a un objeto Geometry (Point)
    try:
        # Verificar si la cadena de WKT tiene el formato correcto
        if not ubicacion.startswith("POINT("):
            print(f"Ubicación no tiene el formato esperado: {ubicacion}")
            return {'Error': 'Formato de ubicación no válido'}, 400

        # Intentar convertir la cadena WKT a un WKTElement con SRID 4326
        ubicacion_geometria = WKTElement(ubicacion, srid=4326)
        print(f"Ubicación convertida a geometría: {ubicacion_geometria}")
    except Exception as e:
        print(f"Error al convertir la ubicación: {str(e)}")
        return {'Error': 'Formato de ubicación no válido'}, 400
    
    # Creamos el nuevo puesto de comida
    nuevo_puesto = PuestoDeComida(
        nombre_puesto=nombre_puesto, 
        ubicacion=ubicacion_geometria, 
        comentario=comentario,  # La reseña
        foto=foto,
        id_usuario=usuario.id_usuario  # Usar 'id_usuario' en lugar de 'id'
    )
    
    try:
        # Guardamos el puesto en la base de datos
        db.session.add(nuevo_puesto)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return {'Error': f'Error al registrar el puesto de comida: {str(e)}'}, 500
    
    # Convertir la ubicación a WKT antes de devolver la respuesta
    ubicacion_wkt = convertir_a_wkt(nuevo_puesto.ubicacion)

    # Validar si ocurrió un error al convertir la ubicación
    if isinstance(ubicacion_wkt, dict) and 'Error' in ubicacion_wkt:
        return ubicacion_wkt, 500  # Devolver el error si la conversión falló
    
    # Crear la respuesta con la ubicación convertida
    return {
        'ID': nuevo_puesto.id_puesto,
        'Nombre': nuevo_puesto.nombre_puesto,
        'Ubicacion': ubicacion_wkt,  # Ubicación convertida a WKT
        'Comentario': nuevo_puesto.comentario,
        'Foto': nuevo_puesto.foto,
        'Fecha': nuevo_puesto.fecha_creacion,
        'Usuario': nuevo_puesto.id_usuario
    }, 201