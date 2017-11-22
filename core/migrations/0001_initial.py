# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 12:17
from __future__ import unicode_literals

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nome', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('ra', models.IntegerField(unique=True)),
                ('password', models.CharField(max_length=150)),
                ('celular', models.CharField(max_length=11)),
                ('perfil', models.CharField(default='C', max_length=1)),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', core.models.UsuarioManager()),
            ],
        ),
        migrations.CreateModel(
            name='ArquivoQestao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ArquivoResposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=5)),
                ('nome', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('carga_horaria', models.IntegerField(default=1000)),
                ('ativo', models.BooleanField(default=True)),
                ('descricao_basica', models.TextField()),
                ('descricao_completa', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=240, unique=True)),
                ('carga_horaria', models.IntegerField()),
                ('teoria', models.DecimalField(decimal_places=0, max_digits=3)),
                ('pratica', models.DecimalField(decimal_places=0, max_digits=3)),
                ('ementa', models.TextField()),
                ('competencias', models.TextField()),
                ('habilidades', models.TextField()),
                ('conteudo', models.TextField()),
                ('bibliografia_basica', models.TextField()),
                ('bibliografia_complementar', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GradeCurricular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField()),
                ('semestre', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('data_limite', models.DateField()),
                ('descricao', models.TextField()),
                ('data', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_avaliacao', models.DateField()),
                ('nota', models.DecimalField(decimal_places=2, max_digits=4)),
                ('avaliacao', models.TextField()),
                ('descricao', models.TextField()),
                ('data_envio', models.DateField()),
                ('questoes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Questao')),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField()),
                ('semestre', models.CharField(max_length=1)),
                ('id_turma', models.CharField(max_length=1)),
                ('turno', models.CharField(max_length=15)),
                ('cursos', models.ManyToManyField(to='core.Curso')),
                ('disciplinas', models.ManyToManyField(to='core.Disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Curso')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.usuario',),
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('object', core.models.UsuarioManager()),
            ],
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('gradecurricular_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.GradeCurricular')),
                ('numero', models.IntegerField()),
            ],
            bases=('core.gradecurricular',),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('apelido', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
            bases=('core.usuario',),
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('object', core.models.UsuarioManager()),
            ],
        ),
        migrations.AddField(
            model_name='questao',
            name='turmas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Turma'),
        ),
        migrations.AddField(
            model_name='gradecurricular',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Curso'),
        ),
        migrations.AddField(
            model_name='arquivoresposta',
            name='respostas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Resposta'),
        ),
        migrations.AddField(
            model_name='arquivoqestao',
            name='questoes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Questao'),
        ),
        migrations.AddField(
            model_name='turma',
            name='matriculas',
            field=models.ManyToManyField(to='core.Aluno'),
        ),
        migrations.AddField(
            model_name='turma',
            name='professores',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Professor'),
        ),
        migrations.AddField(
            model_name='resposta',
            name='alunos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Aluno'),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='periodos',
            field=models.ManyToManyField(to='core.Periodo'),
        ),
    ]
