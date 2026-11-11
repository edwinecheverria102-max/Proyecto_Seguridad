from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.db import IntegrityError
from .models import Usuario

def index(request):
    return render(request, 'core/index.html')

# creado para la visualizacion del diseño login/register
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email or not password:
            return render(request, "core/login.html", {"error": "Completa todos los campos."})

        usuario = Usuario.objects.filter(email=email).first()

        if usuario and check_password(password, usuario.password_hash):
            request.session["user_id"] = usuario.id
            request.session["user_name"] = usuario.nombre
            return redirect("core:index")  # requiere que en urls tengas name="index"

        return render(request, "core/login.html", {"error": "Correo o contraseña incorrectos."})

    return render(request, "core/login.html")

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
            # .create() instancia el objeto y lo guarda en SQLite/MySQL en un solo paso
            Usuario.objects.create(
                nombre=name,
                email=email,
                password_hash=make_password(password1),
                rol="usuario",
                status="activo"
            )
            
            return redirect("core:login")
        except Exception as e:
            # Para tu flujo de trabajo en la terminal, imprime el error para ver la traza exacta
            print(f"Error de base de datos en registro: {e}")
            return render(request, "core/register.html", {"error": f"Error al registrar: {e}"})
            
    return render(request, 'core/register.html')