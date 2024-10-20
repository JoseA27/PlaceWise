from rest_framework import serializers
from .models.PromotorModel import Promotor
from .models.PropiedadModel import (
    Propiedad,
    Ubicacion,
    Bitacora,
    Documento,
    Geolocalizacion,
)
from .models.PropiedadesPorPromotor import PropiedadPorPromotor
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
        fields = "__all__"


class PromotorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotor
        fields = "__all__"


class PropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propiedad
        fields = "__all__"


class PropiedadPorPromotorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropiedadPorPromotor
        fields = "__all__"


class SolicitudPromotorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudPromotor
        fields = "__all__"


class MultimediaPorPropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultimediaPorPropiedad
        fields = "__all__"


class HistorialPromotorSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialPromotor
        fields = "__all__"
