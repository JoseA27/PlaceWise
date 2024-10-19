from rest_framework import serializers

# from .models.PromotorModel import Promotor
from .models.PropiedadModel import Propiedad
from .models.PropiedadesPorPromotor import PropiedadesPorPromotor
from .models.SolicitudesPromotor import Solicitud
from .models.MultimediaPorPropiedad import MultimediaPorPropiedad
from .models.HistorialPromotor import HistorialPromotor

from .models.PromotorModel import (
    Promotor,
    Categoria,
    HistorialTarifas,
    RedesSociales,
    Paquete,
)


class RedesSocialesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedesSociales
        fields = "__all__"


class HistorialTarifasSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialTarifas
        fields = "__all__"


class PaqueteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paquete
        fields = "__all__"


class CategoriaSerializer(serializers.ModelSerializer):
    historialTarifas = HistorialTarifasSerializer(many=True)
    paquetes = PaqueteSerializer(many=True)

    class Meta:
        model = Categoria
        fields = "__all__"


class PromotorSerializer(serializers.ModelSerializer):
    redesSociales = RedesSocialesSerializer()
    categoria = CategoriaSerializer()

    class Meta:
        model = Promotor
        fields = "__all__"


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


class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = (
            "idSolicitud",  # Usando el nombre original
            "idVendedor",
            "idComprador",
            "idPropiedad",
            "fechaSolicitud",
            "status",
        )
