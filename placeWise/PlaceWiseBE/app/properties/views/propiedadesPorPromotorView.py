from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from ..services.property_service import PropertyService

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
