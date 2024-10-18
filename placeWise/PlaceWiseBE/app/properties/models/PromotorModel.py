from djongo import models


class HistorialTarifas(models.Model):
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    tarifa = models.FloatField()

    class Meta:
        abstract = True


class Paquetes(models.Model):
    idPaquete = models.IntegerField()
    nombrePaquete = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.FloatField()
    checksumPrecio = models.CharField(max_length=255)
    url = models.URLField()

    class Meta:
        abstract = True


class Categoria(models.Model):
    rating = models.FloatField()
    tarifaActual = models.FloatField()
    historialTarifas = models.ArrayField(model_container=HistorialTarifas)
    paquetes = models.ArrayField(model_container=Paquetes)

    class Meta:
        abstract = True


class Promotor(models.Model):
    nombre = models.CharField(max_length=255)
    id = models.IntegerField()
    descripcion = models.TextField()
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    redesSociales = models.JSONField()
    categoria = models.EmbeddedField(model_container=Categoria)
