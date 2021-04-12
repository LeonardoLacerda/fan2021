from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Venda, Produto
from django.urls import reverse_lazy
# Create your views here.


class VendaListView(ListView):
    model = Venda
    template_name = 'listar/venda.html'




class VendaCreateView(CreateView):
    model = Venda
    template_name = 'cadastrar/venda.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy("cadastrar_venda")


class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'cadastrar/produto.html'

    # Caso eu queira que sejam cadastrados todos os fields do meu Model você colocará o fields = '__all__'
    # Caso queira especificar, colocar da forma abaixo. Por exemplo, se quiser apenas nome colocar fields = ['nome']
    fields = ['nome', 'valor']

    def get_success_url(self):
        return reverse_lazy('cadastrar_produto')

