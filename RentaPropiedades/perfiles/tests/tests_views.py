from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Group
from perfiles.models import Arrendador, Estudiante
from Propiedades.models import Propiedad, ImagenPropiedad, Resena, Favorito, Estudiante_Interesado
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


class ResenaCreateViewTests(TestCase):
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

        # Crear arrendador y propiedad
        self.group_arrendador, created = Group.objects.get_or_create(name='arrendador')
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

        self.client.login(username='joseguardado@gmail.com', password='testpassword')

    def crear_resena_existente(self):
        # Crear una reseña para el estudiante en la propiedad
        Resena.objects.create(
            calificacion=3,
            descripcion='Buena propiedad',
            estudiante=self.estudiante,
            propiedad=self.propiedad
        )

    def test_acceso_vista_creacion_resena(self):
        response = self.client.get(reverse('agregar_resena', args=[self.propiedad.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'crear_resena.html')

    def test_creacion_resena_valida(self):
        data = {
            'calificacion': 4,
            'descripcion': 'Muy buena propiedad'
        }
        response = self.client.post(reverse('agregar_resena', args=[self.propiedad.id]), data)
        self.assertRedirects(response, reverse('lista_resenas', args=[self.propiedad.id]))
        self.assertEqual(Resena.objects.count(), 1)
        resena = Resena.objects.get()
        self.assertEqual(resena.calificacion, 4)
        self.assertEqual(resena.descripcion, 'Muy buena propiedad')
        self.assertEqual(resena.estudiante, self.estudiante)
        self.assertEqual(resena.propiedad, self.propiedad)
    
    def test_mensaje_reseña_existente_en_titulo(self):
        self.crear_resena_existente()

        # Acceder a la vista de ver reseñas para la misma propiedad
        response = self.client.get(reverse('lista_resenas', args=[self.propiedad.id]))

        # # Imprimir el contenido HTML de la respuesta
        # print(response.content.decode('utf-8'))

        # Verificar que el mensaje "Ya has insertado una reseña" está presente en el cuerpo de la respuesta
        self.assertContains(response, '<h2>Ya has insertado una reseña:</h2>', html=True)
    
    def test_hay_resena_usuario(self):
        # Crear una reseña existente para el estudiante en la propiedad
        self.crear_resena_existente()

        # Simular acceso a la página de reseñas
        response = self.client.get(reverse('lista_resenas', args=[self.propiedad.id]))
        self.assertEqual(response.status_code, 200)
        # Verificar que la variable 'hayResena' sea True en el contexto
        self.assertTrue(response.context['hayResena'])
    
    def test_no_hay_resena_usuario(self):
        # Crear una reseña de otro estudiante en la propiedad

        #Se crea otro usuario

        # Crear grupo de estudiante
        group_estudiante, created = Group.objects.get_or_create(name='estudiante')
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
        response = self.client.get(reverse('lista_resenas', args=[self.propiedad.id]))
        self.assertEqual(response.status_code, 200)
        # Verificar que la variable 'hayResena' sea True en el contexto
        self.assertFalse(response.context['hayResena'])


class ResenaViewTests(TestCase):
    def setUp(self):
        # Crear grupo de estudiante y arrendador
        self.group_estudiante, created = Group.objects.get_or_create(name='estudiante')
        self.group_arrendador, created = Group.objects.get_or_create(name='arrendador')

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

        self.client.login(username='joseguardado@gmail.com', password='testpassword')

    def test_ver_resenas(self):
        response = self.client.get(reverse('lista_resenas', args=[self.propiedad.id]))
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
        self.assertRedirects(response, reverse('lista_resenas', args=[self.propiedad.id]))
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
        self.assertFormError(response, 'form', 'calificacion', 'Este campo es obligatorio.')

    def test_editar_resena_get(self):
        # Simular el almacenamiento del ID de la reseña en la sesión
        session = self.client.session
        session['resena_id'] = self.resena.resena_id
        session.save()

        response = self.client.get(reverse('editar_resena'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'editar_resena.html')
        form = response.context['form']
        self.assertEqual(form.initial['calificacion'], self.resena.calificacion)
        self.assertEqual(form.instance, self.resena)

    def test_eliminar_resena(self):
        # Simular el almacenamiento del ID de la reseña en la sesión
        session = self.client.session
        session['resena_id'] = self.resena.resena_id
        session.save()

        response = self.client.post(reverse('eliminar_resena'))
        self.assertRedirects(response, reverse('lista_resenas', args=[self.propiedad.id]))
        with self.assertRaises(Resena.DoesNotExist):
            Resena.objects.get(resena_id=self.resena.resena_id)
    
    def test_confirmacion_eliminacion_resena(self):
        # Simular el almacenamiento del ID de la reseña en la sesión
        session = self.client.session
        session['resena_id'] = self.resena.resena_id
        session.save()

        response = self.client.get(reverse('confirmacion_eliminacion_resena'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'confirmacion_eliminacion_resena.html')

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
        self.assertEqual(int(self.client.session['_auth_user_id']), self.user.pk)
        self.assertEqual(self.client.session['user_id'], self.user.pk)

    def test_login_password_incorrecto(self):
        data = {
            'username': 'joseguardado@gmail.com',
            'password': 'wrongpassword'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)  # La página de login debería volver a cargar
        self.assertContains(response, 'Contraseña incorrecta :(')
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_login_usuario_no_registrado(self):
        data = {
            'username': 'nonexistentuser@gmail.com',
            'password': 'somepassword'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)  # La página de login debería volver a cargar
        self.assertContains(response, 'Aún no te has registrado. Inicia tu registro :).')
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
        self.assertEqual(response.status_code, 200)  # La página de login debería volver a cargar
        self.assertContains(response, 'Aún no te has registrado. Inicia tu registro :).')
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
        self.assertEqual(response.status_code, 200)  # La página de login debería volver a cargar

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

        # Crear arrendador y propiedad
        self.group_arrendador, created = Group.objects.get_or_create(name='arrendador')
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

        self.client.login(username='joseguardado@gmail.com', password='testpassword')
        
    def test_acceso_vista_detalles_propiedad(self):
        response = self.client.get(reverse('detalle_propiedad', args=[self.propiedad.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detalles_propiedad.html')
        
    def test_acceso_vista_detalles_arrendador(self):
        response = self.client.get(reverse('detalles_arrendador', args=[self.propiedad.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detalles_arrendador.html')
        
    def test_acceso_vista_lista_interesados(self):
        response = self.client.get(reverse('lista_interesados', args=[self.propiedad.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lista_interesados.html')
        
    def test_agregar_propiedad_favoritos(self):
        response = self.client.get(reverse('agregaraListaFavoritos', args=[self.propiedad.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Favorito.objects.count(), 1)
        
    def test_agregar_interes_propiedad(self):
        response = self.client.get(reverse('indicar_interes', args=[self.propiedad.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Estudiante_Interesado.objects.count(), 1)
