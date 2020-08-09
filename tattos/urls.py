from django.urls import path
from . import views


urlpatterns = [
    path('', views.tattoshome, name='tattoshome'),
]