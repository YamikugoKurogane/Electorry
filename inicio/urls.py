
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('productos',productos,name="productos"),
    path('contacto',contacto,name="contacto"),
    path('instalaciones',instalaciones,name="instalaciones"),
    path('developer',developer,name="developer"),
]
