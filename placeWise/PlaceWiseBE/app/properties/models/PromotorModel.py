from djongo import models


# Define el modelo de redes sociales como un modelo embebido
class RedesSociales(models.Model):
    facebook = models.URLField()
    instagram = models.URLField()
    twitter = models.URLField()
    TikTok = models.URLField()

    class Meta:
        abstract = True  # Se mantiene como un modelo abstracto


# Define el modelo de historial de tarifas como un diccionario
class HistorialTarifas(models.Model):
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    tarifa = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = True  # Se mantiene como un modelo abstracto


# Define el modelo de paquetes como un diccionario
class Paquete(models.Model):
    idPaquete = models.IntegerField()
    nombrePaquete = models.CharField(max_length=255)
    version = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    checksumPrecio = models.CharField(max_length=255)
    url = models.URLField()

    class Meta:
        abstract = True  # Se mantiene como un modelo abstracto


# Define el modelo de categoría
class Categoria(models.Model):
    rating = models.FloatField()
    tarifaActual = models.DecimalField(max_digits=10, decimal_places=2)
    historialTarifas = models.ArrayField(
        model_container=HistorialTarifas, blank=True
    )  # Cambia a blank=True si es opcional
    paquetes = models.ArrayField(
        model_container=Paquete, blank=True
    )  # Cambia a blank=True si es opcional

    class Meta:
        abstract = (
            True  # Permite que este modelo sea parte de la colección "promotores"
        )


# Define el modelo de promotor
class Promotor(models.Model):
    nombre = models.CharField(max_length=255)
    id = models.IntegerField(primary_key=True)
    descripcion = models.TextField()
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    redesSociales = models.EmbeddedField(
        model_container=RedesSociales
    )  # Usando RedesSociales como modelo embebido
    categoria = models.EmbeddedField(
        model_container=Categoria
    )  # Usando Categoria como modelo embebido

    class Meta:
        db_table = "promotores"  # Nombre de la colección en MongoDB
