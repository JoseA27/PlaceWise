from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("solitudes/", views.solicitudes, name="solicitudes"),
    path("promotores/", views.promotores, name="promotores"),
]
