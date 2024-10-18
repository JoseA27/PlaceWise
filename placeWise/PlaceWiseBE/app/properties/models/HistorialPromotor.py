from djongo import models


class Comprador(models.Model):
    idComprador = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)

    class Meta:
        abstract = True


class Historial(models.Model):
    idPropiedad = models.CharField(max_length=255)
    fechaVenta = models.DateField()
    montoVenta = models.DecimalField(max_digits=10, decimal_places=2)
    comprador = models.EmbeddedField(model_container=Comprador)

    class Meta:
        abstract = True


class HistorialPromotor(models.Model):
    idPromotor = models.CharField(max_length=255)
    historial = models.ArrayField(model_container=Historial)

    def __str__(self):
        return f"Historial de promotor {self.idPromotor}"
