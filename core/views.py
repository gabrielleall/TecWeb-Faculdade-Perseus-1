from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from core.models import Curso

# Create your views here.
def index(request):
    return render(request, "index.html")

def lista_curso(request):
    contexto = {
        'cursos': Curso.objects.all,
    }
    return render(request, "listaCursos.html", contexto)

def noticias(request):
    return render(request, "noticias.html")

def login(request):
    return render(request, "login.html")

def cadastro_contato(request):
    return render(request, "cadastroContato.html")

def cadastro_usuario(request):
    return render(request, "cadastroUsuario.html")

def cadastro_disciplina(request):
    return render(request, "cadastroDisciplina.html")

def cadastro_curso(request):
    return render(request, "cadastroCurso.html")

#   Curso
def curso(request, sigla):
    contexto = {
        'curso': Curso.objects.get(sigla = sigla.upper())
        }
    return render(request,'curso.html', contexto)

def cadastro_grade_curricular(request):
    return render(request, "cadastroGradeCurricular.html")

def esqueci_senha(request):
    return render(request, "esqueciSenha.html")


def checa_aluno(user):
     return user.perfil == 'A'

@login_required(login_url='/entrar')
@user_passes_test(checa_aluno, login_url='/?error=acesso', redirect_field_name = None)
def area_aluno(request):
    return render(request, "areaAluno.html")

def area_aluno_boletim(request):
    return render(request, "areaAlunoBoletim.html")

def area_aluno_contato_professor(request):
    return render(request, "areaAlunoContatoProfessor.html")

def area_aluno_smart_class1(request):
    return render(request, "areaAlunoSmartClass1.html")

def area_aluno_smart_class2(request):
    return render(request, "areaAlunoSmartClass2.html")