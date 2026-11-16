from django.urls import path
from core.views import index
from . import views

app_name = "core"

urlpatterns = [
    path("", index, name='index'),
    # creado para la visualizacion del diseño login/register
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/<int:producto_id>/', views.cart_add, name='cart_add'),
    path('cart/item/<int:item_id>/update/', views.cart_update, name='cart_update'),
    path('cart/item/<int:item_id>/remove/', views.cart_remove, name='cart_remove'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('receipt/', views.receipt_view, name='receipt'),
    path('download/', views.download_view, name="download"),
    # path('product/', views.product_view, name='product'),
]