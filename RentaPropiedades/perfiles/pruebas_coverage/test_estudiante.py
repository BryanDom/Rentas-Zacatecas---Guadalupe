from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class TestRegistrarEstudiante(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')
        self.client.force_login(self.user)

    def test_valid_form(self):
        form_data = {
            'correo': 'testuser@example.com',
            'foto_perfil': 'path/to/image.jpg'
        }
        response = self.client.post(reverse('registrar_estudiante'), form_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('compromiso'))

    def test_invalid_form(self):
        form_data = {
            'correo': 'invaliduser@example.com',
            'foto_perfil': 'path/to/image.jpg'
        }
        response = self.client.post(reverse('registrar_estudiante'), form_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'correo', 'Ya existe un usuario con ese correo electrónico y tiene una contraseña asociada.')

    def test_existing_user(self):
        existing_user = User.objects.create_user(username='existinguser', email='existinguser@example.com', password='existingpassword')
        form_data = {
            'correo': 'existinguser@example.com',
            'foto_perfil': 'path/to/image.jpg'
        }
        response = self.client.post(reverse('registrar_estudiante'), form_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'correo', 'Ya existe un usuario con ese correo electrónico y tiene una contraseña asociada.')

class TestRegistrarContrasena(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')
        self.client.force_login(self.user)

    def test_valid_form(self):
        form_data = {
            'password': 'newpassword'
        }
        response = self.client.post(reverse('registrar_contrasena'), form_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('confirmacion_cuenta'))

    def test_invalid_form(self):
        form_data = {
            'password': ''
        }
        response = self.client.post(reverse('registrar_contrasena'), form_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'password', 'Este campo es requerido.')

class TestVerPerfilEstudiante(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')
        self.client.force_login(self.user)

    def test_view(self):
        response = self.client.get(reverse('ver_perfil_estudiante'))
        self.assertEqual(response.status_code, 200)
    
class TestEliminarEstudiante(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')
        self.client.force_login(self.user)

    def test_view(self):
        response = self.client.get(reverse('eliminar_estudiante'))
        self.assertEqual(response.status_code, 200)

class TestConfirmaEliminacionEstudiante(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')
        self.client.force_login(self.user)

    def test_view(self):
        response = self.client.get(reverse('confirma_eliminar_estudiante'))
        self.assertEqual(response.status_code, 200)

class TestEditarPerfilEstudiante(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')
        self.client.force_login(self.user)

    def test_valid_form(self):
        form_data = {
            'correo': 'newuser@example.com',
            'foto_perfil': 'path/to/image.jpg'
        }
        response = self.client.post(reverse('editar_perfil_estudiante'), form_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('perfil_estudiante'))

    def test_invalid_form(self):
        form_data = {
            'correo': 'invaliduser@example.com',
            'foto_perfil': 'path/to/image.jpg'
        }
        response = self.client.post(reverse('editar_perfil_estudiante'), form_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'correo', 'Ya existe un usuario con ese correo electrónico y tiene una contraseña asociada.')

class TestListaPropiedades(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')
        self.client.force_login(self.user)

    def test_view(self):
        response = self.client.get(reverse('lista_propiedades'))
        self.assertEqual(response.status_code, 200)
        