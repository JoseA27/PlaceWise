from djongo import models


# Documentación del modelo para la colección de propiedades por promotor
# Modelo que representa las propiedades asignadas a un promotor
# Clases abstractas: Lead sirve para representar los datos de un lead en los campos embebidos de PropiedadPorPromotor
class Lead(models.Model):
    idLead = models.CharField(max_length=255)
    fechaLead = models.DateField()
    nombreLead = models.CharField(max_length=255)
    telefonoLead = models.CharField(max_length=20)
    correoLead = models.EmailField()
    estadoLead = models.CharField(max_length=50)
    comentariosLead = models.TextField()

    class Meta:
        abstract = True  # Se establece como abstracta para que no se cree una colección en la base de datos


# Clase PropiedadPorPromotor
# Modelo que representa las propiedades asignadas a un promotor
# se modela la estructura de la colección de propiedades por promotor


class PropiedadPorPromotor(models.Model):
    idPropiedad = models.IntegerField()
    idPromotor = models.IntegerField()
    idPaquete = models.IntegerField()
    versionPaquete = models.CharField(max_length=50)
    fechaAsignacion = models.DateField()
    fechaVencimiento = models.DateField()
    estadoAsignacion = models.CharField(max_length=50)
    leads = models.ArrayField(model_container=Lead)

    class Meta:
        db_table = "propiedadesPorPromotor"  # nombre de la tabla (collection) en la base de datos para que tenga referencia
