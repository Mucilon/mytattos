from django.shortcuts import render

# Create your views here.

def tattoshome(request):
    return render(request, 'tattos/tattoshome.html')