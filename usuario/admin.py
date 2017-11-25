from django.contrib import admin

from usuario.models import *
from usuario.forms import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
#   Aluno    
class AlunoAdmin(UserAdmin):
    add_form = AlunoForm
    form = AlunoAlterarForm
    add_fieldsets = ((None, { "fields": ('ra', 'nome', 'email', 'celular', 'ativo', 'curso')}),)
    fieldsets = ((None, { "fields": ('nome', 'email', 'celular', 'ativo', 'curso')}),)
    list_display = ["ra","nome","email","curso"]
    filter_horizontal = []
    ordering = ["ra"]
    list_filter = ["curso"]

#   Professor
class ProfessorAdmin(UserAdmin):
    add_form = ProfessorForm
    form = ProfessorAlterarForm
    add_fieldsets = ((None, { "fields": ('ra','nome', 'email', 'celular', 'ativo', 'apelido')}),)
    fieldsets = ((None, { "fields": ('nome', 'email', 'celular', 'ativo', 'apelido')}),)
    list_display = ["ra","nome","email","apelido"]
    filter_horizontal = []
    ordering = ["ra"]
    list_filter = []

#   Coordenador
class CoordenadorAdmin(UserAdmin):
    add_form = CoordenadorForm
    form = CoordenadorAlterarForm
    add_fieldsets = ((None, { "fields": ('ra','nome', 'email', 'celular', 'ativo')}),)
    fieldsets = ((None, { "fields": ('nome', 'email', 'celular', 'ativo')}),)
    list_display = ["ra","nome","email"]
    filter_horizontal = []
    ordering = ["ra"]
    list_filter = []

admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Coordenador, CoordenadorAdmin)