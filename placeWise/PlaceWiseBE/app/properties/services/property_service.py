from ..repositories.property_repository import PropertyRepository
from ..serializers import SolicitudSerializer, PropiedadSerializer
from datetime import date

class PropertyService:
    @staticmethod
    def get_all_solicitudes():
        solicitudes = PropertyRepository.get_all_solicitudes()
        solicitudes_serializer = SolicitudSerializer(solicitudes, many=True)
        return solicitudes_serializer.data
    @staticmethod
    def obtener_todas_propiedades():
        propiedades = PropertyRepository.obtener_todas()
        serializer = PropiedadSerializer(propiedades, many=True)
        return serializer.data
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
            status=status
        )

        return solicitud