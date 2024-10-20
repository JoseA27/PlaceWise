from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from ..services.property_service import PropertyService

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