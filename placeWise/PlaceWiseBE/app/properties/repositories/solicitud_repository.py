from ..models.SolicitudesPromotor import SolicitudPromotor

# Documentación
# Clase que representa el repositorio de solicitudes
# Se encarga de realizar las operaciones de lectura y escritura en la base de datos

class SolicitudRepository:
    # Solicitudes
    # Método que obtiene todas las solicitudes
    @staticmethod
    def get_all_solicitudes():
        return SolicitudPromotor.objects.all()

    # Método que crea una solicitud
    # recibe los datos validados de la solicitud
    @staticmethod
    def crear_solicitud(id_vendedor, id_comprador, id_propiedad, fecha_solicitud, status):
        try:
            nueva_solicitud = SolicitudPromotor(
                idVendedor=id_vendedor,
                idComprador=id_comprador,
                idPropiedad=id_propiedad,
                fechaSolicitud=fecha_solicitud,
                status=status,
            )
            nueva_solicitud.save()
            return nueva_solicitud
        except Exception as e:
            print(f"Error al guardar la solicitud: {str(e)}")
            return None