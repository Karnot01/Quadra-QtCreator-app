import sys
from PySide6.QtWidgets import QLabel, QApplication, QMainWindow
from PySide6.QtGui import QPixmap, Qt, QMouseEvent
from helpers import load_token, obtener_usuario_token, token_is_valid, url_api, delete_token
from routes import RouteManager

# Importamos la librería que nos permite manejar la API
import requests

# Importamos el apartado gráfico del archivo "register.ui"
from ui_principal import Ui_PrincipalWindow

class PrincipalWindow(QMainWindow):
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

        # Inicializo atributos
        self.fotos = []
        self.comentarios = []
        self.current_puesto_id = 1  # ID del puesto que se está mostrando
        self.current_index = 0

        # Este atributo contendrá todo el apartado gráfico
        self.ui = Ui_PrincipalWindow()
        # Inicializamos el apartado gráfico
        self.ui.setupUi(self)

        # Mostrar el correo del usuario en la etiqueta
        self.ui.mostrar_correo.setText(f'Bienvenido a Quadra: {self.nombre_usuario}')

        # Conectar botones a funciones
        self.ui.boton_buscar.clicked.connect(self.buscar_puesto_nombre)
        self.ui.boton_cerrar.clicked.connect(self.cerrar_sesion)
        self.ui.boton_siguiente.clicked.connect(self.mostrar_siguiente)
        self.ui.boton_anterior.clicked.connect(self.mostrar_anterior)
        self.ui.agregar_puesto.clicked.connect(self.registrar_puesto)
        self.ui.boton_perfil_puesto.clicked.connect(self.perfil_puesto)
        self.ui.mostrar_foto.setPixmap(QPixmap())  # Instancia vacía de QPixmap

        # Redirigir a la pantalla de login si el token no es válido
        self.dirigir_a_login(load_token())

    # Método para realizar peticiones GET a la API
    def hacer_peticion_get(self, url, headers):
        """Realiza una petición GET a la API y maneja errores."""
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as http_err:
            print(f"Error HTTP: {http_err}")
        except Exception as err:
            print(f"Error inesperado: {err}")
        return None

    # Método para cargar fotos y comentarios
    def cargar_fotos_y_comentarios(self):
        """Hace peticiones al API para cargar las fotos y comentarios del puesto actual."""
        try:
            # Definir las URLs para fotos y comentarios
            fotos_url = f"{url_api}/puestos/{self.current_puesto_id}/foto"
            comentarios_url = f"{url_api}/puestos/{self.current_puesto_id}/comentario"

            # Obtener el token actual para la autorización
            token_actual = load_token()
            headers = {"Authorization": f"Bearer {token_actual}"}

            # Petición para obtener las fotos
            respuesta_fotos_json = self.hacer_peticion_get(fotos_url, headers)
            if isinstance(respuesta_fotos_json, list):  # Verificamos si la respuesta es una lista
                self.fotos = [foto['url_foto'] for foto in respuesta_fotos_json]
            else:
                print("Error al obtener las fotos.")

            # Petición para obtener los comentarios
            respuesta_comentarios_json = self.hacer_peticion_get(comentarios_url, headers)
            if isinstance(respuesta_comentarios_json, list):  # Verificamos si la respuesta es una lista
                self.comentarios = [comentario['texto'] for comentario in respuesta_comentarios_json]
            else:
                print("Error al obtener los comentarios.")

        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

    # Método para buscar un puesto de comida a través de la API
    def buscar_puesto_nombre(self):
        """Busca un puesto de comida por nombre a través de la API y muestra el resultado en la interfaz."""
        try:
            # Obtener el texto ingresado en el buscador
            nombre_puesto = self.ui.buscador.text().strip() # Eliminar espacios en blanco
            if not nombre_puesto:
                self.ui.mostrar_resultado.setText('Por favor ingrese un nombre de puesto.')
                return

            # URL para buscar el puesto de comida por nombre
            url = f"{url_api}/puesto_de_comida?nombre={nombre_puesto}"

            # Obtener el token actual
            token_actual = load_token()

            # Configurar los headers con el token de autorización
            headers = {"Authorization": f"Bearer {token_actual}"}

            # Hacer la petición GET a la API
            respuesta_json = self.hacer_peticion_get(url, headers)

            # Verificar si la respuesta fue exitosa (código 200)
            if respuesta_json and "Nombre" in respuesta_json:
                # Mostrar el nombre del puesto
                self.ui.mostrar_resultado.setText(f'Nombre del puesto: {respuesta_json["Nombre"]}')

                # Si hay una foto disponible, mostrarla
                if "url_foto" in respuesta_json:
                    self.ui.mostrar_foto.setPixmap(QPixmap(respuesta_json["url_foto"]))
                else:
                    self.ui.mostrar_foto.clear()
            else:
                # Mostrar mensaje de que no se encontró el puesto
                self.ui.mostrar_resultado.setText('No se encontró ningún puesto de comida')
                self.ui.mostrar_foto.clear()

        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            self.ui.mostrar_resultado.setText('Ocurrió un error inesperado')
            self.ui.mostrar_foto.clear()

    def mostrar_foto_y_comentarios(self):
        """Muestra la foto y los comentarios actuales del puesto."""
        if not self.fotos or not self.comentarios:
            self.ui.label_foto.setText("No hay fotos o comentarios disponibles")
            return

        # Mostrar la foto actual
        foto_url = self.fotos[self.current_index]
        try:
            response = requests.get(foto_url)
            if response.status_code == 200:
                pixmap = QPixmap()
                pixmap.loadFromData(response.content)
                self.ui.mostrar_foto.setPixmap(pixmap)
            else:
                self.ui.mostrar_foto.setText("Error al cargar la foto")
        except Exception as e:
            print(f"Error al cargar la foto: {e}")
            self.ui.mostrar_foto.setText("Error al cargar la foto")

        # Actualizar comentarios
        self.lista_comentarios.clear()
        self.lista_comentarios.addItem(self.comentarios[self.current_index])

    def cambiar_foto(self, direccion):
        """Cambiar la foto actual y los comentarios en función de la dirección.."""
        if len(self.fotos) == 0:
            print("No hay fotos disponibles.")
            return # Salir de la función si no hay fotos

        if direccion == 'siguiente':
            self.current_index = (self.current_index + 1) % len(self.fotos)
        elif direccion == 'anterior':
            self.current_index = (self.current_index - 1) % len(self.fotos)
        self.mostrar_foto_y_comentarios()

    # Luego en los métodos individuales
    def mostrar_siguiente(self):
        self.cambiar_foto('siguiente')

    def mostrar_anterior(self):
        self.cambiar_foto('anterior')

    # Método para mandar a la página de registro de nuevos puestos de comida
    def registrar_puesto(self):
        print("Registrar nuevo puesto de comida")
        try:
            # Mandamos al usuario a pantalla del registro de puesto de comida
            token_actual = load_token()
            self.route_manager.mandar_a_registro_puesto(ventana_anterior=self, token=token_actual)
        except AttributeError as e:
            print(f"Error: No se pudo acceder al método de registro: {e}")
        except Exception as e:
            print(f"Error inesperado al intentar redirigir al registro: {e}")

    # Método para mandar a la página del perfil del puesto
    def perfil_puesto(self):
        print("Diriguiendo al perfil del puesto de comida")
        try:
            # Mandamos al usuario a la pantalla del perfil del puesto de comida
            token_actual = load_token()
            self.route_manager.mandar_a_perfil_puesto(ventana_anterior=self, token=token_actual)
        except AttributeError as e:
            print(f"Error: No se pudo acceder al método de registro: {e}")
        except Exception as e:
            print(f"Error inesperado al intentar redirigir al registro: {e}")

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
            self.route_manager.mandar_a_login()  # Mandar al usuario a la pantalla de login

        except Exception as e:
            print(f"Error inesperado al intentar cerrar sesión: {e}")

    def dirigir_a_login(self, token_actual):
        """Dirigir al usuario al login si el token no es válido."""
        if not token_is_valid(token_actual):
            self.ui.mostrar_resultado.setText('Tu sesión ha expirado. Por favor inicia sesión nuevamente.')
            self.route_manager.mandar_a_login()

# Es un método mágico -> Verifica si el archivo se está ejecutando de raíz
if __name__ == '__main__':
    # Inicializamos la aplicación (Ventana)
    app = QApplication(sys.argv)
    window = PrincipalWindow()
    window.show()
    sys.exit(app.exec())
