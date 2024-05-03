from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Padaria

# Create your views here.

def home(request): 
    return render(request, 'home.html')

def about(request):
    qtd_padarias = Padaria.objects.count()
    padarias = Padaria.objects.all()
    msg_enviada = False
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        print("--Enviando email-------------------------")
        print(f"Nome: {nome}, Email: {email}, Mensagem: {mensagem}")
        print("-----------------------------------------")
        msg_enviada = True 
    context = {
        'qtd_padarias': qtd_padarias,
        'padarias': padarias,
        'msg_enviada': msg_enviada,
    }
    return render(request, 'sobre.html', context) 

def contact(request):
    return HttpResponse('Entre em contato')
