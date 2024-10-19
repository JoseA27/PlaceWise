from ..models.SolicitudesPromotor import SolicitudPromotor
from ..models.PropiedadModel import Propiedad

class PropertyRepository:

    @staticmethod
    def get_all_solicitudes():
        return SolicitudPromotor.objects.all()
    @staticmethod
    def crear_solicitud(id_vendedor, id_comprador, id_propiedad, fecha_solicitud, status):
        try:
            # Crear una nueva instancia del modelo SolicitudPromotor
            nueva_solicitud = SolicitudPromotor(
                idVendedor=id_vendedor,
                idComprador=id_comprador,
                idPropiedad=id_propiedad,
                fechaSolicitud=fecha_solicitud,
                status=status
            )
            # Guardar en la base de datos
            nueva_solicitud.save()

            return nueva_solicitud
        except Exception as e:
            print(f"Error al guardar la solicitud: {str(e)}")
            return None
    @staticmethod
    def get_all_Propiedades():
        return Propiedad.objects.all()

    
    