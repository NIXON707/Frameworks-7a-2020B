from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    #return HttpResponse("::: Welcome, this is our first VIEW :::")
    return render(request, 'index.html', {})

def listar_categorias(request):
    return HttpResponse("::: LISTADO DE CATEGORIAS :::")

def listar_productos(request):
    return HttpResponse("::: LISTADO DE PRODUCTOS :::")