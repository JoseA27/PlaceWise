
### Repositorios de referencia:
Estructura básica: https://github.com/vintasoftware/django-react-boilerplate/tree/main/backend
s3: https://github.com/etianen/django-s3-storage/tree/master



## Estructura de Carpetas

- **app**: Contiene las aplicaciones de Django.
  - **properties**: Aplicación principal de la API REST.
    - **migration**: Migraciones de la base de datos.
    - **repositories**: Repositorios de la aplicación.
    - **services**: Servicios de la aplicación.
    - **permissions** Permisos de la aplicación.
  - **auth**: Aplicación de autenticación de usuarios.
- **mongo-init-scripts**: Scripts de inicialización de la base de datos de MongoDB con las colecciones de Propiedades.
- **placeWise**: Configuración de Django.
- **templates**: Plantillas HTML de la aplicación. 

```
PlaceWiseBE/
├── app/
│   ├── auth/
│   │   ├── cognito.py
│   │   ├── permission.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   └── properties/
│       ├── migrations/
│       │   └── __init__.py
│       ├── permission/
│       │   └── cognito_access_control.py
│       ├── repositories/
│       │   └── property_repository.py
│       ├── services/
│       │   ├── hubspot_service.py
│       │   ├── property_service.py
│       │   └── s3_service.py
│       ├── users/
│       │   └── admin.py
│       ├── __pycache__/
│       │   ├── services.cpython-312.pyc
│       │   ├── urls.cpython-312.pyc
│       │   ├── views.cpython-312.pyc
│       │   └── __init__.cpython-312.pyc
│       ├── apps.py
│       ├── models.py
│       ├── serializers.py
│       ├── tests.py
│       ├── urls.py
│       ├── views.py
│       └── __init__.py
├── mongo-init-scripts/
│   ├── Costa_Rica_Real_Estate_Dataset.csv
│   └── init-mongo.js
├── placeWise/
│   ├── __pycache__/
│   │   ├── settings.cpython-312.pyc
│   │   ├── urls.cpython-312.pyc
│   │   ├── wsgi.cpython-312.pyc
│   │   └── __init__.cpython-312.pyc
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __init__.py
├── templates/
│   ├── common/
│   │   └── index.html
│   └── base.html
├── .dockerignore
├── db.sqlite3
├── docker-compose.yaml
├── dockerfile
├── manage.py
├── README.md
├── README.pdf
└── requirements.txt
```

### Descripción de los Archivos

#### app/: 
Contiene las aplicaciones de Django.

- **auth/**:
Aplicación de autenticación de usuarios.

- **properties/**:
Aplicación principal de la API REST.

  - **migrations/**: Migraciones de la base de datos.
  - **permission/**:
    - **cognito_access_control.py**: Permisos de acceso a las vistas de la aplicación.
  - **repositories/**:
    - **property_repository.py**: Repositorio de la aplicación.
  - **services/**:
    - **hubspot_service.py**: Servicio de HubSpot para las redes sociales.
    - **property_service.py**: Servicio de Propiedades para la aplicación.
    - **s3_service.py**: Servicio de S3 para almacenar archivos.
  - **users/**:
    - **admin.py**: Configuración del administrador de usuarios.
  - **apps.py**: Configuración de la aplicación.
  - **models.py**: Modelos de la aplicación.
  - **serializers.py**: Serializadores de la aplicación.
  - **tests.py**: Pruebas de la aplicación.
  - **urls.py**: URLs de la aplicación.
  - **views.py**: Vistas de la aplicación.


