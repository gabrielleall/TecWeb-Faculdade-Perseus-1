from django.shortcuts import render

from curriculo.models import Curso

# Create your views here.
#   Curso
def curso(request, sigla):
    contexto = {
        'curso': Curso.objects.get(sigla = sigla.upper())
        }
    return render(request,'curso.html', contexto)

def lista_curso(request):
    contexto = {
        'cursos': Curso.objects.all,
    }
    return render(request, "listaCursos.html", contexto)