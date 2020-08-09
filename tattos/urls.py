from django.urls import path
from . import views


urlpatterns = [
    path('', views.tattoshome, name='tattoshome'),
    path('<int:tatto_id>',views.ver_tatto,name='ver_tatto'),
    path('busca/',views.busca,name='busca')
]