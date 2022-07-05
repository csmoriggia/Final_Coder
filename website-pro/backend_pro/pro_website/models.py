from django.db import models
from django.forms import IntegerField, DateField
from django.contrib.auth.models import User

# Create your models here.
class afiliado(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    dni = models.IntegerField()
    telefono = models.IntegerField()
    fecha_nacimiento = models.DateField()
    def __str__(self):
        return f" {self.nombre} {self.apellido} -  {self.direccion}   DNI: {self.dni}   Teléfono: {self.telefono}   {self.fecha_nacimiento}"


class fiscal(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    dni = models.IntegerField()
    telefono = models.IntegerField()
    fecha_nacimiento = models.DateField()
    def __str__(self):
        return f" {self.nombre} {self.apellido} -  {self.direccion}   DNI: {self.dni}   Teléfono: {self.telefono}   {self.fecha_nacimiento}"

class juventud(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    telefono = models.IntegerField()
    fecha_nacimiento = models.DateField()
    redes_sociales = models.CharField(max_length=40)
    def __str__(self):
        return f" {self.nombre} {self.apellido} Teléfono: {self.telefono}  {self.fecha_nacimiento} {self.redes_sociales}"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to = 'avatares', null = True, blank = True)

class proyecto(models.Model):
    titulo = models.CharField(max_length=40)
    contenido = models.CharField(max_length=35000)
    autor = models.CharField(max_length=40)
    resumen = models.CharField(max_length=5000)
    def __str__(self):
        return f" {self.titulo} por {self.autor}"

