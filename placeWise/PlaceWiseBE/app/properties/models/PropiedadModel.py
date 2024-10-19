from djongo import models


class Geolocalizacion(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()

    class Meta:
        abstract = True


class Ubicacion(models.Model):
    idContry = models.IntegerField()
    idState = models.IntegerField()
    idCity = models.IntegerField()
    direccion = models.CharField(max_length=255)
    geolocalizacion = models.EmbeddedField(model_container=Geolocalizacion)

    class Meta:
        abstract = True


class Bitacora(models.Model):
    fechaEvento = models.DateField()
    tipoEvento = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    descripcion = models.TextField()
    usuarioResponsable = models.CharField(max_length=255)

    class Meta:
        abstract = True


class Documento(models.Model):
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    fechaEmision = models.DateField()
    fechaVencimiento = models.DateField()
    emitidoPor = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    url = models.URLField()

    class Meta:
        abstract = True


class Propiedad(models.Model):
    id = models.IntegerField()
    idPromotorActual = models.IntegerField()
    titulo = models.CharField(max_length=255)
    ubicacion = models.EmbeddedField(model_container=Ubicacion)
    descripcion = models.TextField()
    estatus = models.CharField(max_length=50)
    bitacora = models.ArrayField(model_container=Bitacora)
    documentos = models.ArrayField(model_container=Documento)

    class Meta:
        db_table = 'propiedades'
