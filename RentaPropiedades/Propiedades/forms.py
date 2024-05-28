from django import forms
from Propiedades.models import Propiedad, ImagenPropiedad, Resena


class FormPropiedad(forms.ModelForm):

    class Meta:
        model = Propiedad
        exclude = ['ubicacion', 'arrendador']
        widgets = {
            'descripcion': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Ingresa la descripción de la propiedad'}
            ),
            'precio': forms.NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Precio de la propiedad',
                       'min': 100, 'title': 'Solo precios superiores a $100'}
            ),
            'tipo': forms.Select(
                attrs={'class': 'form-control'}
            ),
        }


class FormImagenPropiedad(forms.ModelForm):

    class Meta:
        model = ImagenPropiedad
        fields = ['imagen']


class FiltrosPropiedad(forms.Form):
    tipo = forms.ChoiceField(
        choices=[(1, 'Casa'), (2, 'Departamento'), (3, 'Cuarto')],
        required=False
    )
    servicios = forms.BooleanField(
        required=False,
        initial=True
    )
    precio_min = forms.IntegerField(
        required=False,
        min_value=100,
        widget=forms.NumberInput(attrs={'size': '10'})
    )
    precio_max = forms.IntegerField(
        required=False,
        min_value=100,
        widget=forms.NumberInput(attrs={'size': '10'})
    )


class CalificacionEstrellasFormField(forms.TypedChoiceField):

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = [(i, i) for i in range(1, 6)]
        kwargs['coerce'] = int
        super().__init__(*args, **kwargs)


class FormResena(forms.ModelForm):
    calificacion = CalificacionEstrellasFormField()

    class Meta:
        model = Resena
        fields = ['descripcion', 'calificacion']
