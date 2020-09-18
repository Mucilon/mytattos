from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import Value
from django.db.models.functions import Concat
from django.core.paginator import Paginator
from .models import Tattos


# Create your views here.

def tattoshome(request):
    tattos = Tattos.objects.order_by('id').filter(mostrar=True)
    paginator = Paginator(tattos,5)
    page = request.GET.get('p')
    tattos = paginator.get_page(page)
    return render(request, 'tattos/index.html', {
        'tattos': tattos
    })

def ver_tatto(request, tatto_id):
    tatto = get_object_or_404(Tattos, id=tatto_id)
    if not tatto.mostrar:
        raise Http404()
    return render(request,'tattos/ver_tatto.html',{
        'tatto': tatto
    })

def busca(request):
    termo = request.GET.get('termo')
    if termo is None or not termo:
        raise Http404()
    tattos = Tattos.objects.order_by('id').filter(nome_tatto__icontains=termo,mostrar=True)
    paginator = Paginator(tattos, 5)
    page = request.GET.get('p')
    tattos =  paginator.get_page(page)
    return render(request,'tattos/busca.html',{
        'tattos':   tattos
    })