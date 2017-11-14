from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length = 50)
    ra = models.IntegerField(unique = True)
    password = models.CharField(max_length = 150)
    email = models.EmailField()
    perfil = models.CharField(max_length = 1)
    ativo = models.BooleanField(default = True)
