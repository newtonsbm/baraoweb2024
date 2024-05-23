from rest_framework import permissions, viewsets
from .. import models

from .serializers import CategoriaSerializer, ProdutoSerializer, CestaSerializer, PadariaSerializer, AssinaturaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = models.Categoria.objects.all()

class ProdutoViewSet(viewsets.ModelViewSet):
    serializer_class = ProdutoSerializer
    queryset = models.Produto.objects.all()

class CestaViewSet(viewsets.ModelViewSet):
    serializer_class = CestaSerializer
    queryset = models.Cesta.objects.all()

class PadariaViewSet(viewsets.ModelViewSet):
    serializer_class = PadariaSerializer
    queryset = models.Padaria.objects.all()

class AssinaturaViewSet(viewsets.ModelViewSet):
    serializer_class = AssinaturaSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return models.Assinatura.objects.filter(user=self.request.user).all()

