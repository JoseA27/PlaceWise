from ..models.SolicitudesPromotor import SolicitudPromotor

class PropertyRepository:

    @staticmethod
    def get_all_solicitudes():
        return SolicitudPromotor.objects.all()
    