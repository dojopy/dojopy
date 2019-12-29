from django import forms
from .models import ModelContact

class RegistrarContacto(forms.Form):
    name = forms.CharField(label='Nombre', max_length=100)
    correo = forms.EmailField(label='Email', max_length=200)
    mensaje = forms.CharField(label='Mensaje', max_length=250)

    def registrar_contact(self):
            new_message = ModelContact(name=self.data['name'],
                            correo=self.data['correo'],
                            mensaje=self.data['mensaje'])
            new_message.save()
            return 'Registro exitoso'
