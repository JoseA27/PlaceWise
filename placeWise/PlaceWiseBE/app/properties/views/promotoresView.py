from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from ..services.property_service import PropertyService

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