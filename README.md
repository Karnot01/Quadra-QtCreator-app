## Quadra - Puestos de Comida Callejera

Quadra es una aplicación desarrollada con Python y Qt que permite a los usuarios ubicar y calificar puestos de comida callejera. Los usuarios pueden subir información sobre diferentes puestos de comida, incluyendo su ubicación georreferenciada, una breve reseña y una foto. Otros usuarios pueden calificar y comentar sobre los puestos creados.

### Características:
- **Subir puestos de comida**: Los usuarios pueden subir nuevos puestos con ubicación, foto y descripción.
- **Calificaciones y comentarios**: Los usuarios pueden calificar y dejar comentarios sobre los puestos de comida.
- **Geolocalización**: La aplicación utiliza geolocalización para mostrar la ubicación exacta de cada puesto.

## Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- **Python 3.8+**
- **PostgreSQL** (para gestionar la base de datos)
- **Qt 6** (o superior)

Puedes instalar las dependencias del proyecto utilizando el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Instalación

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/Karnot01/Quadra-QtCreator-app.git
   cd Quadra-QtCreator-app
   ```

2. **Configura la base de datos:**

   Asegúrate de tener PostgreSQL instalado y ejecutándose. Configura la base de datos en tu entorno local o remoto según sea necesario.

   ```sql
   CREATE DATABASE quadra_db;
   ```

   Asegúrate de que las credenciales de conexión estén configuradas correctamente en los archivos de la aplicación.

3. **Instala las dependencias del proyecto:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecuta la aplicación:**

   Puedes ejecutar la aplicación directamente desde QtCreator o desde la terminal:

   ```bash
   python quadra-foodplace-app.pyproject.py
   ```

## Uso

1. **Crear una cuenta**: El usuario debe registrarse para poder subir puestos de comida y dejar reseñas.
2. **Subir un puesto**: Usa el formulario dentro de la app para agregar la ubicación, una breve descripción y una foto del puesto.
3. **Calificar puestos**: Explora los puestos cercanos, califica y deja comentarios en los puestos de otros usuarios.

## Estructura del Proyecto

- `dir quadra-foodplace-app / quadra-foodplace-app.pyproject`: Archivo principal que arranca la aplicación.
- `dir quadra-foodplace-app / Qt UI Files/`: Interfaces gráficas diseñadas con Qt.
- `dir quadra_api/`: Archivos de configuración de la API
- `Entregables`: Diagramas, Scripts de configuración de la base de datos PostgreSQL y otros documentos relacionados con el diseño de la aplicación.

## Diagramas

En la carpeta `Entregables` encontrarás diagramas que detallan la arquitectura y los flujos de datos de la aplicación.

## Contribuciones

Actualmente, este proyecto no acepta contribuciones externas ya que es un proyecto privado. Sin embargo, si tienes sugerencias o encuentras algún error, siéntete libre de abrir un "Issue" en el repositorio.

## Licencia

Este proyecto está bajo una licencia privada. No está permitido el uso, distribución, modificación o copia de este código sin la autorización explícita del propietario.

---

**Propietario del Proyecto**: [Karnot01](https://github.com/Karnot01)

© 2024 Quadra

---

## Enlaces

- Repositorio: [Quadra en GitHub](https://github.com/Karnot01/Quadra-QtCreator-app.git)

---
