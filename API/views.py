from rest_framework import viewsets
from .models import Cliente, Veiculos, Entrada
from .serializer import ClienteSerializer, VeiculoSerializer, EntradaSerializer


class ClientesViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os clientes'''

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class VeiculosViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os veiculos'''

    queryset = Veiculos.objects.all()
    serializer_class = VeiculoSerializer


class EntradaViewSet(viewsets.ModelViewSet):
    '''Listando Entradas'''
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer


class ListaPatio(viewsets.ModelViewSet):
    '''Listando todos os veiculos no patio'''
    queryset = Entrada.objects.filter(status='A')
    serializer_class = EntradaSerializer
    http_method_names = ['get']
