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
    url = models.URLField()
    organizacao = models.CharField(max_length=255)
    salario = models.CharField(max_length=255, null=True, blank=True)
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)
    adicional_logo = models.BooleanField(default=False)
    destacado = models.BooleanField(default=False)
    cor_destaque_adicional = models.CharField(max_length=7, null=True, blank=True) # Assume código de cor hex
    impulso_semanal_adicional = models.BooleanField(default=False)
    impulso_diario_adicional = models.BooleanField(default=False)
    usuario = models.ForeignKey('usuarios.Perfil', on_delete=models.CASCADE, limit_choices_to={'tipo': 'EMPRESA'})
    criado_em = models.DateTimeField(default=timezone.now)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

# Modelo para Tags
class Tag(models.Model):
    nome = models.CharField(max_length=100)
    criado_em = models.DateTimeField(default=timezone.now)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

# Modelo de Associação para Tags de Vagas
class VagaTag(models.Model):
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('vaga', 'tag')

    def __str__(self):
        return f"{self.vaga.titulo} - {self.tag.nome}"
