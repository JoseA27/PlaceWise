from rest_framework import generics
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connection
import hashlib
"""from .models.PromotorModel import Promotor
from .models.PropiedadModel import Propiedad
from .models.PropiedadesPorPromotor import PropiedadesPorPromotor
from .models.HistorialPromotor import HistorialPromotor
from .models.MultimediaPorPropiedad import MultimediaPorPropiedad"""
from .services.property_service import PropertyService


@csrf_exempt
def solicitudes(request,id=0):
    if request.method=='GET':
        data = PropertyService.get_all_solicitudes()
        return JsonResponse(data, safe=False)


"""
class PromotorListView(generics.ListAPIView):
    queryset = Promotor.objects.all()
    serializer_class = PromotorSerializer

    def get(self, request, *args, **kwargs):
        print(self.queryset)  # Depuración
        return super().get(request, *args, **kwargs)


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


class SolicitudesPromotorListView(generics.ListAPIView):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudesPromotorSerializer
"""