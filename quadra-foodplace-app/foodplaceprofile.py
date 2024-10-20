import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QPixmap
import requests
from helpers import load_token, url_api
from PySide6.QtCore import Qt
from ui_foodplaceprofile import Ui_FoodPlaceProfileWindow

class FoodPlaceProfile(QMainWindow):
    def __init__(self, foodplace_id, parent=None):
        super().__init__(parent)

        # Este atributo contendrá todo el apartado gráfico
        self.ui = Ui_FoodPlaceProfileWindow()
        self.ui.setupUi(self)

        # Guardar el ID del puesto de comida
        self.foodplace_id = foodplace_id

        # Inicializo variables
        self.fotos = []  # Lista de URLs de fotos

        # Conectar eventos de las miniaturas de fotos
        self.ui.mostrar_foto_1.mousePressEvent = lambda event: self.cambiar_foto(0) if 0 < len(self.fotos) else None
        self.ui.mostrar_foto_2.mousePressEvent = lambda event: self.cambiar_foto(1) if 1 < len(self.fotos) else None
        self.ui.mostrar_foto_3.mousePressEvent = lambda event: self.cambiar_foto(2) if 2 < len(self.fotos) else None
        self.ui.mostrar_foto_4.mousePressEvent = lambda event: self.cambiar_foto(3) if 3 < len(self.fotos) else None
        self.ui.mostrar_foto_5.mousePressEvent = lambda event: self.cambiar_foto(4) if 4 < len(self.fotos) else None

        # Cargar la información del puesto de comida
        self.cargar_perfil()

    def cargar_perfil(self):
        """Cargar la información del perfil del puesto de comida."""
        try:
            token_actual = load_token()
            headers = {"Authorization": f"Bearer {token_actual}"}

            # URL para obtener los detalles del puesto de comida
            url = f"{url_api}/puestos/{self.foodplace_id}"
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                datos_puesto = response.json()

                # Mostrar el nombre del puesto
                self.ui.mostrar_resultado.setText(datos_puesto.get("nombre", "Nombre no disponible"))

                # Cargar las fotos
                self.fotos = datos_puesto.get("fotos", [])
                print(f"Fotos cargadas: {self.fotos}")  # Depuración
                self.mostrar_foto_principal()
                self.cargar_miniaturas()

                # Mostrar el mapa
                mapa_url = datos_puesto.get("mapa_url")
                if mapa_url:
                    self.cargar_mapa(mapa_url)

                # Cargar los comentarios
                comentarios = datos_puesto.get("comentarios", [])
                self.cargar_comentarios(comentarios)
            else:
                QMessageBox.warning(self, "Error", f"No se pudo cargar el perfil: {response.status_code}")
                print(f"Error al cargar el perfil del puesto: {response.status_code}")  # Depuración
        except requests.RequestException as e:
            QMessageBox.warning(self, "Error", f"Error de conexión: {e}")
            print(f"Error de conexión: {e}")  # Depuración

    def mostrar_foto_principal(self):
        """Mostrar la primera foto como foto principal."""
        if self.fotos:
            foto_url = self.fotos[0]  # Usamos la primera foto como principal
            print(f"Mostrando la foto principal: {foto_url}")  # Depuración
            self.cargar_imagen(self.ui.mostrar_foto, foto_url)
        else:
            self.ui.mostrar_foto.setText("No hay fotos disponibles")
            print("No hay fotos disponibles")  # Depuración

    def cargar_miniaturas(self):
        """Cargar las miniaturas de las fotos en los 5 QLabel pequeños."""
        labels = [
            self.ui.mostrar_foto_1,
            self.ui.mostrar_foto_2,
            self.ui.mostrar_foto_3,
            self.ui.mostrar_foto_4,
            self.ui.mostrar_foto_5
        ]

        # Cargar fotos en las miniaturas (máximo 5 fotos)
        for i in range(min(5, len(self.fotos))):
            print(f"Cargando miniatura {i + 1}: {self.fotos[i]}")  # Depuración
            self.cargar_imagen(labels[i], self.fotos[i])

    def cambiar_foto(self, indice):
        """Cambiar la foto principal al hacer clic en una miniatura."""
        if 0 <= indice < len(self.fotos):
            print(f"Cambiando a la foto {indice + 1}: {self.fotos[indice]}")  # Depuración
            self.cargar_imagen(self.ui.mostrar_foto, self.fotos[indice])

    def cargar_mapa(self, mapa_url):
        """Cargar la imagen del mapa de la ubicación."""
        print(f"Cargando el mapa desde: {mapa_url}")  # Depuración
        self.cargar_imagen(self.ui.mostrar_mapa, mapa_url)

    def cargar_imagen(self, label, url):
        """Cargar una imagen desde una URL y mostrarla en un QLabel."""
        try:
            response = requests.get(url)
            if response.status_code == 200:
                pixmap = QPixmap()
                pixmap.loadFromData(response.content)
                label.setPixmap(pixmap.scaled(label.size(), Qt.KeepAspectRatio))
                print(f"Imagen cargada correctamente desde: {url}")  # Depuración
            else:
                label.setText("Error al cargar la imagen")
                print(f"Error al cargar la imagen desde: {url}")  # Depuración
        except Exception as e:
            print(f"Error al cargar la imagen desde {url}: {e}")
            label.setText("Error al cargar la imagen")

    def cargar_comentarios(self, comentarios):
        """Cargar los comentarios del puesto de comida en la lista."""
        self.ui.lista_comentarios.clear()
        for comentario in comentarios:
            texto_comentario = comentario.get("texto", "Comentario no disponible")
            print(f"Cargando comentario: {texto_comentario}")  # Depuración
            self.ui.lista_comentarios.addItem(texto_comentario)


# Método mágico para inicializar la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Simulación de ID de puesto de comida
    window = FoodPlaceProfile(foodplace_id=123)  # Puedes cambiar el ID de prueba
    window.show()
    sys.exit(app.exec())
