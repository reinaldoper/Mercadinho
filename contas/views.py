from django.shortcuts import render, redirect
from .forms import mercadoForm, clienteForm
from .models import Mercado , Cliente
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def newCompras(request):
    num_compras = Mercado.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_compras': num_compras,
        'num_visits': num_visits,
    }

    return render(request, 'compras.html', context = context)


def newMercado(request):
    if request.method == 'POST':
        form = mercadoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = mercadoForm()
        return render(request,'new_mercado.html',{'form':form})


def listaMercado(request):
    list = Mercado.objects.all().order_by('-data')
    paginator = Paginator(list, 3)
    page = request.GET.get('page')
    list = paginator.get_page(page)
    return render(request, 'list_mercado.html',{'list':list})

class clienteCreate(CreateView):
    model = Cliente
    fields = '__all__'
    template_name = 'new_Cliente.html'
    success_url = reverse_lazy('compras')

                



# Create your views here.
