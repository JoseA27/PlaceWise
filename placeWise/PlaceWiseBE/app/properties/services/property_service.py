from ..repositories.property_repository import PropertyRepository
from ..serializers import SolicitudSerializer

class PropertyService:
    @staticmethod
    def get_all_solicitudes():
        solicitudes = PropertyRepository.get_all_solicitudes()
        solicitudes_serializer = SolicitudSerializer(solicitudes, many=True)
        return solicitudes_serializer.data