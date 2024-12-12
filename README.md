# M6S4_DjangoTemplate
#Esquema jerárquico de carpetas y archivos Desafio Template M6S4 - Daniela Miranda
site_django/               # Proyecto principal
│
├── site_django/           # Configuración del proyecto principal
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py            # Configuración de rutas del proyecto
│   └── wsgi.py
│
├── book/                  # Aplicación "book"
│   ├── migrations/        # Migraciones de la base de datos
│   │   ├── __init__.py
│   │   └── (archivos de migración generados)
│   ├── templates/         # Carpeta de plantillas HTML
│   │   └── index.html     # Archivo de bienvenida
│   ├── __init__.py
│   ├── admin.py           # Configuración del panel de administración
│   ├── apps.py            # Configuración de la app
│   ├── models.py          # Modelos de base de datos
│   ├── tests.py           # Pruebas unitarias
│   ├── urls.py            # Configuración de rutas de la app "book"
│   └── views.py           # Vistas de la app "book"
│
├── manage.py              # Comando principal de Django
└── db.sqlite3             # Base de datos (creada automáticamente por Django)
