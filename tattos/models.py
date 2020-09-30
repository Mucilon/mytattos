from django.db import models
from django.utils import timezone
# Create your models here.

class Estudio(models.Model):
    nome = models.CharField(max_length=40,verbose_name='Estúdio')

    def __str__(self):
        return self.nome


class Tattos(models.Model):
    nome_tatto = models.CharField(max_length=40,verbose_name='Nome da Tatto')
    orcamento = models.IntegerField(blank=True,verbose_name='Orçamento')
    tatto = models.ImageField(upload_to='fotos/%Y/%m/%d',verbose_name='Imagem da Tatto')
    data_criacao = models.DateTimeField(default=timezone.now,verbose_name='Data')
    descricao = models.TextField(blank=True,verbose_name='Descrição')
    mostrar = models.BooleanField(default=True,verbose_name='Mostrar')
    estudio = models.ForeignKey(Estudio,on_delete=models.DO_NOTHING,verbose_name='Estúdio', blank=True)

    def __str__(self):
        return self.nome_tatto