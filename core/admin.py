from django.contrib import admin
from core.models import Curso, Aluno, Professor, Disciplina, GradeCurricular
from django import forms


from django.contrib.auth.admin import UserAdmin

#   Aluno
class NovoAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ('ra','nome', 'email', 'curso')

    def save(self, commit=True):
        user = super(NovoAlunoForm, self).save(commit=False)
        user.set_password('123@mudar')
        user.perfil = 'A'
        if commit:
            user.save()
        return user

class AlterarAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ('nome', 'curso')
    
class AlunoAdmin(UserAdmin):
    form = AlterarAlunoForm
    add_form = NovoAlunoForm
    list_display = ('ra', 'nome', 'email', 'curso')
    list_filter = ('perfil',)
    fieldsets = ( (None, {'fields': ('ra', 'nome', 'curso')}),)
    add_fieldsets = ((None, { 'fields': ('ra', 'nome', 'email', 'curso')} ),)
    search_fields = ('ra',)
    ordering = ('ra',)
    filter_horizontal = ()

#   Professor
class NovoProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ('ra','nome', 'email', 'apelido')

    def save(self, commit=True):
        user = super(NovoProfessorForm, self).save(commit=False)
        user.set_password('123@mudar')
        user.perfil = 'P'
        if commit:
            user.save()
        return user

class AlterarProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ('nome', 'apelido')

class ProfessorAdmin(UserAdmin):
    form = AlterarProfessorForm
    add_form = NovoProfessorForm
    list_display = ('ra', 'nome', 'email', 'apelido')
    list_filter = ('perfil',)
    fieldsets = ( (None, {'fields': ('ra', 'nome', 'apelido')}),)
    add_fieldsets = ((None, { 'fields': ('ra', 'nome', 'email', 'apelido')} ),)
    search_fields = ('ra',)
    ordering = ('ra',)
    filter_horizontal = ()

class CursoAdmin(admin.ModelAdmin):
    list_display = ('sigla', 'nome', 'tipo')
    search_fields = ('sigla',)

''' class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('sigla',)

# class GradeCurricularAdmin(admin.ModelAdmin):
    list_display = ('curso', 'ano', 'semestre')
    search_fields = ('curso',)'''

admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Curso, CursoAdmin)
# admin.site.register(Disciplina, DisciplinaAdmin)
# admin.site.register(GradeCurricular, GradeCurricularAdmin)