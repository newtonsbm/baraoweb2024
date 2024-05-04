from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required 
from .models import Padaria, Produto, Cesta, Email

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
    qtd_padarias = Padaria.objects.count()
    padarias = Padaria.objects.all()
    msg_enviada = False
    consulta = request.GET.get('consulta')
    print(consulta)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        Email.objects.create(nome=nome, email=email, mensagem=mensagem)
        print("--Enviando email-------------------------")
        print(f"Nome: {nome}, Email: {email}, Mensagem: {mensagem}")
        print("-----------------------------------------")
        msg_enviada = True 
    context = {
        'qtd_padarias': qtd_padarias,
        'padarias': padarias,
        'msg_enviada': msg_enviada
    }
    return render(request, 'sobre.html', context) 

def contact(request):
    return HttpResponse('Entre em contato')

def cestas_list(request):
    """
    Função que retorna a lista de cestas
    equivalente a classe CestasList
    """
    cestas = Cesta.objects.all()
    context = {
        'cestas': cestas
    }
    return render(request, 'padarias/cestas_list.html', context)

class CestasList(generic.ListView):
    model = Cesta
    template_name = 'padarias/cestas_list.html'
    context_object_name = 'cestas'

def cestas_detail(request, pk):
    """
    Função que retorna o detalhe de uma cesta
    equivalente a classe CestasDetail
    """
    cesta = get_object_or_404(Cesta, pk=pk)
    context = {
        'cesta': cesta
    }
    return render(request, 'padarias/cestas_detail.html', context)

class CestasDetail(generic.DetailView):
    model = Cesta
    template_name = 'padarias/cestas_detail.html'
    context_object_name = 'cesta'


@login_required
def minha_conta(request):
    return render(request, 'padarias/minha_conta.html')

class PadariasList(generic.ListView):
    model = Padaria
    template_name = 'padarias/padarias_list.html'
    context_object_name = 'padarias'

