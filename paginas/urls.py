from django.urls import path
from .views import index, UsuarioCreate
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='usuario/login.html'), name='login'),
    path('registrar/', UsuarioCreate.as_view(),name='registrar'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('addcomment/', views.addcomment, name='addcomment')
]

    