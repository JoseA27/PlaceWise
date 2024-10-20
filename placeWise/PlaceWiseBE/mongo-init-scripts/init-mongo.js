// Conectar a la base de datos
db = db.getSiblingDB('PlaceWiseDB');

// Crear las colecciones si no existen
db.createCollection('promotores');
db.createCollection('propiedades');
db.createCollection('propiedadesPorPromotor');
db.createCollection('solicitudesPromotor');
db.createCollection('multimediaPorPropiedad');
db.createCollection('historialPromotor');

// Crear datos de prueba para la colección "promotores"
db.promotores.insertMany([
    {
        "nombre": "Promotor 1",
        "id": 1,
        "descripcion": "Promotor especializado en propiedades residenciales",
        "telefono": "123456789",
        "correo": "promotor1@example.com",
        "redesSociales": {
            "facebook": "fb.com/promotor1",
            "instagram": "instagram.com/promotor1",
            "twitter": "twitter.com/promotor1",
            "tiktok": "tiktok.com/@promotor1"
        },
        "categoria": {
            "rating": 4.5,
            "tarifaActual": 3000,
            "historialTarifas": [
                {
                    "fechaInicio": "2023-01-01",
                    "fechaFin": "2023-12-31",
                    "tarifa": 2800
                }
            ],
            "paquetes": [
                {
                    "idPaquete": 1,
                    "nombrePaquete": "Paquete Residencial",
                    "version": "v1.0",
                    "descripcion": "Paquete básico para propiedades residenciales",
                    "precio": 3000.0,
                    "checksumPrecio": "e99a18c428cb38d5f260853678922e03",
                    "url": "https://paquetes.com/residencial"
                }
            ]
        }
    }
]);

// Crear datos de prueba para la colección "propiedades"
db.propiedades.insertMany([
    {
        "id": 1,
        "idPromotorActual": 1,
        "titulo": "Casa en la playa",
        "ubicacion": {
            "idContry": 1,
            "idState": 1,
            "idCity": 1,
            "direccion": "Calle Falsa 123",
            "geolocalizacion": {
                "latitud": 9.935,
                "longitud": -84.085
            }
        },
        "descripcion": "Hermosa casa frente al mar.",
        "estatus": "Disponible",
        "bitacora": [
            {
                "fechaEvento": "2024-01-10",
                "tipoEvento": "Visita",
                "status": "Pendiente",
                "descripcion": "Visita programada con cliente",
                "usuarioResponsable": "Promotor 1"
            }
        ],
        "documentos": [
            {
                "nombre": "Escritura",
                "tipo": "Legal",
                "fechaEmision": "2020-05-15",
                "fechaVencimiento": "2030-05-15",
                "emitidoPor": "Registro Nacional",
                "status": "Vigente",
                "url": "https://docs.com/escritura"
            }
        ]
    }
]);

// Crear datos de prueba para la colección "propiedadesPorPromotor"
db.propiedadesPorPromotor.insertMany([
    {
        "idPropiedad": 1,
        "idPromotor": 1,
        "idPaquete": 1,
        "versionPaquete": "v1.0",
        "fechaAsignacion": "2024-01-01",
        "fechaVencimiento": "2024-12-31",
        "estadoAsignacion": "Activo",
        "leads": [
            {
                "idLead": "lead1",
                "fechaLead": "2024-02-01",
                "nombreLead": "Cliente 1",
                "telefonoLead": "987654321",
                "correoLead": "cliente1@example.com",
                "estadoLead": "En contacto",
                "comentariosLead": "El cliente está interesado en programar una segunda visita."
            }
        ]
    }
]);

// Crear datos de prueba para la colección "solicitudesPromotor"
db.solicitudesPromotor.insertMany([
    {
        "idSolicitud": "solicitud1",
        "idVendedor": "promotor1",
        "idComprador": "comprador1",
        "idPropiedad": 1,
        "fechaSolicitud": "2024-03-15",
        "status": "En proceso"
    }
]);

// Crear datos de prueba para la colección "multimediaPorPropiedad"
db.multimediaPorPropiedad.insertMany([
    {
        "idPropiedad": 1,
        "idPromotor": 1,
        "imagenes": [
            {
                "nombre": "Frente de la casa",
                "descripcion": "Imagen de la fachada de la casa",
                "fechaSubida": "2024-01-05",
                "usuarioSubida": "Promotor 1",
                "url": "https://multimedia.com/imagen1"
            }
        ],
        "videos": [
            {
                "nombre": "Recorrido virtual",
                "descripcion": "Video mostrando la casa",
                "fechaSubida": "2024-01-06",
                "usuarioSubida": "Promotor 1",
                "url": "https://multimedia.com/video1"
            }
        ],
        "modelos3D": [
            {
                "nombre": "Plano 3D de la casa",
                "descripcion": "Modelo 3D de la casa",
                "fechaSubida": "2024-01-07",
                "usuarioSubida": "Promotor 1",
                "url": "https://multimedia.com/modelo3d1"
            }
        ]
    }
]);

// Crear datos de prueba para la colección "historialPromotor"
db.historialPromotor.insertMany([
    {
        "idPromotor": 1,
        "historial": [
            {
                "idPropiedad": 1,
                "fechaVenta": "2024-04-10",
                "montoVenta": 500000.0,
                "comprador": {
                    "idComprador": "comprador1",
                    "nombre": "Comprador 1"
                }
            }
        ]
    }
]);

