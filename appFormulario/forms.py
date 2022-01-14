from django import forms

class EmpleadoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellidos = forms.CharField(label="Apellidos", max_length=150)
    edad = forms.IntegerField(label="Edad")
    direccion = forms.CharField(label="Direccion")
    email = forms.EmailField(label="Email", required=False)
    
