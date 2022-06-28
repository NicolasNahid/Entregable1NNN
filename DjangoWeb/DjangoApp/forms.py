from django import forms

from .models import *

class ProfesorForm(forms.ModelForm):

    class Meta:
        model = Profesor
        fields = ('nombre','apellido',)

class AlumnoForm(forms.ModelForm):

    class Meta:
        model = Alumno
        fields = ('nombre','apellido','carrera',)

class MateriaForm(forms.ModelForm):

    class Meta:
        model = Materia
        fields = ('nombre','comision',)