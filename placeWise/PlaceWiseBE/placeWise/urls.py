from django.urls import path
from app.properties.views import (
    PromotorListView,
    PropiedadListView,
    PropiedadesPorPromotorListView,
    HistorialPromotorListView,
    MultimediaPorPropiedadListView,
    SolicitudesPromotorListView,
)

urlpatterns = [
    path("promotores/", PromotorListView.as_view(), name="promotor-list"),
    path("propiedades/", PropiedadListView.as_view(), name="propiedad-list"),
    path(
        "propiedades-por-promotor/",
        PropiedadesPorPromotorListView.as_view(),
        name="propiedades-por-promotor-list",
    ),
    path(
        "historial-promotor/",
        HistorialPromotorListView.as_view(),
        name="historial-promotor-list",
    ),
    path(
        "multimedia-por-propiedad/",
        MultimediaPorPropiedadListView.as_view(),
        name="multimedia-por-propiedad-list",
    ),
    path(
        "solicitudes-promotor/",
        SolicitudesPromotorListView.as_view(),
        name="solicitudes-promotor-list",
    ),
]
