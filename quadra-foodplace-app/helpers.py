# Este archivo contendrá funciones que se estarán ejecutando muy seguido en el código
# Methods - Helpers - Extensions - Manejadores

import jwt
import os # Crear un archivo en el proyecto
import datetime # Determinar si mi token sigue vigente

token_file_path = 'token.txt' # Archivo donde se va almacenar el token

url_api = 'https://479c-109-178-234-7.ngrok-free.app'

def save_token(token):
    # Abrimos el archivo donde se va a almacenar el token en modo de escritura
    with open(token_file_path, 'w') as file:
        # Se escribe lo que contenga token
        file.write(token)

def load_token():
    # Determinamos si el archivo token.txt existe
    if os.path.exists(token_file_path):
        # Abrimos el archivo txt en modo de lectura
        with open(token_file_path, 'r') as file:
            # Se lee lo que contenga el archivo
            return file.read()
    else:
        # Que el archivo con el token no existe
        return None

# Función para validar token
def token_is_valid(token):
    # Obtengo el payload del token
    info_token = decode_token(token)
    # Obtenemos el tiempo de expiración
    expiration = datetime.datetime.fromtimestamp(info_token['exp'])

    # Token válido = True
    # Token expirado = False
    return expiration > datetime.datetime.now()

def delete_token():
    # Abrimos el archivo que queremos reescribir
    with open(token_file_path, 'w') as file:
        # Borrar el contenido
        file.write('') # Reescribe el documento con un string vacio

# Función para desencriptar el payload del token
def decode_token(token):
    payload = jwt.decode(token, options={'verify_signature': False})

    return payload

def obtener_usuario_token(token):
    # Obtenemos la información del payload del token
    info_user = decode_token(token)
    # Retornamos el nombre
    return info_user['sub']
