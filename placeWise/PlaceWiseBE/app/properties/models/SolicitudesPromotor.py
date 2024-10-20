from djongo import models


class SolicitudPromotor(models.Model):
    idSolicitud = models.CharField(max_length=255, primary_key=True)
    idVendedor = models.CharField(max_length=255)
    idComprador = models.CharField(max_length=255)
    idPropiedad = models.IntegerField()
    fechaSolicitud = models.DateField()
    status = models.CharField(max_length=50)

    class Meta:
        db_table = "solicitudesPromotor"
