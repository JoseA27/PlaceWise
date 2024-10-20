from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from ..services.property_service import PropertyService

# Historial Promotor
@csrf_exempt
async def historial_promotor(request):
    if request.method == "GET":
        historial = await PropertyService.get_all_historial_promotor()
        return JsonResponse(historial, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        historial = await PropertyService.agregar_historial_promotor(data)
        if historial:
            return JsonResponse(
                {"message": "Historial agregado exitosamente"},
                status=status.HTTP_201_CREATED,
            )
        return JsonResponse(
            {"error": "Error al agregar el historial"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
