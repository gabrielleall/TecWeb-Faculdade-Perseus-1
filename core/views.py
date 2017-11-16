from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def curso(request):
    return render(request, "listaCursos.html")

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

def cadastro_grade_curricular(request):
    return render(request, "cadastroGradeCurricular.html")

def esqueci_senha(request):
    return render(request, "esqueciSenha.html")

def area_aluno(request):
    return render(request, "areaAluno.html")

def area_aluno_boletim(request):
    return render(request, "areaAlunoBoletim.html")