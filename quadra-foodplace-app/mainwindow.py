import sys
import requests
import json

from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow

from routes import RouteManager
from helpers import url_api

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.route_manager = RouteManager()
        self.ui.boton_inicio.clicked.connect(self.iniciar_sesion)
        self.ui.boton_registro.clicked.connect(self.ir_a_registro)
        # Usar una sesión de requests para mejorar el rendimiento
        self.session = requests.Session()

    def iniciar_sesion(self):
        # Ruta completa de login de la API
        url_login = f'{url_api}/usuarios/login'

        # Obtener datos de los inputs
        email = self.ui.input_email.text().strip()
        password = self.ui.input_pass.text().strip()

        # Validación básica antes de hacer la solicitud
        if not email or not password:
            self.ui.texto_error.setText("Por favor, ingrese un correo y contraseña válidos.")
            return

        # Información a enviar
        info_a_enviar = {
            'email': email,
            'password': password
        }

        try:
            # Enviar solicitud a la API
            response = self.session.post(url_login, data=info_a_enviar)

            # Manejo del código de respuesta HTTP
            if response.status_code == 200:
                self.procesar_respuesta_ok(response)
            elif response.status_code == 401:
                self.manejar_error_autenticacion(response)
            else:
                self.ui.texto_error.setText(f"Error en la solicitud: Código {response.status_code}")

        except requests.exceptions.RequestException as e:
            # Error en la conexión
            self.ui.texto_error.setText("Error en la conexión con el servidor")
            print(f"Error en la conexión: {e}")

    def procesar_respuesta_ok(self, response):
        try:
            # Verificar que la respuesta es JSON y procesarla
            respuesta_decodificada = response.json()  # Esto lanza un ValueError si no es un JSON
        except ValueError as e:
            print(f"Error al decodificar JSON: {e}")
            self.ui.texto_error.setText("Error al procesar la respuesta del servidor")
            return

        # Verificar si el token está presente
        if 'Token' in respuesta_decodificada:
            token = respuesta_decodificada['Token']
            print('Sesión iniciada correctamente')
            self.route_manager.mandar_a_principal(self, token)
        else:
            print('Respuesta inesperada del servidor')
            self.ui.texto_error.setText('Respuesta inesperada del servidor')

    def manejar_error_autenticacion(self, response):
        try:
            respuesta_decodificada = response.json()
            # Mostrar el mensaje de error proporcionado por la API
            error_mensaje = respuesta_decodificada.get('Error', 'Error desconocido')
            print(f"Error de autenticación: {error_mensaje}")
            self.ui.texto_error.setText(error_mensaje)
        except json.JSONDecodeError:
            print("Error al decodificar el mensaje de error")
            self.ui.texto_error.setText('El correo o contraseña son incorrectos')

    # Método para ir a la ventana de registro
    def ir_a_registro(self):
        # Redirige a la ventana de registro
        self.route_manager.mandar_a_registro(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
