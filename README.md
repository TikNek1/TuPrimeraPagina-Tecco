# TikNek Viajes - Plataforma Web

Este proyecto es una página web para la empresa **TikNek Viajes**, que organiza y ofrece viajes en moto. La plataforma permite a los usuarios explorar información sobre los viajes planificados, los pilotos y los guías que participan en ellos. Además, los administradores y usuarios del grupo TikNek tienen acceso a funcionalidades adicionales.

## Funcionalidades principales

### Para usuarios no autenticados:
- Ver la lista de viajes planificados.
- Consultar detalles de cada viaje.
- Ver la lista de pilotos y guías.

### Para usuarios autenticados:
- **Usuarios administradores o del grupo TikNek**:
  - Crear nuevos viajes desde la interfaz web.
  - Acceder al menú de administración de Django para gestionar datos.

## Estructura del proyecto
Practico_3/ ├── TikNek_Viajes/ │ ├── settings.py # Configuración del proyecto Django │ ├── urls.py # Configuración de rutas principales │ ├── wsgi.py # Configuración WSGI │ ├── asgi.py # Configuración ASGI │ └── templates/ # Plantillas base del proyecto ├── viajes/ │ ├── models.py # Modelos de datos (Viaje, Piloto, Guía) │ ├── views.py # Vistas para manejar la lógica de negocio │ ├── urls.py # Rutas específicas de la app "viajes" │ ├── templates/ # Plantillas específicas de la app │ │ ├── lista_viajes.html │ │ ├── lista_guias.html │ │ ├── lista_pilotos.html │ │ └── detalle_viaje.html │ └── forms.py # Formularios para crear y editar viajes └── db_viajes.sqlite3 # Base de datos SQLite


## Requisitos

- **Python**: 3.8 o superior.
- **Django**: 4.2 o superior.
- Dependencias adicionales:
  - `widget_tweaks` (para mejorar la apariencia de los formularios).

## Configuración e instalación

1. Clona el repositorio y navega al directorio del proyecto:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd Practico_3

2. Crea un entorno virtual e instala las dependencias
    python -m venv _myenv
    source _myenv/bin/activate  # En Windows: _myenv\Scripts\activate
    pip install -r requirements.txt

3. Realiza las migraciones para configurar la base de datos:
    python manage.py migrate

4. Inicia el servidor de desarrollo:
    python manage.py runserver

5. Accede a la aplicación en tu navegador en http://127.0.0.1:8000.

## Cómo usar la aplicación
1. Usuarios no autenticados:
Navega por la página para explorar los viajes, pilotos y guías.

2. Usuarios autenticados:
Inicia sesión desde la página de login.
Si eres administrador o perteneces al grupo TikNek, podrás:
Crear nuevos viajes desde la página de lista de viajes.
Acceder al menú de administración de Django en /admin.