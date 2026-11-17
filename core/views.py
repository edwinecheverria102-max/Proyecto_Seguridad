from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import get_user_model, login, logout
from django.db import IntegrityError
from .models import Usuario

User = get_user_model()

def index(request):
    # Simulacion dela Base de Datos
    productos_falsos = [
        {'id': 1, 'nombre': 'Manual Python Avanzado', 'precio': 25.00, 'formato': 'PDF', 'imagen': 'img/ebook.jpg'},
        {'id': 2, 'nombre': 'Apuntes de Redes', 'precio': 10.00, 'formato': 'PDF/ZIP', 'imagen': 'img/redes-info.jpg'},
    ]
    return render(request, 'core/index.html', {'productos': productos_falsos})

# creado para la visualizacion del diseño login/register
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email") or request.POST.get("username")
        password = request.POST.get("password")

        if not email or not password:
            return render(request, "core/login.html", {"error": "Completa todos los campos."})

        auth_user = User.objects.filter(email__iexact=email).first()
        if auth_user and auth_user.check_password(password):
            login(request, auth_user)
            request.session["user_id"] = auth_user.id
            request.session["user_name"] = auth_user.get_full_name() or auth_user.username
            return redirect("core:index")

        usuario = Usuario.objects.filter(email__iexact=email).first()
        if usuario and check_password(password, usuario.password_hash):
            request.session["user_id"] = usuario.id
            request.session["user_name"] = usuario.nombre
            return redirect("core:index")

        return render(request, "core/login.html", {"error": "Correo o contraseña incorrectos."})

    return render(request, "core/login.html")

def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect("core:index")


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

def product_detail_view(request, pk):
    # backend busca el producto en la base de datos con ese 'pk'
    # producto = Product.objects.get(id=pk)
    return render(request, 'core/product.html')

def cart_view(request):
    return render(request, 'core/cart.html')

def checkout_view(request):
    return render(request, 'core/checkout.html')

def receipt_view(request):
    return render(request, 'core/receipt.html')

def download_view(request):
    return render(request, 'core/download.html')

def profile_view(request):
    return render(request, 'core/profile.html')

def operator_dashboard_view(request):
    return render(request, 'core/operator_dashboard.html')

def admin_dashboard_view(request):
    return render(request, 'core/admin_dashboard.html')

def product_form_view(request):
    return render(request, 'core/product_form.html')