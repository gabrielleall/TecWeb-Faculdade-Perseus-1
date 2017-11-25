from django import forms
from usuario.models import Aluno, Professor, Coordenador

#   Aluno
class AlunoForm(forms.ModelForm):
    def save(self, commit=True):
        aluno = super(AlunoForm,self).save(commit=False)
        aluno.set_password("aluno@123")
        aluno.perfil = 'A'
        if commit:
            aluno.save()
        return aluno
    class Meta:
        model = Aluno
        fields = ["ra", "nome", "email", "curso"]

class AlunoAlterarForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ["nome", "email", "curso"]

#   Professor
class ProfessorForm(forms.ModelForm):
    def save(self, commit=True):
        professor = super(ProfessorForm,self).save(commit=False)
        professor.set_password("professor@123")
        professor.perfil = 'P'
        if commit:
            professor.save()
        return professor
    class Meta:
        model = Professor
        fields = ["ra", "nome", "email", "apelido"]

class ProfessorAlterarForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ["nome", "email", "apelido"]

#   Coordenador
class CoordenadorForm(forms.ModelForm):
    def save(self, commit=True):
        coordenador = super(CoordenadorForm,self).save(commit=False)
        coordenador.set_password("Faculdade123")
        coordenador.perfil = 'C'
        if commit:
            coordenador.save()
        return coordenador
    class Meta:
        model = Coordenador
        fields = ["ra", "nome", "email"]

class CoordenadorAlterarForm(forms.ModelForm):
    class Meta:
        model = Coordenador
        fields = ["nome", "email"]