from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from Propiedades.models import Propiedad, ImagenPropiedad, Favorito
from Propiedades.models import Resena, Estudiante_Interesado
from Propiedades.models import Municipio, Colonia
from perfiles.models import Estudiante
from Propiedades.forms import FiltrosPropiedad, FormResena
from Propiedades.forms import FormPropiedad, FormImagenPropiedad
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from perfiles.views import tiene_permiso_arrendador, tiene_permiso_estudiante
from django.utils.decorators import method_decorator
import math


@method_decorator(login_required, name='dispatch')
class Bienvenida(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener el ID del usuario de la sesión
        user_id = self.request.session.get('user_id')
        if user_id is not None:
            try:
                # Obtener el objeto de usuario usando el ID
                user = User.objects.get(id=user_id)
                context['user'] = user
            except User.DoesNotExist:
                # Manejar el caso si el usuario no existe
                context['user'] = None
        return context


def arrendador_bienvenido(request):
    return render(request, 'bienvenida_arrendador.html')


@login_required
@user_passes_test(tiene_permiso_arrendador)
def nueva_propiedad(request):
    municipios = Municipio.objects.all()
    colonias = Colonia.objects.all()
    primera_imagen = None

    if request.method == 'POST':
        form_propiedad = FormPropiedad(request.POST)
        form_imagenes = [FormImagenPropiedad(
            request.POST,
            request.FILES, prefix=f'imagen_{i}') for i in range(5)]

        if (form_propiedad.is_valid()
                and all(form.is_valid() for form in form_imagenes[:2])):
            # Obtén los datos de ubicación del formulario
            calle = request.POST.get('calle')
            numero = request.POST.get('numero')
            colonia = request.POST.get('colonia')
            municipio = request.POST.get('municipio')

            # Verificar si ya existe una propiedad con los mismos datos
            existing_property = Propiedad.objects.filter(
                ubicacion__icontains=f'{calle} {
                    numero}, {colonia}, {municipio}'
            ).exists()

            if existing_property:
                context = {'mensaje':
                           "Error: La propiedad ya está registrada.",
                           'form_propiedad': form_propiedad,
                           'form_imagenes': form_imagenes,
                           'colonias': colonias,
                           'municipios': municipios}
                return render(request, 'nueva_propiedad.html', context)
            else:
                propiedad = form_propiedad.save(
                    commit=False)  # No guardamos todavía

                # Concatenamos la ubicación
                propiedad.ubicacion = f'{calle} {
                    numero}, {colonia}, {municipio}'
                propiedad.arrendador = request.user.arrendador

                propiedad.save()
                # Ahora guardamos con la ubicación actualizada

                for i, form_imagen in enumerate(form_imagenes):
                    if request.FILES.get(form_imagen.add_prefix('imagen')):
                        imagen_propiedad = form_imagen.save(commit=False)
                        imagen_propiedad.propiedad = propiedad
                        imagen_propiedad.save()
                        if i == 0:
                            primera_imagen = imagen_propiedad.imagen.url
                context = {'propiedad': propiedad,
                           'primera_imagen': primera_imagen}
                return render(request, 'confirmacion_propiedad.html', context)
    else:
        form_propiedad = FormPropiedad()
        form_imagenes = [FormImagenPropiedad(
            prefix=f'imagen_{i}') for i in range(5)]

    context = {
        'form_propiedad': form_propiedad,
        'form_imagenes': form_imagenes,
        'colonias': colonias,
        'municipios': municipios
    }

    return render(request, 'nueva_propiedad.html', context)


@login_required
@user_passes_test(tiene_permiso_estudiante)
def listaPropiedades(request):
    propiedades = Propiedad.objects.all()
    municipios = Municipio.objects.all()
    colonias = Colonia.objects.all()
    form = FiltrosPropiedad()

    for propiedad in propiedades:
        primer_imagen = ImagenPropiedad.objects.filter(
            propiedad=propiedad).first()
        propiedad.primerImagen = primer_imagen.imagen.url

    context = {
        'object_list': propiedades,
        'propiedades': propiedades,
        'form': form,
        'colonias': colonias,
        'municipios': municipios
    }
    return render(request, 'lista_propiedades.html', context)


@login_required
def detalle_propiedad(request, id):
    user = request.user
    es_arrendador = user.groups.filter(name='arrendador').exists()
    es_estudiante = user.groups.filter(name='estudiante').exists()

    propiedad = Propiedad.objects.get(id=id)
    imagenes = ImagenPropiedad.objects.filter(propiedad=propiedad)
    datos = {'propiedad': propiedad, 'imagenes': imagenes,
             'es_arrendador': es_arrendador,
             'es_estudiante': es_estudiante}
    return render(request, 'detalles_propiedad.html', datos)


@login_required
@user_passes_test(tiene_permiso_estudiante)
def detalles_arrendador(request, id):
    propiedad = Propiedad.objects.get(id=id)
    arrendador = propiedad.arrendador
    context = {'arrendador': arrendador,
               'id_propiedad': id, 'propiedad': propiedad}
    return render(request, 'detalles_arrendador.html', context)


def obtener_colonias(request):
    if (request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
            and request.method == 'GET'):
        municipio = request.GET.get('municipio')
        colonias = Colonia.objects.filter(municipio__nombre=municipio)
        colonias_list = [{'nombre': colonia.nombre} for colonia in colonias]
        return JsonResponse({'colonias': colonias_list})
    return JsonResponse({}, status=400)


@login_required
@user_passes_test(tiene_permiso_arrendador)
def propiedades_arrendador(request):
    propiedades = Propiedad.objects.filter(arrendador=request.user.arrendador)

    for propiedad in propiedades:
        primer_imagen = ImagenPropiedad.objects.filter(
            propiedad=propiedad).first()

        if primer_imagen is not None:
            propiedad.primerImagen = primer_imagen.imagen.url
        else:
            propiedad.primerImagen = ''
            # Puedes definir un valor por defecto si no hay imagen

    context = {'propiedades': propiedades}
    return render(request, 'propiedades_arrendador.html', context)


@login_required
@user_passes_test(tiene_permiso_arrendador)
def editarPropiedad(request, id):
    propiedad = Propiedad.objects.get(id=id)
    arrendador = propiedad.arrendador

    if arrendador == request.user.arrendador:
        if request.method == 'POST':
            form = FormPropiedad(
                request.POST, request.FILES, instance=propiedad)

            if form.is_valid():
                # Guarda la propiedad con los cambios
                propiedad = form.save(commit=False)

                editarImagenes(propiedad.id, form, request)

                # Guarda los cambios en la propiedad
                propiedad.save()

                # Crea una instancia con la nueva imagen si se proporciona
                if 'imagen' in request.FILES:
                    ImagenPropiedad.objects.create(
                        propiedad=propiedad, imagen=request.FILES['imagen'])

                return redirect('propiedades_arrendador')
        else:
            form = FormPropiedad(instance=propiedad)
            imagenes_propiedad = ImagenPropiedad.objects.filter(
                propiedad=propiedad)
            context = {'form': form, 'id': id,
                       'imagenes_propiedad': imagenes_propiedad}
            return render(request, 'editar_propiedad.html', context)
    else:
        mensaje = "Acción no permitida."
        propiedades = Propiedad.objects.filter(
            arrendador=request.user.arrendador)

        for propiedad in propiedades:
            primer_imagen = ImagenPropiedad.objects.filter(
                propiedad=propiedad).first()

            if primer_imagen is not None:
                propiedad.primerImagen = primer_imagen.imagen.url
            else:
                propiedad.primerImagen = ''
                # Puedes definir un valor por defecto si no hay imagen

        context = {'propiedades': propiedades, 'mensaje': mensaje}
        return render(request, 'propiedades_arrendador.html', context)


def editarImagenes(id, form, request):
    propiedad = Propiedad.objects.get(id=id)
    # Obtiene las imágenes existentes para la propiedad
    imagenes_propiedad = ImagenPropiedad.objects.filter(
        propiedad=propiedad)
    # Contar el número de imágenes existentes
    num_imagenes = imagenes_propiedad.count()
    # Variable para verificar si al menos un checkbox fue seleccionado
    checkbox_seleccionado = False
    checkboxes_seleccionados = 0
    for imagen in imagenes_propiedad:
        checkbox_name = 'eliminar_imagen_' + str(imagen.id)
        if checkbox_name in request.POST:
            checkboxes_seleccionados += 1
            # Aumenta el contador si un checkbox está seleccionado
            checkbox_seleccionado = True
            # Se encontró al menos un checkbox selecciona
    resultado = num_imagenes - checkboxes_seleccionados
    if resultado == 0 or resultado == 1:
        # Si la propiedad tiene menos de tres imágenes
        # mostrar un mensaje de error
        messages.warning(
            request,
            "¡La propiedad debe tener al menos dos imágenes!")
        context = {'form': form, 'id': id,
                   'imagenes_propiedad': imagenes_propiedad}
        return render(request, 'editar_propiedad.html', context)
    else:
        if checkbox_seleccionado:
            for imagen in imagenes_propiedad:
                if 'eliminar_imagen_' + str(imagen.id) in request.POST:
                    imagen.delete()
        else:
            pass


@login_required
@user_passes_test(tiene_permiso_arrendador)
def confirmarEliminacionPropiedad(request, id):
    propiedad = Propiedad.objects.get(id=id)
    arrendador = propiedad.arrendador
    if arrendador == request.user.arrendador:
        return render(request, 'confirmacion_eliminacion_propiedad.html',
                      {'propiedad': propiedad})
    else:
        mensaje = "Acción no permitida."
        propiedades = Propiedad.objects.filter(
            arrendador=request.user.arrendador)

        for propiedad in propiedades:
            primer_imagen = ImagenPropiedad.objects.filter(
                propiedad=propiedad).first()

            if primer_imagen is not None:
                propiedad.primerImagen = primer_imagen.imagen.url
            else:
                propiedad.primerImagen = ''
                # Puedes definir un valor por defecto si no hay imagen

        context = {'propiedades': propiedades, 'mensaje': mensaje}
        return render(request, 'propiedades_arrendador.html', context)


@login_required
@user_passes_test(tiene_permiso_arrendador)
def eliminarPropiedad(request, id):
    propiedad = Propiedad.objects.get(id=id)
    arrendador = propiedad.arrendador
    if arrendador == request.user.arrendador:
        imagenes_propiedad = ImagenPropiedad.objects.filter(
            propiedad=propiedad)
        for imagen in imagenes_propiedad:
            # Asegúrate de eliminar también los archivos
            # de las imágenes en el sistema de archivos
            imagen.imagen.delete()
            imagen.delete()
        # Elimina la propiedad
        propiedad.delete()

        return redirect('propiedades_arrendador')
    else:
        mensaje = "Acción no permitida."
        propiedades = Propiedad.objects.filter(
            arrendador=request.user.arrendador)

        for propiedad in propiedades:
            primer_imagen = ImagenPropiedad.objects.filter(
                propiedad=propiedad).first()

            if primer_imagen is not None:
                propiedad.primerImagen = primer_imagen.imagen.url
            else:
                propiedad.primerImagen = ''
                # Puedes definir un valor por defecto si no hay imagen

        context = {'propiedades': propiedades, 'mensaje': mensaje}
        return render(request, 'propiedades_arrendador.html', context)

# Función que muestra las propiedades que fueron agregadas a la lista.


@login_required
@user_passes_test(tiene_permiso_estudiante)
def lista_favoritos(request):
    usuario = request.user
    estudiante = usuario.estudiante
    # Recuperamos la lista de favoritos para el estudiante actual.
    favoritos = Favorito.objects.filter(estudiante=estudiante)
    # Recuperamos las propiedades agregadas.
    propiedades = [favorito.propiedad for favorito in favoritos]
    for propiedad in propiedades:
        primer_imagen = ImagenPropiedad.objects.filter(
            propiedad=propiedad).first()
        propiedad.primerImagen = primer_imagen.imagen.url
    context = {'propiedades': propiedades}
    return render(request, 'lista_favoritos.html', context)

# Función para agregar una función a la lista de favoritos.


@login_required
@user_passes_test(tiene_permiso_estudiante)
def agregaraListaFavoritos(request, propiedad_id):
    usuario = request.user
    estudiante = usuario.estudiante

    # lista_favoritos = False

    # Recuperamos el id de la propiedad a agregar.
    propiedad = Propiedad.objects.get(id=propiedad_id)

    favorito = Favorito(estudiante=estudiante, propiedad=propiedad)

    # Verificamos si ya existe un favorito para la propiedad y el estudiante.
    existeFav = Favorito.objects.filter(
        estudiante=estudiante, propiedad=propiedad).first()
    if existeFav is None:
        # lista_favoritos = True
        favorito.save()
        favoritos_estudiante = Favorito.objects.filter(
            estudiante=estudiante).count()
        messages.success(
            request,
            f"Agregaste {favoritos_estudiante} propiedad(es) a favoritos.")
    else:
        messages.warning(
            request, "No se pudo agregar la propiedad, ya está en favoritos")
    # Redirección a la página de favoritos.
    return redirect('detalle_propiedad', propiedad_id)

# Función para eliminar una propiedad de la lista.


@login_required
@user_passes_test(tiene_permiso_estudiante)
def eliminarDeListaFavorito(request, propiedad_id):
    usuario = request.user
    estudiante = usuario.estudiante

    # Verifica si el favorito existe y si pertenece al estudiante actual.
    favorito = get_object_or_404(
        Favorito, propiedad=propiedad_id, estudiante=estudiante)

    if favorito:
        favorito.delete()
        messages.success(request, f"Se eliminó la propiedad: {propiedad_id}")
    else:
        messages.warning(
            request, "El favorito no existe o no pertenece al estudiante")

    return redirect('lista_favoritos')

# Función para mostrar una confirmación
# antes de eliminar una propiedad de la lista de favoritos.


@login_required
@user_passes_test(tiene_permiso_estudiante)
def confirmarEliminacionFavorito(request, propiedad_id):
    # Utiliza get_object_or_404 para obtener
    # la propiedad o mostrar una página 404 si no existe.
    propiedad = get_object_or_404(Propiedad, id=propiedad_id)

    # Filtra los favoritos relacionados con esta propiedad.
    favoritos = Favorito.objects.filter(propiedad=propiedad)

    context = {
        'propiedad': propiedad,
        'favoritos': favoritos
    }
    return render(request, 'confirmar_eliminacion_favorito.html', context)


@login_required
@user_passes_test(tiene_permiso_estudiante)
def filtrarPropiedades(request):
    propiedades = Propiedad.objects.all()
    municipios = Municipio.objects.all()
    colonias = Colonia.objects.all()

    if request.method == "POST":
        form = FiltrosPropiedad(request.POST)
        if form.is_valid():
            municipio = request.POST.get('municipio')
            print(municipio)
            colonia = request.POST.get('colonia')
            print(colonia)
            tipo = form.cleaned_data.get('tipo')
            servicios = form.cleaned_data.get('servicios')
            print(servicios)
            precio_min = form.cleaned_data.get('precio_min')
            precio_max = form.cleaned_data.get('precio_max')

            propiedades = filtrarColonia(propiedades, colonia, municipio)
            if tipo:
                propiedades = propiedades.filter(tipo=tipo)
            if servicios is not None:
                propiedades = propiedades.filter(serviciosIncluidos=servicios)
            if precio_min:
                propiedades = propiedades.filter(precio__gte=precio_min)
            if precio_max:
                propiedades = propiedades.filter(precio__lte=precio_max)
    colocarImagenes(propiedades)
    context = {
        'propiedades': propiedades,
        'municipios': municipios,
        'colonias': colonias,
        'form': form,
    }

    return render(request, 'lista_propiedades.html', context)


def filtrarColonia(propiedades, colonia, municipio):
    if municipio:
        if colonia != "":
            return propiedades.filter(
                ubicacion__icontains=f'{colonia}')
        else:
            return propiedades.filter(
                ubicacion__icontains=f'{municipio}')


def colocarImagenes(propiedades):
    for propiedad in propiedades:
        primer_imagen = ImagenPropiedad.objects.filter(
            propiedad=propiedad).first()
        propiedad.primerImagen = primer_imagen.imagen.url


@login_required
def ver_resenas(request, id):
    user = request.user
    es_arrendador = user.groups.filter(name='arrendador').exists()
    es_estudiante = user.groups.filter(name='estudiante').exists()

    user = request.user
    es_arrendador = user.groups.filter(name='arrendador').exists()
    es_estudiante = user.groups.filter(name='estudiante').exists()

    resenas = Resena.objects.filter(propiedad=id)
    propiedad = Propiedad.objects.get(id=id)
    vacia = False

    if len(resenas) == 0:  # Hay reseñas?
        vacia = True
        context = {
            'propiedad': propiedad,
            'vacia': vacia,
            'es_arrendador': es_arrendador,
            'es_estudiante': es_estudiante
        }
    else:
        cont = 0
        suma = 0
        for resena in resenas:
            cont += 1
            suma += int(resena.calificacion)

        promedio = suma/cont
        promedioRedondeado = math.floor(promedio)

        try:
            resena_usuario = resenas.get(estudiante=request.user.estudiante)
            hayResena = True

        except Exception:
            hayResena = False

        if hayResena:
            # Guardar el ID de la reseña en la sesión del usuario
            request.session['resena_id'] = resena_usuario.resena_id

            context = {
                'propiedad': propiedad,
                'resenas': resenas,
                'hayResena': hayResena,
                'resena_usuario': resena_usuario,
                'promedio': promedio,
                'promedioRedondeado': promedioRedondeado,
                'vacia': vacia,
                'es_arrendador': es_arrendador,
                'es_estudiante': es_estudiante,
                'rango_estrellas': range(1, 6)
            }
        else:
            context = {
                'propiedad': propiedad,
                'resenas': resenas,
                'hayResena': hayResena,
                'promedio': promedio,
                'promedioRedondeado': promedioRedondeado,
                'vacia': vacia,
                'es_arrendador': es_arrendador,
                'es_estudiante': es_estudiante,
                'rango_estrellas': range(1, 6)
            }

    return render(request, 'ver_resenas.html', context)


@login_required
def CrearResena(request, id):
    propiedad = Propiedad.objects.get(id=id)

    if request.method == 'POST':
        form = FormResena(request.POST)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.propiedad = propiedad

            estudiante_actual = Estudiante.objects.get(usuario=request.user)
            form_instance.estudiante = estudiante_actual

            form_instance.save()

            return redirect('lista_resenas', propiedad.id)
    else:
        form = FormResena()
    context = {
        'form': form,
        'rango_estrellas': range(1, 6),
        'propiedad_id': propiedad.id,
    }
    return render(request, 'crear_resena.html', context)


@login_required
def EditarResena(request):
    resena_id = request.session.get('resena_id')
    resena = Resena.objects.get(resena_id=resena_id)

    if request.method == 'POST':
        form = FormResena(request.POST, instance=resena)
        if form.is_valid():
            form_instance = form.save(commit=False)

            # Actualizar la calificación visual
            if 'calificacion' in form.cleaned_data:
                form_instance.calificacion = form.cleaned_data['calificacion']

            form_instance.save()

            return redirect('lista_resenas', resena.propiedad.id)
    else:
        # Inicializar el formulario con
        # el valor actual de calificacion_estrellas
        form = FormResena(instance=resena, initial={
                          'calificacion': resena.calificacion})

    context = {
        'form': form,
        'propiedad_id': resena.propiedad.id,
        'rango_estrellas': range(1, 6)
    }
    return render(request, 'editar_resena.html', context)


@login_required
def ConfirmacionEliminacionResena(request):
    resena_id = request.session.get('resena_id')
    resena = Resena.objects.get(resena_id=resena_id)

    context = {
        'propiedad_id': resena.propiedad.id
    }
    return render(request, 'confirmacion_eliminacion_resena.html', context)


@login_required
def EliminarResena(request):
    # Obtener el ID de la reseña de la sesión del usuario
    resena_id = request.session.get('resena_id')

    resena = Resena.objects.get(resena_id=resena_id)
    id_propiedad = resena.propiedad.id
    resena.delete()

    return redirect('lista_resenas', id_propiedad)


@login_required
def lista_interesados(request, id):
    propiedad = Propiedad.objects.get(id=id)
    interesados = Estudiante_Interesado.objects.filter(propiedad=propiedad)
    vacia = False

    if len(interesados) == 0:  # Hay interesados?
        vacia = True
        context = {
            'propiedad': propiedad,
            'vacia': vacia
        }
    else:

        # Veremos si el usuario logueado ya se intereso en la propiedad
        try:
            interesado_usuario = interesados.get(user=request.user.estudiante)
            hayInteresado = True
        except Exception:
            hayInteresado = False

        if hayInteresado:

            context = {
                'propiedad': propiedad,
                'interesados': interesados,
                'hayInteresado': hayInteresado,
                'interesado_usuario': interesado_usuario,
                'vacia': vacia,
            }
        else:
            context = {
                'propiedad': propiedad,
                'interesados': interesados,
                'hayInteresado': hayInteresado,
                'vacia': vacia,
            }

    return render(request, 'lista_interesados.html', context)


@login_required
def indicarInteres(request, id):
    propiedad = Propiedad.objects.get(id=id)
    estudiante = request.user.estudiante
    existe_interes = Estudiante_Interesado.objects.filter(
        estudiante=estudiante, propiedad=propiedad).exists()

    if existe_interes:
        messages.warning(request, 'Ya estás interesado en esta propiedad.')
    else:
        Estudiante_Interesado.objects.create(
            estudiante=estudiante, propiedad=propiedad)
        messages.success(
            request, 'Te has interesado exitosamente en esta propiedad.')
    return redirect('detalle_propiedad', id=id)


@login_required
def detalles_estudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    context = {'estudiante': estudiante}
    return render(request, 'detalles_estudiante.html', context)
