from rest_framework import generics


from django.core.cache import cache
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connection
import hashlib

from .models.PromotorModel import Promotor
from .models.PropiedadModel import Propiedad
from .models.PropiedadesPorPromotor import PropiedadesPorPromotor
from .models.HistorialPromotor import HistorialPromotor
from .models.MultimediaPorPropiedad import MultimediaPorPropiedad
from .models.SolicitudesPromotor import Solicitud
from .serializers import (
    PromotorSerializer,
    PropiedadSerializer,
    PropiedadesPorPromotorSerializer,
    HistorialPromotorSerializer,
    MultimediaPorPropiedadSerializer,
    SolicitudSerializer,
)


@csrf_exempt
def solicitudes(request, id=0):
    if request.method == "GET":
        solicitudes = Solicitud.objects.all()
        solicitudes_serializer = SolicitudSerializer(solicitudes, many=True)
        return JsonResponse(solicitudes_serializer.data, safe=False)


@csrf_exempt
def promotores(request):
    if request.method == "GET":
        promotores = Promotor.objects.all()
        promotores_serializer = PromotorSerializer(promotores, many=True)
        return JsonResponse(promotores_serializer.data, safe=False)


class PropiedadListView(generics.ListAPIView):
    queryset = Propiedad.objects.all()
    serializer_class = PropiedadSerializer


class PropiedadesPorPromotorListView(generics.ListAPIView):
    queryset = PropiedadesPorPromotor.objects.all()
    serializer_class = PropiedadesPorPromotorSerializer


class HistorialPromotorListView(generics.ListAPIView):
    queryset = HistorialPromotor.objects.all()
    serializer_class = HistorialPromotorSerializer


class MultimediaPorPropiedadListView(generics.ListAPIView):
    queryset = MultimediaPorPropiedad.objects.all()
    serializer_class = MultimediaPorPropiedadSerializer
