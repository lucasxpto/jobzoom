from django.urls import path
from jobs.views import home, publicar_vaga

urlpatterns = [
    path('', home, name='home'),
    path('vaga/publicar/', publicar_vaga, name='publicar_vaga'),
]
