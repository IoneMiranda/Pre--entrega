from django.shortcuts import render
from django.http import HttpResponse
from AppSeg.models import Cliente, Empleado, Proveedor

def inicio(resquest):
    return render(resquest,"AppSeg/inicio.html")

def cliente(request):
    cli1 = Cliente(nombre='Jose Argento', direccion='Junin 200', telefono=12345678)
    cli1.save()
    return HttpResponse(f"Alta de cliente {cli1.nombre}, domicilio: {cli1.direccion}, tel: {cli1.telefono}, OK")

def empleado(request):
    emp1 = Empleado(nombre='Juan Perez', cargo='Gerente', fecha_contratacion='2024-01-01')
    emp1.save()
    return HttpResponse(f"Alta de empleado {emp1.nombre}, cargo: {emp1.cargo}, fecha de contratación: {emp1.fecha_contratacion}, OK")

def proveedor(request):
    prov1 = Proveedor(nombre='Proveedor ABC', direccion='Calle Principal 123', telefono=987654321)
    prov1.save()
    return HttpResponse(f"Alta de proveedor {prov1.nombre}, domicilio: {prov1.direccion}, tel: {prov1.telefono}, OK")