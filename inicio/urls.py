from django.urls import path
from inicio.views import inicio, crear_perro

urlpatterns = [
    path('', inicio),
    path('crear-perro/<str:nombre>/<int:edad>', crear_perro)
]
