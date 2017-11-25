from django.contrib import admin

from .models import Curso, Disciplina, GradeCurricular, Periodo, DisciplinaOfertada, Turma

# Register your models here.
#   Curso
class CursoAdmin (admin.ModelAdmin):
    list_display = ["sigla", "nome"]
    search_fields = ('sigla',)

#   Disciplina
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ["nome","carga_horaria","teoria","pratica"]
    search_fields = ('nome',)

#  Grade Curricular
class GradeCurricularAdmin(admin.ModelAdmin):
    list_display = ["curso","ano","semestre"]
    search_fields = ("curso","ano","semestre")

#   Periodo
class PeriodoAdmin(admin.ModelAdmin):
    list_display = ["grade","numero"]

#  Disciplina Ofertada
class DisciplinaOfertadaAdmin(admin.ModelAdmin):
    list_display = ["disciplina","ano","semestre"]

class TurmaAdmin(admin.ModelAdmin):
    list_display = ["id_turma","turno","professores"]

admin.site.register(Curso, CursoAdmin)
admin.site.register(Disciplina,DisciplinaAdmin)
admin.site.register(GradeCurricular,GradeCurricularAdmin)
admin.site.register(Periodo,PeriodoAdmin)
admin.site.register(DisciplinaOfertada,DisciplinaOfertadaAdmin)
admin.site.register(Turma,TurmaAdmin)