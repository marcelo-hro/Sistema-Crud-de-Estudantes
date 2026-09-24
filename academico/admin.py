from django.contrib import admin

from academico.models import Curso, Departamento, Disciplina, Professor, Turma

# Register your models here.



class ProfessorAdmin(admin.ModelAdmin):
    list_display=('matricula','nome','email','cpf')


class CursoAdmin(admin.ModelAdmin):
    list_display=('codigo','nome','foto','duracao','data_inicio','cargaHoraria')

class TurmaAdmin(admin.ModelAdmin):
    list_display=('codigo','anoIngresso','periodo','curso')

class DisciplinaAdmin(admin.ModelAdmin):
    list_display=('codigo','nome','cargaHoraria','turno','turma','professor')

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'imagem')
  

admin.site.register(Curso, CursoAdmin)
admin.site.register(Professor,ProfessorAdmin)
admin.site.register(Turma,TurmaAdmin)
admin.site.register(Disciplina,DisciplinaAdmin)
admin.site.register(Departamento, DepartamentoAdmin)  