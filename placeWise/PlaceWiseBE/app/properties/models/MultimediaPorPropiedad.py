from djongo import models


class Multimedia(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fechaSubida = models.DateField()
    usuarioSubida = models.CharField(max_length=255)
    url = models.URLField()

    class Meta:
        abstract = True


class MultimediaPorPropiedad(models.Model):
    idPropiedad = models.IntegerField()
    idPromotor = models.IntegerField()
    imagenes = models.ArrayField(model_container=Multimedia)
    videos = models.ArrayField(model_container=Multimedia)
    modelos3D = models.ArrayField(model_container=Multimedia)

    class Meta:
        db_table = "multimediaPorPropiedad"
