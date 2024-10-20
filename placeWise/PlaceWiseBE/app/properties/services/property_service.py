from ..repositories.property_repository import PropertyRepository
from ..serializers import (
    SolicitudSerializer,
    PropiedadSerializer,
    PropiedadPorPromotorSerializer,
    PromotorSerializer,
    MultimediaPorPropiedadSerializer,
    HistorialPromotorSerializer,
)
from datetime import date

# Clase que contiene los métodos para interactuar con la base de datos y la vista
# Se encarga de realizar las operaciones de lectura y escritura en la base de datos
# Se encarga de la lógica de negocio de la aplicación


class PropertyService:
    # Solicitudes
    # Método que obtiene todas las solicitudes
    @staticmethod
    def get_all_solicitudes():
        solicitudes = (
            PropertyRepository.get_all_solicitudes()
        )  # Se obtienen todas las solicitudes
        solicitudes_serializer = SolicitudSerializer(
            solicitudes, many=True
        )  # Se serializan los datos
        return solicitudes_serializer.data

    # Método que crea una solicitud
    # recibe los datos validados de la solicitud

    @staticmethod
    def agregar_solicitud(id_vendedor, id_comprador, id_propiedad, status):
        # Establecer la fecha de la solicitud
        fecha_solicitud = date.today()

        # Llamar al repositorio para agregar la solicitud
        solicitud = PropertyRepository.crear_solicitud(
            id_vendedor=id_vendedor,
            id_comprador=id_comprador,
            id_propiedad=id_propiedad,
            fecha_solicitud=fecha_solicitud,
            status=status,
        )

        return solicitud

    # Propiedades
    # Método que obtiene todas las propiedades

    @staticmethod
    def get_all_propiedades():
        propiedades = PropertyRepository.get_all_propiedades()
        propiedades_serializer = PropiedadSerializer(propiedades, many=True)
        return propiedades_serializer.data

    # Método que crea una propiedad
    # recibe los datos validados de la propiedads
    @staticmethod
    def agregar_propiedad(data):
        propiedad_serializer = PropiedadSerializer(data=data)  # Se serializan los datos
        if propiedad_serializer.is_valid():  # Se valida la información
            propiedad = PropertyRepository.crear_propiedad(
                propiedad_serializer.validated_data
            )
            return PropiedadSerializer(propiedad).data
        return None

    # Promotores
    # Método que obtiene todos los promotores
    @staticmethod
    def get_all_promotores():
        promotores = PropertyRepository.get_all_promotores()
        promotores_serializer = PromotorSerializer(promotores, many=True)
        return promotores_serializer.data

    # Método que crea un promotor
    # recibe los datos validados del promotor
    @staticmethod
    def agregar_promotor(data):
        promotor_serializer = PromotorSerializer(data=data)
        if promotor_serializer.is_valid():
            promotor = PropertyRepository.crear_promotor(
                promotor_serializer.validated_data
            )
            return PromotorSerializer(promotor).data
        return None

    # Propiedad por Promotor
    # Método que obtiene todas las propiedades por promotor
    @staticmethod
    def get_all_propiedades_por_promotor():
        propiedades_por_promotor = PropertyRepository.get_all_propiedades_por_promotor()
        propiedad_por_promotor_serializer = PropiedadPorPromotorSerializer(
            propiedades_por_promotor, many=True
        )
        return propiedad_por_promotor_serializer.data

    # Método que crea una propiedad por promotor
    # recibe los datos validados de la propiedad por prom
    @staticmethod
    def agregar_propiedad_por_promotor(data):
        propiedad_por_promotor_serializer = PropiedadPorPromotorSerializer(data=data)

        if propiedad_por_promotor_serializer.is_valid():
            propiedad_por_promotor = PropertyRepository.crear_propiedad_por_promotor(
                propiedad_por_promotor_serializer.validated_data
            )
            return PropiedadPorPromotorSerializer(propiedad_por_promotor).data
        else:
            return propiedad_por_promotor_serializer.errors

    # Multimedia por Propiedad
    # Método que obtiene todas las multimedia por propiedad
    @staticmethod
    def get_all_multimedia():
        multimedia = PropertyRepository.get_all_multimedia()
        multimedia_serializer = MultimediaPorPropiedadSerializer(multimedia, many=True)
        return multimedia_serializer.data

    # Método que crea una multimedia
    # recibe los datos validados de la multimedia
    @staticmethod
    def agregar_multimedia(data):
        multimedia_serializer = MultimediaPorPropiedadSerializer(data=data)
        if multimedia_serializer.is_valid():
            multimedia = PropertyRepository.crear_multimedia(
                multimedia_serializer.validated_data
            )
            return MultimediaPorPropiedadSerializer(multimedia).data
        return None

    # Historial Promotor
    # Método que obtiene todo el historial de promotor
    @staticmethod
    def get_all_historial_promotor():
        historial = PropertyRepository.get_all_historial_promotor()
        historial_serializer = HistorialPromotorSerializer(historial, many=True)
        return historial_serializer.data

    # Método que crea un historial de promotor
    # recibe los datos validados del historial de promotor
    @staticmethod
    def agregar_historial_promotor(data):
        historial_serializer = HistorialPromotorSerializer(data=data)
        if historial_serializer.is_valid():
            historial = PropertyRepository.crear_historial_promotor(
                historial_serializer.validated_data
            )
            return HistorialPromotorSerializer(historial).data
        return None
