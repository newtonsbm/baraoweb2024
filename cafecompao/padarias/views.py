from django.shortcuts import render
from django.http import HttpResponse
from .models import Padaria

# Create your views here.

def home(request): 
    return render(request, 'home.html')

def about(request):
    qtd_padarias = Padaria.objects.count()
    padarias = Padaria.objects.all()
    context = {
        'qtd_padarias': qtd_padarias,
        'padarias': padarias
    }
    return render(request, 'sobre.html', context) 

def contact(request):
    return HttpResponse('Entre em contato')
