def RegistrarEstudiante(request):
    if request.method == 'POST':
        form = FormEstudiante(request.POST, request.FILES)
        if form.is_valid():
            estudiante = form.save(commit=False)
            correo = request.POST.get('correo')
            existing_user = User.objects.filter(username=correo).first()
            if existing_user:
                if existing_user.has_usable_password():
                    # El usuario ya existe y tiene una contraseña válida, muestra un error
                    form.add_error('correo', 'Ya existe un usuario con ese correo electrónico y tiene una contraseña asociada.')
                    return render(request, 'registrar_estudiante.html', {'form': form})
                else:
                    # El usuario existe pero no tiene una contraseña, lo eliminamos
                    existing_user.delete()
            
            user = User.objects.create_user(username=correo, email=correo)
            
            # Verifica si se proporcionó un archivo de imagen
            if not request.FILES.get('foto_perfil'):
                # Si no se proporcionó una imagen, establece la imagen predeterminada
                imagen_predeterminada = 'perfiles/1144760.png'
                estudiante.foto_perfil.name = imagen_predeterminada  # Establece la ruta de la imagen predeterminada

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

def registrar_contrasena(request):
    id = request.user.id
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            # Obtenemos el usuario que acabamos de crear en RegistrarEstudiante desde la sesión
            correo = request.session.get('correo')
            user = User.objects.get(username=correo)
            
            # Establecemos la contraseña del usuario
            password = request.POST.get('password')
            user.set_password(password)
               
            user.is_active = True
            
            user.save()  # Ahora guardamos con el usuario y la foto de perfil actualizados
            
            return render(request, 'confirmacion_cuenta.html', {'user': user})
        else:
            # Si el formulario no es válido, muestra los errores en la página del formulario
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
    return render(request, 'perfil_estudiante.html', {'estudiante': estudiante, 'user': usuario})

@login_required
@user_passes_test(tiene_permiso_estudiante)
def eliminarEstudiante(request):
    return render(request, 'confirmar_eliminacion_estudiante.html')

@login_required
@user_passes_test(tiene_permiso_estudiante)
def confirmaEliminacionEstudiante(request):
    usuario = request.user
    estudiante = usuario.estudiante
    Favorito.objects.filter(estudiante=estudiante).delete()
    estudiante.delete()
    usuario.delete()
    messages.success(request,"Usuario eliminado con exito")
    return redirect('login')

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
            existing_user = User.objects.filter(username=correo).exclude(id=usuario.id).first()
            if existing_user:
                if existing_user.has_usable_password():
                    # El usuario ya existe y tiene una contraseña válida, muestra un error
                    errors = form.errors
                    form.add_error('correo', 'Ya existe un usuario con ese correo electrónico y tiene una contraseña asociada.')
                    return render(request, 'editar_perfil_estudiante.html', {'form': form, 'user_id': id, 'errors': errors})
                else:
                    # El usuario existe pero no tiene una contraseña lo eliminamos y se guarda 
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
        imagen_perfil_url = estudiante.foto_perfil.url if estudiante.foto_perfil else ""
        form = FormEstudiante(instance=estudiante, initial={'foto_perfil': imagen_perfil_url})
        errors = {}

    return render(request, 'editar_perfil_estudiante.html', {'form': form, 'user_id': id, 'errors': errors})

@login_required
@user_passes_test(tiene_permiso_estudiante)
def listaPropiedades(request):
    propiedades = Propiedad.objects.all()
    municipios = Municipio.objects.all()
    colonias = Colonia.objects.all()
    form = FiltrosPropiedad() 

    for propiedad in propiedades:
        primer_imagen = ImagenPropiedad.objects.filter(propiedad=propiedad).first()
        propiedad.primerImagen = primer_imagen.imagen.url

    context = {
        'object_list': propiedades,
        'propiedades': propiedades,
        'form': form, 
        'colonias': colonias,
        'municipios': municipios
    }
    return render(request, 'lista_propiedades.html', context)
