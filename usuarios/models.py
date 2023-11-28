from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=[('EMPRESA', 'Empresa'), ('CANDIDATO', 'Candidato')])
    # Outros campos conforme necessário

    def __str__(self):
        return self.usuario.username
