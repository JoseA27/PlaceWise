from djongo import models

# Documentación del modelo para la colección de promotores
# Modelo que representa a un promotor
# Clases abstractas: RedesSociales, HistorialTarifa, Paquete, Categoria sirven para representar los datos de las redes sociales,
# historial de tarifas, paquetes y categoría respectivamente en los campos embebidos de Promotor


class RedesSociales(models.Model):
    facebook = models.URLField()
    instagram = models.URLField()
    twitter = models.URLField()
    tiktok = models.URLField()

    class Meta:
        abstract = True  # Se establece como abstracta para que no se cree una colección en la base de datos


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
    checksumPrecio = models.CharField(max_length=255)
    url = models.URLField()

    class Meta:
        abstract = True


class Categoria(models.Model):
    rating = models.FloatField()
    tarifaActual = models.DecimalField(max_digits=10, decimal_places=2)
    historialTarifas = models.ArrayField(model_container=HistorialTarifa)
    paquetes = models.ArrayField(model_container=Paquete)

    class Meta:
        abstract = True


# Clase Promotor
# Modelo que representa a un promotor
# se modela la estructura de la colección de promotores


class Promotor(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    redesSociales = models.EmbeddedField(
        model_container=RedesSociales
    )  # Se establece como campo embebido
    categoria = models.EmbeddedField(model_container=Categoria)

    class Meta:
        db_table = (
            "promotores"  # Se establece el nombre de la colección en la base de datos
        )
