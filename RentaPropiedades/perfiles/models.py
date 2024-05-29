from django.db import models
from django.contrib.auth.models import User


class Estudiante (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=[(
        'M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')])
    foto_perfil = models.ImageField(
        'Foto', upload_to='perfiles', null=True, blank=True)
    universidad_actual = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    whatsapp = models.CharField(max_length=10)
    correo = models.CharField(max_length=100)
    preferencias_busqueda = models.CharField(max_length=500)
    pasatiempos = models.CharField(max_length=500)
    usuario = models.OneToOneField(
        User, verbose_name="Usuario", on_delete=models.CASCADE)


class Arrendador (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=[(
        'M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')])
    foto_perfil = models.ImageField(
        'perfil', upload_to='perfiles', null=True, blank=True)
    ocupacion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    whatsapp = models.CharField(max_length=10)
    correo = models.CharField(max_length=100)
    preferencias_arrendatarios = models.CharField(max_length=500)
    usuario = models.OneToOneField(
        User, verbose_name="Usuario", on_delete=models.CASCADE)
