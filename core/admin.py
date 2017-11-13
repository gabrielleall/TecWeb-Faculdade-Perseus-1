from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from core.models import Aluno #outrasClasses
# Register your models here.

class NovoAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ('ra','email', 'nome','curso')

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
        fields = ('email', 'nome', 'curso')
      
    
class AlunoAdmin(UserAdmin):
    form = AlterarAlunoForm
    add_form = NovoAlunoForm
    #o que vai aparecer listando
    list_display = ('ra','email', 'nome', 'curso')
    #campos de filtro
    list_filter = ('perfil',)
    fieldsets = ( (None, {'fields': ('email', 'nome', 'curso')}),)
    add_fieldsets = ((None, { 'fields': ('ra', 'email', 'nome', 'curso')} ),)
    #como procura
    search_fields = ('ra',)
    #como ordena
    ordering = ('ra',)
    filter_horizontal = ()

admin.site.register(Aluno,AlunoAdmin)
#admin.site.register(Curso,CursoAdmin)


#admin.site.register(Classe1)
#admin.site.register(Classe2)
