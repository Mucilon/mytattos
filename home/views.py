from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormTatto, FormEstudio

# Create your views here.
def login(request):
    if request.method != 'POST':
        return render(request, 'home/home.html')
    usuario =  request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuário ou senha inválidos')
        return render(request,'home/home.html')
    else:
        auth.login(request, user)

        return redirect('index')

def logout(request):
    auth.logout(request)
    return redirect('login')

def cadastro(request):
    if request.method != 'POST':

        return render(request, 'home/cadastro.html')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not usuario or not senha or not senha2:
        messages.error(request,'Nenhum campo pode estar vazio.')
        return render(request,'home/cadastro.html')

    if len(senha) < 6:
        messages.error(request, 'Senha precisa ter 6 caracteres ou mais.')
        return render(request, 'home/cadastro.html')

    if len(usuario) < 6:
        messages.error(request, 'Usuário precisa ter 6 caracteres ou mais.')
        return render(request, 'home/cadastro.html')

    if senha != senha2:
        messages.error(request, 'Senhas não conferem.')
        return render(request, 'home/cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já existe.')
        return render(request, 'home/cadastro.html')

    messages.success(request, 'Registrado com sucesso! Agora faça login.')

    user = User.objects.create_user(username=usuario,password=senha)
    user.save()

    return redirect('login')

@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormTatto()
        estudio = FormEstudio()

        return render(request, 'home/dashboard.html', {'form':form, 'estudio':estudio})

    form = FormTatto(request.POST, request.FILES)
    estudio = FormEstudio(request.POST)


    if not form.is_valid():
        messages.ERROR(request,'Erro ao enviar form!')
        form = FormTatto(request.POST)
        estudio = FormEstudio(request.POST)

        return render(request, 'home/dashboard.html', {'form': form, 'estudio':estudio})

    form.save()
    return redirect('dashboard')