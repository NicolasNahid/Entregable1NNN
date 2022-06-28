from django.urls import path, include
from DjangoApp import views
urlpatterns = [
    
    path('Profesores/', views.profesorFormulario, name='profesor' ),
    path('Alumnos/', views.alumnoFormulario, name='alumnos' ),
    path('Materias/', views.materiaFormulario, name='materias' ),
    
]