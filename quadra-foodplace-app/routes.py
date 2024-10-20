# Este archivo se va a encargar de las redirecciones

from helpers import decode_token, save_token

class RouteManager:
    def __init__(self):
        # La ventana actual se inicializa como None
        self.current_window = None

    # Método auxiliar para cerrar la ventana anterior
    def cerrar_ventana(self, ventana_anterior):
        if ventana_anterior:
            ventana_anterior.close()

    # Mandar al usuario a la vista login
    def mandar_a_login(self, ventana_anterior=None):
        from mainwindow import MainWindow  # Importación diferida

        self.current_window = MainWindow()
        self.current_window.show()

        self.cerrar_ventana(ventana_anterior)

    # Mandar al usuario a la vista registro
    def mandar_a_registro(self, ventana_anterior=None):
        from register import RegisterWindow  # Importación diferida

        self.current_window = RegisterWindow(correo_usuario="")
        self.current_window.show()

        self.cerrar_ventana(ventana_anterior)

    # Mandar al usuario a la vista principal
    def mandar_a_principal(self, ventana_anterior=None, token=None):
        from principal import PrincipalWindow  # Importación diferida

        # Guardamos el token y decodificamos la información del usuario
        if token:
            save_token(token)

            try:
                info_user = decode_token(token)
                nombre_usuario = info_user.get('sub', 'Usuario')
            except (KeyError, TypeError, ValueError) as e:
                print(f"Error al decodificar el token: {e}")
                nombre_usuario = 'Usuario'  # Valor por defecto en caso de error
        else:
            nombre_usuario = 'Usuario'  # Si no hay token, se usa un nombre genérico

        # Mostrar la ventana principal
        self.current_window = PrincipalWindow(nombre_usuario=nombre_usuario)
        self.current_window.show()

        self.cerrar_ventana(ventana_anterior)

    # Mandar al usuario a la página de nuevo registro de puestos de comida
    def mandar_a_registro_puesto(self, ventana_anterior=None, token=None):
        from RegisterFoodPlace import RegisterFoodPlaceWindow # Importación diferida

        # Guardamos el token y decodificamos la información del usuario
        if token:
            save_token(token)

            try:
                info_user = decode_token(token)
                nombre_usuario = info_user.get('sub', 'Usuario')
            except (KeyError, TypeError, ValueError) as e:
                print(f"Error al decodificar el token: {e}")
                nombre_usuario = 'Usuario'  # Valor por defecto en caso de error
        else:
            nombre_usuario = 'Usuario'  # Si no hay token, se usa un nombre genérico

        # Mostrar la ventana de nuevo registro de puesto de comida
        self.current_window = RegisterFoodPlaceWindow(nombre_usuario=nombre_usuario)
        self.current_window.show()

        self.cerrar_ventana(ventana_anterior)

    # Mandar al usuario a la página del perfil del puesto de comida
    def mandar_a_perfil_puesto(self, ventana_anterior=None, token=None):
        from foodplaceprofile import FoodPlaceProfileWindow # Importación diferida

        # Guardamos el token y decodificamos la información del usuario
        if token:
            save_token(token)

            try:
                info_user = decode_token(token)
                nombre_usuario = info_user.get('sub', 'Usuario')
            except (KeyError, TypeError, ValueError) as e:
                print(f"Error al decodificar el token: {e}")
                nombre_usuario = 'Usuario'  # Valor por defecto en caso de error
        else:
            nombre_usuario = 'Usuario'  # Si no hay token, se usa un nombre genérico

        # Mostrar la ventana del perfil del puesto de comida
        self.current_window = FoodPlaceProfileWindow(nombre_usuario=nombre_usuario)
        self.current_window.show()

        self.cerrar_ventana(ventana_anterior)



