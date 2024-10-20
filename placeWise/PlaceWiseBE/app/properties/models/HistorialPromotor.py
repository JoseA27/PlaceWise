from djongo import models


# Modelo HistorialPromotor
# Modelo que representa el historial de ventas de un promotor
# clases abstractas: Comprador, HistorialVenta sirven para representar los datos de un comprador y una venta respectivamente
# en los campos embebidos de HistorialPromotor
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
    historial = models.ArrayField(
        model_container=HistorialVenta
    )  # historial es un array de historiales de venta

    class Meta:
        db_table = "historialPromotor"  # nombre de la tabla (collection) en la base de datos para que tenga referencia
