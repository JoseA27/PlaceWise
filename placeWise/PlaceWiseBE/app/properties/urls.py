from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('solicitudes/', views.solicitudes, name='solicitudes'),
    path('propiedades/', views.obtener_propiedades, name='propiedades'),
]