from django import forms

#Uso api form
class FormularioContacto(forms.Form):
    consulta=forms.CharField()
    email=forms.EmailField()
    mensaje=forms.CharField()