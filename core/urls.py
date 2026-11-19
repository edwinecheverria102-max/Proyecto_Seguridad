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
<<<<<<< HEAD
    path('cart/add/<int:producto_id>/', views.cart_add, name='cart_add'),
    path('cart/item/<int:item_id>/update/', views.cart_update, name='cart_update'),
    path('cart/item/<int:item_id>/remove/', views.cart_remove, name='cart_remove'),
=======
    path('product/<int:pk>/', views.product_detail_view, name='product_detail'),
>>>>>>> c1df5f155926eba16910b861563b4932a9897720
    path('checkout/', views.checkout_view, name='checkout'),
    path('receipt/', views.receipt_view, name='receipt'),
    path('download/', views.download_view, name="download"),
    path('profile/', views.profile_view, name='profile'),
    path('error404/', lambda request: render(request, '404.html')), #error404
    path('operator/', views.operator_dashboard_view, name='operator_dashboard'),
    path('admin-panel/', views.admin_dashboard_view, name='admin_dashboard'),
    path('operator/product/new/', views.product_form_view, name='product_form'),
]