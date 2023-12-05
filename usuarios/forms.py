from django.forms import ModelForm

from usuarios.models import Perfil


class PerfilForm(ModelForm):
    class Meta:
        model = Perfil
        fields = ['tipo']
