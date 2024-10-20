import sys
from PySide6.QtWidgets import QLabel, QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtGui import QPixmap, Qt, QMouseEvent
from helpers import load_token, obtener_usuario_token, token_is_valid, url_api, delete_token
from routes import RouteManager
import requests
from ui_RegisterFoodPlace import Ui_RegisterFoodPlaceWindow

class ClickableLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            # Aquí llamas a la función para subir la foto
            self.parent().subir_foto()

class RegisterFoodPlaceWindow(QMainWindow):
    def __init__(self, nombre_usuario=None, parent=None):
        super().__init__(parent)

        # Inicializo mi administrador de rutas
        self.route_manager = RouteManager()

        # Si no se proporciona nombre_usuario, cargarlo desde el token
        if nombre_usuario is None:
            token_actual = load_token()
            self.nombre_usuario = obtener_usuario_token(token_actual)
        else:
            self.nombre_usuario = nombre_usuario

        # Este atributo contendrá todo el apartado gráfico
        self.ui = Ui_RegisterFoodPlaceWindow()
        # Lo inicializamos el apartado gráfico
        self.ui.setupUi(self)

        # Reemplazar el QLabel por ClickableLabel
        self.ui.subir_foto = ClickableLabel(self)
        self.ui.subir_foto.setText("Haz clic para subir una foto")
        self.ui.subir_foto.setAlignment(Qt.AlignCenter)

        # Conectar botones a funciones
        self.ui.boton_cerrar.clicked.connect(self.cerrar_sesion)
        self.ui.crear_puesto.clicked.connect(self.crear_puesto)

        self.current_photo = None  # Para almacenar la ruta de la foto seleccionada

    def subir_foto(self):
        """Diálogo para seleccionar una imagen y mostrarla en el QLabel."""
        photo_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar Foto", "", "Images (*.png *.jpg *.jpeg)")
        if photo_path:
            # Cargar la imagen seleccionada en el QLabel
            pixmap = QPixmap(photo_path)

            self.ui.subir_foto.setPixmap(pixmap)
            self.current_photo = photo_path  # Guardar la ruta de la foto actual
        else:
            QMessageBox.warning(self, "Error", "No se seleccionó ninguna foto.")

    def captura_nombre_puesto(self):
        """Captura el nombre del puesto."""
        nombre_puesto = self.ui.captura_nombre_puesto.text().strip()  # Obtener el texto del campo de nombre
        if not nombre_puesto:
            QMessageBox.warning(self, "Error", "Por favor ingrese un nombre para el puesto.")
        else:
            print(f"Nombre del puesto capturado: {nombre_puesto}")

    def subir_ubicacion(self):
        """Captura la ubicación del puesto de comida."""
        ubicacion = self.ui.subir_ubicacion.text().strip()  # Obtener el texto del campo de ubicación
        if not ubicacion:
            QMessageBox.warning(self, "Error", "Por favor ingrese la ubicación del puesto.")
        else:
            print(f"Ubicación del puesto capturada: {ubicacion}")

    def subir_comentarios(self):
        """Captura los comentarios para el puesto."""
        comentarios = self.ui.subir_comentarios.toPlainText().strip()  # Obtener el texto del campo de comentarios
        if not comentarios:
            QMessageBox.warning(self, "Error", "Por favor ingrese comentarios para el puesto.")
        else:
            print(f"Comentarios capturados: {comentarios}")

    def crear_puesto(self):
        """Lógica para crear un nuevo puesto de comida."""
        nombre_puesto = self.ui.nombre_puesto.text().strip()
        ubicacion = self.ui.ubicacion.text().strip()
        comentarios = self.ui.comentarios.text().strip()

        # Verificar que se hayan ingresado todos los datos
        if not nombre_puesto or not ubicacion or not comentarios or not self.current_photo:
            QMessageBox.warning(self, "Error", "Por favor complete todos los campos y suba una foto.")
            return

        # Enviar la solicitud POST a la API para crear el puesto
        token_actual = load_token()
        headers = {"Authorization": f"Bearer {token_actual}"}
        data = {
            "nombre": nombre_puesto,
            "ubicacion": ubicacion,
            "comentarios": comentarios
        }
        try:
            response = requests.post(f"{url_api}/puesto", json=data, headers=headers)
            if response.status_code == 201:
                QMessageBox.information(self, "Éxito", "Puesto de comida creado exitosamente.")
                self.mandar_a_principal()  # Redirigir a la página principal
            else:
                QMessageBox.warning(self, "Error", f"Error al crear el puesto: {response.status_code}")
        except requests.RequestException as e:
            QMessageBox.warning(self, "Error", f"Error de conexión: {e}")

    def eliminar_sesion(self, token_actual):
        """Elimina la sesión y el token, tanto local como remotamente."""
        headers = {"Authorization": f"Bearer {token_actual}"}
        try:
            response = requests.post(f"{url_api}/cerrar_sesion", headers=headers)
            if response.status_code == 200:
                delete_token()  # Eliminar el token local
                print("Sesión cerrada y token eliminado correctamente.")
            else:
                print(f"Error al cerrar sesión: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error de conexión: {e}")
        except Exception as e:
            print(f"Error inesperado al intentar cerrar sesión: {e}")

    def cerrar_sesion(self):
        """Cerrar la sesión actual y eliminar el token."""
        try:
            print("Cerrando sesión")
            token_actual = load_token()
            self.eliminar_sesion(token_actual)
            self.route_manager.mandar_a_login(ventana_anterior=self)  # Mandar al usuario a la pantalla de login

        except Exception as e:
            print(f"Error inesperado al intentar cerrar sesión: {e}")

    def dirigir_a_login(self, ventana_anterior=None, token=None):
        """Dirigir al usuario al login si el token no es válido."""

        # Usar el token actual si no se proporciona uno
        if token is None:
            token = load_token()  # Cargar el token de la fuente que tengas configurada

        # Verificar si el token es válido
        if not token_is_valid(token):
            self.ui.mostrar_resultado.setText('Tu sesión ha expirado. Por favor, inicia sesión nuevamente.')
            self.route_manager.mandar_a_login(ventana_anterior=ventana_anterior)

    # Método para mandar a la página principal
    def mandar_a_principal(self):
        print("Redirigiendo a la página principal")
        try:
            # Mandamos al usuario a pantalla principal
            self.route_manager.mandar_a_principal()
        except AttributeError as e:
            print(f"Error: No se pudo acceder al método de registro: {e}")
        except Exception as e:
            print(f"Error inesperado al intentar redirigir al registro: {e}")

# Método mágico para inicializar la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegisterFoodPlaceWindow()
    window.show()
    sys.exit(app.exec())
