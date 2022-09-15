from xml.parsers.expat import model
from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    correo = models.EmailField()
    contraseña = models.TextField()
    telefono = models.CharField(max_length=9)
    sexo = models.TextField()
    cumpleaño = models.DateTimeField()
    dia_registro = models.DateTimeField(auto_now_add=True)
