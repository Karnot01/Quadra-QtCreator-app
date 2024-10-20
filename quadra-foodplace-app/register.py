import sys
import requests

from PySide6.QtWidgets import QApplication, QMainWindow
from ui_register import Ui_RegisterWindow
from routes import RouteManager
from helpers import url_api

class RegisterWindow(QMainWindow):
    def __init__(self, correo_usuario, parent=None):
        super().__init__(parent)
        self.correo_usuario = correo_usuario
        self.ui = Ui_RegisterWindow()
        self.ui.setupUi(self)

        # Asignar el correo a la etiqueta de la interfaz
        self.ui.captura_mail.setText(self.correo_usuario)

        # Inicializamos el manejador de rutas
        self.route_manager = RouteManager()

        # Conectar el botón de crear cuenta al método
        self.ui.crear_cuenta.clicked.connect(self.capturar_info)

    def capturar_info(self):
        username = self.ui.captura_username.text().strip()
        email = self.ui.captura_mail.text().strip()
        password = self.ui.captura_pass.text()
        password_confirm = self.ui.captura_pass_confirm.text()

        # Validaciones de los campos
        if not username or not email or not password or not password_confirm:
            self.mostrar_error('Faltan completar campos')
            return
        elif not self.validar_email(email):
            self.mostrar_error('Ingresa un correo válido')
            return
        elif password != password_confirm:
            self.mostrar_error('Las contraseñas no coinciden')
            return

        # Llamar al método para crear el usuario
        self.crear_usuario(username, email, password)

    def mostrar_error(self, mensaje):
        """Muestra el mensaje de error en la interfaz."""
        print(mensaje)
        self.ui.alerta_error.setText(mensaje)

    def validar_email(self, email):
        """Validar el formato básico del correo."""
        return "@" in email and "." in email

    def crear_usuario(self, username, email, password):
        url = f'{url_api}/usuarios/registro'
        informacion_user = {
            'username': username,
            'email': email,
            'password': password
        }

        print('Se está creando un nuevo usuario...')

        try:
            response = requests.post(url, data=informacion_user)
            # Verificar si la solicitud fue exitosa
            if response.status_code == 200:
                respuesta_decodificada = response.json()
                self.procesar_respuesta(respuesta_decodificada)
            else:
                self.mostrar_error(f'Error en la solicitud: {response.status_code}')
        except requests.exceptions.RequestException as e:
            self.mostrar_error('Error al conectar con el servidor')
            print(f"Error de red: {e}")

    def procesar_respuesta(self, respuesta_decodificada):
        """Procesa la respuesta del servidor."""
        if 'Error' in respuesta_decodificada:
            self.mostrar_error("Ese correo ya está registrado")
        elif 'Nuevo usuario' in respuesta_decodificada:
            print('Se creó nuevo usuario correctamente')
            self.route_manager.mandar_a_login(self)
        else:
            self.mostrar_error('Error interno del servidor')

# Método de entrada principal para ejecutar la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = RegisterWindow(correo_usuario="")  # Se requiere pasar un correo al inicializar
    widget.show()
    sys.exit(app.exec())
