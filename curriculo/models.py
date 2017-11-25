from django.db import models

# Create your models here.

#   CURSO
class Curso(models.Model):
    sigla = models.CharField(max_length = 5, blank = False, null=False)
    nome = models.CharField(max_length = 50, blank = False, null=False)
    tipo = models.CharField(max_length = 50, blank = False, null=False)
    carga_horaria = models.IntegerField(default = 1000, blank = False)

    descricao_basica = models.TextField(blank = False, null=False)
    descricao_completa = models.TextField(blank = False, null=False)

    def __str__(self):
        return self.nome

#   Disciplina
class Disciplina(models.Model):
    nome = models.CharField(max_length= 240, unique=True,null=False)
    carga_horaria = models.IntegerField(null=False)
    teoria = models.DecimalField(max_digits=3,decimal_places=0,null=False)
    pratica = models.DecimalField(max_digits=3,decimal_places=0,null=False)
    ementa = models.TextField(null=False)
    competencias = models.TextField(null=False)
    habilidades = models.TextField(null=False)
    conteudo = models.TextField(null=False)
    bibliografia_basica = models.TextField(null=False)
    bibliografia_complementar = models.TextField(null=False)

    def __str__(self):
        return self.nome

#   Grade Curricular
class GradeCurricular(models.Model):
    curso = models.ForeignKey(Curso)
    ano = models.IntegerField(null=False)
    semestre = models.CharField(max_length = 1,null=False)

    def __str__(self):
        return ('curso: {} ano: {} semestre: {}'.format(self.curso, self.ano, self.semestre))

#   Periodo
class Periodo(models.Model):
    grade = models.ForeignKey(GradeCurricular)
    numero = models.SmallIntegerField(blank = False, null=False)
    disciplinas = models.ManyToManyField(Disciplina)

#   Disciplina Ofertada
class DisciplinaOfertada(models.Model):
    disciplina = models.ForeignKey(Disciplina)
    ano = models.SmallIntegerField(null=False)
    semestre = models.CharField(max_length=1,blank = False, null=False)

#   Turma
class Turma(models.Model):
    disciplina_ofertada = models.ForeignKey(DisciplinaOfertada)
    id_turma = models.CharField(max_length=1,null=False)
    turno = models.CharField(max_length=15,null=False)
    professores = models.ForeignKey('usuario.Professor')
    matriculas = models.ManyToManyField(to='usuario.Aluno')
    cursos = models.ManyToManyField(to=Curso)