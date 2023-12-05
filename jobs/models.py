from django.db import models
from django.utils import timezone


# Enum para os tipos de vagas
class TipoVaga(models.TextChoices):
    TEMPO_INTEGRAL = 'TEMPO_INTEGRAL', 'Tempo integral'
    MEIO_PERIODO = 'MEIO_PERIODO', 'Meio período'
    CONTRATADO = 'CONTRATADO', 'Contratado'
    TEMPORARIO = 'TEMPORARIO', 'Temporário'
    ESTAGIARIO = 'ESTAGIARIO', 'Estagiário'
    VOLUNTARIO = 'VOLUNTARIO', 'Voluntário'
    DIARISTA = 'DIARISTA', 'Diarista'
    OUTRO = 'OUTRO', 'Outro'


# Modelo para Vagas
class Vaga(models.Model):
    titulo = models.CharField(max_length=255)
    localizacao = models.CharField(max_length=255)
    tipo = models.CharField(max_length=50, choices=TipoVaga.choices)
    descricao = models.TextField(null=False, blank=False)
    organizacao = models.CharField(max_length=255)
    salario = models.CharField(max_length=255, null=True, blank=True)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(default=timezone.now)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
