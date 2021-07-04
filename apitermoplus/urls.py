from django.contrib import admin
from django.db import router
from django.urls import path, include
from rest_framework import routers
from API.views import ClientesViewSet, VeiculosViewSet, ListaPatio, EntradaViewSet

router = routers.DefaultRouter()
router.register('clientes', ClientesViewSet, basename='Clientes')
router.register('veiculos', VeiculosViewSet, basename='Veiculos')
router.register('entrada', EntradaViewSet, basename='Entrada')
router.register('patio', ListaPatio, basename='Patio')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
