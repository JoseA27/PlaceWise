from djongo import models

# Documentación del modelo MultimediaPorPropiedad
# Modelo que representa el multimedia asociado a una propiedad
# Clases abstractas: Multimedia sirve para representar los datos de un archivo multimedia
# en los campos embebidos de MultimediaPorPropiedad


class Multimedia(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fechaSubida = models.DateField()
    usuarioSubida = models.CharField(max_length=255)
    url = models.URLField()

    class Meta:
        abstract = True


# Clase MultimediaPorPropiedad
# Modelo que representa el multimedia asociado a una propiedad
class MultimediaPorPropiedad(models.Model):
    idPropiedad = models.IntegerField()
    idPromotor = models.IntegerField()
    imagenes = models.ArrayField(model_container=Multimedia)
    videos = models.ArrayField(model_container=Multimedia)
    modelos3D = models.ArrayField(model_container=Multimedia)

    class Meta:
        db_table = "multimediaPorPropiedad"  # nombre de la tabla (collection) en la base de datos para que tenga referencia
