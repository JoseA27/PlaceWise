from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connection
from app.models import Propiedades
from app.serializers import PropiedadesSerializer
import hashlib


from django.core.files.storage import default_storage

# Vista para obtener todas las propiedades 
@csrf_exempt
def propiedades(request,id=0):
    if request.method=='GET':
        propiedades = Propiedades.objects.filter(Ciudad__in=['Alajuela','San José'])
        propiedades_serializer=PropiedadesSerializer(propiedades,many=True)
        return JsonResponse(propiedades_serializer.data,safe=False)
    
@csrf_exempt
def propiedadesParametro(request,id=0):
    if request.method == 'GET':
        ciudades = request.GET.getlist('ciudad')  # Obtener una lista de ciudades desde los parámetros GET
        if ciudades:
            propiedades = Propiedades.objects.using("default").filter(Ciudad__in=ciudades)  # Filtrar propiedades en varias ciudades
        else:
            propiedades = Propiedades.objects.using("default").all()  # Si no hay ciudades en la solicitud, devolver todas las propiedades
        
        propiedades_serializer = PropiedadesSerializer(propiedades, many=True)
        return JsonResponse(propiedades_serializer.data, safe=False)
    
@csrf_exempt
def propiedadesPool(request,id=0):
    if request.method == 'GET':
        ciudades = request.GET.getlist('ciudad')  # Obtener una lista de ciudades desde los parámetros GET
        
        # Usamos una conexión del pool
        with connection.cursor() as cursor:
            if ciudades:
                propiedades = Propiedades.objects.using("pooldb").filter(Ciudad__in=ciudades)  # Filtrar propiedades por ciudades
            else:
                propiedades = Propiedades.objects.using("pooldb").all()  # Si no hay ciudades, obtener todas las propiedades
                
        propiedades_serializer = PropiedadesSerializer(propiedades, many=True)
        return JsonResponse(propiedades_serializer.data, safe=False)



