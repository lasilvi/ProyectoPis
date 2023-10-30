from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('importar/', views.importar_datos, name='importar_datos'),
    path('UCE/', views.viewUCE, name='uce'),
]