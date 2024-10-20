from django.urls import path
from django.contrib import admin
from .views import (
    solicitudes,
    propiedades,
    promotores,
    propiedades_por_promotor,
    multimedia_por_propiedad,
    historial_promotor,
)

urlpatterns = [
    path("solicitudes/", solicitudes, name="solicitudes"),
    path("propiedades/", propiedades, name="propiedades"),
    path("promotores/", promotores, name="promotores"),
    path(
        "propiedadesporpromotor/",
        propiedades_por_promotor,
        name="propiedades_por_promotor",
    ),
    path(
        "multimedia_por_propiedad/",
        multimedia_por_propiedad,
        name="multimedia_por_propiedad",
    ),
    path("historial_promotor/", historial_promotor, name="historial_promotor"),
]
