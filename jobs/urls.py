from django.urls import path

from jobs import views
from jobs.views import home, publicar_vaga

app_name = 'jobs'

urlpatterns = [
    path('', home, name='home'),
    path('minhas-vagas/', views.minhas_vagas, name='minhas_vagas'),
    path('vaga/<int:vaga_id>/', views.vaga, name='vaga'),
    path('api/vagas/', views.api_listar_vagas, name='api_listar_vagas'),
    path('editar-vaga/<int:vaga_id>/', views.editar_vaga, name='editar_vaga'),
    path('publicar/', publicar_vaga, name='publicar_vaga'),

]
