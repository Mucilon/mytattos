from django.db import models
from tattos.models import Estudio, Tattos
from django import forms

# Create your models here.
class FormEstudio(forms.ModelForm):
    class Meta:
        model = Estudio
        exclude = ()

class FormTatto(forms.ModelForm):
    class Meta:
        model = Tattos
        exclude = ('mostrar',)

