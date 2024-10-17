from djongo import models


class SolicitudesPromotor(models.Model):
    idSolicitud = models.CharField(max_length=255)
    idVendedor = models.CharField(max_length=255)
    idComprador = models.CharField(max_length=255)
    idPropiedad = models.CharField(max_length=255)
    fechaSolicitud = models.DateField()
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"Solicitud {self.idSolicitud} para propiedad {self.idPropiedad}"
