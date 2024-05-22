from django.db import models
from django.contrib.auth.models import User

class Propiedad(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()
    tipo = models.IntegerField(choices=[(1,'Casa'), (2,'Departamento'), (3,'Cuarto')])
    ubicacion = models.CharField(max_length=100)
    serviciosIncluidos = models.BooleanField(default=False)
    arrendador = models.ForeignKey("perfiles.Arrendador", verbose_name="Arrendador", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ubicacion} - {self.precio}" 
    

class ImagenPropiedad(models.Model):
    propiedad = models.ForeignKey("Propiedades.Propiedad", verbose_name= "Propiedad", on_delete= models.CASCADE )
    imagen = models.ImageField('imagen', upload_to = 'imagenes',null=True, blank=True)


class Municipio(models.Model):
    id =  models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre 

class Colonia(models.Model):
    municipio = models.ForeignKey("Propiedades.Municipio", verbose_name= "Municipio", on_delete= models.CASCADE )
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre 
    
class Favorito (models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey("perfiles.Estudiante", verbose_name="Estudiante", on_delete= models.CASCADE, related_name='favoritos_estudiante')
    propiedad = models.ForeignKey("Propiedades.Propiedad", verbose_name="Propiedad", on_delete=models.CASCADE, related_name='favoritos_propiedad')

class Resena(models.Model):
    resena_id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey("perfiles.Estudiante", verbose_name="Estudiante", on_delete= models.CASCADE, related_name='resenas_estudiante')
    propiedad = models.ForeignKey("Propiedades.Propiedad", verbose_name="Propiedad", on_delete=models.CASCADE, related_name='resenas_propiedad')
    descripcion = models.TextField(max_length=500)
    calificacion = models.IntegerField(default=0)
    fecha = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.estudiante} - {self.fecha}"
    
class Estudiante_Interesado(models.Model):
    estudiante = models.ForeignKey("perfiles.Estudiante", verbose_name="Estudiante", on_delete= models.CASCADE, related_name='interesado_estudiante')
    propiedad = models.ForeignKey("Propiedades.Propiedad", verbose_name="Propiedad", on_delete=models.CASCADE, related_name='interesado_propiedad')