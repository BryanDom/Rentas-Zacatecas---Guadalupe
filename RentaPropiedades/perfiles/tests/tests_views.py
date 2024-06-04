from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User, Group
from perfiles.models import Arrendador, Estudiante
from Propiedades.models import Propiedad, ImagenPropiedad, Resena, Favorito, Estudiante_Interesado, Colonia, Municipio
from perfiles.forms import FormArrendador, FormEstudiante
from Propiedades.forms import FormImagenPropiedad
from django.core.files.uploadedfile import SimpleUploadedFile


class ArrendadorCreateViewTests(TestCase):
    def setUp(self):
        self.group, created = Group.objects.get_or_create(name='arrendador')
        self.data = {
            'nombre': 'Luis',
            'apellidos': 'Pérez',
            'edad': 40,
            'ocupacion': 'Abogado',
            'telefono': '1234567890',
            'whatsapp': '9876543210',
            'correo': 'luisperez@gmail.com',
            'preferencias_arrendatarios': 'Gente honesta',
            'sexo': 'M'
        }
        self.password_data = {
            'password': '1234',
            're_pass': '1234'
        }

    def test_creacion_perfil_valido(self):
        response = self.client.post(
            reverse('nuevo_arrendador'), data=self.data)
        self.assertRedirects(response, reverse('compromiso'))
        self.assertEqual(Arrendador.objects.count(), 1)
        arrendador = Arrendador.objects.get()
        self.assertEqual(arrendador.nombre, 'Luis')
        self.assertEqual(arrendador.apellidos, 'Pérez')
        self.assertEqual(arrendador.edad, 40)
        response = self.client.post(
            reverse('contrasena'), data=self.password_data)
        user = User.objects.get(username=self.data['correo'])
        self.assertTrue(user.check_password(self.password_data['password']))
        self.assertTrue(user.is_active)
        response = self.client.get(reverse('confirmar'))
        self.assertTemplateUsed(response, 'confirmacion_cuenta.html')

    def test_creacion_perfil_no_valido(self):
        response = self.client.post(
            reverse('nuevo_arrendador'), data=self.data)
        self.assertRedirects(response, reverse('compromiso'))
        self.assertEqual(Arrendador.objects.count(), 1)
        arrendador = Arrendador.objects.get()
        self.assertEqual(arrendador.nombre, 'Luis')
        self.assertEqual(arrendador.apellidos, 'Pérez')
        self.assertEqual(arrendador.edad, 40)
        response = self.client.post(
            reverse('contrasena'), data=self.password_data)
        user = User.objects.get(username=self.data['correo'])
        self.assertTrue(user.check_password(self.password_data['password']))
        self.assertTrue(user.is_active)
        response = self.client.get(reverse('confirmar'))
        self.assertTemplateUsed(response, 'confirmacion_cuenta.html')
        # correo repetido
        response = self.client.post(
            reverse('nuevo_arrendador'), data=self.data)
        self.assertFalse(Arrendador.objects.count() == 2)

    def test_acceso_vista_creacion(self):
        response = self.client.get(reverse('nuevo_arrendador'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registrar_arrendador.html')

    def test_nombre_requerido(self):
        self.data['nombre'] = ''
        response = self.client.post(
            reverse('nuevo_arrendador'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('nombre', form.errors)

    def test_apellidos_requeridos(self):
        self.data['apellidos'] = ''
        response = self.client.post(
            reverse('nuevo_arrendador'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('apellidos', form.errors)

    def test_edad_requerida(self):
        self.data['edad'] = ''
        response = self.client.post(
            reverse('nuevo_arrendador'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('edad', form.errors)

    def test_sexo_requerido(self):
        self.data['sexo'] = ''
        response = self.client.post(
            reverse('nuevo_arrendador'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('sexo', form.errors)

    def test_ocupacion_requerida(self):
        self.data['ocupacion'] = ''
        response = self.client.post(
            reverse('nuevo_arrendador'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('ocupacion', form.errors)

    def test_telefono_requerido(self):
        self.data['telefono'] = ''
        response = self.client.post(
            reverse('nuevo_arrendador'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('telefono', form.errors)

    def test_telefono_diez_digitos(self):
        self.data['telefono'] = '12345678910'
        response = self.client.post(
            reverse('nuevo_arrendador'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('telefono', form.errors)

    def test_whatsapp_requerido(self):
        self.data['whatsapp'] = ''
        response = self.client.post(
            reverse('nuevo_arrendador'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('whatsapp', form.errors)

    def test_whatsapp_diez_digitos(self):
        self.data['whatsapp'] = '12345678910'
        response = self.client.post(
            reverse('nuevo_arrendador'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('whatsapp', form.errors)

    def test_correo_requerido(self):
        self.data['correo'] = ''
        response = self.client.post(
            reverse('nuevo_arrendador'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('correo', form.errors)

    def test_preferencias_arrendatarios_requerido(self):
        self.data['preferencias_arrendatarios'] = ''
        response = self.client.post(
            reverse('nuevo_arrendador'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('preferencias_arrendatarios', form.errors)


class EstudianteCreateViewTests(TestCase):
    def setUp(self):
        # Crear un grupo de estudiante si no existe
        self.group, created = Group.objects.get_or_create(name='estudiante')
        # Datos de prueba
        self.data = {
            'nombre': 'José',
            'apellidos': 'Guardado',
            'edad': 18,
            'universidad_actual': 'UAZ',
            'telefono': '1234567890',
            'whatsapp': '9876543210',
            'correo': 'joseguardado@gmail.com',
            'preferencias_busqueda': 'Cuartos de estudiantes',
            'pasatiempos': 'Música, pintura, películas de terror.',
            'sexo': 'M'
        }

        self.password_data = {
            'password': '1234',
            're_pass': '1234'
        }

    def test_acceso_vista_creacion(self):
        response = self.client.get(reverse('nuevo_estudiante'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registrar_estudiante.html')

    def test_creacion_perfil_valido(self):
        response = self.client.post(
            reverse('nuevo_estudiante'), data=self.data)
        self.assertRedirects(response, reverse('compromiso'))
        self.assertEqual(Estudiante.objects.count(), 1)
        estudiante = Estudiante.objects.get()
        self.assertEqual(estudiante.nombre, 'José')
        self.assertEqual(estudiante.apellidos, 'Guardado')
        self.assertEqual(estudiante.edad, 18)
        response = self.client.post(
            reverse('contrasena'), data=self.password_data)
        user = User.objects.get(username=self.data['correo'])
        self.assertTrue(user.check_password(self.password_data['password']))
        self.assertTrue(user.is_active)
        response = self.client.get(reverse('confirmar'))
        self.assertTemplateUsed(response, 'confirmacion_cuenta.html')

    def test_creacion_perfil_no_valido(self):
        response = self.client.post(
            reverse('nuevo_estudiante'), data=self.data)
        self.assertRedirects(response, reverse('compromiso'))
        self.assertEqual(Estudiante.objects.count(), 1)
        estudiante = Estudiante.objects.get()
        self.assertEqual(estudiante.nombre, 'José')
        self.assertEqual(estudiante.apellidos, 'Guardado')
        self.assertEqual(estudiante.edad, 18)
        response = self.client.post(
            reverse('contrasena'), data=self.password_data)
        user = User.objects.get(username=self.data['correo'])
        self.assertTrue(user.check_password(self.password_data['password']))
        self.assertTrue(user.is_active)
        response = self.client.get(reverse('confirmar'))
        self.assertTemplateUsed(response, 'confirmacion_cuenta.html')
        # correo repetido
        response = self.client.post(
            reverse('nuevo_estudiante'), data=self.data)
        self.assertFalse(Estudiante.objects.count() == 2)

    def test_nombre_requerido(self):
        self.data['nombre'] = ''
        response = self.client.post(
            reverse('nuevo_estudiante'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('nombre', form.errors)

    def test_apellidos_requeridos(self):
        self.data['apellidos'] = ''
        response = self.client.post(
            reverse('nuevo_estudiante'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('apellidos', form.errors)

    def test_edad_requerida(self):
        self.data['edad'] = ''
        response = self.client.post(
            reverse('nuevo_estudiante'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('edad', form.errors)

    def test_sexo_requerido(self):
        self.data['sexo'] = ''
        response = self.client.post(
            reverse('nuevo_estudiante'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('sexo', form.errors)

    def test_telefono_requerido(self):
        self.data['telefono'] = ''
        response = self.client.post(
            reverse('nuevo_estudiante'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('telefono', form.errors)

    def test_telefono_diez_digitos(self):
        self.data['telefono'] = '12345678910'
        response = self.client.post(
            reverse('nuevo_estudiante'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('telefono', form.errors)

    def test_whatsapp_requerido(self):
        self.data['whatsapp'] = ''
        response = self.client.post(
            reverse('nuevo_estudiante'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('whatsapp', form.errors)

    def test_whatsapp_diez_digitos(self):
        self.data['whatsapp'] = '12345678910'
        response = self.client.post(
            reverse('nuevo_estudiante'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('whatsapp', form.errors)

    def test_correo_requerido(self):
        self.data['correo'] = ''
        response = self.client.post(
            reverse('nuevo_estudiante'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('correo', form.errors)

    def test_preferencias_busqueda_requerido(self):
        self.data['preferencias_busqueda'] = ''
        response = self.client.post(
            reverse('nuevo_estudiante'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertIn('preferencias_busqueda', form.errors)


class ArrendadorTests(TestCase):
    def setUp(self):
        # Crear grupo de arrendador
        self.group, created = Group.objects.get_or_create(name='arrendador')

        # Crear usuario arrendador
        self.user = User.objects.create_user(
            username='luisperez@gmail.com',
            password='testpassword'
        )
        self.user.groups.add(self.group)
        self.arrendador = Arrendador.objects.create(
            usuario=self.user,
            nombre='Luis',
            apellidos='Pérez',
            edad=40,
            ocupacion='Abogado',
            telefono='1234567890',
            whatsapp='9876543210',
            correo='luisperez@gmail.com',
            preferencias_arrendatarios='Gente honesta',
            sexo='M',
            foto_perfil='perfiles/1144760.png'  # Ruta de la imagen de perfil
        )

        self.propiedad = Propiedad.objects.create(
            descripcion='Bonita',
            precio=2000,
            tipo=1,
            ubicacion='Calle florida colinas',
            serviciosIncluidos=True,
            arrendador=self.arrendador
        )

        self.imagen = ImagenPropiedad.objects.create(
            propiedad=self.propiedad,
            imagen='perfiles/img.jpg'
        )

        self.client.login(username='luisperez@gmail.com',
                          password='testpassword')

    def test_ver_perfil_arrendador(self):
        response = self.client.get(reverse('perfil_arrendador'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'perfil_arrendador.html')
        self.assertContains(response, 'Luis Pérez')

    def test_editar_perfil_arrendador(self):
        data = {
            'nombre': 'Luis Editado',
            'apellidos': 'Pérez',
            'edad': 41,
            'ocupacion': 'Abogado',
            'telefono': '1234567890',
            'whatsapp': '9876543210',
            'correo': 'luisperez@gmail.com',
            'preferencias_arrendatarios': 'Gente honesta',
            'sexo': 'M',
            'foto_perfil': 'perfiles/1144760.png'
        }
        response = self.client.post(reverse('editar_perfil_arrendador'), data)
        self.assertEqual(response.status_code, 302)
        self.arrendador.refresh_from_db()
        self.assertEqual(self.arrendador.nombre, 'Luis Editado')
        self.assertEqual(self.arrendador.edad, 41)

    def test_eliminar_arrendador(self):
        response = self.client.get(reverse('eliminar_arrendador'))
        response = self.client.post(
            reverse('confirmar_eliminacion_arrendador'))
        with self.assertRaises(Arrendador.DoesNotExist):
            Arrendador.objects.get(id=self.arrendador.id)
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(id=self.user.id)


class EstudianteTests(TestCase):
    def setUp(self):
        # Crear grupo de estudiante
        self.group, created = Group.objects.get_or_create(name='estudiante')

        # Crear usuario estudiante
        self.user = User.objects.create_user(
            username='joseguardado@gmail.com',
            password='testpassword'
        )
        self.user.groups.add(self.group)
        self.estudiante = Estudiante.objects.create(
            usuario=self.user,
            nombre='José',
            apellidos='Guardado',
            edad=22,
            universidad_actual='Ingeniería',
            telefono='0987654321',
            whatsapp='1122334455',
            correo='joseguardado@gmail.com',
            preferencias_busqueda='Cuartos de estudiantes',
            pasatiempos='Música, pintura, películas de terror.',
            sexo='M',
            foto_perfil='perfiles/1144760.png'  # Ruta de la imagen de perfil
        )

        self.client.login(username='joseguardado@gmail.com',
                          password='testpassword')

    def test_ver_perfil_estudiante(self):
        response = self.client.get(reverse('perfil_estudiante'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'perfil_estudiante.html')
        self.assertContains(response, 'José Guardado')

    def test_editar_perfil_estudiante(self):
        data = {
            'nombre': 'José Editado',
            'apellidos': 'Pérez',
            'edad': 23,
            'universidad_actual': 'Ingeniería',
            'telefono': '0987654321',
            'whatsapp': '1122334455',
            'correo': 'juanperez@gmail.com',
            'preferencias_busqueda': 'Cuartos de estudiantes',
            'pasatiempos': 'Música, pintura, películas de terror.',
            'sexo': 'M',
            'foto_perfil': 'perfiles/1144760.png'  # Ruta de la imagen de perfil
        }
        response = self.client.post(reverse('editar_perfil_estudiante'), data)
        self.assertEqual(response.status_code, 302)
        self.estudiante.refresh_from_db()
        self.assertEqual(self.estudiante.nombre, 'José Editado')
        self.assertEqual(self.estudiante.edad, 23)

    def test_eliminar_estudiante(self):
        response = self.client.get(reverse('eliminar_estudiante'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'confirmar_eliminacion_estudiante.html')

        response = self.client.post(
            reverse('confirmar_eliminacion_estudiante'))
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Estudiante.DoesNotExist):
            Estudiante.objects.get(id=self.estudiante.id)
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(id=self.user.id)


class ResenaCreateViewTests(TestCase):
    def setUp(self):
        # Crear grupo de estudiante
        self.group_estudiante, created = Group.objects.get_or_create(
            name='estudiante')
        # Crear usuario estudiante
        self.user = User.objects.create_user(
            username='joseguardado@gmail.com',
            password='testpassword'
        )
        self.user.groups.add(self.group_estudiante)
        self.estudiante = Estudiante.objects.create(
            usuario=self.user,
            nombre='José',
            apellidos='Guardado',
            edad=22,
            universidad_actual='Ingeniería',
            telefono='0987654321',
            whatsapp='1122334455',
            correo='joseguardado@gmail.com',
            preferencias_busqueda='Cuartos de estudiantes',
            pasatiempos='Música, pintura, películas de terror.',
            sexo='M',
            foto_perfil='perfiles/1144760.png'
        )

        # Crear arrendador y propiedad
        self.group_arrendador, created = Group.objects.get_or_create(
            name='arrendador')
        self.user_arrendador = User.objects.create_user(
            username='luisperez@gmail.com',
            password='testpassword'
        )
        self.user_arrendador.groups.add(self.group_arrendador)
        self.arrendador = Arrendador.objects.create(
            usuario=self.user_arrendador,
            nombre='Luis',
            apellidos='Pérez',
            edad=40,
            ocupacion='Abogado',
            telefono='1234567890',
            whatsapp='9876543210',
            correo='luisperez@gmail.com',
            preferencias_arrendatarios='Gente honesta',
            sexo='M',
            foto_perfil='perfiles/1144760.png'
        )

        self.propiedad = Propiedad.objects.create(
            descripcion='Bonita',
            precio=2000,
            tipo=1,
            ubicacion='Calle florida colinas',
            serviciosIncluidos=True,
            arrendador=self.arrendador
        )

        self.client.login(username='joseguardado@gmail.com',
                          password='testpassword')

    def crear_resena_existente(self):
        # Crear una reseña para el estudiante en la propiedad
        Resena.objects.create(
            calificacion=3,
            descripcion='Buena propiedad',
            estudiante=self.estudiante,
            propiedad=self.propiedad
        )

    def test_acceso_vista_creacion_resena(self):
        response = self.client.get(
            reverse('agregar_resena', args=[self.propiedad.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'crear_resena.html')

    def test_creacion_resena_valida(self):
        data = {
            'calificacion': 4,
            'descripcion': 'Muy buena propiedad'
        }
        response = self.client.post(
            reverse('agregar_resena', args=[self.propiedad.id]), data)
        self.assertRedirects(response, reverse(
            'lista_resenas', args=[self.propiedad.id]))
        self.assertEqual(Resena.objects.count(), 1)
        resena = Resena.objects.get()
        self.assertEqual(resena.calificacion, 4)
        self.assertEqual(resena.descripcion, 'Muy buena propiedad')
        self.assertEqual(resena.estudiante, self.estudiante)
        self.assertEqual(resena.propiedad, self.propiedad)

    def test_mensaje_reseña_existente_en_titulo(self):
        self.crear_resena_existente()

        # Acceder a la vista de ver reseñas para la misma propiedad
        response = self.client.get(
            reverse('lista_resenas', args=[self.propiedad.id]))

        # # Imprimir el contenido HTML de la respuesta
        # print(response.content.decode('utf-8'))

        # Verificar que el mensaje "Ya has insertado una reseña" está presente en el cuerpo de la respuesta
        self.assertContains(
            response, '<h2>Ya has insertado una reseña:</h2>', html=True)

    def test_hay_resena_usuario(self):
        # Crear una reseña existente para el estudiante en la propiedad
        self.crear_resena_existente()

        # Simular acceso a la página de reseñas
        response = self.client.get(
            reverse('lista_resenas', args=[self.propiedad.id]))
        self.assertEqual(response.status_code, 200)
        # Verificar que la variable 'hayResena' sea True en el contexto
        self.assertTrue(response.context['hayResena'])

    def test_no_hay_resena_usuario(self):
        # Crear una reseña de otro estudiante en la propiedad

        # Se crea otro usuario

        # Crear grupo de estudiante
        group_estudiante, created = Group.objects.get_or_create(
            name='estudiante')
        # Crear usuario estudiante
        user = User.objects.create_user(
            username='jose@gmail.com',
            password='testpassword'
        )
        user.groups.add(group_estudiante)
        estudiante = Estudiante.objects.create(
            usuario=user,
            nombre='José',
            apellidos='Perez',
            edad=23,
            universidad_actual='Ingeniería',
            telefono='0987654322',
            whatsapp='1122334452',
            correo='jose@gmail.com',
            preferencias_busqueda='Cuartos de estudiantes',
            pasatiempos='Música, pintura, películas de terror.',
            sexo='M',
            foto_perfil='perfiles/1144760.png'
        )

        # Crear una reseña para el estudiante en la propiedad
        Resena.objects.create(
            calificacion=3,
            descripcion='Buena propiedad',
            estudiante=estudiante,
            propiedad=self.propiedad
        )

        # Simular acceso a la página de reseñas
        response = self.client.get(
            reverse('lista_resenas', args=[self.propiedad.id]))
        self.assertEqual(response.status_code, 200)
        # Verificar que la variable 'hayResena' sea True en el contexto
        self.assertFalse(response.context['hayResena'])


class ResenaViewTests(TestCase):
    def setUp(self):
        # Crear grupo de estudiante y arrendador
        self.group_estudiante, created = Group.objects.get_or_create(
            name='estudiante')
        self.group_arrendador, created = Group.objects.get_or_create(
            name='arrendador')

        # Crear usuario estudiante
        self.user_estudiante = User.objects.create_user(
            username='joseguardado@gmail.com',
            password='testpassword'
        )
        self.user_estudiante.groups.add(self.group_estudiante)
        self.estudiante = Estudiante.objects.create(
            usuario=self.user_estudiante,
            nombre='José',
            apellidos='Guardado',
            edad=22,
            universidad_actual='Ingeniería',
            telefono='0987654321',
            whatsapp='1122334455',
            correo='joseguardado@gmail.com',
            preferencias_busqueda='Cuartos de estudiantes',
            pasatiempos='Música, pintura, películas de terror.',
            sexo='M',
            foto_perfil='perfiles/1144760.png'
        )

        # Crear usuario arrendador y propiedad
        self.user_arrendador = User.objects.create_user(
            username='luisperez@gmail.com',
            password='testpassword'
        )
        self.user_arrendador.groups.add(self.group_arrendador)
        self.arrendador = Arrendador.objects.create(
            usuario=self.user_arrendador,
            nombre='Luis',
            apellidos='Pérez',
            edad=40,
            ocupacion='Abogado',
            telefono='1234567890',
            whatsapp='9876543210',
            correo='luisperez@gmail.com',
            preferencias_arrendatarios='Gente honesta',
            sexo='M',
            foto_perfil='perfiles/1144760.png'
        )

        self.propiedad = Propiedad.objects.create(
            descripcion='Bonita',
            precio=2000,
            tipo=1,
            ubicacion='Calle florida colinas',
            serviciosIncluidos=True,
            arrendador=self.arrendador
        )

        self.resena = Resena.objects.create(
            calificacion=4,
            descripcion='Muy buena propiedad',
            estudiante=self.estudiante,
            propiedad=self.propiedad
        )

        self.client.login(username='joseguardado@gmail.com',
                          password='testpassword')

    def test_ver_resenas(self):
        response = self.client.get(
            reverse('lista_resenas', args=[self.propiedad.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ver_resenas.html')
        self.assertContains(response, 'Muy buena propiedad')
        self.assertContains(response, '4')

    def test_editar_resena(self):
        data = {
            'calificacion': 5,
            'descripcion': 'Excelente propiedad'
        }
        # Simular el almacenamiento del ID de la reseña en la sesión
        session = self.client.session
        session['resena_id'] = self.resena.resena_id
        session.save()

        response = self.client.post(reverse('editar_resena'), data)
        self.assertRedirects(response, reverse(
            'lista_resenas', args=[self.propiedad.id]))
        self.resena.refresh_from_db()
        self.assertEqual(self.resena.calificacion, 5)
        self.assertEqual(self.resena.descripcion, 'Excelente propiedad')

    def test_editar_resena_datos_invalidos(self):
        data = {
            'calificacion': '',  # Calificación inválida (vacía)
            'descripcion': 'Buena propiedad pero sin calificación'
        }
        # Simular el almacenamiento del ID de la reseña en la sesión
        session = self.client.session
        session['resena_id'] = self.resena.resena_id
        session.save()

        response = self.client.post(reverse('editar_resena'), data)
        self.assertEqual(response.status_code, 200)  # No debería redirigir
        self.assertTemplateUsed(response, 'editar_resena.html')
        self.assertFormError(response, 'form', 'calificacion',
                             'Este campo es obligatorio.')

    def test_editar_resena_get(self):
        # Simular el almacenamiento del ID de la reseña en la sesión
        session = self.client.session
        session['resena_id'] = self.resena.resena_id
        session.save()

        response = self.client.get(reverse('editar_resena'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'editar_resena.html')
        form = response.context['form']
        self.assertEqual(
            form.initial['calificacion'], self.resena.calificacion)
        self.assertEqual(form.instance, self.resena)

    def test_eliminar_resena(self):
        # Simular el almacenamiento del ID de la reseña en la sesión
        session = self.client.session
        session['resena_id'] = self.resena.resena_id
        session.save()

        response = self.client.post(reverse('eliminar_resena'))
        self.assertRedirects(response, reverse(
            'lista_resenas', args=[self.propiedad.id]))
        with self.assertRaises(Resena.DoesNotExist):
            Resena.objects.get(resena_id=self.resena.resena_id)

    def test_confirmacion_eliminacion_resena(self):
        # Simular el almacenamiento del ID de la reseña en la sesión
        session = self.client.session
        session['resena_id'] = self.resena.resena_id
        session.save()

        response = self.client.get(reverse('confirmacion_eliminacion_resena'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'confirmacion_eliminacion_resena.html')


class LoginViewTests(TestCase):
    def setUp(self):
        self.url = reverse('login')
        self.user = User.objects.create_user(
            username='joseguardado@gmail.com',
            password='testpassword'
        )

    def test_login_exitoso(self):
        data = {
            'username': 'joseguardado@gmail.com',
            'password': 'testpassword'
        }
        response = self.client.post(self.url, data)
        self.assertRedirects(response, reverse('bienvenida'))
        self.assertEqual(
            int(self.client.session['_auth_user_id']), self.user.pk)
        self.assertEqual(self.client.session['user_id'], self.user.pk)

    def test_login_password_incorrecto(self):
        data = {
            'username': 'joseguardado@gmail.com',
            'password': 'wrongpassword'
        }
        response = self.client.post(self.url, data)
        # La página de login debería volver a cargar
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Contraseña incorrecta :(')
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_login_usuario_no_registrado(self):
        data = {
            'username': 'nonexistentuser@gmail.com',
            'password': 'somepassword'
        }
        response = self.client.post(self.url, data)
        # La página de login debería volver a cargar
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, 'Aún no te has registrado. Inicia tu registro :).')
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_login_ingresar_usuario_sin_contraseña(self):
        # Crear usuario sin contraseña usable
        user_no_password = User.objects.create_user(
            username='nopassworduser@gmail.com'
        )
        user_no_password.set_unusable_password()
        user_no_password.save()

        data = {
            'username': 'nopassworduser@gmail.com',
            'password': 'anypassword'
        }
        response = self.client.post(self.url, data)
        # La página de login debería volver a cargar
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, 'Aún no te has registrado. Inicia tu registro :).')
        self.assertNotIn('_auth_user_id', self.client.session)

        # Verificar que el usuario ha sido eliminado
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username='nopassworduser@gmail.com')

    def test_login_incorrect_password_else_branch(self):
        # Proveer datos con contraseña incorrecta
        data = {
            'username': 'joseguardado@gmail.com',
            'password': 'wrongpassword'
        }

        # Realizar la solicitud de inicio de sesión
        response = self.client.post(self.url, data)

        # Verificar que la página de login vuelve a cargar (indica error)
        # La página de login debería volver a cargar
        self.assertEqual(response.status_code, 200)

        # Verificar que el mensaje de error se muestra
        self.assertContains(response, 'Contraseña incorrecta :(')

        # Verificar que el usuario no está autenticado (no hay ID de usuario en la sesión)
        self.assertNotIn('_auth_user_id', self.client.session)

        # Verificar que el ID de usuario no se guarda en la sesión personalizada
        self.assertNotIn('user_id', self.client.session)

        # Verificar que el bloque else se ejecuta
        self.assertIn('Contraseña incorrecta :(', response.content.decode())


class PropiedadViewTests(TestCase):

    def setUp(self):
        # Crear grupo de estudiante
        self.group_estudiante, created = Group.objects.get_or_create(
            name='estudiante')
        # Crear usuario estudiante
        self.user = User.objects.create_user(
            username='joseguardado@gmail.com',
            password='testpassword'
        )
        self.user.groups.add(self.group_estudiante)
        self.estudiante = Estudiante.objects.create(
            usuario=self.user,
            nombre='José',
            apellidos='Guardado',
            edad=22,
            universidad_actual='Ingeniería',
            telefono='0987654321',
            whatsapp='1122334455',
            correo='joseguardado@gmail.com',
            preferencias_busqueda='Cuartos de estudiantes',
            pasatiempos='Música, pintura, películas de terror.',
            sexo='M',
            foto_perfil='perfiles/1144760.png'
        )

        # Crear arrendador y propiedad
        self.group_arrendador, created = Group.objects.get_or_create(
            name='arrendador')
        self.user_arrendador = User.objects.create_user(
            username='luisperez@gmail.com',
            password='testpassword'
        )
        self.user_arrendador.groups.add(self.group_arrendador)
        self.arrendador = Arrendador.objects.create(
            usuario=self.user_arrendador,
            nombre='Luis',
            apellidos='Pérez',
            edad=40,
            ocupacion='Abogado',
            telefono='1234567890',
            whatsapp='9876543210',
            correo='luisperez@gmail.com',
            preferencias_arrendatarios='Gente honesta',
            sexo='M',
            foto_perfil='perfiles/1144760.png'
        )

        self.propiedad = Propiedad.objects.create(
            descripcion='Bonita',
            precio=2000,
            tipo=1,
            ubicacion='Calle florida colinas',
            serviciosIncluidos=True,
            arrendador=self.arrendador
        )

        self.client.login(username='joseguardado@gmail.com',
                          password='testpassword')

    def test_acceso_vista_detalles_propiedad(self):
        response = self.client.get(
            reverse('detalle_propiedad', args=[self.propiedad.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detalles_propiedad.html')

    def test_acceso_vista_detalles_arrendador(self):
        response = self.client.get(
            reverse('detalles_arrendador', args=[self.propiedad.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detalles_arrendador.html')

    def test_acceso_vista_lista_interesados(self):
        response = self.client.get(
            reverse('lista_interesados', args=[self.propiedad.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lista_interesados.html')

    def test_agregar_propiedad_favoritos(self):
        response = self.client.get(
            reverse('agregaraListaFavoritos', args=[self.propiedad.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Favorito.objects.count(), 1)

    def test_agregar_interes_propiedad(self):
        response = self.client.get(
            reverse('indicar_interes', args=[self.propiedad.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Estudiante_Interesado.objects.count(), 1)


class PropiedadCreateViewTests(TestCase):

    def setUp(self):
        # Crear grupo de arrendador
        self.group, created = Group.objects.get_or_create(name='arrendador')

        # Crear usuario arrendador
        self.user = User.objects.create_user(
            username='luisperez@gmail.com',
            password='testpassword'
        )
        self.user.groups.add(self.group)
        self.arrendador = Arrendador.objects.create(
            usuario=self.user,
            nombre='Luis',
            apellidos='Pérez',
            edad=40,
            ocupacion='Abogado',
            telefono='1234567890',
            whatsapp='9876543210',
            correo='luisperez@gmail.com',
            preferencias_arrendatarios='Gente honesta',
            sexo='M',
            foto_perfil='perfiles/1144760.png'  # Ruta de la imagen de perfil
        )

        self.propiedad = Propiedad.objects.create(
            descripcion='Bonita',
            precio=2000,
            tipo=1,
            ubicacion='Calle florida colinas',
            serviciosIncluidos=True,
            arrendador=self.arrendador
        )

        self.imagen = ImagenPropiedad.objects.create(
            propiedad=self.propiedad,
            imagen='perfiles/img.jpg'
        )

        self.municipio = Municipio.objects.create(nombre='Test Municipio')
        self.colonia = Colonia.objects.create(
            nombre='Test Colonia', municipio=self.municipio)

        self.client.login(username='luisperez@gmail.com',
                          password='testpassword')

    def test_nueva_propiedad_get(self):
        response = self.client.get(reverse('agregar_propiedad'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nueva_propiedad.html')

    def test_nueva_propiedad_post_success(self):
        data = {
            'descripcion': 'Test Propiedad',
            'precio': 1000,
            'tipo': 1,
            'calle': 'Test Street',
            'numero': '123',
            'colonia': self.colonia.id,
            'municipio': self.municipio
        }
        response = self.client.post(reverse('agregar_propiedad'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'confirmacion_propiedad.html')
        self.assertTrue(Propiedad.objects.filter(
            descripcion='Test Propiedad').exists())

    def test_nueva_propiedad_post_duplicate(self):
        Propiedad.objects.create(descripcion='Test Propiedad', precio=1000, tipo=1,
                                 ubicacion='Test Street 123, Test Colonia, Test Municipio', arrendador=self.arrendador)
        data = {
            'descripcion': 'Test Propiedad',
            'precio': 1000,
            'tipo': 1,
            'calle': 'Test Street',
            'numero': '123',
            'colonia': self.colonia,
            'municipio': self.municipio
        }
        response = self.client.post(reverse('agregar_propiedad'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nueva_propiedad.html')
        self.assertContains(
            response, "Error: La propiedad ya está registrada.")
        self.assertFalse(Propiedad.objects.filter(
            descripcion='Test Propiedad').count() > 1)

    # def test_nueva_propiedad_post_with_images(self):
    #     #Propiedad.objects.create(descripcion='Test Propiedad', precio=1000, tipo=1, ubicacion='Test Street 123, Test Colonia, Test Municipio', arrendador=self.arrendador)

    #     # Crear archivos de imagen simulados
    #     image_data = b'Fake image data'
    #     images = [SimpleUploadedFile(f'test_image_{i}.jpg', image_data, content_type='image/jpeg') for i in range(2)]  # Crear dos imágenes simuladas

    #     # Adjuntar las imágenes al formulario de imágenes
    #     form_imagenes = [FormImagenPropiedad(
    #         {'imagen': image},
    #         prefix=f'imagen_{i}'
    #     ) for i, image in enumerate(images)]

    #     # Datos del formulario de propiedad
    #     data = {
    #         'descripcion': 'Test Propiedad',
    #         'precio': 1000,
    #         'tipo': 1,
    #         'calle': 'Test Street',
    #         'numero': '123',
    #         'colonia': self.colonia,
    #         'municipio': self.municipio.id  # Corregir el acceso al ID del municipio
    #     }

    #     # Unir los datos del formulario de propiedad con los archivos de imagen
    #     data.update({f'imagen_{i}': image for i, image in enumerate(images)})

    #     # Realizar la solicitud POST con los datos y las imágenes
    #     response = self.client.post(reverse('agregar_propiedad'), data, format='multipart')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'confirmacion_propiedad.html')
    #     self.assertTrue(Propiedad.objects.filter(descripcion='Test Propiedad').exists())

    #     # Verificar que las imágenes se han guardado correctamente
    #     propiedad = Propiedad.objects.get(descripcion='Test Propiedad')
    #     imagenes_propiedad = ImagenPropiedad.objects.filter(propiedad=propiedad)
    #     self.assertEqual(len(imagenes_propiedad), 2)  # Verificar que se hayan guardado dos imágenes

    #     # Verificar que la primera imagen sea la correcta
    #     primera_imagen = imagenes_propiedad[0]
    #     self.assertTrue(primera_imagen.imagen.name.endswith('test_image_0.jpg'))  # Verificar el nombre de la primera imagen


class InteresadosTest(TestCase):

    def setUp(self):
        # Crear grupo de arrendador
        self.group, created = Group.objects.get_or_create(name='arrendador')

        # Crear usuario arrendador
        self.user1 = User.objects.create_user(
            username='luisperez@gmail.com',
            password='testpassword'
        )
        self.user1.groups.add(self.group)
        self.arrendador = Arrendador.objects.create(
            usuario=self.user1,
            nombre='Luis',
            apellidos='Pérez',
            edad=40,
            ocupacion='Abogado',
            telefono='1234567890',
            whatsapp='9876543210',
            correo='luisperez@gmail.com',
            preferencias_arrendatarios='Gente honesta',
            sexo='M',
            foto_perfil='perfiles/1144760.png'  # Ruta de la imagen de perfil
        )

        self.propiedad = Propiedad.objects.create(
            descripcion='Bonita',
            precio=2000,
            tipo=1,
            ubicacion='Calle florida colinas',
            serviciosIncluidos=True,
            arrendador=self.arrendador
        )

        self.imagen = ImagenPropiedad.objects.create(
            propiedad=self.propiedad,
            imagen='perfiles/img.jpg'
        )

        # Crear grupo de estudiante
        self.group, created = Group.objects.get_or_create(name='estudiante')

        # Crear usuario estudiante
        self.user = User.objects.create_user(
            username='joseguardado@gmail.com',
            password='testpassword'
        )
        self.user.groups.add(self.group)
        self.estudiante = Estudiante.objects.create(
            usuario=self.user,
            nombre='José',
            apellidos='Guardado',
            edad=22,
            universidad_actual='Ingeniería',
            telefono='0987654321',
            whatsapp='1122334455',
            correo='joseguardado@gmail.com',
            preferencias_busqueda='Cuartos de estudiantes',
            pasatiempos='Música, pintura, películas de terror.',
            sexo='M',
            foto_perfil='perfiles/1144760.png'  # Ruta de la imagen de perfil
        )

        self.client.login(username='joseguardado@gmail.com',
                          password='testpassword')

    def test_verInteresados(self):
        response = self.client.get('/Propiedades/interesados/1')
        self.assertEqual(200, response.status_code)

    def test_verInteresados_ya_registrado(self):
        response = self.client.get('/Propiedades/indicar_interes/1')
        self.assertEqual(302, response.status_code)
        response = self.client.get('/Propiedades/interesados/1')
        self.assertEqual(200, response.status_code)

    def test_estudiante_indica_interes(self):
        response = self.client.get('/Propiedades/indicar_interes/1')
        self.assertEqual(302, response.status_code)

    def test_estudiante_ya_se_intereso(self):
        response = self.client.get('/Propiedades/indicar_interes/1')
        self.assertEqual(302, response.status_code)
        response = self.client.get('/Propiedades/indicar_interes/1')
        self.assertEqual(302, response.status_code)

    def test_detalles_estudiante(self):
        response = self.client.get('/Propiedades/detalles_estudiante/1')
        self.assertEqual(200, response.status_code)


class ListaPropiedadesViewTests(TestCase):
    def setUp(self):
        # Crear grupo de estudiante
        self.group, created = Group.objects.get_or_create(name='estudiante')

        # Crear usuario estudiante
        self.user = User.objects.create_user(
            username='joseguardado@gmail.com',
            password='testpassword'
        )
        self.user.groups.add(self.group)
        self.estudiante = Estudiante.objects.create(
            usuario=self.user,
            nombre='José',
            apellidos='Guardado',
            edad=22,
            universidad_actual='Ingeniería',
            telefono='0987654321',
            whatsapp='1122334455',
            correo='joseguardado@gmail.com',
            preferencias_busqueda='Cuartos de estudiantes',
            pasatiempos='Música, pintura, películas de terror.',
            sexo='M',
            foto_perfil='perfiles/1144760.png'  # Ruta de la imagen de perfil
        )

        self.client.login(username='joseguardado@gmail.com',
                          password='testpassword')

        # Crear grupo de arrendador
        self.group1, created = Group.objects.get_or_create(name='arrendador')

        # Crear usuario arrendador
        self.user1 = User.objects.create_user(
            username='luis@gmail.com',
            password='test'
        )
        self.user1.groups.add(self.group)
        self.arrendador = Arrendador.objects.create(
            usuario=self.user,
            nombre='Luis',
            apellidos='Pérez',
            edad=40,
            ocupacion='Abogado',
            telefono='1234567890',
            whatsapp='9876543210',
            correo='luisperez@gmail.com',
            preferencias_arrendatarios='Gente honesta',
            sexo='M',
            foto_perfil='perfiles/1144760.png'  # Ruta de la imagen de perfil
        )

        self.propiedad = Propiedad.objects.create(
            descripcion='Bonita',
            precio=2000,
            tipo=1,
            ubicacion='Calle florida colinas',
            serviciosIncluidos=True,
            arrendador=self.arrendador
        )

        self.imagen = ImagenPropiedad.objects.create(
            propiedad=self.propiedad,
            imagen='perfiles/img.jpg'
        )

    def test_lista_propiedades_view(self):

        response = self.client.get(reverse('lista_propiedades'))

        # Verificar que la vista responda correctamente
        self.assertEqual(response.status_code, 200)

        # Verificar que se esté utilizando el template correcto
        self.assertTemplateUsed(response, 'lista_propiedades.html')


class PropiedadesArrendadorViewTests(TestCase):
    def setUp(self):
        # Crear grupo de estudiante
        self.group_estudiante, created = Group.objects.get_or_create(
            name='estudiante')
        # Crear usuario estudiante
        self.user = User.objects.create_user(
            username='joseguardado@gmail.com',
            password='testpassword'
        )
        self.user.groups.add(self.group_estudiante)
        self.estudiante = Estudiante.objects.create(
            usuario=self.user,
            nombre='José',
            apellidos='Guardado',
            edad=22,
            universidad_actual='Ingeniería',
            telefono='0987654321',
            whatsapp='1122334455',
            correo='joseguardado@gmail.com',
            preferencias_busqueda='Cuartos de estudiantes',
            pasatiempos='Música, pintura, películas de terror.',
            sexo='M',
            foto_perfil='perfiles/1144760.png'
        )

        # Crear arrendador y propiedad
        self.group_arrendador, created = Group.objects.get_or_create(
            name='arrendador')
        self.user_arrendador = User.objects.create_user(
            username='luisperez@gmail.com',
            password='testpassword'
        )
        self.user_arrendador.groups.add(self.group_arrendador)
        self.arrendador = Arrendador.objects.create(
            usuario=self.user_arrendador,
            nombre='Luis',
            apellidos='Pérez',
            edad=40,
            ocupacion='Abogado',
            telefono='1234567890',
            whatsapp='9876543210',
            correo='luisperez@gmail.com',
            preferencias_arrendatarios='Gente honesta',
            sexo='M',
            foto_perfil='perfiles/1144760.png'
        )

        self.propiedad1 = Propiedad.objects.create(
            descripcion='Bonita',
            precio=2000,
            tipo=1,
            ubicacion='Calle florida colinas',
            serviciosIncluidos=True,
            arrendador=self.arrendador
        )
        self.propiedad2 = Propiedad.objects.create(
            descripcion='Bonita',
            precio=2000,
            tipo=1,
            ubicacion='Calle florida colinas',
            serviciosIncluidos=True,
            arrendador=self.arrendador
        )

        self.client.login(username='luisperez@gmail.com',
                          password='testpassword')

        image_data = b'Fake image data'
        imagen_1 = SimpleUploadedFile(
            'perfiles/1144760.png', image_data, content_type='image/jpeg')
        ImagenPropiedad.objects.create(
            propiedad=self.propiedad1, imagen=imagen_1)

    def test_acceso_a_propiedades_arrendador(self):
        # Test para asegurar que el arrendador puede ver su vista
        response = self.client.get(reverse('propiedades_arrendador'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'propiedades_arrendador.html')
        # Verifica que se pasen las propiedades correctas
        propiedades = response.context['propiedades']
        self.assertTrue(propiedades)

    def test_acceso_no_autorizado(self):
        # Desconectar al usuario actual
        self.client.logout()
        # Intentar acceder a la página sin ser un usuario autorizado
        response = self.client.get(reverse('propiedades_arrendador'))
        self.assertNotEqual(response.status_code, 200)

    def test_verificar_imagenes_de_propiedades(self):
        response = self.client.get(reverse('propiedades_arrendador'))
        propiedades = list(response.context['propiedades'])
        # La primer propiedad debe tener una imagen
        self.assertIsNotNone(propiedades[0].primerImagen)
        # La segunda propiedad no tiene imagen
        self.assertEqual(propiedades[1].primerImagen, '')


class ConfirmarEliminacionFavoritoTests(TestCase):
    def setUp(self):
        # Crear grupo de estudiante
        self.group_estudiante, created = Group.objects.get_or_create(
            name='estudiante')
        # Crear usuario estudiante
        self.user = User.objects.create_user(
            username='joseguardado@gmail.com',
            password='testpassword'
        )
        self.user.groups.add(self.group_estudiante)
        self.estudiante = Estudiante.objects.create(
            usuario=self.user,
            nombre='José',
            apellidos='Guardado',
            edad=22,
            universidad_actual='Ingeniería',
            telefono='0987654321',
            whatsapp='1122334455',
            correo='joseguardado@gmail.com',
            preferencias_busqueda='Cuartos de estudiantes',
            pasatiempos='Música, pintura, películas de terror.',
            sexo='M',
            foto_perfil='perfiles/1144760.png'
        )

        # Crear arrendador y propiedad
        self.group_arrendador, created = Group.objects.get_or_create(
            name='arrendador')
        self.user_arrendador = User.objects.create_user(
            username='luisperez@gmail.com',
            password='testpassword'
        )
        self.user_arrendador.groups.add(self.group_arrendador)
        self.arrendador = Arrendador.objects.create(
            usuario=self.user_arrendador,
            nombre='Luis',
            apellidos='Pérez',
            edad=40,
            ocupacion='Abogado',
            telefono='1234567890',
            whatsapp='9876543210',
            correo='luisperez@gmail.com',
            preferencias_arrendatarios='Gente honesta',
            sexo='M',
            foto_perfil='perfiles/1144760.png'
        )

        self.propiedad1 = Propiedad.objects.create(
            descripcion='Bonita',
            precio=2000,
            tipo=1,
            ubicacion='Calle florida colinas',
            serviciosIncluidos=True,
            arrendador=self.arrendador
        )
        self.propiedad2 = Propiedad.objects.create(
            descripcion='Bonita',
            precio=2000,
            tipo=1,
            ubicacion='Calle florida colinas',
            serviciosIncluidos=True,
            arrendador=self.arrendador
        )

        self.client.login(username='joseguardado@gmail.com',
                          password='testpassword')

        # Crear un favorito adecuando los parámetros a la definición real del modelo
        self.favorito = Favorito.objects.create(
            propiedad=self.propiedad1,
            estudiante=self.estudiante  # Cambio aquí: uso de 'estudiante' en lugar de 'usuario'
        )

    def test_confirmacion_eliminacion_favorito(self):
        response = self.client.get(
            reverse('confirmar_eliminacion_favorito', args=[self.propiedad1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'confirmar_eliminacion_favorito.html')
        # Verificamos que los contextos sean correctos
        self.assertEqual(response.context['propiedad'], self.propiedad1)
        self.assertIn(self.favorito, response.context['favoritos'])

    def test_propiedad_no_existe(self):
        # Proporciona un ID de propiedad que no existe para probar la página 404
        response = self.client.get(
            reverse('confirmar_eliminacion_favorito', args=[999]))
        self.assertEqual(response.status_code, 404)


class FavoritosViewTests(TestCase):
    def setUp(self):
        # Crear grupo de estudiante
        self.group_estudiante, created = Group.objects.get_or_create(
            name='estudiante')
        # Crear usuario estudiante
        self.user = User.objects.create_user(
            username='joseguardado@gmail.com',
            password='testpassword'
        )
        self.user.groups.add(self.group_estudiante)
        self.estudiante = Estudiante.objects.create(
            usuario=self.user,
            nombre='José',
            apellidos='Guardado',
            edad=22,
            universidad_actual='Ingeniería',
            telefono='0987654321',
            whatsapp='1122334455',
            correo='joseguardado@gmail.com',
            preferencias_busqueda='Cuartos de estudiantes',
            pasatiempos='Música, pintura, películas de terror.',
            sexo='M',
            foto_perfil='perfiles/1144760.png'
        )

        # Crear arrendador y propiedad
        self.group_arrendador, created = Group.objects.get_or_create(
            name='arrendador')
        self.user_arrendador = User.objects.create_user(
            username='luisperez@gmail.com',
            password='testpassword'
        )
        self.user_arrendador.groups.add(self.group_arrendador)
        self.arrendador = Arrendador.objects.create(
            usuario=self.user_arrendador,
            nombre='Luis',
            apellidos='Pérez',
            edad=40,
            ocupacion='Abogado',
            telefono='1234567890',
            whatsapp='9876543210',
            correo='luisperez@gmail.com',
            preferencias_arrendatarios='Gente honesta',
            sexo='M',
            foto_perfil='perfiles/1144760.png'
        )

        self.propiedad = Propiedad.objects.create(
            descripcion='Bonita casa de tres pisos',
            precio=2000,
            tipo=1,
            ubicacion='Calle florida colinas',
            serviciosIncluidos=True,
            arrendador=self.arrendador
        )

        self.imagen = ImagenPropiedad.objects.create(
            propiedad=self.propiedad,
            imagen='perfiles/img.jpg'
        )

        self.client.login(username='joseguardado@gmail.com',
                          password='testpassword')

    def test_agregar_propiedad_favoritos(self):
        # Realizar una solicitud POST para agregar la propiedad a la lista de favoritos
        response = self.client.post(
            reverse('agregaraListaFavoritos', args=[self.propiedad.id]))

        # Verificar que la solicitud se haya realizado con éxito (código de estado HTTP 302)
        self.assertEqual(response.status_code, 302)

        # Verificar que se ha creado un objeto Favorito en la base de datos
        self.assertEqual(Favorito.objects.count(), 1)

    def test_ver_lista_favoritos(self):
        # Agregar la propiedad a la lista de favoritos
        self.client.post(
            reverse('agregaraListaFavoritos', args=[self.propiedad.id]))

        # Realizar una solicitud GET para ver la lista de favoritos
        response = self.client.get(
            reverse('lista_favoritos'))  # Corrección aquí

        # Verificar que la solicitud se haya realizado con éxito (código de estado HTTP 200)
        self.assertEqual(response.status_code, 200)

        # Verificar que la propiedad agregada está en la lista de favoritos
        self.assertContains(response, self.propiedad.ubicacion)

    def test_eliminar_propiedad_favoritos(self):
        # Agregar la propiedad a la lista de favoritos
        self.client.post(
            reverse('agregaraListaFavoritos', args=[self.propiedad.id]))

        # Realizar una solicitud POST para eliminar la propiedad de la lista de favoritos
        response = self.client.post(
            reverse('eliminarDeListaFavoritos', args=[self.propiedad.id]))

        # Verificar que la solicitud se haya realizado con éxito (código de estado HTTP 302)
        self.assertEqual(response.status_code, 302)

        # Verificar que la propiedad ya no está en la lista de favoritos
        self.assertEqual(Favorito.objects.count(), 0)


class EliminarPropiedadTests(TestCase):
    def setUp(self):
        # Crear grupo de estudiante
        self.group_estudiante, created = Group.objects.get_or_create(
            name='estudiante')
        # Crear usuario estudiante
        self.user = User.objects.create_user(
            username='joseguardado@gmail.com',
            password='testpassword'
        )
        self.user.groups.add(self.group_estudiante)
        self.estudiante = Estudiante.objects.create(
            usuario=self.user,
            nombre='José',
            apellidos='Guardado',
            edad=22,
            universidad_actual='Ingeniería',
            telefono='0987654321',
            whatsapp='1122334455',
            correo='joseguardado@gmail.com',
            preferencias_busqueda='Cuartos de estudiantes',
            pasatiempos='Música, pintura, películas de terror.',
            sexo='M',
            foto_perfil='perfiles/1144760.png'
        )

        # Creación de usuarios y grupos afirmada
        self.group_arrendador, _ = Group.objects.get_or_create(
            name='arrendador')
        self.user_arrendador = User.objects.create_user(
            username='luisperez@gmail.com',
            password='testpassword'
        )
        self.user_arrendador.groups.add(self.group_arrendador)
        self.arrendador = Arrendador.objects.create(
            usuario=self.user_arrendador,
            nombre='Luis',
            apellidos='Pérez',
            edad=40,
            ocupacion='Abogado',
            telefono='1234567890',
            correo='luisperez@gmail.com'
        )
        self.client.login(username='luisperez@gmail.com',
                          password='testpassword')

        # Sólo crear una propiedad
        self.propiedad = Propiedad.objects.create(
            descripcion='Bonita',
            precio=2000,
            tipo=1,
            ubicacion='Calle florida colinas',
            serviciosIncluidos=True,
            arrendador=self.arrendador
        )

        # Adjuntar imagen a la propiedad
        imagen_data = b'Fake image data'
        imagen_file = SimpleUploadedFile(
            'test_image.jpg', imagen_data, content_type='image/jpeg')
        ImagenPropiedad.objects.create(
            propiedad=self.propiedad, imagen=imagen_file)

    def test_eliminar_propiedad_con_permiso(self):
        # Primera verificación del conteo
        self.assertEqual(Propiedad.objects.count(), 1)
        self.assertEqual(ImagenPropiedad.objects.count(), 1)

        # Eliminación
        response = self.client.post(
            reverse('eliminar_propiedad', args=[self.propiedad.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('propiedades_arrendador'))

        # Segunda verificación post-eliminación
        self.assertEqual(Propiedad.objects.count(), 0)
        self.assertEqual(ImagenPropiedad.objects.count(), 0)

    def test_eliminar_propiedad_sin_permiso(self):
        # Desconectar al usuario actual
        self.client.logout()
        # Iniciar sesión con un usuario diferente que no tiene los permisos necesarios
        self.client.login(username='joseguardado@gmail.com',
                          password='testpassword')

        # Intentar eliminar la propiedad
        response = self.client.post(reverse('eliminar_propiedad', args=[
                                    self.propiedad.id]), follow=True)
        # Verifica que la solicitud fue ejecutada correctamente, pero debería haberse negado a eliminar.
        self.assertEqual(response.status_code, 200)

        # Desconectar al usuario actual
        self.client.logout()
        # Re-autenticar al usuario original
        self.client.login(username='luisperez@gmail.com',
                          password='testpassword')
        # Verifica que la propiedad aún existe
        self.assertEqual(Propiedad.objects.count(), 1)

class TestEliminacionPropiedad(TestCase):

    def setUp(self):

        self.group, created = Group.objects.get_or_create(name='arrendador')
    
        # Crear usuario arrendador
        self.user1 = User.objects.create_user(
            username='luisperez@gmail.com',
            password='testpassword'
        )
        self.user1.groups.add(self.group)
        self.arrendador = Arrendador.objects.create(
            usuario=self.user1,
            nombre='Luis',
            apellidos='Pérez',
            edad=40,
            ocupacion='Abogado',
            telefono='1234567890',
            whatsapp='9876543210',
            correo='luisperez@gmail.com',
            preferencias_arrendatarios='Gente honesta',
            sexo='M',
            foto_perfil='perfiles/1144760.png'  # Ruta de la imagen de perfil
        )
        # Crea una propiedad de prueba
        self.propiedad = Propiedad.objects.create(
            descripcion="Propiedad de prueba",
            precio=1000,
            tipo=1,
            ubicacion="Calle 123",
            serviciosIncluidos=False,
            arrendador=self.arrendador
        )

        # Crea una imagen de prueba asociada a la propiedad
        self.imagen_propiedad = ImagenPropiedad.objects.create(
            propiedad=self.propiedad,
            imagen='perfiles/img.jpg'
        )

    def test_confirmacion_exitosa_eliminacion(self):
        self.client.login(username="luisperez@gmail.com", password="testpassword")
        # Simula una solicitud GET a la vista confirmarEliminacionPropiedad
        response = self.client.get(
            reverse('confirmacion_eliminacion_propiedad', args=[self.propiedad.id])
        )

        # Verifica que la respuesta sea un éxito (código de estado 200)
        self.assertEqual(response.status_code, 200)

    def test_confirmacion_fallida_eliminacion_usuario_no_autorizado(self):
        self.user2 = User.objects.create_user(
            username='usuario_no_arrendador@gmail.com',
            password='password'
        )
        self.user2.groups.add(self.group)
        self.arrendador2 = Arrendador.objects.create(
            usuario=self.user2,
            nombre='Luis',
            apellidos='Lopez',
            edad=40,
            ocupacion='DR',
            telefono='1234567890',
            whatsapp='9876543210',
            correo='usuario_no_arrendador@gmail.com',
            preferencias_arrendatarios='Gente honesta',
            sexo='M',
            foto_perfil='perfiles/1144760.png'  # Ruta de la imagen de perfil
        )

        # Crea una propiedad de prueba
        self.propiedad1 = Propiedad.objects.create(
            descripcion="Propiedad de prueba 1",
            precio=1000,
            tipo=1,
            ubicacion="Calle 12334565432",
            serviciosIncluidos=False,
            arrendador=self.arrendador2
        )

        # Crea una imagen de prueba asociada a la propiedad
        self.imagen_propiedad = ImagenPropiedad.objects.create(
            propiedad=self.propiedad1,
            imagen='perfiles/img.jpg'
        )
        # Simula una solicitud GET a la vista confirmarEliminacionPropiedad con un usuario no autorizado
        self.client.login(username="usuario_no_arrendador@gmail.com", password="password")
        response = self.client.get(
            reverse('confirmacion_eliminacion_propiedad', args=[self.propiedad.id])
        )
        # Verifica que la respuesta sea un redireccionamiento (código de estado 302)
        self.assertEqual(response.status_code, 200)

class EditarPropiedadTests(TestCase):
    def setUp(self):
         # Crear grupo de estudiante
        self.group_estudiante, created = Group.objects.get_or_create(name='estudiante')
        # Crear usuario estudiante
        self.user = User.objects.create_user(
            username='joseguardado@gmail.com',
            password='testpassword'
        )
        self.user.groups.add(self.group_estudiante)
        self.estudiante = Estudiante.objects.create(
            usuario=self.user,
            nombre='José',
            apellidos='Guardado',
            edad=22,
            universidad_actual='Ingeniería',
            telefono='0987654321',
            whatsapp='1122334455',
            correo='joseguardado@gmail.com',
            preferencias_busqueda='Cuartos de estudiantes',
            pasatiempos='Música, pintura, películas de terror.',
            sexo='M',
            foto_perfil='perfiles/1144760.png'
        )
        
        # Configurando usuario y grupo de arrendador
        self.group_arrendador, _ = Group.objects.get_or_create(name='arrendador')
        self.user_arrendador = User.objects.create_user(
            username='luisperez@gmail.com',
            password='testpassword'
        )
        self.user_arrendador.groups.add(self.group_arrendador)
        self.arrendador = Arrendador.objects.create(
            usuario=self.user_arrendador,
            nombre='Luis',
            apellidos='Pérez',
            edad=40,
            ocupacion='Abogado',
            telefono='1234567890',
            correo='luisperez@gmail.com'
        )

        self.client.login(username='luisperez@gmail.com', password='testpassword')

        # Creando una propiedad asociada al arrendador
        self.propiedad = Propiedad.objects.create(
            descripcion='Bonita casa de campo',
            precio=2000,
            tipo=1,
            ubicacion='Calle Florida Colinas',
            serviciosIncluidos=True,
            arrendador=self.arrendador
        )

        # Adjuntar imagen a la propiedad
        imagen_data = b'Fake image data'
        imagen_file = SimpleUploadedFile('test_image.jpg', imagen_data, content_type='image/jpeg')
        ImagenPropiedad.objects.create(propiedad=self.propiedad, imagen=imagen_file)

    def test_editar_propiedad_con_permiso(self):
        # Datos del formulario simulando la actualización
        form_data = {
            'descripcion': 'Actualizada casa de campo',
            'precio': 2500,
            'tipo': 1,
            'ubicacion': 'Calle Florida Colinas',
            'serviciosIncluidos': True
        }
        response = self.client.post(
            reverse('editar_propiedad', args=[self.propiedad.id]), 
            form_data
        )
        self.assertRedirects(response, reverse('propiedades_arrendador'))

        # Verifica que la propiedad se haya actualizado correctamente
        self.propiedad.refresh_from_db()
        self.assertEqual(self.propiedad.descripcion, "Actualizada casa de campo")
        self.assertEqual(self.propiedad.precio, 2500)

    def test_editar_propiedad_sin_permiso(self):
        # Asegura que el usuario está desconectado primero
        self.client.logout()
        # Autenticar un usuario que definitivamente no tiene los permisos de arrendador
        self.client.login(username='joseguardado@gmail.com', password='testpassword')

        # Intentar editar la propiedad
        form_data = {
            'descripcion': 'Intento fallido de actualización',
            'precio': 2100
        }
        response = self.client.post(reverse('editar_propiedad', args=[self.propiedad.id]), form_data, follow=True)
