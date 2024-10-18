from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connection

# from app.models import Propiedades
# from app.serializers import PropiedadesSerializer
import hashlib


from django.core.files.storage import default_storage
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models.PropiedadModel import Propiedad  # Importa el modelo
from .serializers import PropiedadSerializer


def ping(request):
    return JsonResponse({"message": "pong"}, status=200)


@api_view(["GET"])
def get_all_propiedades(request):
    try:
        # Recupera todas las propiedades
        propiedades = Propiedad.objects.all()
        # Serializa los datos
        serializer = PropiedadSerializer(propiedades, many=True)
        # Devuelve la respuesta en formato JSON
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
