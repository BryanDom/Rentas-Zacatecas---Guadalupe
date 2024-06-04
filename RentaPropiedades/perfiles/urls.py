from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('logout/', LogoutView.as_view(),
         name='logout'),
    path('nuevo_estudiante/',
         views.RegistrarEstudiante,
         name='nuevo_estudiante'),
    path('nuevo_arrendador/',
         views.RegistrarArrendador,
         name='nuevo_arrendador'),
    path('compromiso/',
         views.compromiso,
         name='compromiso'),
    path('registrar_contrasena/',
         views.registrar_contrasena,
         name='contrasena'),
    path('confirmacion_cuenta/',
         views.confirmar_cuenta,
         name='confirmar'),
    path('perfil_estudiante/',
         views.verPerfilEstudiante,
         name='perfil_estudiante'),
    path('perfil_arrendador/',
         views.verPerfilArrendador,
         name='perfil_arrendador'),
    path('editar_perfil_estudiante/',
         views.editar_perfil_estudiante,
         name='editar_perfil_estudiante'),
    path('editar_perfil_arrendador/',
         views.editar_perfil_arrendador,
         name='editar_perfil_arrendador'),
    path('eliminar_estudiante/',
         views.eliminarEstudiante,
         name='eliminar_estudiante'),
    path('eliminar_arrendador/',
         views.eliminarArrendador,
         name='eliminar_arrendador'),
    path('confirmar_eliminacion_arrendador/',
         views.confirmaEliminacionArrendador,
         name='confirmar_eliminacion_arrendador'),
    path('confirmar_eliminacion_estudiante/',
         views.confirmaEliminacionEstudiante,
         name='confirmar_eliminacion_estudiante'),
]

if settings.DEBUG:  # pragma no cover
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
