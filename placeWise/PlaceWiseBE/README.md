
### Repositorios de referencia:
Estructura básica: https://github.com/vintasoftware/django-react-boilerplate/tree/main/backend
s3: https://github.com/etianen/django-s3-storage/tree/master

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
│       │   ├── historial_promotor_repository.py
│       │   ├── multimedia_repository.py
│       │   ├── promotor_repository.py
│       │   ├── property_repository.py
│       │   ├── propiedad_promotor_repository.py
│       │   └── solicitud_repository.py
│       ├── services/
│       │   ├── cognito_service.py
│       │   ├── hubspot_service.py
│       │   ├── property_service.py
│       │   ├── s3_service.py
│       │   └── social_media_service.py
│       ├── users/
│       │   └── admin.py
│       ├── views/
│       │   ├── historialPromotorView.py
│       │   ├── multimediaPorPropiedadView.py
│       │   ├── promotoresView.py
│       │   ├── propiedadesPorPromotorView.py
│       │   ├── propiedadesView.py
│       │   └── solicitudesView.py
│       ├── apps.py
│       ├── serializers.py
│       ├── tests.py
│       ├── urls.py
│       └── __init__.py
├── mongo-init-scripts/
│   └── init-mongo.js
├── placeWise/
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
    - **promotor_repository.py**: Repositorio de Promotor.
    - **historial_promotor_repository.py**: Repositorio de Historial de Promotor.
    - **multimedia_repository.py**: Repositorio de Multimedia.
    - **propiedad_promotor_repository.py**: Repositorio de Propiedades por Promotor.
    - **solicitud_repository.py**: Repositorio de Solicitudes.
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
  - **views/**:
    - **historialPromotorView.py**: Vista de Historial de Promotor.
    - **multimediaPorPropiedadView.py**: Vista de Multimedia por Propiedad.
    - **promotoresView.py**: Vista de Promotores.
    - **propiedadesPorPromotorView.py**: Vista de Propiedades por Promotor.
    - **propiedadesView.py**: Vista de Propiedades.
    - **solicitudesView.py**: Vista de Solicitudes.
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




