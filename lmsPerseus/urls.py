"""lmsPerseus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from core.views import *
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name = 'home'),
    url(r'^noticias/', noticias),
    url(r'^cadastroContato/', cadastro_contato),
    url(r'^cadastroUsuario/', cadastro_usuario),
    url(r'^cadastroDisciplina/', cadastro_disciplina),
    url(r'^cadastroCurso/', cadastro_curso),
    url(r'^cadastroGradeCurricular/', cadastro_grade_curricular),
    url(r'^esqueciSenha/', esqueci_senha),

    #Curso
    url(r'^curso/([A-Z, a-z]+)', curso),

    #Lista Curso
    url(r'^listacurso/', lista_curso),

    #Login
    url(r'^entrar/', login, {'template_name':'login.html'}),
    url(r'^sair/', logout, {'template_name':'index.html'}),

    #Area Aluno
    url(r'^areaAluno/', area_aluno, name = 'area_aluno'),
    url(r'^areaAlunoBoletim/', area_aluno_boletim),
    url(r'^areaAlunoContatoProfessor/', area_aluno_contato_professor),
    url(r'^areaAlunoSmartClass1/', area_aluno_smart_class1),
    url(r'^areaAlunoSmartClass2/', area_aluno_smart_class2),


]
