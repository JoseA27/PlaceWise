from djongo import models


class Solicitud(models.Model):
    idSolicitud = models.CharField(max_length=255)
    idVendedor = models.CharField(max_length=255)
    idComprador = models.CharField(max_length=255)
    idPropiedad = models.CharField(max_length=255)
    fechaSolicitud = models.DateField()
    status = models.CharField(max_length=50)
