from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from .forms import FormEstudiante, FormArrendador, UserForm
from Propiedades.models import Favorito
from Propiedades.models import Propiedad, ImagenPropiedad
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


def tiene_permiso_estudiante(user):
    return user.groups.filter(name='estudiante').exists()


def tiene_permiso_arrendador(user):
    return user.groups.filter(name='arrendador').exists()


@login_required
@user_passes_test(tiene_permiso_estudiante)
def editar_perfil_estudiante(request):
    usuario = request.user
    estudiante = usuario.estudiante

    if request.method == 'POST':
        form = FormEstudiante(request.POST, request.FILES, instance=estudiante)
        if form.is_valid():
            correo = request.POST.get('correo')
            # Excluye el propio usuario actual (id=usuario.id)
            existing_user = User.objects.filter(username=correo)\
                .exclude(id=usuario.id).first()
            if existing_user:
                if existing_user.has_usable_password():
                    # El usuario ya existe y tiene una contraseña válida.
                    # Esto muestra un error
                    errors = form.errors
                    form.add_error(
                        'correo',
                        ('Ya existe un usuario con ese correo electrónico '
                         'y tiene una contraseña asociada.')
                    )
                    template = 'editar_perfil_estudiante.html'
                    data = {
                        'form': form,
                        'user_id': id,
                        'errors': errors
                    }

                    return render(request, template, data)
                else:
                    # El usuario existe pero no tiene una contraseña
                    # lo eliminamos y se guarda
                    existing_user.delete()
                    # Actualizar correo del usuario actual
                    usuario.email = correo
                    usuario.username = correo
                    usuario.save()
                    form.save()
                    return redirect('perfil_estudiante')
            else:
                usuario.email = correo
                usuario.username = correo
                usuario.save()
                form.save()
                return redirect('perfil_estudiante')
        else:
            errors = form.errors
    else:
        imagen_perfil_url = (
            estudiante.foto_perfil.url if estudiante.foto_perfil
            else ""
        )
        form = FormEstudiante(instance=estudiante, initial={
                              'foto_perfil': imagen_perfil_url})
        errors = {}

    context = {
        'form': form,
        'user_id': id,
        'errors': errors
    }

    return render(
        request,
        'editar_perfil_estudiante.html',
        context=context
    )


@login_required
@user_passes_test(tiene_permiso_arrendador)
def editar_perfil_arrendador(request):
    usuario = request.user
    arrendador = usuario.arrendador

    if request.method == 'POST':
        form = FormArrendador(request.POST, request.FILES, instance=arrendador)
        if form.is_valid():
            form.save()
            return redirect('perfil_arrendador')
    else:
        imagen_perfil_url = arrendador.foto_perfil.url if arrendador.foto_perfil else ""
        form = FormArrendador(instance=arrendador, initial={
                              'foto_perfil': imagen_perfil_url})

    return render(request, 'editar_perfil_arrendador.html', {'form': form, 'user_id': id})


class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            user = form.get_user()
            if user.check_password(form.cleaned_data['password']):
                # Si el formulario es válido y la contraseña
                # es correcta, inicia sesión
                response = self.form_valid(form)
                # Guarda el ID del usuario en la sesión
                self.request.session['user_id'] = user.id
                return response
            else:
                messages.warning(request, 'Contraseña incorrecta :(')
                return self.form_invalid(form)
        else:
            username = form.cleaned_data.get('username')
            User = get_user_model()

            try:
                user = User.objects.get(username=username)
                if not user.has_usable_password():
                    # Si el usuario no tiene una contraseña, elimínalo
                    user.delete()
                    message1 = 'Aún no te has registrado correctamente.'
                    message2 = 'Inicia tu registro.'

                    message = message1 + " " + message2

                    messages.warning(request, message)

                    return self.form_invalid(form)
                else:
                    messages.warning(request, 'Contraseña incorrecta :(')
                    return self.form_invalid(form)
            except User.DoesNotExist:
                message1 = 'Aún no te has registrado correctamente.'
                message2 = 'Inicia tu registro.'

                message = message1 + " " + message2

                messages.warning(request, message)
                return self.form_invalid(form)


def compromiso(request):
    return render(request, 'compromiso.html')


def confirmar_cuenta(request):
    return render(request, 'confirmacion_cuenta.html')


def RegistrarEstudiante(request):
    if request.method == 'POST':
        form = FormEstudiante(request.POST, request.FILES)
        if form.is_valid():
            estudiante = form.save(commit=False)
            correo = request.POST.get('correo')
            existing_user = User.objects.filter(username=correo).first()
            if existing_user:
                if existing_user.has_usable_password():
                    # El usuario ya existe y tiene una
                    # contraseña válida, muestra un error
                    message = 'Ya existe un usuario '
                    message = 'con ese correo electrónico '
                    message += 'y tiene una contraseña asociada.'

                    form.add_error('correo', message)
                    context = {
                        'form': form
                    }

                    return render(
                        request,
                        'registrar_estudiante.html',
                        context
                    )
                else:
                    # El usuario existe pero no tiene
                    # una contraseña, lo eliminamos
                    existing_user.delete()

            user = User.objects.create_user(username=correo, email=correo)

            # Verifica si se proporcionó un archivo de imagen
            if not request.FILES.get('foto_perfil'):
                # Si no se proporcionó una imagen,
                # establece la imagen predeterminada
                imagen_predeterminada = 'perfiles/1144760.png'
                # Establece la ruta de la imagen predeterminada
                estudiante.foto_perfil.name = imagen_predeterminada

            estudiante.usuario = user
            request.session['correo'] = correo
            request.session.save()
            grupo = Group.objects.get(name='estudiante')
            user.groups.add(grupo)
            estudiante.save()
            return HttpResponseRedirect(reverse('compromiso'))
        else:
            return render(request, 'registrar_estudiante.html', {'form': form})
    else:
        form = FormEstudiante()
        context = {'form': form}
        return render(request, 'registrar_estudiante.html', context)


def RegistrarArrendador(request):
    if request.method == 'POST':
        form = FormArrendador(request.POST, request.FILES)
        if form.is_valid():
            arrendador = form.save(commit=False)
            correo = request.POST.get('correo')
            existing_user = User.objects.filter(username=correo).first()
            if existing_user:
                if existing_user.has_usable_password():
                    # El usuario ya existe y tiene una contraseña válida, muestra un error
                    form.add_error(
                        'correo', 'Ya existe un usuario con ese correo electrónico y tiene una contraseña asociada.')
                    return render(request, 'registrar_arrendador.html', {'form': form})
                else:
                    # El usuario existe pero no tiene una contraseña, lo eliminamos
                    existing_user.delete()

            user = User.objects.create_user(username=correo, email=correo)

            # Verifica si se proporcionó un archivo de imagen
            if not request.FILES.get('foto_perfil'):
                # Si no se proporcionó una imagen, establece la imagen predeterminada
                imagen_predeterminada = 'perfiles/1144760.png'
                # Establece la ruta de la imagen predeterminada
                arrendador.foto_perfil.name = imagen_predeterminada

            arrendador.usuario = user
            request.session['correo'] = correo
            request.session.save()
            grupo = Group.objects.get(name='arrendador')
            user.groups.add(grupo)
            arrendador.save()
            return HttpResponseRedirect(reverse('compromiso'))
        else:
            return render(request, 'registrar_arrendador.html', {'form': form})
    else:
        form = FormArrendador()
        context = {'form': form}
        return render(request, 'registrar_arrendador.html', context)


def registrar_contrasena(request):
    id = request.user.id
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            # Obtenemos el usuario que acabamos
            # de crear en RegistrarEstudiante desde la sesión
            correo = request.session.get('correo')
            user = User.objects.get(username=correo)

            # Establecemos la contraseña del usuario
            password = request.POST.get('password')
            user.set_password(password)

            user.is_active = True
            # Ahora guardamos con el usuario y
            # la foto de perfil actualizados
            user.save()

            return render(request, 'confirmacion_cuenta.html', {'user': user})
        else:
            # Si el formulario no es válido
            # Muestra los errores en la página del formulario
            return render(request, 'registrar_contrasena.html', {'form': form})

    else:
        form = UserForm()

    context = {
        'form': form,
        'userid': id
    }

    return render(request, 'registrar_contrasena.html', context)


@login_required
@user_passes_test(tiene_permiso_estudiante)
def verPerfilEstudiante(request):
    usuario = request.user
    estudiante = usuario.estudiante
    context = {'estudiante': estudiante, 'user': usuario}

    return render(request, 'perfil_estudiante.html', context=context)


@login_required
@user_passes_test(tiene_permiso_arrendador)
def verPerfilArrendador(request):
    usuario = request.user
    arrendador = usuario.arrendador
    return render(request, 'perfil_arrendador.html', {'arrendador': arrendador, 'user': usuario})


@login_required
@user_passes_test(tiene_permiso_estudiante)
def eliminarEstudiante(request):
    return render(request, 'confirmar_eliminacion_estudiante.html')


@login_required
@user_passes_test(tiene_permiso_arrendador)
def eliminarArrendador(request):
    return render(request, 'confirmar_eliminacion_arrendador.html')


@login_required
@user_passes_test(tiene_permiso_estudiante)
def confirmaEliminacionEstudiante(request):
    usuario = request.user
    estudiante = usuario.estudiante
    Favorito.objects.filter(estudiante=estudiante).delete()
    estudiante.delete()
    usuario.delete()
    messages.success(request, "Usuario eliminado con exito")
    return redirect('login')


@login_required
@user_passes_test(tiene_permiso_arrendador)
def confirmaEliminacionArrendador(request):
    usuario = request.user
    arrendador = usuario.arrendador
    propiedades = Propiedad.objects.filter(arrendador=arrendador)
    for propiedad in propiedades:
        favoritos = Favorito.objects.filter(propiedad=propiedad)
        favoritos.delete()
        imagenes_propiedad = ImagenPropiedad.objects.filter(
            propiedad=propiedad)
        for imagen_propiedad in imagenes_propiedad:
            imagen_propiedad.imagen.delete()
        imagenes_propiedad.delete()
        propiedades.delete()
    arrendador.delete()
    usuario.delete()
    return redirect('login')
