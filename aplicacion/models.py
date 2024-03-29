from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Repuestos(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    precio = models.IntegerField()
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}"
    
class Maquina(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    area = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}"

class Proveedores(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    fono = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}"
    
class SolicitarRepuestos(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    fechasolicitud = models.DateField()
   
    def __str__(self):
        return f"{self.nombre}"

class Avatar(models.Model):
    imagen = models.ImageField(upload_to= "avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"

