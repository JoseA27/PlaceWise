from rest_framework import serializers
from .models.PromotorModel import Promotor
from .models.PropiedadModel import Propiedad, Ubicacion, Bitacora, Documento, Geolocalizacion
from .models.PropiedadesPorPromotor import PropiedadesPorPromotor
from .models.SolicitudesPromotor import SolicitudPromotor
from .models.MultimediaPorPropiedad import MultimediaPorPropiedad
from .models.HistorialPromotor import HistorialPromotor


class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudPromotor
        fields = (
            "idSolicitud",  # Usando el nombre original
            "idVendedor",
            "idComprador",
            "idPropiedad",
            "fechaSolicitud",
            "status",
        )
class PropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propiedad
        fields = '__all__'