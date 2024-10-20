from djongo import models


# Documentación del modelo para la colección de propiedades
# Modelo que representa a una propiedad
# Clases abstractas: Geolocalizacion, Ubicacion, Bitacora, Documento sirven para representar los datos de la geolocalización,
# ubicación, bitácora y documentos respectivamente en los campos embebidos de Propiedad
class Geolocalizacion(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()

    class Meta:
        abstract = True  # Se establece como abstracta para que no se cree una colección en la base de datos


class Ubicacion(models.Model):
    idContry = models.IntegerField()
    idState = models.IntegerField()
    idCity = models.IntegerField()
    direccion = models.CharField(max_length=255)
    geolocalizacion = models.EmbeddedField(model_container=Geolocalizacion)

    class Meta:
        abstract = True  # Se establece como abstracta para que no se cree una colección en la base de datos


class Bitacora(models.Model):
    fechaEvento = models.DateField()
    tipoEvento = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    descripcion = models.TextField()
    usuarioResponsable = models.CharField(max_length=255)

    class Meta:
        abstract = True  # Se establece como abstracta para que no se cree una colección en la base de datos


class Documento(models.Model):
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    fechaEmision = models.DateField()
    fechaVencimiento = models.DateField()
    emitidoPor = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    url = models.URLField()

    class Meta:
        abstract = True  # Se establece como abstracta para que no se cree una colección en la base de datos


# Clase Propiedad
# Modelo que representa a una propiedad
# se modela la estructura de la colección de propiedades
# se establece la tabla (collection) en la base de datos para que tenga referencia


class Propiedad(models.Model):
    id = models.IntegerField()
    idPromotorActual = models.IntegerField()
    titulo = models.CharField(max_length=255)
    ubicacion = models.EmbeddedField(
        model_container=Ubicacion
    )  # campo embebido de Ubicacion
    descripcion = models.TextField()
    estatus = models.CharField(max_length=50)
    bitacora = models.ArrayField(model_container=Bitacora)  # campo embebido de Bitacora
    documentos = models.ArrayField(
        model_container=Documento
    )  # campo embebido de Documento

    class Meta:
        db_table = "propiedades"  # nombre de la tabla (collection) en la base de datos para que tenga referencia
