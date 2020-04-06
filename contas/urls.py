from django.urls import path
from .import views

urlpatterns = [
   path('', views.newCompras, name='compras'),
   path('newmercado/', views.newMercado, name="new-mercado"),
   path('newCliente/', views.clienteCreate.as_view(), name="new-cliente"),
    path('lista/', views.listaMercado, name='lista-mercado'),
] 
