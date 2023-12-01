from django.shortcuts import render

def home(request):
    return render(request, 'jobs/home.html')

def publicar_vaga(request):
    return render(request, 'jobs/publicar_vaga.html')
    