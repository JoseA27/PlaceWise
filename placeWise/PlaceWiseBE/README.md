
### Repositorios de referencia:
Estructura básica: https://github.com/vintasoftware/django-react-boilerplate/tree/main/backend
s3: https://github.com/etianen/django-s3-storage/tree/master

## Diagrama 
![alt text](<../../imagenes/DiagramaBE.png>)

## Estructura de Carpetas

- **app**: Contiene las aplicaciones de Django.
  - **properties**: Aplicación principal de la API REST.
    - **migration**: Migraciones de la base de datos.
    - **repositories**: Repositorios de la aplicación.
    - **services**: Servicios de la aplicación.
    - **api**: API de la aplicación.
    - **models**: Modelos de la aplicación.
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
│       ├── apis/
│       │   ├── facebook_adapter.py
│       │   ├── instagram_adapter.py
│       │   ├── social_media_adapter.py
│       │   ├── social_media_factory.py
│       │   ├── tiktok_adapter.py
│       │   └── twitter_adapter.py
│       ├── migrations/
│       │   └── __init__.py
│       ├── models/
│       │   ├── HistorialPromotor.py
│       │   ├── MultimediaPorPropiedad.py
│       │   ├── PromotorModel.py
│       │   ├── PropiedadesPorPromotor.py
│       │   ├── PropiedadModel.py
│       │   ├── SolicitudesPromotor.py
│       │   └── __init__.py
│       ├── repositories/
│       │   └── property_repository.py
│       ├── services/
│       │   ├── cognito_service.py
│       │   ├── hubspot_service.py
│       │   ├── property_service.py
│       │   ├── s3_service.py
│       │   └── social_media_service.py
│       ├── users/
│       │   └── admin.py
│       ├── __pycache__/
│       │   ├── services.cpython-312.pyc
│       │   ├── urls.cpython-312.pyc
│       │   ├── views.cpython-312.pyc
│       │   └── __init__.cpython-312.pyc
│       ├── apps.py
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
│   │   ├── settings.cpython-310.pyc
│   │   ├── settings.cpython-312.pyc
│   │   ├── urls.cpython-312.pyc
│   │   ├── wsgi.cpython-312.pyc
│   │   ├── __init__.cpython-310.pyc
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
  - **repositories/**:
    - **property_repository.py**: Repositorio de la aplicación.
  - **models/**:
    - **HistorialPromotor.py**: Modelo de Historial de Promotor.
    - **MultimediaPorPropiedad.py**: Modelo de Multimedia por Propiedad.
    - **PromotorModel.py**: Modelo de Promotor.
    - **PropiedadesPorPromotor.py**: Modelo de Propiedades por Promotor.
    - **PropiedadModel.py**: Modelo de Propiedad.
    - **SolicitudesPromotor.py**: Modelo de Solicitudes de Promotor.
  - **apis/**:
    - **facebook_adapter.py**: Adaptador de Facebook.
    - **instagram_adapter.py**: Adaptador de Instagram.
    - **social_media_adapter.py**: Adaptador de Redes Sociales.
    - **social_media_factory.py**: Fábrica de Redes Sociales.
    - **tiktok_adapter.py**: Adaptador de TikTok.
    - **twitter_adapter.py**: Adaptador de Twitter.
  - **services/**:
    - **hubspot_service.py**: Servicio de HubSpot para las redes sociales.
    - **property_service.py**: Servicio de Propiedades para la aplicación.
    - **s3_service.py**: Servicio de S3 para almacenar archivos.
    - **social_media_service.py**: Servicio de Redes Sociales para conectarse con las APIs.
    - **cognito_service.py**: Servicio de Cognito para autenticación de usuarios.
  - **users/**:
    - **admin.py**: Configuración del administrador de usuarios.
  - **apps.py**: Configuración de la aplicación.
  - **models.py**: Modelos de la aplicación.
  - **serializers.py**: Serializadores de la aplicación.
  - **tests.py**: Pruebas de la aplicación.
  - **urls.py**: URLs de la aplicación.
  - **views.py**: Vistas de la aplicación.

#### mongo-init-scripts/:
Scripts de inicialización de la base de datos de MongoDB con las colecciones de Propiedades.

- **init-mongo.js**: Script de inicialización de la base de datos.

#### placeWise/:
Configuración de Django.

- **asgi.py**: Configuración de ASGI.
- **settings.py**: Configuración de la aplicación.
- **urls.py**: URLs de la aplicación.
- **wsgi.py**: Configuración de WSGI.
- **__init__.py**: Inicialización de la aplicación.

#### templates/:
Plantillas HTML de la aplicación.
- **base.html**: Plantilla base.
- **common/**: Plantillas comunes.
  - **index.html**: Plantilla de la página principal.




