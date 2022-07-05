from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User



class formulario_afiliados(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    direccion = forms.CharField(max_length=40)
    dni = forms.IntegerField()
    telefono = forms.IntegerField()
    fecha_nacimiento = forms.DateField()

class user_edit_form(UserCreationForm):

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la Contraseña", widget=forms.PasswordInput)


class formulario_proyectos(forms.Form):

    titulo = forms.CharField(max_length=40)
    contenido = forms.CharField(max_length=35000)
    autor = forms.CharField(max_length=40)
    resumen = forms.CharField(max_length=5000)

