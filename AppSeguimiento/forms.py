from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import *

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Correo electrónico', 'autocomplete': 'off'}),
        label="Correo electrónico")

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Contraseña', 'autocomplete': 'off'}),
        label="Contraseña")
    
class ImportarDatosForm(forms.Form):
    archivo_excel = forms.FileField(label='Seleccionar archivo Excel')
    
class BusquedaEquiposForm(forms.Form):
    ubicacion = forms.CharField(required=False)
    equipo = forms.CharField(required=False)
    sede = forms.CharField(required=False)