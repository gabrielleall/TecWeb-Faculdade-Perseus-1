from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def checa_aluno(user):
     return user.perfil == 'A'

@login_required(login_url='/entrar')
@user_passes_test(checa_aluno, login_url='/?error=acesso', redirect_field_name = None)
def area_aluno(request):
    return render(request, "areaAluno.html")

@login_required(login_url='/entrar')
@user_passes_test(checa_aluno, login_url='/?error=acesso', redirect_field_name = None)
def area_aluno_boletim(request):
    return render(request, "areaAlunoBoletim.html")

@login_required(login_url='/entrar')
@user_passes_test(checa_aluno, login_url='/?error=acesso', redirect_field_name = None)
def area_aluno_contato_professor(request):
    return render(request, "areaAlunoContatoProfessor.html")

@login_required(login_url='/entrar')
@user_passes_test(checa_aluno, login_url='/?error=acesso', redirect_field_name = None)
def area_aluno_smart_class1(request):
    return render(request, "areaAlunoSmartClass1.html")

@login_required(login_url='/entrar')
@user_passes_test(checa_aluno, login_url='/?error=acesso', redirect_field_name = None)
def area_aluno_smart_class2(request):
    return render(request, "areaAlunoSmartClass2.html")