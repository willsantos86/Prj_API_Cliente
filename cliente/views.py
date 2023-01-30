from rest_framework import viewsets
from cliente.serializers import ClienteSerializer
from cliente.models import Cliente

class ClienteViewSet(viewsets.ModelViewSet):
    """Listando todos os clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

