from djongo import models


class HistorialTarifa(models.Model):
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    tarifa = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = True


class Paquete(models.Model):
    idPaquete = models.IntegerField()
    nombrePaquete = models.CharField(max_length=255)
    version = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    checksumPrecio = models.CharField(max_length=32)
    url = models.URLField()

    class Meta:
        abstract = True


class Categoria(models.Model):
    rating = models.IntegerField()
    tarifaActual = models.DecimalField(max_digits=10, decimal_places=2)
    historialTarifas = models.ArrayField(model_container=HistorialTarifa)
    paquetes = models.ArrayField(model_container=Paquete)

    class Meta:
        abstract = True


class Promotor(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    redesSociales = (
        models.JSONField()
    )  # {facebook: '', instagram: '', twitter: '', TikTok: ''}
    categoria = models.EmbeddedField(model_container=Categoria)

    def __str__(self):
        return self.nombre
