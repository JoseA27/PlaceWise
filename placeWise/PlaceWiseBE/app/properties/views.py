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


# Solicitudes
@csrf_exempt
def solicitudes(request, id=0):
    if request.method == "GET":
        data = PropertyService.get_all_solicitudes()
        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        # Parsear los datos de la solicitud POST
        print(request.body)
        data = JSONParser().parse(request)
        print(data)
        id_vendedor = data.get("idVendedor")
        id_comprador = data.get("idComprador")
        id_propiedad = data.get("idPropiedad")
        estado = data.get("estado")

        # Validar que todos los campos requeridos estén presentes
        if not id_vendedor or not id_comprador or not id_propiedad or not estado:
            return JsonResponse(
                {"error": "Todos los campos son requeridos"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # Crear la solicitud usando el servicio
        solicitud = PropertyService.agregar_solicitud(
            id_vendedor, id_comprador, id_propiedad, estado
        )

        if solicitud:
            return JsonResponse(
                {"message": "Solicitud agregada exitosamente"},
                status=status.HTTP_201_CREATED,
            )
        else:
            return JsonResponse(
                {"error": "Error al agregar la solicitud"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


# Propiedades
@csrf_exempt
def propiedades(request):
    if request.method == "GET":
        propiedades = PropertyService.get_all_propiedades()
        return JsonResponse(propiedades, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        propiedad = PropertyService.agregar_propiedad(data)
        if propiedad:
            return JsonResponse(
                {"message": "Propiedad agregada exitosamente"},
                status=status.HTTP_201_CREATED,
            )
        return JsonResponse(
            {"error": "Error al agregar la propiedad"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


# Promotores
@csrf_exempt
def promotores(request):
    if request.method == "GET":
        promotores = PropertyService.get_all_promotores()
        return JsonResponse(promotores, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        promotor = PropertyService.agregar_promotor(data)
        if promotor:
            return JsonResponse(
                {"message": "Promotor agregado exitosamente"},
                status=status.HTTP_201_CREATED,
            )
        return JsonResponse(
            {"error": "Error al agregar el promotor"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


# Propiedades por Promotor
@csrf_exempt
def propiedades_por_promotor(request):
    if request.method == "GET":
        propiedades_por_promotor = PropertyService.get_all_propiedades_por_promotor()
        return JsonResponse(propiedades_por_promotor, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        propiedad_por_promotor = PropertyService.agregar_propiedad_por_promotor(data)
        if propiedad_por_promotor:
            return JsonResponse(
                {"message": "Propiedad por promotor agregada exitosamente"},
                status=status.HTTP_201_CREATED,
            )
        return JsonResponse(
            {"error": "Error al agregar la propiedad por promotor"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


# Multimedia por Propiedad
@csrf_exempt
def multimedia_por_propiedad(request):
    if request.method == "GET":
        multimedia = PropertyService.get_all_multimedia()
        return JsonResponse(multimedia, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        multimedia = PropertyService.agregar_multimedia(data)
        if multimedia:
            return JsonResponse(
                {"message": "Multimedia agregada exitosamente"},
                status=status.HTTP_201_CREATED,
            )
        return JsonResponse(
            {"error": "Error al agregar la multimedia"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


# Historial Promotor
@csrf_exempt
def historial_promotor(request):
    if request.method == "GET":
        historial = PropertyService.get_all_historial_promotor()
        return JsonResponse(historial, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        historial = PropertyService.agregar_historial_promotor(data)
        if historial:
            return JsonResponse(
                {"message": "Historial agregado exitosamente"},
                status=status.HTTP_201_CREATED,
            )
        return JsonResponse(
            {"error": "Error al agregar el historial"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
