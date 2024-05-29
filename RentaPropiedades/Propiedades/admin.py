from django.contrib import admin
from .models import (Propiedad, ImagenPropiedad, Municipio,
                     Colonia, Favorito, Resena, Estudiante_Interesado)

admin.site.register(Propiedad)
admin.site.register(ImagenPropiedad)
admin.site.register(Municipio)
admin.site.register(Colonia)
admin.site.register(Favorito)
admin.site.register(Resena)
admin.site.register(Estudiante_Interesado)
