from django.contrib import admin
from .models import Estudio, Tattos
# Register your models here.

class TattoAdmin(admin.ModelAdmin):
    list_display =('id','nome_tatto','estudio','orcamento','data_criacao','mostrar')
    list_display_links = ('id',)
    list_filter = ('estudio',)
    list_per_page = 12
    search_fields = ('nome_tatto','estudio')
    list_editable = ('nome_tatto','mostrar')

admin.site.register(Tattos,TattoAdmin)
admin.site.register(Estudio)