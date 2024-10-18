from rest_framework import serializers
from .models.PropiedadModel import Propiedad  # Importa el modelo de propiedades


class PropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propiedad
        fields = "__all__"  # Incluye todos los campos del modelo
