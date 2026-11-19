from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import get_user_model, login, logout
from django.db import IntegrityError
from django.db.models import F
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from .models import ItemCarrito, Producto, Usuario

User = get_user_model()

def index(request):
    return render(request, 'core/index.html')

# creado para la visualizacion del diseño login/register
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email") or request.POST.get("username")
        password = request.POST.get("password")

        if not email or not password:
            print("Login fallido: faltan campos obligatorios.")
            return render(request, "core/login.html", {"error": "Completa todos los campos."})

        auth_user = User.objects.filter(email__iexact=email).first()
        if auth_user and auth_user.check_password(password):
            login(request, auth_user)
            request.session.pop("cart_user_id", None)
            request.session["user_id"] = auth_user.id
            request.session["user_name"] = auth_user.get_full_name() or auth_user.username
            print("Login exitoso.")
            return redirect("core:index")

        usuario = Usuario.objects.filter(email__iexact=email).first()
        if usuario and check_password(password, usuario.password_hash):
            request.session["cart_user_id"] = usuario.id
            request.session["user_id"] = usuario.id
            request.session["user_name"] = usuario.nombre
            print("Login exitoso.")
            return redirect("core:index")

        print("Login fallido: correo o contraseña incorrectos.")
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
            print("Registro fallido: faltan campos obligatorios.")
            return render(request, "core/register.html", {"error": "Completa todos los campos."})

        if password1 != password2:
            print("Registro fallido: las contraseñas no coinciden.")
            return render(request, "core/register.html", {"error": "Las contraseñas no coinciden."})

        if Usuario.objects.filter(email=email).exists():
            print("Registro fallido: el correo ya está registrado.")
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
            print("Registro exitoso.")
            return redirect("core:login")
        except Exception as e:
            # Para tu flujo de trabajo en la terminal, imprime el error para ver la traza exacta
            print(f"Error de base de datos en registro: {e}")
            return render(request, "core/register.html", {"error": f"Error al registrar: {e}"})
            
    return render(request, 'core/register.html')

# def product(request):
   # return render(request, 'core/product.html') 

def cart_view(request):
    usuario = _cart_usuario(request)
    if usuario is None:
        return redirect("core:login")

    items = ItemCarrito.objects.filter(usuario=usuario).select_related("producto")
    total = sum((item.subtotal for item in items), start=0)
    return render(request, "core/cart.html", {"items": items, "total": total})


def _cart_usuario(request):
    usuario_id = request.session.get("cart_user_id")
    if usuario_id is None:
        return None
    return Usuario.objects.filter(pk=usuario_id).first()


@require_POST
def cart_add(request, producto_id):
    usuario = _cart_usuario(request)
    if usuario is None:
        return redirect("core:login")

    producto = get_object_or_404(Producto, pk=producto_id)
    item, created = ItemCarrito.objects.get_or_create(
        usuario=usuario,
        producto=producto,
        defaults={"cantidad": 1},
    )
    if not created:
        ItemCarrito.objects.filter(pk=item.pk).update(cantidad=F("cantidad") + 1)
    return redirect("core:cart")


@require_POST
def cart_update(request, item_id):
    usuario = _cart_usuario(request)
    if usuario is None:
        return redirect("core:login")

    try:
        cantidad = int(request.POST.get("cantidad", ""))
    except ValueError:
        return HttpResponseBadRequest("La cantidad debe ser un número entero positivo.")
    if cantidad < 1:
        return HttpResponseBadRequest("La cantidad debe ser un número entero positivo.")

    item = get_object_or_404(ItemCarrito, pk=item_id, usuario=usuario)
    item.cantidad = cantidad
    item.save(update_fields=["cantidad"])
    return redirect("core:cart")


@require_POST
def cart_remove(request, item_id):
    usuario = _cart_usuario(request)
    if usuario is None:
        return redirect("core:login")

    item = get_object_or_404(ItemCarrito, pk=item_id, usuario=usuario)
    item.delete()
    return redirect("core:cart")

def checkout_view(request):
    return render(request, 'core/checkout.html')

def receipt_view(request):
    return render(request, 'core/receipt.html')

def download_view(request):
    return render(request, 'core/download.html')