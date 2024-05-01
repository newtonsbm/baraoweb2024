from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Padaria, Produto, Cesta

def home(request): 
    qtd_padarias = Padaria.objects.count()
    qtd_produtos = Produto.objects.count()
    qtd_cestas = Cesta.objects.count()
    context = {
        'qtd_padarias': qtd_padarias,
        'qtd_produtos': qtd_produtos,
        'qtd_cestas': qtd_cestas,
    }
    return render(request, 'home.html', context)

def about(request):
    return HttpResponse('Sobre o Café com Pão')

def contact(request):
    return HttpResponse('Entre em contato')

class CestasList(generic.ListView):
    model = Cesta
    template_name = 'padarias/cestas_list.html'
    context_object_name = 'cesta_list'

class CestasDetail(generic.DetailView):
    model = Cesta
    template_name = 'padarias/cestas_detail.html'
    context_object_name = 'cesta'

