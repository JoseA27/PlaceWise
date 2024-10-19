from rest_framework import serializers
from .models.PromotorModel import Promotor
from .models.PropiedadModel import Propiedad, Ubicacion, Bitacora, Documento, Geolocalizacion
from .models.PropiedadesPorPromotor import PropiedadesPorPromotor
from .models.SolicitudesPromotor import SolicitudPromotor
from .models.MultimediaPorPropiedad import MultimediaPorPropiedad
from .models.HistorialPromotor import HistorialPromotor


"""
class PromotorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotor
        fields = (
            "nombre",
            "categoria",
            "tarifa",
            "asignaciones",  # lista de propiedades asignadas al promotor
            "redesSociales",  # lista de redes sociales
            "fecha_de_registro",
        )


class PropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propiedad
        fields = (
            "ID_de_Propiedad",
            "ubicacion",  # puede incluir latitud y longitud
            "tipo_de_propiedad",
            "precio",
            "descripcion",
            "estado",
        )


class PropiedadesPorPromotorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropiedadesPorPromotor
        fields = (
            "promotor",  # relación con el promotor
            "propiedad",  # relación con la propiedad
            "fecha_de_asignacion",
            "estado_de_asignacion",
        )


class HistorialPromotorSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialPromotor
        fields = (
            "promotor",
            "fecha",
            "evento",  # descripción del evento en el historial
            "detalles",  # detalles adicionales del historial
        )


class MultimediaPorPropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultimediaPorPropiedad
        fields = (
            "propiedad",
            "archivo",  # nombre del archivo multimedia
            "tipo",  # tipo de multimedia (imagen, video, etc.)
            "subido_por",
            "fecha_de_subida",
        )


class SolicitudesPromotorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = (
            "promotor",
            "solicitud",  # descripción de la solicitud
            "estado",  # estado de la solicitud (pendiente, aceptada, etc.)
            "fecha_de_solicitud",
       ) """

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