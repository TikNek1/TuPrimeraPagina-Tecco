# TikNek Viajes - Plataforma Web

Este proyecto es una página web para la empresa ficticia **TikNek Viajes**, que organiza y ofrece viajes en moto. La plataforma permite explorar información sobre los viajes planificados, los pilotos y los guías. Además, los administradores o usuarios del grupo *TikNek* pueden crear nuevos viajes desde la web y los demás datos desde el menu **admin**.

---

## Funcionalidades principales

### Usuarios no autenticados:
- Ver la lista de viajes planificados.
- Consultar detalles de cada viaje.
- Ver la lista de pilotos y guías.

### Usuarios autenticados:
- Iniciar sesión desde la página de login.
- Si son administradores o pertenecen al grupo **TikNek**, podrán:
  - Crear nuevos viajes desde la interfaz web.
  - Acceder al panel de administración de Django (`/admin`).

---

## Usuarios disponibles para pruebas

| Rol              | Usuario     | Contraseña |
|------------------|-------------|------------|
| Superusuario     | `nicotecco` | `coder123` |
| Usuario TikNek   | `profe`     | `coder123` |

> El usuario `profe` pertenece al grupo *TikNek* y tiene permisos para crear viajes desde la interfaz.

---

## Requisitos

- Python 3.8 o superior
- Django 4.2 o superior
- Paquete adicional:
  - `django-widget-tweaks`

---

## Estructura

TuPrimeraPagina-Tecco/
├── static/img               # Imagenes/logo que se usarán en la Web
├── TikNek_Viajes/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py / asgi.py
│   └── templates/           # Plantillas base del proyecto
├── viajes/
│   ├── models.py            # Modelos: Viaje, Piloto, Guía
│   ├── views.py             # Lógica de negocio
│   ├── urls.py              # Rutas específicas de la app
│   ├── forms.py             # Formularios para viajes
│   └── templates/
│       ├── lista_viajes.html
│       ├── lista_guias.html
│       ├── lista_pilotos.html
│       └── detalle_viaje.html
└── db_viajes.sqlite3        # Base de datos