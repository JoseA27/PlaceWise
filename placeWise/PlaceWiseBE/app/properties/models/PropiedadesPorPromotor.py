from djongo import models


class Lead(models.Model):
    idLead = models.CharField(max_length=255)
    fechaLead = models.DateField()
    nombreLead = models.CharField(max_length=255)
    telefonoLead = models.CharField(max_length=20)
    correoLead = models.EmailField()
    estadoLead = models.CharField(max_length=50)
    comentariosLead = models.TextField()

    class Meta:
        abstract = True


class PropiedadesPorPromotor(models.Model):
    idPropiedad = models.CharField(max_length=255)
    idPromotor = models.CharField(max_length=255)
    idPaquete = models.IntegerField()
    versionPaquete = models.CharField(max_length=50)
    fechaAsignacion = models.DateField()
    fechaVencimiento = models.DateField()
    estadoAsignacion = models.CharField(max_length=50)
    leads = models.ArrayField(model_container=Lead)
