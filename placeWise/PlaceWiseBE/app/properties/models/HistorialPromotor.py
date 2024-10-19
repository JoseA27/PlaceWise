from djongo import models


class Comprador(models.Model):
    idComprador = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)

    class Meta:
        abstract = True


class HistorialVenta(models.Model):
    idPropiedad = models.CharField(max_length=255)
    fechaVenta = models.DateField()
    montoVenta = models.FloatField()
    comprador = models.EmbeddedField(model_container=Comprador)

    class Meta:
        abstract = True


class HistorialPromotor(models.Model):
    idPromotor = models.CharField(max_length=255)
    historial = models.ArrayField(model_container=HistorialVenta)

    class Meta:
        db_table = 'historialPromotor'
