from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Perfil
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import PerfilForm
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Perfil
from .forms import PerfilForm


def registrar(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        perfil_form = PerfilForm(request.POST)

        if user_form.is_valid() and perfil_form.is_valid():
            # Verifica se o usuário já existe
            username = user_form.cleaned_data.get('username')
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Usuário já existe.')
                return redirect('usuarios:registrar')

            user = user_form.save()

            # Cria ou obtém o perfil do usuário
            perfil, created = Perfil.objects.get_or_create(usuario=user)
            perfil.tipo = perfil_form.cleaned_data['tipo']  # Atribui o tipo de perfil
            perfil.save()

            messages.success(request, 'Conta criada com sucesso.')
            return redirect('usuarios:login')

    else:
        user_form = UserCreationForm()
        perfil_form = PerfilForm()

    return render(request, 'usuarios/registrar.html', {
        'form': user_form,
        'perfil_form': perfil_form
    })


def login_view(request):
    if request.user.is_authenticated:
        return redirect('jobs:home')

    next_page = request.GET.get('next')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bem-vindo {username}!")
                return redirect(next_page or 'jobs:publicar_vaga')  # Redireciona para 'next' ou 'home'
            else:
                messages.error(request, "Nome de usuário ou senha inválidos.")
        else:
            messages.error(request, "Nome de usuário ou senha inválidos.")

    else:
        form = AuthenticationForm()

    # Passa a variável next_page para o contexto do template
    return render(request, "usuarios/login.html", {"form": form, "next": next_page})