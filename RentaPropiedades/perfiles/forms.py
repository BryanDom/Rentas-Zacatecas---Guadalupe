from django import forms
from .models import Estudiante, Arrendador
from django.contrib.auth.models import User


class FormEstudiante(forms.ModelForm):

    class Meta:
        model = Estudiante
        exclude = ['usuario']  # Excluimos el campo 'usuario'

        widgets = {
            'nombre': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Ingresa tu nombre',
                       'required': True}
            ),
            'apellidos': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Ingresa tus apellidos',
                       'required': True}
            ),
            'edad': forms.NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Edad',
                       'min': 18,
                       'title': 'Debes de ser mayor a 18 años',
                       'required': True}
            ),
            'foto_perfil': forms.FileInput(
                attrs={'required': False}
            ),
            'universidad_actual': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Ingresa tu universidad',
                       'required': True}
            ),
            'telefono': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': '1234567890',
                       'pattern': r'^\d{10}$',
                       'title': 'El teléfono debe contener exactamente' +
                       ' 10 dígitos y solo números.',
                       'required': True}
            ),
            'whatsapp': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': '1234567890',
                       'pattern': r'^\d{10}$',
                       'title': 'El WhatsApp debe contener exactamente ' +
                       '10 dígitos y solo números.',
                       'required': True}
            ),
            'correo': forms.EmailInput(
                attrs={'class': 'form-control',
                       'placeholder': 'ejemplo@dominio.com',
                       'required': True}
            ),
            'preferencias_busqueda': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Preferencias de búsqueda',
                       'required': True}
            ),
            'pasatiempos': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Pasatiempos',
                       'required': True}
            )
        }
    sexo = forms.ChoiceField(choices=[('M', 'Masculino'),
                                      ('F', 'Femenino'),
                                      ('O', 'Otro')],
                             widget=forms.RadioSelect(attrs={
                                 'class': 'custom-radio-buttons'
                             }))


class FormArrendador(forms.ModelForm):

    class Meta:
        model = Arrendador
        # Excluimos el campo 'usuario'
        exclude = ['usuario']

        widgets = {
            'nombre': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Ingresa tu nombre',
                       'required': True}
            ),
            'apellidos': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Ingresa tus apellidos',
                       'required': True}
            ),
            'edad': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder':
                       'Edad', 'min': 18,
                       'title': 'Debes de ser mayor a 18 años',
                       'required': True}
            ),
            'foto_perfil': forms.FileInput(
                attrs={'class': 'form-control',
                       'required': False}
            ),
            'ocupacion': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Ingresa tu ocupación',
                       'required': True}
            ),
            'telefono': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': '1234567890',
                       'pattern': r'^\d{10}$',
                       'title': 'El teléfono debe contener exactamente ' +
                       '10 dígitos y solo números.',
                       'required': True}
            ),
            'whatsapp': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': '1234567890',
                       'pattern': r'^\d{10}$',
                       'title': 'El WhatsApp debe contener exactamente ' +
                       '10 dígitos y solo números.',
                       'required': True}
            ),
            'correo': forms.EmailInput(
                attrs={'class': 'form-control',
                       'placeholder': 'ejemplo@dominio.com',
                       'required': True}
            ),
            'preferencias_arrendatarios': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Preferencias de búsqueda',
                       'required': True}
            )
        }

    sexo = forms.ChoiceField(choices=[('M', 'Masculino'),
                                      ('F', 'Femenino'),
                                      ('O', 'Otro')],
                             widget=forms.RadioSelect(
                                 attrs={'class': 'custom-radio-buttons'}))


class UserForm(forms.ModelForm):
    re_pass = forms.CharField(
        label='Confirma contraseña',
        widget=forms.PasswordInput(attrs={'class':
                                          'form-control'}),
        required=True
    )

    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class':
                                          'form-control'}),
        required=True
    )

    class Meta:
        model = User
        # Solo incluye los campos de contraseña y confirmación de contraseña
        fields = ['password', 're_pass']

    def clean_password(self, *args, **kwargs):
        if self.data['password'] != self.data['re_pass']:
            raise forms.ValidationError(
                'Las contraseñas no son iguales',
                code='passwords_not_equals')
        return self.data['password']

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
