from djongo import models


# Documentación del modelo para la colección de solicitudes de promotor
# se modela la estructura de la colección de solicitudes de promotor
class SolicitudPromotor(models.Model):
    idSolicitud = models.CharField(max_length=255, primary_key=True)
    idVendedor = models.CharField(max_length=255)
    idComprador = models.CharField(max_length=255)
    idPropiedad = models.IntegerField()
    fechaSolicitud = models.DateField()
    status = models.CharField(max_length=50)

    class Meta:
        db_table = "solicitudesPromotor"  # nombre de la tabla (collection) en la base de datos para que tenga referencia
