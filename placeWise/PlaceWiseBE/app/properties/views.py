from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connection

# from app.models import Propiedades
# from app.serializers import PropiedadesSerializer
import hashlib


from django.core.files.storage import default_storage
from django.http import JsonResponse


def ping(request):
    return JsonResponse({"message": "pong"}, status=200)
