from django.db import models


class Solicitud(models.Model):
    idSolicitud = models.CharField(
        max_length=100, primary_key=True
    )  # Usando el nombre original
    idVendedor = models.CharField(max_length=100)
    idComprador = models.CharField(max_length=100)
    idPropiedad = models.IntegerField()  # Manteniendo el tipo de dato correcto
    fechaSolicitud = models.DateField()
    status = models.CharField(max_length=100)

    class Meta:
        db_table = "solicitudesPromotor"
