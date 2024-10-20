# Este archivo se va a encargar de poner a correr el servidor

# Aqui solamente se va a ejecutar el comando necesario para ponerlo a correr

from app import configurar_app  # Importamos la función que configura la app

app = configurar_app()  # Configura la app correctamente

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Inicia el servidor en el puerto 5000