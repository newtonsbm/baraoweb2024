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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include 
from padarias import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('sobre', views.about, name='about'),
    path('padarias', views.PadariasList.as_view(), name='padarias_list'),
    path('cestas', views.CestasList.as_view(), name='cestas_list'),
    path('cestas/<uuid:pk>/', views.CestasDetail.as_view(), name='cestas_detail'),
    path('minha_conta', views.minha_conta, name='minha_conta'),
    path('nova_conta', views.nova_conta, name='nova_conta'),
    # ATIVIDADE 9 e 10
    path('assinaturas/criar', views.AssinaturaCreateView.as_view(), name='assinatura_create'),
    path('assinaturas/<pk>/editar', views.AssinaturaUpdateView.as_view(), name='assinatura_update'), 
    path('assinaturas/<pk>/cancelar', views.AssinaturaDeleteView.as_view(), name='assinatura_delete'), # nova linha
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

