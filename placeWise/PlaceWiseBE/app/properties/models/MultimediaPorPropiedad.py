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
    idPropiedad = models.CharField(max_length=255)
    idPromotor = models.CharField(max_length=255)
    imagenes = models.ArrayField(model_container=Multimedia)
    videos = models.ArrayField(model_container=Multimedia)
    modelos3D = models.ArrayField(model_container=Multimedia)

    def __str__(self):
        return f"Multimedia para propiedad {self.idPropiedad}"
