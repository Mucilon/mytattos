from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'home/home.html')

def logout(request):
    return render(request, 'home/logout.html')

def cadastro(request):
    return render(request, 'home/cadastro.html')

def dashboard(request):
    return render(request, 'home/dashboard.html')


