from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
class UsuarioManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, ra, password, **extra_fields):
        if not ra:
            raise ValueError('RA precisa ser preenchido')
        user = self.model(ra=ra, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user
    def create_user(self, ra, password=None, **extra_fields):
        return self._create_user(ra, password, **extra_fields)
    def create_superuser(self, ra, password, **extra_fields):
        return self._create_user(ra, password, **extra_fields)

#   USUARIOS
class Usuario(AbstractBaseUser):
    nome = models.CharField(max_length = 150, blank = False, null=False)
    email = models.EmailField(blank = False, null=False)
    ra = models.IntegerField(unique = True, blank = False, null=False)
    password = models.CharField(max_length = 150, blank = False, null=False)
    celular = models.CharField(max_length=11, blank = False, null=False)
    perfil = models.CharField(max_length = 1, default = 'C')
    ativo = models.BooleanField(default = True)

    USERNAME_FIELD = 'ra'
    REQUIRED_FIELDS = ['nome']

    object = UsuarioManager()

    @property
    def is_staff(self):
        return self.perfil == 'C'
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    def get_short_name(self):
        return self.nome

    def get_full_name(self):
        return self.nome
    
    def __str__(self):
        return self.nome

#   CURSO
class Curso(models.Model):
    sigla = models.CharField(max_length = 5, blank = False, null=False)
    nome = models.CharField(max_length = 50, blank = False, null=False)
    tipo = models.CharField(max_length = 50, blank = False, null=False)
    carga_horaria = models.IntegerField(default = 1000, blank = False)
    ativo = models.BooleanField(default = True)

    descricao_basica = models.TextField(blank = False, null=False)
    descricao_completa = models.TextField(blank = False, null=False)

    def __str__(self):
        return self.nome

#   GRADE CURRICULAR
class GradeCurricular(models.Model):
    curso = models.ForeignKey(Curso)
    ano = models.IntegerField(null=False)
    semestre = models.CharField(max_length = 1,null=False)

#   Periodo
class Periodo(GradeCurricular):
    numero =models.IntegerField(blank = False, null=False)

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

    periodos = models.ManyToManyField(
        to = Periodo
    )

    def __str__(self):
        return self.nome

#   Aluno
class Aluno(Usuario):
    curso = models.ForeignKey(Curso)

#   Professor
class Professor(Usuario):
    apelido = models.CharField(max_length = 30)

# Turma
class Turma(models.Model):
    ano = models.IntegerField(null=False)
    semestre = models.CharField(max_length=1,null=False)
    id_turma = models.CharField(max_length=1,null=False)
    turno = models.CharField(max_length=15,null=False)
    professores = models.ForeignKey(Professor,null=False)
    disciplinas = models.ManyToManyField(to=Disciplina)
    matriculas = models.ManyToManyField(to=Aluno)
    cursos = models.ManyToManyField(to=Curso)

#   Questão
class Questao(models.Model):
    turmas = models.ForeignKey(Turma,null=False)
    numero = models.IntegerField(null=False)
    data_limite = models.DateField(null=False)
    descricao = models.TextField(null=False)
    data = models.DateField(auto_now_add=True)

#   Arquivo Questão
class ArquivoQestao(models.Model):
    questoes = models.ForeignKey(Questao,null=False)
    arquivo = models.CharField(max_length=500, null=False)

#   Resposta
class Resposta(models.Model):
    questoes = models.ForeignKey(Questao, null=False)
    alunos = models.ForeignKey(Aluno, null=False)
    data_avaliacao = models.DateField()
    nota = models.DecimalField(max_digits=4,decimal_places=2)
    avaliacao = models.TextField()
    descricao = models.TextField()
    data_envio = models.DateField()

# ArquivoResposta
class ArquivoResposta(models.Model):
    respostas = models.ForeignKey(Resposta, null=False)
    arquivo = models.CharField(max_length=500, null=False)


