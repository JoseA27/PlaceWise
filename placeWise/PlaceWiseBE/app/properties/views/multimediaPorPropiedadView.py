from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from ..services.property_service import PropertyService

# Multimedia por Propiedad
@csrf_exempt
async def multimedia_por_propiedad(request):
    if request.method == "GET":
        multimedia = await PropertyService.get_all_multimedia()
        return JsonResponse(multimedia, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        multimedia = await PropertyService.agregar_multimedia(data)
        if multimedia:
            return JsonResponse(
                {"message": "Multimedia agregada exitosamente"},
                status=status.HTTP_201_CREATED,
            )
        return JsonResponse(
            {"error": "Error al agregar la multimedia"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
