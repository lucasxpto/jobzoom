from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from jobs.models import Vaga, TipoVaga
from usuarios.models import Perfil


def home(request):
    return render(request, 'jobs/home.html')


def api_listar_vagas(request):
    query = request.GET.get('q')
    if query:
        vagas = Vaga.objects.filter(titulo__icontains=query).order_by('criado_em').reverse().values(
            'id',
            'titulo',
            'localizacao',
            'tipo',
            'localizacao',
            'descricao',
            'organizacao',
            'salario',
            'logo',
            'criado_em',
        )
    else:
        vagas = Vaga.objects.all().order_by('criado_em').reverse().values(
            'id',
            'titulo',
            'localizacao',
            'tipo',
            'localizacao',
            'descricao',
            'organizacao',
            'salario',
            'logo',
            'criado_em',
        )
    return JsonResponse(list(vagas), safe=False)


def publicar_vaga(request):
    if not request.user.is_authenticated:
        return redirect(f"{reverse('usuarios:login')}?next={request.path}")

    # Verifica se o usuário tem um perfil e se é do tipo 'EMPRESA'
    try:
        perfil_usuario = Perfil.objects.get(usuario=request.user)
        if perfil_usuario.tipo != 'EMPRESA':
            messages.error(request, 'Apenas empresas podem publicar vagas.')
            return redirect('jobs:home')
    except Perfil.DoesNotExist:
        messages.error(request, 'Perfil não encontrado.')
        return redirect('usuarios:registrar')

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        localizacao = request.POST.get('localizacao')
        tipo = request.POST.get('tipo')
        descricao = request.POST.get('descricao')
        organizacao = request.POST.get('organizacao')
        salario = request.POST.get('salario')
        logo = request.FILES.get('logo')

        vaga = Vaga(
            titulo=titulo,
            localizacao=localizacao,
            tipo=tipo,
            descricao=descricao,
            organizacao=organizacao,
            salario=salario,
            logo=logo,
            usuario=request.user
        )

        # Tratando o upload da logo
        logo = request.FILES.get('logo')
        if logo:
            fs = FileSystemStorage()
            filename = fs.save(logo.name, logo)
            vaga.logo = fs.url(filename)

        vaga.save()

        messages.success(request, 'Vaga criada com sucesso!')
        return redirect('jobs:editar_vaga', vaga.id)
    return render(request, 'jobs/publicar_vaga.html', {'tipo_vaga_choices': TipoVaga.choices,})


def editar_vaga(request, vaga_id):

    if not request.user.is_authenticated:
        return redirect(f"{reverse('usuarios:login')}?next={request.path}")

    # Verifica se o usuário tem um perfil e se é do tipo 'EMPRESA'
    try:
        perfil_usuario = Perfil.objects.get(usuario=request.user)
        if perfil_usuario.tipo != 'EMPRESA':
            messages.error(request, 'Apenas empresas podem publicar vagas.')
            return redirect('jobs:home')
    except Perfil.DoesNotExist:
        messages.error(request, 'Perfil não encontrado.')
        return redirect('usuarios:registrar')

    vaga = get_object_or_404(Vaga, pk=vaga_id, usuario=request.user)

    if request.method == 'POST':
        vaga.titulo = request.POST.get('titulo')
        vaga.localizacao = request.POST.get('localizacao')
        vaga.tipo = request.POST.get('tipo')
        vaga.descricao = request.POST.get('descricao')
        vaga.organizacao = request.POST.get('organizacao')
        vaga.salario = request.POST.get('salario')

        # Tratando o upload da logo
        logo = request.FILES.get('logo')
        if logo:
            fs = FileSystemStorage()
            filename = fs.save(logo.name, logo)
            vaga.logo = fs.url(filename)

        vaga.save()

        # Atualizar tags aqui, se necessário

        messages.success(request, 'Vaga atualizada com sucesso!')
        return redirect('jobs:editar_vaga', vaga.id)

    return render(request, 'jobs/editar_vaga.html', {
        'vaga': vaga,
        'tipo_vaga_choices': TipoVaga.choices,
    })


def minhas_vagas(request):

    if not request.user.is_authenticated:
        return redirect(f"{reverse('usuarios:login')}?next={request.path}")

    # Verifica se o usuário tem um perfil e se é do tipo 'EMPRESA'
    try:
        perfil_usuario = Perfil.objects.get(usuario=request.user)
        if perfil_usuario.tipo != 'EMPRESA':
            messages.error(request, 'Apenas empresas podem publicar vagas.')
            return redirect('jobs:home')
    except Perfil.DoesNotExist:
        messages.error(request, 'Perfil não encontrado.')
        return redirect('usuarios:registrar')

    vagas = Vaga.objects.filter(usuario=request.user).order_by('criado_em').reverse()

    return render(request, 'jobs/vagas.html', {
        'vagas': vagas,
    })
