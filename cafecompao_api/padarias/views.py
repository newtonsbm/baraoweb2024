from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Padaria, Cesta, Assinatura

def principal(request):
    return render(request, 'padarias/principal.html')

def sobre(request):
    mensagem_enviada = False
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        if nome and email and mensagem:
            print('Formulário válido')
            print("Enviando email...")
            print(f"Nome: {nome}")
            print(f"E-mail: {email}")
            print(f"Mensagem: {mensagem}")
            mensagem_enviada = True
    context = {
        'mensagem_enviada': mensagem_enviada,
    }
    return render(request, 'padarias/sobre.html', context)

class PadariasList(ListView):
    model = Padaria
    template_name = 'padarias/list_padarias.html'
    paginate_by = 2

class CestasList(ListView):
    model = Cesta
    template_name = 'padarias/list_cestas.html'

class CestasDetail(DetailView):
    model = Cesta
    template_name = 'padarias/detail_cestas.html'

# PAGINAS LOGADAS

@login_required
def minha_conta(request):
    return render(request, 'padarias/minha_conta.html')

class AssinaturaCreate(CreateView):
    model = Assinatura
    template_name = 'padarias/assinatura_form.html'
    fields = ['cesta', 'observacao']
    success_url = reverse_lazy('minha_conta')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Assinatura realizada com sucesso!')
        return super().form_valid(form)

class AssinaturaUpdate(UpdateView):
    model = Assinatura
    template_name = 'padarias/assinatura_form_edit.html'
    fields = ['cesta', 'observacao']
    success_url = reverse_lazy('minha_conta')

    def form_valid(self, form):
        messages.success(self.request, 'Assinatura atualizada com sucesso!')
        return super().form_valid(form)

class AssinaturaDelete(DeleteView):
    model = Assinatura
    template_name = 'padarias/assinatura_cancelar.html'
    success_url = reverse_lazy('minha_conta')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Assinatura cancelada com sucesso!')
        return super().delete(request, *args, **kwargs)