from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
'''
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
    arquivo = models.CharField(max_length=500, null=False)'''