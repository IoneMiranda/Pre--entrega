
from django.urls import path
from AppSeg.views import *


urlpatterns = [
    path('', inicio),
    path('clientes/', cliente),
    path('empleados/', empleado),
    path('proveedor/', proveedor),


]