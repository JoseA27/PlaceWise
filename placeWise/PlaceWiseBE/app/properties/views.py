from rest_framework import generics
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
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
    
    elif request.method == 'POST':
        # Parsear los datos de la solicitud POST
        print(request.body)
        data = JSONParser().parse(request)
        print(data)
        id_vendedor = data.get('idVendedor')
        id_comprador = data.get('idComprador')
        id_propiedad = data.get('idPropiedad')
        estado = data.get('estado')

        # Validar que todos los campos requeridos estén presentes
        if not id_vendedor or not id_comprador or not id_propiedad or not estado:
            return JsonResponse({'error': 'Todos los campos son requeridos'}, status=status.HTTP_400_BAD_REQUEST)
        # Crear la solicitud usando el servicio
        solicitud = PropertyService.agregar_solicitud(id_vendedor, id_comprador, id_propiedad, estado)

        if solicitud:
            return JsonResponse({'message': 'Solicitud agregada exitosamente'}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'error': 'Error al agregar la solicitud'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
def obtener_propiedades(request):
    if request.method == 'GET':
        propiedades = PropertyService.obtener_todas_propiedades()
        return JsonResponse(propiedades, safe=False)