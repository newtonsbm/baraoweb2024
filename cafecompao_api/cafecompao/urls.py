"""
URL configuration for cafecompao project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from padarias import views
from padarias.api import views as api_views 

from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = routers.DefaultRouter()
router.register(r'categorias', api_views.CategoriaViewSet, basename='categorias')
router.register(r'produtos', api_views.ProdutoViewSet, basename='produtos')
router.register(r'cestas', api_views.CestaViewSet, basename='cestas')
router.register(r'padarias', api_views.PadariaViewSet, basename='padarias')
router.register(r'assinaturas', api_views.AssinaturaViewSet, basename='assinaturas')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("django.contrib.auth.urls")),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('', views.principal, name='principal'),
    path('sobre/', views.sobre, name='sobre'),
    path('padarias/', views.PadariasList.as_view(), name='padarias_list'),
    path('cestas/', views.CestasList.as_view(), name='cestas_list'),
    path('cestas/<pk>/', views.CestasDetail.as_view(), name='cestas_detail'),
    path('assinaturas/criar', views.AssinaturaCreate.as_view(), name='assinaturas_create'),
    path('assinaturas/<pk>/editar', views.AssinaturaUpdate.as_view(), name='assinaturas_update'),
    path('assinaturas/<pk>/cancelar', views.AssinaturaDelete.as_view(), name='assinaturas_delete'),
    path('minha_conta/', views.minha_conta, name='minha_conta'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






