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

#   COORDENADOR
class Coordenador(Usuario):
    pass

#   Aluno
class Aluno(Usuario):
    curso = models.ForeignKey('curriculo.Curso')

#   Professor
class Professor(Usuario):
    apelido = models.CharField(max_length = 30)