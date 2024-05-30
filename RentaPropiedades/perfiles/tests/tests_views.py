from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Group
from perfiles.models import Arrendador, Estudiante
from Propiedades.models import Propiedad, ImagenPropiedad
from perfiles.forms import FormArrendador, FormEstudiante

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
        response = self.client.post(reverse('nuevo_arrendador'), data=self.data)
        self.assertRedirects(response, reverse('compromiso'))
        self.assertEqual(Arrendador.objects.count(), 1)
        arrendador = Arrendador.objects.get()
        self.assertEqual(arrendador.nombre, 'Luis')
        self.assertEqual(arrendador.apellidos, 'Pérez')
        self.assertEqual(arrendador.edad, 40)
        response = self.client.post(reverse('contrasena'), data=self.password_data)
        user = User.objects.get(username=self.data['correo'])
        self.assertTrue(user.check_password(self.password_data['password']))
        self.assertTrue(user.is_active)
        response = self.client.get(reverse('confirmar'))
        self.assertTemplateUsed(response, 'confirmacion_cuenta.html')

    def test_creacion_perfil_no_valido(self):
        response = self.client.post(reverse('nuevo_arrendador'), data=self.data)
        self.assertRedirects(response, reverse('compromiso'))
        self.assertEqual(Arrendador.objects.count(), 1)
        arrendador = Arrendador.objects.get()
        self.assertEqual(arrendador.nombre, 'Luis')
        self.assertEqual(arrendador.apellidos, 'Pérez')
        self.assertEqual(arrendador.edad, 40)
        response = self.client.post(reverse('contrasena'), data=self.password_data)
        user = User.objects.get(username=self.data['correo'])
        self.assertTrue(user.check_password(self.password_data['password']))
        self.assertTrue(user.is_active)
        response = self.client.get(reverse('confirmar'))
        self.assertTemplateUsed(response, 'confirmacion_cuenta.html')
        # correo repetido
        response = self.client.post(reverse('nuevo_arrendador'), data=self.data)
        self.assertFalse(Arrendador.objects.count() == 2)


    def test_acceso_vista_creacion(self):
        response = self.client.get(reverse('nuevo_arrendador'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registrar_arrendador.html')

    def test_nombre_requerido(self):
        self.data['nombre'] = ''
        response = self.client.post(reverse('nuevo_arrendador'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('nombre', form.errors)

    def test_apellidos_requeridos(self):
        self.data['apellidos'] = ''
        response = self.client.post(reverse('nuevo_arrendador'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('apellidos', form.errors)

    def test_edad_requerida(self):
        self.data['edad'] = ''
        response = self.client.post(reverse('nuevo_arrendador'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('edad', form.errors)

    def test_sexo_requerido(self):
        self.data['sexo'] = ''
        response = self.client.post(reverse('nuevo_arrendador'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('sexo', form.errors)

    def test_ocupacion_requerida(self):
        self.data['ocupacion'] = ''
        response = self.client.post(reverse('nuevo_arrendador'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('ocupacion', form.errors)

    def test_telefono_requerido(self):
        self.data['telefono'] = ''
        response = self.client.post(reverse('nuevo_arrendador'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('telefono', form.errors)

    def test_telefono_diez_digitos(self):
        self.data['telefono'] = '12345678910'
        response = self.client.post(reverse('nuevo_arrendador'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('telefono', form.errors)

    def test_whatsapp_requerido(self):
        self.data['whatsapp'] = ''
        response = self.client.post(reverse('nuevo_arrendador'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('whatsapp', form.errors)

    def test_whatsapp_diez_digitos(self):
        self.data['whatsapp'] = '12345678910'
        response = self.client.post(reverse('nuevo_arrendador'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('whatsapp', form.errors)

    def test_correo_requerido(self):
        self.data['correo'] = ''
        response = self.client.post(reverse('nuevo_arrendador'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('correo', form.errors)

    def test_preferencias_arrendatarios_requerido(self):
        self.data['preferencias_arrendatarios'] = ''
        response = self.client.post(reverse('nuevo_arrendador'), data=self.data)
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
        response = self.client.post(reverse('nuevo_estudiante'), data=self.data)
        self.assertRedirects(response, reverse('compromiso'))
        self.assertEqual(Estudiante.objects.count(), 1)
        estudiante = Estudiante.objects.get()
        self.assertEqual(estudiante.nombre, 'José')
        self.assertEqual(estudiante.apellidos, 'Guardado')
        self.assertEqual(estudiante.edad, 18)
        response = self.client.post(reverse('contrasena'), data=self.password_data)
        user = User.objects.get(username=self.data['correo'])
        self.assertTrue(user.check_password(self.password_data['password']))
        self.assertTrue(user.is_active)
        response = self.client.get(reverse('confirmar'))
        self.assertTemplateUsed(response, 'confirmacion_cuenta.html')

    def test_creacion_perfil_no_valido(self):
        response = self.client.post(reverse('nuevo_estudiante'), data=self.data)
        self.assertRedirects(response, reverse('compromiso'))
        self.assertEqual(Estudiante.objects.count(), 1)
        estudiante = Estudiante.objects.get()
        self.assertEqual(estudiante.nombre, 'José')
        self.assertEqual(estudiante.apellidos, 'Guardado')
        self.assertEqual(estudiante.edad, 18)
        response = self.client.post(reverse('contrasena'), data=self.password_data)
        user = User.objects.get(username=self.data['correo'])
        self.assertTrue(user.check_password(self.password_data['password']))
        self.assertTrue(user.is_active)
        response = self.client.get(reverse('confirmar'))
        self.assertTemplateUsed(response, 'confirmacion_cuenta.html')
        # correo repetido
        response = self.client.post(reverse('nuevo_estudiante'), data=self.data)
        self.assertFalse(Estudiante.objects.count() == 2)

    def test_nombre_requerido(self):
        self.data['nombre'] = ''
        response = self.client.post(reverse('nuevo_estudiante'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('nombre', form.errors)

    def test_apellidos_requeridos(self):
        self.data['apellidos'] = ''
        response = self.client.post(reverse('nuevo_estudiante'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('apellidos', form.errors)

    def test_edad_requerida(self):
        self.data['edad'] = ''
        response = self.client.post(reverse('nuevo_estudiante'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('edad', form.errors)

    def test_sexo_requerido(self):
        self.data['sexo'] = ''
        response = self.client.post(reverse('nuevo_estudiante'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('sexo', form.errors)

    def test_telefono_requerido(self):
        self.data['telefono'] = ''
        response = self.client.post(reverse('nuevo_estudiante'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('telefono', form.errors)

    def test_telefono_diez_digitos(self):
        self.data['telefono'] = '12345678910'
        response = self.client.post(reverse('nuevo_estudiante'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('telefono', form.errors)

    def test_whatsapp_requerido(self):
        self.data['whatsapp'] = ''
        response = self.client.post(reverse('nuevo_estudiante'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('whatsapp', form.errors)

    def test_whatsapp_diez_digitos(self):
        self.data['whatsapp'] = '12345678910'
        response = self.client.post(reverse('nuevo_estudiante'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('whatsapp', form.errors)

    def test_correo_requerido(self):
        self.data['correo'] = ''
        response = self.client.post(reverse('nuevo_estudiante'), data=self.data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('correo', form.errors)

    def test_preferencias_busqueda_requerido(self):
        self.data['preferencias_busqueda'] = ''
        response = self.client.post(reverse('nuevo_estudiante'), data=self.data)
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
            descripcion= 'Bonita',
            precio = 2000,
            tipo = 1,
            ubicacion = 'Calle florida colinas',
            serviciosIncluidos= True,
            arrendador=self.arrendador
        )

        self.imagen = ImagenPropiedad.objects.create(
            propiedad=self.propiedad,
            imagen ='perfiles/img.jpg'
        )

        self.client.login(username='luisperez@gmail.com', password='testpassword')

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
        response = self.client.post(reverse('confirmar_eliminacion_arrendador'))
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
            preferencias_busqueda = 'Cuartos de estudiantes',
            pasatiempos = 'Música, pintura, películas de terror.',
            sexo='M',
            foto_perfil='perfiles/1144760.png'  # Ruta de la imagen de perfil
        )

        self.client.login(username='joseguardado@gmail.com', password='testpassword')

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
        self.assertTemplateUsed(response, 'confirmar_eliminacion_estudiante.html')

        response = self.client.post(reverse('confirmar_eliminacion_estudiante'))
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Estudiante.DoesNotExist):
            Estudiante.objects.get(id=self.estudiante.id)
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(id=self.user.id)