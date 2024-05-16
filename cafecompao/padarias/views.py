import datetime
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login

from .models import Padaria, Email, Cesta, Assinatura, Produto


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

class AssinaturaCreateView(LoginRequiredMixin, generic.CreateView):
    model = Assinatura
    fields = ['cesta', 'observacao']
    template_name = 'padarias/assinatura_form.html'
    success_url = reverse_lazy('minha_conta')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.data_inicio = datetime.date.today()
        messages.success(message="Assinatura realizada com sucesso!", request=self.request)
        return super().form_valid(form)

class AssinaturaUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Assinatura
    fields = ['cesta', 'observacao']
    template_name = 'padarias/assinatura_form_update.html'
    success_url = reverse_lazy('minha_conta')

    def form_valid(self, form):
        messages.success(message="Assinatura alterada com sucesso!", request=self.request)
        return super().form_valid(form)

class AssinaturaDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Assinatura
    template_name = 'padarias/assinatura_cancelar.html'
    context_object_name = 'assinatura'
    success_url = reverse_lazy('minha_conta')

    def form_valid(self, form):
        messages.success(message="Assinatura cancelada com sucesso!", request=self.request)
        return super().form_valid(form)


# ATIVIDADE 9 e 10

def nova_conta(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        nome = request.POST.get('nome')
        first_name = nome.split(' ')[0]
        last_name = ' '.join(nome.split(' ')[1:])
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        # validacao
        erro = None
        if password != password2:
            erro = 'Senhas não coincidem.'
        if User.objects.filter(username=username).exists():
            erro = 'Nome de usuário já existente.'
        if User.objects.filter(email=email).exists():
            erro = 'Email já cadastrado.'
        if erro:
            return render(request, 'registration/nova_conta.html', {'erro': erro})

        # Criar usuário e logar e redirecionar para minha conta
        try:
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            login(request, user)
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('minha_conta')
        except Exception as e:
            erro = str(e)
            print(erro)
            return render(request, 'registration/nova_conta.html', {'erro': erro})
    return render(request, 'registration/nova_conta.html')
