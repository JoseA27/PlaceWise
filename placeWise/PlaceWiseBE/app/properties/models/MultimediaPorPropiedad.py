from djongo import models


class Imagen(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fechaSubida = models.DateField()
    usuarioSubida = models.CharField(max_length=255)
    url = models.URLField()

    class Meta:
        abstract = True


class Video(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fechaSubida = models.DateField()
    usuarioSubida = models.CharField(max_length=255)
    url = models.URLField()

    class Meta:
        abstract = True


class Modelo3D(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fechaSubida = models.DateField()
    usuarioSubida = models.CharField(max_length=255)
    url = models.URLField()

    class Meta:
        abstract = True


class MultimediaPorPropiedad(models.Model):
    idPropiedad = models.CharField(max_length=255)
    idPromotor = models.CharField(max_length=255)
    imagenes = models.ArrayField(model_container=Imagen)
    videos = models.ArrayField(model_container=Video)
    modelos3D = models.ArrayField(model_container=Modelo3D)

    class Meta:
        db_table = 'historialPromotor'
