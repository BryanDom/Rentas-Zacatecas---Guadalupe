from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('arrendador_bienvenido/', views.arrendador_bienvenido, name='arrendador_bienvenido'),
    path('agregar/', views.nueva_propiedad, name='agregar_propiedad'),
    path('lista_propiedades/', views.listaPropiedades, name='lista_propiedades'),
    path('detalle_propiedad/<int:id>', views.detalle_propiedad, name='detalle_propiedad'),
    path('detalles_arrendador/<int:id>', views.detalles_arrendador, name='detalles_arrendador'),
    path('obtener_colonias/', views.obtener_colonias, name='obtener_colonias'),
    path('propiedades_arrendador/', views.propiedades_arrendador, name='propiedades_arrendador'),
    path('editar_propiedad/<int:id>', views.editarPropiedad, name='editar_propiedad'),
    path('eliminar/<int:id>/', views.eliminarPropiedad, name='eliminar_propiedad'),
    path('confirmacion_eliminacion_propiedad/<int:id>', views.confirmarEliminacionPropiedad, name='confirmacion_eliminacion_propiedad'),
    path('favoritos/', views.lista_favoritos, name='lista_favoritos'),  
    path('favoritos/agregar/<int:propiedad_id>/', views.agregaraListaFavoritos, name='agregaraListaFavoritos'),
    path('favoritos/eliminar/<int:propiedad_id>', views.eliminarDeListaFavorito, name='eliminarDeListaFavoritos'),
    #path('eliminar_favorito/', views.eliminarFavorito, name='eliminar_favorito'),
    path('confirmar_eliminacion_favorito/<int:propiedad_id>', views.confirmarEliminacionFavorito, name='confirmar_eliminacion_favorito'),
    path('filtrar/', views.filtrarPropiedades, name='filtrar_propiedades'),
    path('resenas/<int:id>', views.ver_resenas, name='lista_resenas'),
    path('agregar_resena/<int:id>', views.CrearResena, name='agregar_resena'),
    path('editar_resena/', views.EditarResena, name='editar_resena'),
    path('eliminar_resena/', views.EliminarResena, name='eliminar_resena'),
    path('confirmacion_eliminacion_resena/', views.ConfirmacionEliminacionResena, name='confirmacion_eliminacion_resena'),
    path('interesados/<int:id>', views.lista_interesados, name='lista_interesados'),
    path('indicar_interes/<int:id>', views.indicarInteres, name='indicar_interes'),
    path('detalles_estudiante/<int:id>', views.detalles_estudiante, name='detalles_estudiante'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)