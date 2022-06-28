from django.shortcuts import render

from forms import *
# Create your views here.



def profesorFormulario(request):
  if request.method == 'POST':
    formulario = ProfesorForm(request.POST)
    print(formulario)
    if formulario.is_valid:
        info = formulario.cleaned_data

        profesor = Profesor(nombre = info['nombre'],apellido = info['apellido'])

        profesor.save()
        return render(request,"MVTPrimerProyectoApp/index.html")
  else:
    formulario = ProfesorForm()

  return render(request,"MVTPrimerProyectoApp/index.html",{'formulario': formulario})