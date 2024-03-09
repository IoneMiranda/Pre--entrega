from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField()
    def _str_(self):
        return self.nombre
     
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()
    def _str_(self):
        return self.nombre
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField()
    def _str_(self):
        return self.nombre
    