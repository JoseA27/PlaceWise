from django.contrib import admin
from django.urls import path, include
from app.properties import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "app/", include("app.properties.urls")
    ),  # Incluir las rutas de la app 'appname'
    path("ping/", views.ping, name="ping"),
    path("api/propiedades/", views.get_all_propiedades, name="get_all_propiedades"),
]
