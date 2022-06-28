from django.shortcuts import render

from .forms import *
# Create your views here.



def profesorFormulario(request):
    
  if request.method == 'POST':
      
    FormularioProfesores = ProfesorForm(request.POST)
    
    print(FormularioProfesores)
    
    if FormularioProfesores.is_valid:
        
        info = FormularioProfesores.cleaned_data

        profesor = Profesor(nombre = info['nombre'],apellido = info['apellido'])

        profesor.save()
        
        return render(request,"DjangoApp/profesores.html")
    
  else:
      
    FormularioProfesores = ProfesorForm()

  return render(request,"DjangoApp/profesores.html",{'FormularioProfesores': FormularioProfesores})





def alumnoFormulario(request):
    
  if request.method == 'POST':
      
    FormularioAlumno = AlumnoForm(request.POST)
    
    print(FormularioAlumno)
    
    if FormularioAlumno.is_valid:
        
        info = FormularioAlumno.cleaned_data

        alumno = Alumno(nombre = info['nombre'],apellido = info['apellido'],carrera = info['carrera'])

        alumno.save()
        
        return render(request,"DjangoApp/alumnos.html")
    
  else:
      
    FormularioAlumno = AlumnoForm()

  return render(request,"DjangoApp/alumnos.html",{'FormularioAlumno': FormularioAlumno})





def materiaFormulario(request):
    
  if request.method == 'POST':
      
    FormularioMaterias = MateriaForm(request.POST)
    
    print(FormularioMaterias)
    
    if FormularioMaterias.is_valid:
        
        info = FormularioMaterias.cleaned_data

        materia = Materia(nombre = info['nombre'],comision = info['comision'])

        materia.save()
        
        return render(request,"DjangoApp/materias.html")
    
  else:
      
    FormularioMaterias = MateriaForm()

  return render(request,"DjangoApp/materias.html",{'FormularioMaterias': FormularioMaterias})
