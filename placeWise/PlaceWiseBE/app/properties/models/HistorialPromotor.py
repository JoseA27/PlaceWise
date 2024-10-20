from djongo import models


class Comprador(models.Model):
    idComprador = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)

    class Meta:
        abstract = True


class HistorialVenta(models.Model):
    idPropiedad = models.IntegerField()
    fechaVenta = models.DateField()
    montoVenta = models.DecimalField(max_digits=15, decimal_places=2)
    comprador = models.EmbeddedField(model_container=Comprador)

    class Meta:
        abstract = True


class HistorialPromotor(models.Model):
    idPromotor = models.IntegerField()
    historial = models.ArrayField(model_container=HistorialVenta)

    class Meta:
        db_table = "historialPromotor"
