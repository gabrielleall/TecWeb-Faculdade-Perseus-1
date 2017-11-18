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
from core.views import index, curso, noticias, login, cadastro_contato, cadastro_usuario, cadastro_disciplina, cadastro_curso, cadastro_grade_curricular, esqueci_senha, area_aluno, area_aluno_boletim, area_aluno_contato_professor, area_aluno_smart_class1, area_aluno_smart_class2, detalhe_curso

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^curso/', curso),
    url(r'^noticias/', noticias),
    url(r'^detalheCurso/', detalhe_curso),
    url(r'^login/', login),
    url(r'^cadastroContato/', cadastro_contato),
    url(r'^cadastroUsuario/', cadastro_usuario),
    url(r'^cadastroDisciplina/', cadastro_disciplina),
    url(r'^cadastroCurso/', cadastro_curso),
    url(r'^cadastroGradeCurricular/', cadastro_grade_curricular),
    url(r'^esqueciSenha/', esqueci_senha),
    url(r'^areaAluno/', area_aluno),
    url(r'^areaAlunoBoletim/', area_aluno_boletim),
    url(r'^areaAlunoContatoProfessor/', area_aluno_contato_professor),
    url(r'^areaAlunoSmartClass1/', area_aluno_smart_class1),
    url(r'^areaAlunoSmartClass2/', area_aluno_smart_class2),
]
