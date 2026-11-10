from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

# creado para la visualizacion del diseño login/register
def login_view(request):
    return render(request, 'core/login.html')

def register_view(request):
    return render(request, 'core/register.html')