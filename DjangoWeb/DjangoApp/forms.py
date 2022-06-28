from django import forms

from .models import *

class ProfesorForm(forms.ModelForm):

    class Meta:
        model = Profesor
        fields = ('nombre', 'apellido',)

class alumnoForm(forms.ModelForm):

    class Meta:
        model = Alumno
        fields = ('nombre','apellido')

class materiaForm(forms.ModelForm):

    class Meta:
        model = Materias
        fields = ('nombre','comision')