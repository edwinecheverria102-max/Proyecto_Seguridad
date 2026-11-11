from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from .models import Usuario

def index(request):
    return render(request, 'core/index.html')

# creado para la visualizacion del diseño login/register
def login_view(request):
    return render(request, 'core/login.html')

def register_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if not name or not email or not password1 or not password2:
            return render(request, "core/register.html", {"error": "Completa todos los campos."})

        if password1 != password2:
            return render(request, "core/register.html", {"error": "Las contraseñas no coinciden."})

        if Usuario.objects.filter(email=email).exists():
            return render(request, "core/register.html", {"error": "Este correo ya está registrado."})

        try:
            Usuario.objects.create(
                nombre=name,
                email=email,
                password_hash=make_password(password1),
                rol="usuario",
                status="activo"
            )
            return redirect("core:login")
        except Exception as e:
            return render(request, "core/register.html", {"error": f"Error al registrar: {e}"})
    return render(request, 'core/register.html')