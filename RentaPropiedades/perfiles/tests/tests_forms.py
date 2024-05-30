from django.test import TestCase
from perfiles.forms import FormEstudiante, FormArrendador

class TestFormArrendador(TestCase):
    def setUp(self):
        self.data = {
            'nombre': 'Luis',
            'apellidos': 'Pérez',
            'edad': 40,
            'foto_perfil': None,
            'ocupacion': 'Abogado',
            'telefono': '1234567890',
            'whatsapp': '9876543210',
            'correo': 'juanperez@gmail.com',
            'preferencias_arrendatarios': 'Gente honesta',
            'sexo': 'M'
        }


    def test_nombre_requerido(self):
        self.data['nombre'] = ''
        form = FormArrendador(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertIn('nombre', form.errors)

    def test_apellidos_requeridos(self):
        self.data['apellidos'] = ''
        form = FormArrendador(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertIn('apellidos', form.errors)

    def test_edad_requerida(self):
        self.data['edad'] = ''
        form = FormArrendador(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertIn('edad', form.errors)

    def test_sexo_requerido(self):
        self.data['sexo'] = ''
        form = FormArrendador(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertIn('sexo', form.errors)

    def test_foto_opcional(self):
        self.data['foto_perfil'] = None
        form = FormArrendador(data=self.data)
        self.assertTrue(form.is_valid())

    def test_ocupacion_requerida(self):
        self.data['ocupacion'] = ''
        form = FormArrendador(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertIn('ocupacion', form.errors)

    def test_telefono_requerido(self):
        self.data['telefono'] = ''
        form = FormArrendador(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertIn('telefono', form.errors)

    def test_telefono_diez_digitos(self):
        self.data['telefono'] = '12345678910'
        form = FormArrendador(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertIn('telefono', form.errors)

    def test_whatsapp_requerido(self):
        self.data['whatsapp'] = ''
        form = FormArrendador(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertIn('whatsapp', form.errors)

    def test_whatsapp_diez_digitos(self):
        self.data['whatsapp'] = '12345678910'
        form = FormArrendador(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertIn('whatsapp', form.errors)

    def test_telefono_whatsapp_iguales(self):
        self.data['whatsapp'] = '1234567890'
        form = FormArrendador(data=self.data)
        self.assertTrue(form.is_valid())

    def test_correo_requerido(self):
        self.data['correo'] = ''
        form = FormArrendador(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertIn('correo', form.errors)

    def test_preferencias_arrendatarios_requerido(self):
        self.data['preferencias_arrendatarios'] = ''
        form = FormArrendador(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertIn('preferencias_arrendatarios', form.errors)


class TestFormEstudiante(TestCase):
    def setUp(self):
        self.data = {
            'nombre': 'José',
            'apellidos': 'Guardado',
            'edad': 18,
            'foto_perfil': None,
            'universidad_actual': 'UAZ',
            'telefono': '1234567890',
            'whatsapp': '9876543210',
            'correo': 'juanperez@gmail.com',
            'preferencias_busqueda': 'Cuartos de estudiantes',
            'pasatiempos': 'Música, pintura, películas de terror.',
            'sexo': 'M'
        }

    def test_nombre_requerido(self):
        self.data['nombre'] = ''
        form = FormEstudiante(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertIn('nombre', form.errors)

    def test_apellidos_requeridos(self):
        self.data['apellidos'] = ''
        form = FormEstudiante(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertIn('apellidos', form.errors)

    def test_edad_requerida(self):
        self.data['edad'] = ''
        form = FormEstudiante(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertIn('edad', form.errors)

    def test_sexo_requerido(self):
        self.data['sexo'] = ''
        form = FormEstudiante(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertIn('sexo', form.errors)

    def test_foto_opcional(self):
        self.data['foto_perfil'] = None
        form = FormEstudiante(data=self.data)
        self.assertTrue(form.is_valid())

    def test_universidad_requerida(self):
        self.data['universidad_actual'] = ''
        form = FormEstudiante(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertIn('universidad_actual', form.errors)

    def test_telefono_requerido(self):
        self.data['telefono'] = ''
        form = FormEstudiante(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertIn('telefono', form.errors)

    def test_telefono_diez_digitos(self):
        self.data['telefono'] = '12345678910'
        form = FormEstudiante(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertIn('telefono', form.errors)

    def test_whatsapp_requerido(self):
        self.data['whatsapp'] = ''
        form = FormEstudiante(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertIn('whatsapp', form.errors)

    def test_whatsapp_diez_digitos(self):
        self.data['whatsapp'] = '12345678910'
        form = FormEstudiante(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertIn('whatsapp', form.errors)

    def test_telefono_whatsapp_iguales(self):
        self.data['whatsapp'] = '1234567890'
        form = FormEstudiante(data=self.data)
        self.assertTrue(form.is_valid())

    def test_correo_requerido(self):
        self.data['correo'] = ''
        form = FormEstudiante(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertIn('correo', form.errors)

    def test_preferencias_busqueda_requerido(self):
        self.data['preferencias_busqueda'] = ''
        form = FormEstudiante(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertIn('preferencias_busqueda', form.errors)

    def test_pasatiempos_requerido(self):
        self.data['pasatiempos'] = ''
        form = FormEstudiante(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertIn('pasatiempos', form.errors)
    
