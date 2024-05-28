from django.test import TestCase
from perfiles.forms import FormEstudiante, CandidatoForm, VotacionForm
from perfiles.models import Partido, Candidato

class TestFormEstudiante(TestCase):
    def setUp(self):
        self.data = {
            'nombre': 'Juan',
            'apellidos': 'Pérez',
            'edad': 25,
            'foto_perfil': None,
            'universidad_actual': 'Universidad XYZ',
            'telefono': '1234567890',
            'whatsapp': '9876543210',
            'correo': 'juan@example.com',
            'preferencias_busqueda': 'Busco habitación individual',
            'pasatiempos': 'Leer y hacer ejercicio',
            'sexo': 'M'
        }

    def test_formulario_valido(self):
        form = FormEstudiante(self.data)
        self.assertTrue(form.is_valid())

    def test_nombre_vacio(self):
        self.data['nombre'] = ''
        form = FormEstudiante(self.data)
        self.assertFalse(form.is_valid())

    def test_apellidos_vacios(self):
        self.data['apellidos'] = ''
        form = FormEstudiante(self.data)
        self.assertFalse(form.is_valid())

    def test_edad_minima(self):
        self.data['edad'] = 17  # Edad mínima permitida
        form = FormEstudiante(self.data)
        self.assertFalse(form.is_valid())

    def test_foto_perfil_invalida(self):
        self.data['foto_perfil'] = 'ruta/invalida.jpg'
        form = FormEstudiante(self.data)
        self.assertFalse(form.is_valid())

    def test_telefono_invalido(self):
        self.data['telefono'] = '123'  # Teléfono con menos de 10 dígitos
        form = FormEstudiante(self.data)
        self.assertFalse(form.is_valid())

    def test_whatsapp_invalido(self):
        self.data['whatsapp'] = '987'  # WhatsApp con menos de 10 dígitos
        form = FormEstudiante(self.data)
        self.assertFalse(form.is_valid())

    def test_correo_invalido(self):
        self.data['correo'] = 'correo_invalido'  # Correo electrónico inválido
        form = FormEstudiante(self.data)
        self.assertFalse(form.is_valid())

    def test_sexo_invalido(self):
        self.data['sexo'] = 'X'  # Opción de sexo inválida
        form = FormEstudiante(self.data)
        self.assertFalse(form.is_valid())

    def test_clean_password(self):
        form = FormEstudiante(self.data)
        self.assertEqual(form.clean_password(), '12345')  # Suponiendo una lógica específica

    def test_save(self):
        form = FormEstudiante(self.data)
        estudiante = form.save(commit=False)
        self.assertEqual(estudiante.nombre, 'Juan')  # Verificando que se guarda correctamente