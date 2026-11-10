from django.urls import path
from core.views import index
from . import views

app_name = "core"

urlpatterns = [
    path("", index),
    # creado para la visualizacion del diseño login/register
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]